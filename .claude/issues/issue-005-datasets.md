# Issue #5: 添加示例数据集

## 问题
实践项目章节提到使用真实数据集，但仓库中没有提供示例数据。

## 影响
- 用户无法直接运行实践代码
- 需要自行寻找数据集
- 学习门槛提高

## 建议
添加常用的机器学习示例数据集或提供数据获取脚本。

---

## 实现建议

### 方案 A: 内置小数据集（推荐）
```
statistical-learning-notes/
  data/
    iris.csv          # 经典分类数据集
    boston_housing.csv # 回归数据集
    breast_cancer.csv  # 医疗分类数据集
    wine.csv          # 多分类数据集
```

### 方案 B: 数据获取脚本
```python
# data/download_datasets.py
from sklearn.datasets import load_iris, load_breast_cancer, load_wine
import pandas as pd
import os

datasets = {
    'iris.csv': load_iris,
    'breast_cancer.csv': load_breast_cancer,
    'wine.csv': load_wine
}

for filename, loader in datasets.items():
    data = loader()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    df.to_csv(f'data/{filename}', index=False)
```

### 方案 C: 使用 scikit-learn 内置数据集
在代码中直接使用：
```python
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
```

---

## 建议
采用方案 A + 方案 C 的组合：
- 提供预下载的小数据集
- 同时在代码中展示如何使用 scikit-learn 内置数据集