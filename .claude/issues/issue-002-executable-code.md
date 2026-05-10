# Issue #2: 创建可执行的代码文件

## 问题
笔记中包含大量代码示例，但缺少可执行的 Python 文件或 Jupyter Notebook。用户无法直接运行和验证代码。

## 影响
- 学习体验下降
- 用户需要手动复制代码
- 难以调试和修改

## 建议
为每个实践项目和重要算法章节创建可执行的代码文件。

---

## 实现建议

### 方案 A: 使用 Jupyter Notebook
```
statistical-learning-notes/
  code/
    01-linear-regression.ipynb
    02-logistic-regression.ipynb
    03-kmeans.ipynb
    04-decision-tree.ipynb
    05-svm.ipynb
    08-visualization.ipynb
```

### 方案 B: 使用独立 Python 脚本
```
statistical-learning-notes/
  code/
    linear_regression/
      __init__.py
      train.py
      evaluate.py
    ...
```

### 优先级（高到低）
1. `01-实现线性回归.ipynb`
2. `02-真实数据集分类任务.ipynb`
3. `03-可视化决策边界.ipynb`
4. `04-比较不同模型性能.ipynb`

---

## 相关章节
- `08-实践项目/01-实现线性回归.md`
- `08-实践项目/02-真实数据集分类任务.md`
- `08-实践项目/03-可视化决策边界.md`
- `08-实践项目/04-比较不同模型性能.md`