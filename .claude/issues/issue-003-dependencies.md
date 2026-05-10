# Issue #3: 添加依赖管理文件

## 问题
笔记中使用了多个 Python 库（numpy, matplotlib, scikit-learn），但没有 `requirements.txt` 或其他依赖管理文件。

## 影响
- 用户不知道需要安装哪些依赖
- 版本兼容性问题
- 无法复现相同的环境

## 建议
添加依赖管理文件。

---

## 实现建议

### 方案 A: requirements.txt（简单）
```txt
numpy>=1.21.0
matplotlib>=3.4.0
scikit-learn>=1.0.0
pandas>=1.3.0
seaborn>=0.11.0
```

### 方案 B: pyproject.toml（现代）
```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "statistical-learning-notes"
version = "0.1.0"
description = "统计学习入门笔记"
requires-python = ">=3.8"
dependencies = [
    "numpy>=1.21.0",
    "matplotlib>=3.4.0",
    "scikit-learn>=1.0.0",
    "pandas>=1.3.0",
    "seaborn>=0.11.0",
]

[project.optional-dependencies]
dev = ["jupyter>=1.0.0", "pytest>=6.0.0"]
```

### 方案 C: environment.yml（Conda）
```yaml
name: statistical-learning
channels:
  - conda-forge
dependencies:
  - python=3.9
  - numpy
  - matplotlib
  - scikit-learn
  - pandas
  - seaborn
  - jupyter
```

---

## 建议
使用 `requirements.txt` + `pyproject.toml` 组合：
- `requirements.txt` 用于快速安装
- `pyproject.toml` 作为项目元数据