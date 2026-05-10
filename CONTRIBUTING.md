# 贡献指南

感谢你对本项目的兴趣！我们欢迎任何形式的贡献。

## 如何贡献

### 报告问题

如果你发现了错误或有改进建议，请：

1. 检查是否已有相同或相似的 issue
2. 创建新的 issue，详细描述：
   - 问题或建议的描述
   - 复现步骤（如果是 bug）
   - 预期行为
   - 实际行为
   - 环境信息（操作系统、Python 版本等）

### 提交代码

#### 开发流程

1. Fork 本仓库到你的 GitHub 账户
2. 创建新的分支进行开发：
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
   ```
3. 进行修改并测试
4. 提交更改：
   ```bash
   git commit -m "描述你的更改"
   ```
5. 推送到你的 fork：
   ```bash
   git push origin feature/your-feature-name
   ```
6. 创建 Pull Request

#### Commit 信息规范

使用清晰的 commit 信息：

- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更新
- `style:` 代码格式（不影响功能）
- `refactor:` 重构
- `test:` 添加测试
- `chore:` 构建/工具链相关

示例：
```
fix: 修正线性回归代码中的计算错误
docs: 更新 README 添加新章节链接
feat: 添加决策树可视化示例
```

#### 代码规范

- 使用有意义的变量名和函数名
- 添加适当的注释解释复杂逻辑
- 保持代码简洁易读
- 遵循 PEP 8 Python 代码风格

### 文档贡献

文档是项目的重要组成部分。你可以：

- 修正错别字或语法错误
- 改进现有解释
- 添加示例
- 翻译内容
- 补充图片或图表

### 添加示例代码

欢迎添加：

- 更多示例代码
- 不同数据集的应用
- 可视化代码
- 性能比较示例

## 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/xianqiangfu/test_gh.git
cd test_gh

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

## 代码审查

提交 PR 后，维护者会进行代码审查。请注意：

- 回复审查意见
- 根据反馈进行修改
- 保持开放和友好的态度

## 许可证

贡献的代码将使用 MIT 许可证。

## 联系方式

如有疑问，请通过 GitHub Issues 联系我们。