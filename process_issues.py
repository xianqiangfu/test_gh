#!/usr/bin/env python3
"""
GitHub Issue 自动化处理脚本

功能：
1. 读取 GitHub issue 列表
2. 遍历每个 issue，生成 prompt
3. 将 prompt 发送给 Claude Code 修复 issue
4. 每次修复后 git push 并关闭 issue
"""

import os
import subprocess
import json
import re
from pathlib import Path
from typing import List, Dict, Optional


class IssueProcessor:
    def __init__(self, repo_owner: str, repo_name: str, workspace_dir: str = "workspace"):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.workspace_dir = Path(workspace_dir)
        self.workspace_dir.mkdir(exist_ok=True)

        # 确保 workspace 在 .gitignore 中
        self._ensure_gitignore()

    def _ensure_gitignore(self):
        """确保 workspace 目录在 .gitignore 中"""
        gitignore_path = Path(".gitignore")
        gitignore_content = ""
        if gitignore_path.exists():
            gitignore_content = gitignore_path.read_text(encoding="utf-8")

        workspace_entry = "/workspace"
        if workspace_entry not in gitignore_content:
            with open(gitignore_path, "a", encoding="utf-8") as f:
                f.write(f"\n{workspace_entry}  # Claude Code workspace\n")

    def get_open_issues(self) -> List[Dict]:
        """获取所有开放的 issue"""
        cmd = [
            "gh", "issue", "list",
            "--repo", f"{self.repo_owner}/{self.repo_name}",
            "--state", "open",
            "--json", "number,title,body,labels"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)

    def generate_prompt(self, issue: Dict) -> str:
        """根据 issue 内容生成 Claude Code prompt"""
        issue_number = issue["number"]
        title = issue["title"]
        body = issue.get("body", "")
        labels = [label["name"] for label in issue.get("labels", [])]

        prompt = f"""请解决以下 GitHub issue #{issue_number}:

标题: {title}
标签: {', '.join(labels) if labels else '无'}

描述:
{body}

请根据 issue 的要求完成相应的任务。完成后，请提交代码并推送到远程仓库。"""

        return prompt

    def save_prompt_to_workspace(self, issue: Dict, prompt: str) -> Path:
        """将 prompt 保存到 workspace 目录"""
        issue_number = issue["number"]
        safe_title = re.sub(r'[^\w\-_\. ]', '_', issue["title"])[:50]
        filename = f"issue-{issue_number:03d}-{safe_title}.prompt"
        filepath = self.workspace_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(prompt)

        return filepath

    def send_to_claude_code(self, prompt: str) -> bool:
        """将 prompt 发送给 Claude Code 处理"""
        # 使用 claude code CLI
        cmd = ["claude", "code", prompt]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 分钟超时
            )
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            print(f"警告: Claude Code 处理超时")
            return False
        except Exception as e:
            print(f"错误: 执行 Claude Code 失败: {e}")
            return False

    def git_commit_and_push(self, issue_number: int) -> bool:
        """提交并推送代码"""
        try:
            # 检查是否有变更
            status_result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                check=True
            )

            if not status_result.stdout.strip():
                print(f"Issue #{issue_number}: 没有代码变更，跳过提交")
                return True

            # 提交代码
            commit_msg = f"解决 issue #{issue_number} - Auto-generated commit by Claude Code"
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)

            # 推送代码
            subprocess.run(["git", "push"], check=True)

            print(f"Issue #{issue_number}: 代码已推送")
            return True

        except subprocess.CalledProcessError as e:
            print(f"Issue #{issue_number}: Git 操作失败: {e}")
            return False

    def close_issue(self, issue_number: int) -> bool:
        """关闭 GitHub issue"""
        try:
            cmd = [
                "gh", "issue", "close",
                str(issue_number),
                "--repo", f"{self.repo_owner}/{self.repo_name}",
                "--comment", "已通过 Claude Code 自动解决"
            ]
            subprocess.run(cmd, check=True)
            print(f"Issue #{issue_number}: 已关闭")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Issue #{issue_number}: 关闭失败: {e}")
            return False

    def process_issue(self, issue: Dict, use_claude: bool = True) -> bool:
        """处理单个 issue"""
        issue_number = issue["number"]
        title = issue["title"]
        print(f"\n{'='*60}")
        print(f"处理 Issue #{issue_number}: {title}")
        print(f"{'='*60}")

        # 生成 prompt
        prompt = self.generate_prompt(issue)

        # 保存 prompt 到 workspace
        prompt_file = self.save_prompt_to_workspace(issue, prompt)
        print(f"Prompt 已保存到: {prompt_file}")

        # 发送给 Claude Code
        if use_claude:
            print("发送到 Claude Code...")
            success = self.send_to_claude_code(prompt)

            if not success:
                print(f"Issue #{issue_number}: Claude Code 处理失败")
                return False

        # 提交并推送代码
        if not self.git_commit_and_push(issue_number):
            return False

        # 关闭 issue
        if not self.close_issue(issue_number):
            return False

        print(f"Issue #{issue_number}: 处理完成")
        return True

    def process_all(self, use_claude: bool = True, limit: Optional[int] = None):
        """处理所有开放的 issue"""
        issues = self.get_open_issues()

        if limit:
            issues = issues[:limit]

        print(f"找到 {len(issues)} 个开放的 issue")

        for i, issue in enumerate(issues, 1):
            print(f"\n进度: {i}/{len(issues)}")

            success = self.process_issue(issue, use_claude)
            if not success:
                print(f"Issue #{issue['number']}: 处理失败，继续下一个")


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="GitHub Issue 自动化处理")
    parser.add_argument("--owner", default="xianqiangfu", help="仓库所有者")
    parser.add_argument("--repo", default="test_gh", help="仓库名称")
    parser.add_argument("--limit", type=int, help="限制处理的 issue 数量")
    parser.add_argument("--no-claude", action="store_true", help="不调用 Claude Code（仅生成 prompt）")

    args = parser.parse_args()

    processor = IssueProcessor(args.owner, args.repo)
    processor.process_all(use_claude=not args.no_claude, limit=args.limit)


if __name__ == "__main__":
    main()