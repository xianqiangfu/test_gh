# 贡献指南

感谢你对本项目的兴趣！我们欢迎任何形式的贡献，无论是代码改进、文档完善、Bug 修复，还是新功能的添加。

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

**Issue 模板**：

```markdown
## 问题描述
简要描述你遇到的问题

## 复现步骤
1. 第一步
2. 第二步
3. 第三步

## 预期行为
描述你期望发生什么

## 实际行为
描述实际发生了什么

## 环境信息
- 操作系统: [例如：Windows 10, macOS 11, Ubuntu 20.04]
- Python 版本: [例如：3.8.10]
- 相关包版本: [例如：scikit-learn 1.0.2]

## 其他信息
添加任何其他相关信息，截图、错误日志等
```

### 提交代码

#### 开发流程

1. Fork 本仓库到你的 GitHub 账户
2. 克隆你的 fork：
   ```bash
   git clone https://github.com/YOUR_USERNAME/test_gh.git
   cd test_gh
   ```

3. 添加上游仓库：
   ```bash
   git remote add upstream https://github.com/xianqiangfu/test_gh.git
   ```

4. 创建新的分支进行开发：
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
   # 或
   git checkout -b docs/your-docs-update
   ```

5. 进行修改并测试

6. 提交更改：
   ```bash
   git add .
   git commit -m "描述你的更改"
   ```

7. 推送到你的 fork：
   ```bash
   git push origin feature/your-feature-name
   ```

8. 创建 Pull Request

9. 同步上游更新（可选）：
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   git push origin main
   ```

#### Commit 信息规范

使用清晰的 commit 信息：

- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更新
- `style:` 代码格式（不影响功能）
- `refactor:` 重构
- `test:` 添加测试
- `chore:` 构建/工具链相关
- `perf:` 性能优化
- `ci:` CI 配置相关

**示例**：
```
feat: 添加随机森林算法实现
fix: 修正线性回归代码中的计算错误
docs: 更新 README 添加新章节链接
style: 统一代码格式
refactor: 重构模型评估模块
test: 添加单元测试覆盖回归模型
chore: 更新 requirements.txt
perf: 优化矩阵运算性能
ci: 添加 GitHub Actions 配置
```

**详细的 commit 信息格式**：

```
<type>(<scope>): <subject>

<body>

<footer>
```

**示例**：
```
feat(visualization): 添加决策边界可视化功能

- 添加 plot_decision_boundary 函数
- 支持 2D 数据可视化
- 添加颜色图例

Closes #123
```

#### 代码规范

- **变量命名**：使用有意义的变量名，避免缩写
  ```python
  # 好的命名
  training_data = load_data('train.csv')
  model_accuracy = calculate_accuracy(predictions, true_labels)

  # 不好的命名
  td = load_data('train.csv')
  acc = calculate_accuracy(predictions, true_labels)
  ```

- **函数命名**：使用动词或动词短语
  ```python
  # 好的命名
  def calculate_accuracy(y_true, y_pred):
      pass

  def load_data(file_path):
      pass

  # 不好的命名
  def accuracy(y_true, y_pred):
      pass
  ```

- **添加注释**：解释复杂逻辑和算法
  ```python
  def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
      """
      使用梯度下降法优化线性回归模型

      参数:
          X: 特征矩阵 (n_samples, n_features)
          y: 目标值 (n_samples,)
          learning_rate: 学习率，控制每次迭代的步长
          iterations: 迭代次数

      返回:
          weights: 优化后的权重参数
  """
      # 初始化权重
      weights = np.zeros(X.shape[1])

      # 迭代优化
      for i in range(iterations):
          # 计算预测值
          predictions = np.dot(X, weights)

          # 计算梯度
          errors = predictions - y
          gradients = 2 * np.dot(X.T, errors) / len(y)

          # 更新权重
          weights -= learning_rate * gradients

      return weights
  ```

- **遵循 PEP 8 Python 代码风格**
  - 使用 4 个空格缩进
  - 每行不超过 79 个字符
  - 使用空行分隔函数和类定义
  - 使用文档字符串

- **类型提示**：建议添加类型提示
  ```python
  from typing import List, Tuple, Optional
  import numpy as np

  def preprocess_data(
      data: np.ndarray,
      normalize: bool = True,
      remove_outliers: bool = False
  ) -> Tuple[np.ndarray, Optional[np.ndarray]]:
      """
      预处理数据

      参数:
          data: 输入数据
          normalize: 是否归一化
          remove_outliers: 是否移除异常值

      返回:
          Tuple[处理后的数据, 异常值索引]
      """
      pass
  ```

#### Pull Request 规范

创建 PR 时，请确保：

1. **标题清晰**：简要描述 PR 的目的
2. **描述详细**：在 PR 描述中说明：
   - 做了什么更改
   - 为什么做这些更改
   - 如何测试
   - 相关的 issue 编号

**PR 模板**：

```markdown
## 变更描述
简要描述这个 PR 做了什么更改

## 变更类型
- [ ] Bug 修复
- [ ] 新功能
- [ ] 代码重构
- [ ] 文档更新
- [ ] 性能优化
- [ ] 测试覆盖

## 相关 Issue
Closes #(issue 编号)

## 测试
描述如何测试这个更改：

- [ ] 单元测试通过
- [ ] 手动测试通过
- [ ] 文档已更新

## 截图
如果适用，添加截图或 GIF

## 检查清单
- [ ] 代码遵循项目的代码规范
- [ ] 我已经自测了代码
- [ ] 我已经更新了文档（如果需要）
- [ ] 我的更改不会产生新的警告
```

### 文档贡献

文档是项目的重要组成部分。你可以：

#### 修正错误

- 修正错别字或语法错误
- 修正代码示例中的错误
- 修正链接错误

#### 改进内容

- 改进现有解释，使其更清晰
- 添加更多示例和用例
- 补充图片或图表
- 添加代码注释

#### 翻译内容

- 将文档翻译成其他语言
- 更新现有翻译

#### 扩展内容

- 添加新的章节
- 补充进阶内容
- 添加实践项目
- 推荐新的学习资源

### 添加示例代码

欢迎添加：

- 更多示例代码
- 不同数据集的应用
- 可视化代码
- 性能比较示例
- 实际应用案例

**代码示例规范**：

```python
"""
线性回归示例

本示例演示如何使用 scikit-learn 实现线性回归，
并可视化回归结果。
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 生成示例数据
np.random.seed(42)
X = np.random.randn(100, 1) * 10
y = 2 * X + 3 + np.random.randn(100, 1) * 2

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 创建并训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估模型
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 可视化结果
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, alpha=0.6, label='实际值')
plt.scatter(X_test, y_pred, alpha=0.6, label='预测值')
plt.plot(X_test, y_pred, 'r-', linewidth=2, label='回归线')
plt.xlabel('X')
plt.ylabel('y')
plt.title('线性回归结果')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 打印结果
print(f"均方误差 (MSE): {mse:.2f}")
print(f"R² 分数: {r2:.2f}")
print(f"斜率: {model.coef_[0][0]:.2f}")
print(f"截距: {model.intercept_[0]:.2f}")
```

## 开发环境设置

### 安装开发依赖

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

### 代码格式化

推荐使用以下工具保持代码风格一致：

```bash
# 安装格式化工具
pip install black flake8 isort

# 格式化代码
black .

# 检查代码风格
flake8 .

# 排序导入
isort .
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_linear_regression.py

# 运行特定测试函数
pytest tests/test_linear_regression.py::test_fit_predict

# 显示详细输出
pytest -v

# 生成覆盖率报告
pytest --cov=src --cov-report=html
```

## 项目结构

```
test_gh/
├── README.md                    # 项目说明文档
├── LEARNING_PATH.md             # 学习路径指南
├── QUICK_START.md              # 快速入门指南
├── FAQ.md                      # 常见问题解答
├── CONTRIBUTING.md             # 贡献指南
├── requirements.txt            # Python 依赖包
├── statistical-learning-notes/ # 统计学习笔记主目录
│   ├── 01-基础概念/           # 基础概念和理论
│   ├── 02-线性模型/           # 线性回归、逻辑回归等
│   └── ...
├── data/                      # 数据集目录
├── tests/                     # 测试目录
│   ├── __init__.py
│   ├── test_linear_regression.py
│   └── ...
├── docs/                      # 文档目录
│   ├── images/               # 图片资源
│   └── ...
└── .github/                  # GitHub 配置
    ├── workflows/           # GitHub Actions
    └── PULL_REQUEST_TEMPLATE.md
```

## 代码审查

提交 PR 后，维护者会进行代码审查。请注意：

- 回复审查意见
- 根据反馈进行修改
- 保持开放和友好的态度
- 即使 PR 被拒绝也不要气馁

## 获取帮助

如果在贡献过程中遇到问题：

1. 查看 [常见问题解答](./FAQ.md)
2. 在 GitHub 上创建 Issue
3. 阅读相关章节的文档
4. 参考现有代码的实现

## 行为准则

作为贡献者，请遵守以下准则：

- 尊重他人
- 保持专业和友好
- 接受建设性的批评
- 专注于对社区有益的事情
- 对不同的观点保持开放态度

## 许可证

贡献的代码将使用 MIT 许可证。通过提交代码，你同意你的代码将在 MIT 许可证下发布。

## 致谢

感谢所有贡献者！你的贡献让这个项目变得更好。

---

开始贡献吧！我们期待你的 Pull Request。

如有任何问题，请随时通过 GitHub Issues 联系我们。