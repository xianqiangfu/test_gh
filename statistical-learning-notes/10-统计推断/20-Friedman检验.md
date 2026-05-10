# Friedman检验

## 问题

统计推断部分缺少Friedman检验的学习笔记。这是处理重复测量的重要非参数方法。

## 说明

Friedman检验是重复测量ANOVA的非参数替代方法，用于比较同一对象在不同条件下的差异。

## 检验的定义和原理

Friedman检验由Milton Friedman于1937年提出，是比较多个相关样本的非参数检验方法，也称为"双因素方差分析：无重复-秩次方法"。

### 基本思想

1. 在每个"块"（block）内对观测值进行排序并分配秩次
2. 计算每个"处理"（treatment）的秩和
3. 比较各处理秩和的差异是否显著

### 与其他检验的关系

| 检验方法 | 样本类型 | 处理数 | 等价检验 |
|---------|---------|-------|---------|
| 配对t检验 | 配对 | 2 | Wilcoxon符号秩检验 |
| 重复测量ANOVA | 重复测量 | ≥2 | Friedman检验 |
| 单因素ANOVA | 独立样本 | ≥2 | Kruskal-Wallis检验 |
| 2×2配对 | 配对 | 2 | McNemar检验 |

### 与ANOVA的比较

| 特征 | Friedman检验 | 重复测量ANOVA |
|------|-------------|--------------|
| 统计量 | χᵣ²统计量 | F统计量 |
| 分布假设 | 无 | 正态分布 + 球形假设 |
| 数据类型 | 有序数据 | 连续数据 |
| 对异常值 | 不敏感 | 敏感 |
| 适用场景 | 重复测量、配组设计 | 满足假设的重复测量 |

## 统计量的计算

### 步骤1：整理数据

数据格式：n个对象（blocks），k种处理（treatments）

| 对象 | 处理1 | 处理2 | ... | 处理k |
|------|-------|-------|-----|--------|
| 1 | X₁₁ | X₁₂ | ... | X₁ₖ |
| 2 | X₂₁ | X₂₂ | ... | X₂ₖ |
| ... | ... | ... | ... | ... |
| n | Xₙ₁ | Xₙ₂ | ... | Xₙₖ |

### 步骤2：在每个块内排序

在每个对象内，对k个处理进行排序并分配秩次（1到k）。

对于有相同值的观测值（结），使用平均秩次。

### 步骤3：计算每个处理的秩和

```
Rⱼ = Σrank(Xᵢⱼ), j = 1, ..., k
```

### 步骤4：计算χᵣ²统计量

```
χᵣ² = [12 / (nk(k + 1))] × Σ(Rⱼ²) - 3n(k + 1)
```

其中：
- n：对象数（blocks）
- k：处理数（treatments）
- Rⱼ：第j个处理的秩和

### 步骤5：确定p值

χᵣ²统计量近似服从自由度为k-1的卡方分布。

### 存在结时的修正

当存在结时，需要修正χᵣ²统计量：

```
χᵣ²(修正) = χᵣ² / C

C = 1 - Σ(tᵢⱼ³ - tᵢⱼ) / [nk(k² - 1)]
```

其中tᵢⱼ是第i个块中第j个结中相同值的个数。

## 假设检验步骤

### 步骤1：建立假设

- **原假设（H₀）**：所有处理效果相同（各处理的秩和相等）
- **备择假设（H₁）**：至少有一个处理的效果与其他处理不同

### 步骤2：选择显著性水平

通常选择α = 0.05或α = 0.01

### 步骤3：计算检验统计量

按上述步骤计算χᵣ²值

### 步骤4：确定p值

使用卡方分布

### 步骤5：做出决策

- 如果p < α，拒绝H₀
- 否则，无法拒绝H₀

### 步骤6：事后检验

如果拒绝H₀，需要进行事后检验确定哪些处理有差异。

## 事后检验

当Friedman检验拒绝原假设时，需要进行事后检验确定具体哪些处理之间有显著差异。

### 1. Nemenyi检验

最常用的事后检验方法：

```
q = (R̄ᵢ - R̄ⱼ) / √[k(k + 1) / (6n)]
```

其中R̄ⱼ = Rⱼ / n是第j个处理的平均秩。

### 2. Wilcoxon符号秩检验（配对）

进行所有可能的配对Wilcoxon检验，并调整多重比较问题（如Bonferroni校正）。

### 3. Conover检验

基于t检验的配对比较方法。

## Python实现示例

### 基础Friedman检验

```python
import numpy as np
from scipy import stats

def friedman_test(data, alpha=0.05):
    """
    Friedman检验

    参数:
        data: 二维数组，每行代表一个对象（block），每列代表一个处理（treatment）
        alpha: 显著性水平

    返回:
        result: 包含检验结果的字典
    """
    data = np.array(data)
    n, k = data.shape  # n: 对象数, k: 处理数

    # 在每个对象内排序并分配秩次
    ranks = np.zeros_like(data)
    for i in range(n):
        # 使用rankdata处理结
        ranks[i, :] = stats.rankdata(data[i, :])

    # 计算每个处理的秩和
    R_j = np.sum(ranks, axis=0)

    # 计算χᵣ²统计量
    chi2_r = (12 / (n * k * (k + 1))) * np.sum(R_j**2) - 3 * n * (k + 1)

    # 计算p值（卡方分布）
    p_value = 1 - stats.chi2.cdf(chi2_r, df=k-1)

    reject = p_value < alpha

    # 计算每个处理的平均秩
    mean_ranks = R_j / n

    # 计算处理统计
    treatment_stats = []
    for j in range(k):
        treatment_stats.append({
            'treatment': j + 1,
            'rank_sum': R_j[j],
            'mean_rank': mean_ranks[j]
        })

    return {
        'chi2_r': chi2_r,
        'p_value': p_value,
        'reject_null': reject,
        'df': k - 1,
        'n_blocks': n,
        'k_treatments': k,
        'treatment_stats': treatment_stats,
        'ranks': ranks
    }

# 示例1：比较四种教学方法的效果（同一个学生用四种方法学习）
np.random.seed(42)
# 10个学生，4种教学方法
# 每行代表一个学生，每列代表一种方法
teaching_methods = np.array([
    [78, 82, 75, 88],
    [85, 79, 83, 90],
    [72, 76, 70, 80],
    [90, 85, 88, 92],
    [68, 72, 65, 78],
    [82, 80, 79, 86],
    [75, 78, 73, 82],
    [88, 85, 86, 91],
    [70, 74, 68, 77],
    [83, 80, 82, 89]
])

result = friedman_test(teaching_methods, alpha=0.05)

print("Friedman检验结果（教学方法比较）:")
print(f"χᵣ²统计量: {result['chi2_r']:.4f}")
print(f"p值: {result['p_value']:.4f}")
print(f"自由度: {result['df']}")
print(f"是否拒绝原假设: {result['reject_null']}")
print(f"\n各处理统计:")
for stat in result['treatment_stats']:
    print(f"  方法{stat['treatment']}: 秩和={stat['rank_sum']}, 平均秩={stat['mean_rank']:.2f}")
```

### 使用scipy的friedmanchisquare函数

```python
# 示例2：使用scipy的friedmanchisquare函数
chi2, p_value = stats.friedmanchisquare(*teaching_methods.T)

print(f"\n使用scipy.friedmanchisquare的结果:")
print(f"χᵣ²统计量: {chi2:.4f}")
print(f"p值: {p_value:.4f}")
```

### 与重复测量ANOVA的比较

```python
# 示例3：比较Friedman检验与重复测量ANOVA
np.random.seed(42)

# 正态数据
normal_data1 = np.random.normal(50, 5, 20)
normal_data2 = normal_data1 + np.random.normal(2, 3, 20)
normal_data3 = normal_data1 + np.random.normal(4, 3, 20)
normal_rm = np.column_stack([normal_data1, normal_data2, normal_data3])

# 偏态数据
skewed_data1 = np.random.exponential(20, 20)
skewed_data2 = skewed_data1 + np.random.exponential(5, 20)
skewed_data3 = skewed_data1 + np.random.exponential(10, 20)
skewed_rm = np.column_stack([skewed_data1, skewed_data2, skewed_data3])

print("\n正态数据比较:")
print("重复测量ANOVA（使用Greenhouse-Geisser校正）:")
# 注意：scipy没有直接的重复测量ANOVA，需要使用statsmodels
from statsmodels.stats.anova import AnovaRM
import pandas as pd

# 创建数据框
df_normal = pd.DataFrame({
    'subject': np.repeat(range(20), 3),
    'treatment': np.tile(['A', 'B', 'C'], 20),
    'value': normal_rm.flatten()
})

try:
    anova_rm = AnovaRM(df_normal, 'value', 'subject', within=['treatment'])
    res = anova_rm.fit()
    print(res)
except:
    print("需要statsmodels库进行重复测量ANOVA")

print("\nFriedman检验:")
friedman_normal = friedman_test(normal_rm)
print(f"p值: {friedman_normal['p_value']:.4f}")

print("\n偏态数据比较:")
print("Friedman检验:")
friedman_skewed = friedman_test(skewed_rm)
print(f"p值: {friedman_skewed['p_value']:.4f}")
```

### 事后检验（Nemenyi检验）

```python
def nemenyi_posthoc(ranks, alpha=0.05):
    """
    Nemenyi事后检验

    参数:
        ranks: 秩次矩阵（n×k）
        alpha: 显著性水平

    返回:
        comparisons: 比较结果列表
    """
    n, k = ranks.shape

    # 计算每个处理的平均秩
    mean_ranks = np.mean(ranks, axis=0)

    # 计算标准误差
    se = np.sqrt(k * (k + 1) / (6 * n))

    # 进行成对比较
    comparisons = []
    comparisons_count = k * (k - 1) / 2

    # 查q临界值（学生化极差分布）
    # 近似使用t分布
    df = (k - 1) * (n - 1)
    q_critical = stats.t.ppf(1 - alpha / (2 * comparisons_count), df) * np.sqrt(2)

    for i in range(k):
        for j in range(i + 1, k):
            rank_diff = mean_ranks[i] - mean_ranks[j]

            # 计算q统计量
            q_stat = rank_diff / se

            comparisons.append({
                'treatments': (i + 1, j + 1),
                'q_statistic': q_stat,
                'rank_diff': rank_diff,
                'critical_value': q_critical,
                'significant': abs(rank_diff) > q_critical
            })

    return comparisons

# 执行事后检验
if result['reject_null']:
    print("\n事后检验（Nemenyi检验）:")

    comparisons = nemenyi_posthoc(result['ranks'])

    for comp in comparisons:
        print(f"\n方法{comp['treatments'][0]} vs 方法{comp['treatments'][1]}:")
        print(f"  q统计量: {comp['q_statistic']:.4f}")
        print(f"  平均秩差: {comp['rank_diff']:.2f}")
        print(f"  临界值: {comp['critical_value']:.4f}")
        print(f"  是否显著: {'是' if comp['significant'] else '否'}")
```

### 效应量（Kendall's W）

```python
def calculate_kendall_w(chi2_r, n, k):
    """
    计算Kendall's W一致性系数

    参数:
        chi2_r: χᵣ²统计量
        n: 对象数
        k: 处理数

    返回:
        W: Kendall's W一致性系数
    """
    W = chi2_r / (n * (k - 1))
    return W

# 计算Kendall's W
kendall_w = calculate_kendall_w(result['chi2_r'], result['n_blocks'], result['k_treatments'])

print(f"\nKendall's W一致性系数: {kendall_w:.4f}")
print("W的解释:")
print("  0: 完全不一致（各处理效果相同）")
print("  0.1: 小一致性")
print("  0.3: 中等一致性")
print("  0.5: 大一致性")
print("  1: 完全一致（所有对象排序相同）")
```

### 可视化

```python
import matplotlib.pyplot as plt

def plot_friedman_results(data, labels=None, title="Friedman检验：重复测量比较"):
    """可视化Friedman检验结果"""
    if labels is None:
        labels = [f'处理{i+1}' for i in range(data.shape[1])]

    n, k = data.shape

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 处理平均值的条形图
    treatment_means = np.mean(data, axis=0)
    treatment_stds = np.std(data, axis=0)

    x_pos = np.arange(k)
    bars = axes[0].bar(x_pos, treatment_means, yerr=treatment_stds,
                      capsize=5, alpha=0.7,
                      color=['skyblue', 'lightgreen', 'salmon', 'gold'][:k])
    axes[0].set_xticks(x_pos)
    axes[0].set_xticklabels(labels)
    axes[0].set_ylabel('值')
    axes[0].set_title(f'{title} - 各处理平均值')
    axes[0].grid(axis='y', alpha=0.3)

    # 添加数值标签
    for bar, mean in zip(bars, treatment_means):
        height = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width()/2., height,
                    f'{mean:.1f}', ha='center', va='bottom')

    # 折线图（显示每个对象在各处理下的变化）
    for i in range(min(10, n)):  # 最多显示10个对象
        axes[1].plot(range(k), data[i, :], marker='o',
                    alpha=0.5, label=f'对象{i+1}' if i < 3 else None)

    axes[1].set_xticks(range(k))
    axes[1].set_xticklabels(labels)
    axes[1].set_ylabel('值')
    axes[1].set_title(f'{title} - 对象变化轨迹（前3个对象）')
    axes[1].grid(True, alpha=0.3)
    if n >= 3:
        axes[1].legend()

    plt.tight_layout()
    plt.show()

# 可视化教学方法比较
plot_friedman_results(teaching_methods,
                     ['方法A', '方法B', '方法C', '方法D'],
                     "教学方法效果比较")
```

## 注意事项

1. **块内独立性**：每个块（对象）内的观测值应该相关，不同块之间应该独立
2. **有序性**：数据至少应该是有序的
3. **样本量**：建议n ≥ 10且k ≥ 3
4. **结的处理**：存在结时需要使用平均秩次，并可能需要修正统计量
5. **球形假设的非参数替代**：Friedman检验不需要球形假设，这是其相对于重复测量ANOVA的优势

## Friedman检验的适用场景

1. **重复测量设计**：同一对象在不同时间点或条件下的测量
2. **配组设计**：将对象配组，每组内随机分配不同处理
3. **交叉设计**：每个对象按顺序接受所有处理
4. **判断者一致性**：多个判断者对同一组对象进行评分

## Friedman检验的扩展

### 1. Page检验

用于检验有序的组间趋势（如剂量递增效应）。

### 2. Durbin检验

用于不完全区组设计的非参数方法。

### 3. Quade检验

另一种处理重复测量的非参数方法，在区组间差异较大时更有效。

## 参考资源

- 非参数统计学教材
- 重复测量设计方法
- scipy.stats文档
- scipy.stats.friedmanchisquare文档
- Friedman, M. (1937). The use of ranks to avoid the assumption of normality implicit in the analysis of variance
- Conover, W. J. (1999). Practical nonparametric statistics
