# 示例数据集

本目录包含项目使用的示例数据集。

## 数据集加载工具

### dataset_loader.py

统一的数据集加载和预处理工具模块，支持多种真实数据集。

支持的数据集：
- **Iris 鸢尾花数据集**：分类任务，150 样本，4 特征
- **Boston 房价数据集**：回归任务，506 样本，13 特征
- **Wine 葡萄酒数据集**：分类任务，178 样本，13 特征
- **Breast Cancer 乳腺癌数据集**：分类任务，569 样本，30 特征

使用方法：
```python
from data.dataset_loader import load_dataset, get_prepared_data

# 加载原始数据集
X, y = load_dataset('iris')

# 获取预处理后的完整数据集（自动划分训练集和测试集）
data = get_prepared_data('boston', test_size=0.2, standardize=True)
```

## 文件说明

### iris.csv

经典的鸢尾花数据集，包含 150 个样本，分为三个品种：
- setosa（山鸢尾）
- versicolor（变色鸢尾）
- virginica（维吉尼亚鸢尾）

每个样本包含 4 个特征：
- sepal_length：花萼长度（cm）
- sepal_width：花萼宽度（cm）
- petal_length：花瓣长度（cm）
- petal_width：花瓣宽度（cm）

该数据集可用于：
- 分类任务练习
- 可视化学习
- 模型性能比较
- 特征工程实践

### 其他数据集

以下数据集通过 `dataset_loader.py` 从 sklearn.datasets 加载：

#### Boston 房价数据集
- **任务类型**：回归
- **样本数量**：506
- **特征数量**：13
- **目标变量**：MEDV（自住房屋房价的中位数）
- **用途**：回归任务练习、特征工程、模型评估

#### Wine 葡萄酒数据集
- **任务类型**：分类
- **样本数量**：178
- **特征数量**：13
- **类别数量**：3
- **用途**：多分类任务练习、葡萄酒质量分析

#### Breast Cancer 乳腺癌数据集
- **任务类型**：分类
- **样本数量**：569
- **特征数量**：30
- **类别数量**：2（恶性/良性）
- **用途**：二分类任务练习、医学数据分析