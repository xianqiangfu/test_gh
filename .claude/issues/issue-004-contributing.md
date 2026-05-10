# Issue #4: 添加 CONTRIBUTING.md 贡献指南

## 问题
缺少贡献指南，不利于社区协作。

## 影响
- 潜在贡献者不知道如何参与
- 提交的 PR 格式不统一
- 缺少代码规范说明

## 建议
添加 `CONTRIBUTING.md` 文件。

---

## 实现建议

### 基础结构
```markdown
# 贡献指南

感谢对本项目的关注！欢迎任何形式的贡献。

## 如何贡献

### 报告问题
- 使用 GitHub Issues 报告 bug 或建议
- 提供详细的描述和复现步骤

### 提交代码
1. Fork 本仓库
2. 创建分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 代码规范

### Markdown 格式
- 使用中文
- 标题层级清晰
- 代码块指定语言

### 代码风格
- 遵循 PEP 8
- 添加适当的注释

## 许可证
提交代码即表示您同意将代码以 MIT License 许可。
```

---

## 扩展建议
- 添加 ISSUE 模板
- 添加 PR 模板
- 添加 CI/CD 配置（可选）