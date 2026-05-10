# McNemar检验

## 问题

统计推断部分缺少McNemar检验的学习笔记。这是处理配对分类数据的重要方法。

## 说明

McNemar检验用于比较两个配对样本（如同一对象的前后测量）的分类变量，特别适用于2×2列联表的分析。

## McNemar检验的定义和应用场景

McNemar检验是用于分析配对分类数据的非参数检验方法，主要用于比较两个相关样本的二分类结果。

### 应用场景

1. **前后对比研究**：同一对象接受治疗前后
2. **配对病例对照研究**：匹配的病例和对照组
3. **两种诊断方法比较**：同一批样本用两种方法诊断
4. **匹配设计实验**：配对设计的干预实验
5. **流行病学研究**：暴露前后或配对的暴露状态

### 2×2列联表的结构

对于配对的二分类数据，可以构建如下2×2列联表：

| | 方法B = 正 | 方法B = 负 | 合计 |
|---|-----------|-----------|------|
| 方法A = 正 | a | b | a + b |
| 方法A = 负 | c | d | c + d |
| 合计 | a + c | b + d | n |

其中：
- a：两种方法都为正的频数（一致）
- b：方法A为正、方法B为负的频数（不一致）
- c：方法A为负、方法B为正的频数（不一致）
- d：两种方法都为负的频数（一致）

**关键**：McNemar检验只关注不一致的对（b和c），一致的对（a和d）不参与检验。

## 统计量的计算

### 原假设和备择假设

- **原假设（H₀）**：两种方法/条件没有差异，即P(A=正, B=负) = P(A=负, B=正)，即 b = c
- **备择假设（H₁）**：两种方法/条件有差异

### 大样本情况（b + c ≥ 25）

使用卡方近似：

```
χ² = (|b - c| - 1)² / (b + c)
```

其中-1是连续性校正（Yates校正）。

这个统计量在H₀下近似服从自由度为1的卡方分布。

### 小样本情况（b + c < 25）

使用二项分布精确检验：

检验统计量T取b和c中的较小值：
```
T = min(b, c)
```

在H₀下，T服从二项分布B(n = b + c, p = 0.5)

双侧检验的p值：
```
p = 2 × Σ C(b + c, k) × (0.5)^(b + c)
```
其中k ≤ T

### 效应量（Odds Ratio）

McNemar检验可以计算配对数据的odds ratio：

```
OR = b / c
```

解释：
- OR = 1：两种方法无差异
- OR > 1：方法A倾向于得到阳性结果
- OR < 1：方法B倾向于得到阳性结果

## 检验步骤

### 步骤1：构建2×2列联表

整理数据，计算a、b、c、d的值

### 步骤2：检查样本量

- 如果b + c ≥ 25：使用卡方近似
- 如果b + c < 25：使用二项精确检验

### 步骤3：计算检验统计量

根据样本量选择合适的统计量

### 步骤4：计算p值

使用卡方分布或二项分布

### 步骤5：做出决策

比较p值与显著性水平α

### 步骤6：解释结果

在实际应用背景下解释

## McNemar检验与卡方检验的关系

| 特征 | McNemar检验 | 独立样本卡方检验 |
|------|------------|----------------|
| 样本类型 | 配对样本 | 独立样本 |
| 研究设计 | 前后对比、匹配设计 | 完全随机设计 |
| 使用信息 | 只利用不一致对（b, c） | 利用所有信息 |
| 自由度 | 1 | 1 |
| 应用场景 | 同一对象两次测量 | 两个独立组 |

**重要**：不要混淆McNemar检验和独立性卡方检验！
- 独立性卡方检验用于独立样本
- McNemar检验用于配对样本

## 小样本时的精确检验

当b + c很小时（通常 < 25），卡方近似不准确，应使用二项分布精确检验：

```python
# 精确检验的p值计算
from scipy.stats import binom

def mcnemar_exact(b, c, alternative='two-sided'):
    """McNemar精确检验"""
    n = b + c
    T = min(b, c)

    if alternative == 'two-sided':
        # 双侧检验：计算概率小于等于当前观察值的概率
        p_value = 2 * binom.cdf(T, n, 0.5)
        # 修正：p值不能超过1
        p_value = min(p_value, 1.0)
    elif alternative == 'greater':
        p_value = binom.cdf(min(b, c), n, 0.5)
    elif alternative == 'less':
        p_value = binom.cdf(min(b, c), n, 0.5)

    return p_value
```

## Python实现示例

### 基础McNemar检验

```python
import numpy as np
from scipy import stats
from scipy.stats import chi2, binom

def mcnemar_test(a, b, c, d, alpha=0.05, correction=True, alternative='two-sided'):
    """
    McNemar检验

    参数:
        a, b, c, d: 2×2列联表的四个格频数
        alpha: 显著性水平
        correction: 是否使用连续性校正
        alternative: 备择假设类型

    返回:
        result: 包含检验结果的字典
    """
    n = b + c  # 不一致对的数目

    if n == 0:
        return {
            'statistic': 0,
            'p_value': 1.0,
            'reject_null': False,
            'method': 'No discordant pairs'
        }

    if n >= 25:
        # 大样本：卡方近似
        if correction:
            # Yates连续性校正
            chi2_stat = (abs(b - c) - 1)**2 / n
        else:
            chi2_stat = (b - c)**2 / n

        p_value = 1 - chi2.cdf(chi2_stat, df=1)
        statistic = chi2_stat
        method = 'Chi-square approximation'
    else:
        # 小样本：二项分布精确检验
        T = min(b, c)
        p_value = binom.cdf(T, n, 0.5)

        if alternative == 'two-sided':
            p_value = 2 * p_value
            p_value = min(p_value, 1.0)

        statistic = T
        method = 'Binomial exact test'

    # 计算odds ratio
    odds_ratio = b / c if c > 0 else float('inf')

    reject = p_value < alpha

    return {
        'statistic': statistic,
        'p_value': p_value,
        'reject_null': reject,
        'method': method,
        'odds_ratio': odds_ratio,
        'confusion_matrix': [[a, b], [c, d]]
    }

# 示例1：两种诊断方法的比较
# a=两种方法都阳性, b=方法A阳性B阴性, c=方法A阴性B阳性, d=两种方法都阴性
a, b, c, d = 85, 10, 5, 100

result = mcnemar_test(a, b, c, d, alpha=0.05)

print("McNemar检验结果（诊断方法比较）:")
print(f"混淆矩阵:")
print(f"  a(都阳性): {a}, b(A阳性B阴性): {b}")
print(f"  c(A阴性B阳性): {c}, d(都阴性): {d}")
print(f"检验统计量: {result['statistic']:.4f}")
print(f"p值: {result['p_value']:.4f}")
print(f"Odds Ratio: {result['odds_ratio']:.4f}")
print(f"检验方法: {result['method']}")
print(f"是否拒绝原假设: {result['reject_null']}")
```

### 使用scipy的mcnemar函数

```python
from statsmodels.stats.contingency_tables import mcnemar

# 创建2×2列联表
table = np.array([[a, b], [c, d]])

# 执行McNemar检验
result = mcnemar(table, exact=False, correction=True)

print(f"\n使用scipy的McNemar检验:")
print(f"卡方统计量: {result.statistic:.4f}")
print(f"p值: {result.pvalue:.4f}")
```

### 前后对比研究

```python
# 示例2：药物治疗前后的效果
# 患者治疗后是否痊愈
# a=前后都有效, b=前无效后有效, c=前有效后无效, d=前后都无效
a, b, c, d = 20, 35, 10, 15

result = mcnemar_test(a, b, c, d, alpha=0.05)

print("\nMcNemar检验结果（药物治疗前后对比）:")
print(f"治疗有效变化:")
print(f"  无效→有效: {b}")
print(f"  有效→无效: {c}")
print(f"卡方统计量: {result['statistic']:.4f}")
print(f"p值: {result['p_value']:.4f}")
print(f"Odds Ratio: {result['odds_ratio']:.4f}")
print(f"是否拒绝原假设: {result['reject_null']}")
```

### 小样本精确检验

```python
# 示例3：小样本情况
a, b, c, d = 5, 3, 1, 8

result = mcnemar_test(a, b, c, d, alpha=0.05)

print("\nMcNemar检验结果（小样本）:")
print(f"不一致对数: {b + c}")
print(f"检验方法: {result['method']}")
print(f"检验统计量: {result['statistic']}")
print(f"p值: {result['p_value']:.4f}")
print(f"是否拒绝原假设: {result['reject_null']}")
```

### 多分类扩展（Bowker检验）

对于多于两个类别的配对分类数据，可以使用Bowker检验：

```python
from statsmodels.stats.contingency_tables import mcnemar

# 创建k×k列联表（k>2）
# 例如：三种诊断结果的比较
#           诊断B: 良好  中等  差
# 诊断A: 良好    20     5    2
#         中等     8    15    3
#         差       2     4   10

table_kxk = np.array([
    [20, 5, 2],
    [8, 15, 3],
    [2, 4, 10]
])

# 使用mcnemar函数处理对称矩阵
# 注意：scipy的mcnemar主要用于2×2，对于k×k需要其他方法

# 对于k×k情况，需要使用其他方法或自行实现Bowker检验
print("\n多分类情况（Bowker检验）:")
print("对于k×k列联表，需要使用Bowker检验或其他扩展方法")
```

### 可视化

```python
import matplotlib.pyplot as plt

def plot_mcnemar_table(a, b, c, d, title="McNemar检验列联表"):
    """可视化2×2列联表"""
    fig, ax = plt.subplots(figsize=(8, 6))

    # 创建表格
    table = [[f'a = {a}', f'b = {b}'],
             [f'c = {c}', f'd = {d}']]

    # 绘制热图
    heatmap = ax.imshow([[a, b], [c, d]], cmap='Blues', alpha=0.7)

    # 添加标签
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(['方法B = 正', '方法B = 负'])
    ax.set_yticklabels(['方法A = 正', '方法A = 负'])

    # 在每个格子中添加文本
    for i in range(2):
        for j in range(2):
            text = ax.text(j, i, table[i][j],
                          ha="center", va="center", color="black", fontsize=12)

    # 添加颜色条
    plt.colorbar(heatmap)

    # 标记不一致对
    ax.annotate('不一致对', xy=(1, 0), xytext=(0.5, -0.2),
                arrowprops=dict(arrowstyle='->', color='red'),
                ha='center', fontsize=10, color='red')
    ax.annotate('不一致对', xy=(0, 1), xytext=(0.5, -0.2),
                arrowprops=dict(arrowstyle='->', color='red'),
                ha='center', fontsize=10, color='red')

    plt.title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# 可视化第一个示例
plot_mcnemar_table(85, 10, 5, 100, "两种诊断方法比较")
```

## 注意事项

1. **配对要求**：必须是配对数据，而非独立样本
2. **二元分类**：标准McNemar检验只适用于二分类变量
3. **不一致对**：只有不一致对（b和c）参与检验，一致对提供的信息有限
4. **样本量**：小样本时使用精确检验，大样本使用卡方近似
5. **连续性校正**：大样本时建议使用Yates连续性校正
6. **零不一致对**：如果b + c = 0，检验无法进行

## McNemar检验的扩展

### 1. McNemar-Bowker检验

用于多于两个类别的配对分类数据（k×k列联表）

### 2. Stuart-Maxwell检验

另一种处理k×k配对分类数据的方法

### 3. Cox-Stuart趋势检验

用于检测配对数据中的趋势

## 参考资源

- 医学统计学相关资料
- 配对数据分析方法
- McNemar, Q. (1947). "Note on the sampling error of the difference between correlated proportions or percentages"
- statsmodels文档
- Siegel, S., & Castellan, N. J. (1988). Nonparametric statistics for the behavioral sciences
