# 快速入门指南

本指南将帮助您快速开始学习统计学习，从环境配置到第一个项目，全程指导。

## 5分钟快速上手

### 第1步：克隆仓库

```bash
git clone https://github.com/xianqiangfu/test_gh.git
cd test_gh
```

### 第2步：安装依赖

```bash
pip install -r requirements.txt
```

如果安装速度较慢，可以使用国内镜像：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 第3步：启动 Jupyter

```bash
jupyter notebook
```

### 第4步：打开第一个笔记本

浏览器会自动打开 Jupyter，导航到 `statistical-learning-notes/01-基础概念/` 目录，打开第一个文档。

完成！现在您可以开始学习统计学习了。

---

## 详细环境配置

### 系统要求

- **操作系统**：Windows 10+, macOS 10.14+, 或 Linux
- **Python 版本**：3.8 或更高版本
- **内存**：建议 4GB 以上
- **存储空间**：至少 1GB 可用空间

### Python 安装

#### Windows

1. 访问 [Python 官网](https://www.python.org/downloads/)
2. 下载 Python 3.8 或更高版本
3. 运行安装程序，**重要**：勾选 "Add Python to PATH"
4. 验证安装：
   ```bash
   python --version
   ```

#### macOS

使用 Homebrew 安装：
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 虚拟环境创建（推荐）

创建独立的虚拟环境可以避免依赖冲突：

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 验证虚拟环境
which python  # 或 Windows: where python
```

### 安装 Jupyter

```bash
# 安装 Jupyter Notebook
pip install jupyter

# 或者安装 JupyterLab（推荐）
pip install jupyterlab
```

### 安装必需的 Python 包

```bash
# 安装所有依赖
pip install -r requirements.txt

# 如果缺少 requirements.txt，手动安装核心包
pip install numpy pandas matplotlib seaborn scikit-learn scipy jupyter
```

### 验证安装

创建一个测试脚本 `test_install.py`：

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from scipy import stats

print("✓ 所有包安装成功！")
print(f"NumPy 版本: {np.__version__}")
print(f"Pandas 版本: {pd.__version__}")
print(f"scikit-learn 版本: {sklearn.__version__}")
```

运行测试：
```bash
python test_install.py
```

---

## 第一个项目：线性回归

### 创建你的第一个笔记本

1. 启动 Jupyter：
   ```bash
   jupyter notebook
   ```

2. 在 Jupyter 界面中创建新笔记本：`New → Python 3`

3. 命名笔记本为 `first_linear_regression.ipynb`

### 编写第一个线性回归模型

```python
# 导入必要的库
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 生成一些示例数据
np.random.seed(42)
X = np.random.randn(100, 1) * 10  # 特征
y = 2 * X + 3 + np.random.randn(100, 1) * 2  # 目标值（带噪声）

# 创建并训练线性回归模型
model = LinearRegression()
model.fit(X, y)

# 预测
y_pred = model.predict(X)

# 可视化结果
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, label='实际数据')
plt.plot(X, y_pred, 'r-', linewidth=2, label='预测线')
plt.xlabel('X')
plt.ylabel('y')
plt.title('线性回归示例')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 打印模型参数
print(f"斜率: {model.coef_[0][0]:.2f}")
print(f"截距: {model.intercept_[0]:.2f}")
```

### 运行代码

在 Jupyter 中，按 `Shift + Enter` 运行单元格，或点击工具栏的 "Run" 按钮。

恭喜！你已经完成了第一个机器学习模型！

---

## 学习路线建议

### 零基础学习者

1. **第1周**：数学基础复习（线性代数、微积分、概率论）
2. **第2周**：Python 编程基础（NumPy、Pandas、Matplotlib）
3. **第3周**：开始学习 01-基础概念
4. **第4周**：学习 02-线性模型
5. **后续**：按照 [学习路径](./LEARNING_PATH.md) 继续学习

### 有一定基础的学习者

1. 直接从 [01-基础概念](./statistical-learning-notes/01-基础概念/) 开始
2. 快速浏览熟悉的内容
3. 重点学习不熟悉的章节
4. 完成所有实践项目

### 想快速应用的学习者

1. 直接跳到 [08-实践项目](./statistical-learning-notes/08-实践项目/)
2. 运行项目代码
3. 根据需要回顾相关理论知识
4. 修改代码解决自己的问题

---

## 常用命令速查

### Git 操作

```bash
# 查看仓库状态
git status

# 拉取最新更新
git pull origin main

# 提交更改
git add .
git commit -m "提交信息"
git push origin main
```

### Python/Jupyter 操作

```bash
# 启动 Jupyter Notebook
jupyter notebook

# 启动 JupyterLab
jupyter lab

# 安装新包
pip install package_name

# 查看已安装的包
pip list

# 升级包
pip install --upgrade package_name
```

### 虚拟环境操作

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 退出虚拟环境
deactivate

# 删除虚拟环境（Windows）
rmdir /s venv

# 删除虚拟环境（macOS/Linux）
rm -rf venv
```

---

## Jupyter 使用技巧

### 快捷键

- `Shift + Enter`：运行当前单元格并跳到下一个
- `Ctrl + Enter`：运行当前单元格
- `A`：在上方插入新单元格（命令模式）
- `B`：在下方插入新单元格（命令模式）
- `DD`：删除当前单元格（命令模式）
- `M`：将单元格转为 Markdown（命令模式）
- `Y`：将单元格转为代码（命令模式）

### 常用魔法命令

```python
# 显示所有单元格的运行时间
%%time

# 在单元格中显示绘图结果
%matplotlib inline

# 列出所有魔法命令
%lsmagic
```

### 代码补全

- 按 `Tab` 键触发代码补全
- 在函数名后加 `?` 查看帮助信息
- 在函数名后加 `??` 查看源代码

---

## 数据集准备

### 下载数据集

1. 创建 `data` 目录（如果不存在）：
   ```bash
   mkdir data
   ```

2. 将数据集文件放入 `data` 目录

### 使用示例数据集

许多项目使用 scikit-learn 内置数据集：

```python
from sklearn.datasets import load_iris, load_boston, load_diabetes
import pandas as pd

# 加载鸢尾花数据集
iris = load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris['target'] = iris.target

print(df_iris.head())
```

---

## 调试技巧

### 代码调试

```python
# 使用 pdb 调试器
import pdb; pdb.set_trace()

# 或者使用 ipdb（更好用）
import ipdb; ipdb.set_trace()

# 在 Jupyter 中使用调试器
from IPython.core.debugger import Tracer; Tracer()()
```

### 常见错误处理

```python
# 捕获异常
try:
    # 你的代码
    result = some_function()
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
```

### 查看变量

```python
# 在 Jupyter 中
# 直接输入变量名，按 Shift+Enter
df  # 显示 DataFrame
X.shape  # 显示数组形状
```

---

## 下一步

现在你已经完成了快速入门，可以开始正式学习了：

1. 阅读 [学习路径文档](./LEARNING_PATH.md) 了解完整的学习计划
2. 从 [01-基础概念](./statistical-learning-notes/01-基础概念/) 开始学习
3. 完成每个章节的实践项目
4. 遇到问题查看 [常见问题解答](./FAQ.md)

---

## 需要帮助？

- 查看 [常见问题解答](./FAQ.md)
- 阅读 [学习路径文档](./LEARNING_PATH.md)
- 在 GitHub 上创建 Issue
- 参考推荐的在线资源

祝学习顺利！