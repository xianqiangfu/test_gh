# Kruskal-Wallis检验

## 问题

统计推断部分缺少Kruskal-Wallis检验的学习笔记。这是比较多个组的重要非参数方法。

## 说明

Kruskal-Wallis检验是单因素ANOVA的非参数替代方法，用于比较三个或更多独立组的分布差异。

## 检验的定义和原理

Kruskal-Wallis检验由William Kruskal和W. Allen Wallis于1952年提出，是比较多个独立样本的非参数检验方法。

### 基本思想

1. 将所有组的数据合并
2. 对所有数据进行排序并分配秩次
3. 计算每组的秩和
4. 比较各组秩和的差异是否显著

### 与ANOVA的比较

| 特征 | Kruskal-Wallis检验 | 单因素ANOVA |
|------|-------------------|------------|
| 统计量 | H统计量 | F统计量 |
| 分布假设 | 无 | 正态分布 |
| 方差齐性 | 不需要 | 需要 |
| 检验功效 | 较低（正态时） | 较高（正态时） |
| 对异常值 | 不敏感 | 敏感 |
| 数据类型 | 有序数据 | 连续数据 |

### 与其他检验的关系

- **2组情况**：Kruskal-Wallis检验等价于Wilcoxon秩和检验
- **2组情况**：H统计量与Z统计量的关系：H = Z²

## 统计量的计算

### 步骤1：合并并排序

将k个样本的数据合并为一个样本，并从小到大排序。

### 步骤2：分配秩次

为每个观测值分配秩次。对于有相同值的观测值（结），使用平均秩次。

### 步骤3：计算每组的秩和

计算第j组的秩和：
```
Rⱼ = Σrank(Xᵢⱼ)
```

### 步骤4：计算每组平均秩

```
R̄ⱼ = Rⱼ / nⱼ
```

其中nⱼ是第j组的样本量。

### 步骤5：计算H统计量

```
H = [12 / (N(N + 1))] × Σ[nⱼ(R̄ⱼ - R̄)²]
```

其中：
- N = Σnⱼ：总样本量
- R̄ = (N + 1) / 2：总平均秩

等价公式：

```
H = [12 / (N(N + 1))] × Σ[Rⱼ² / nⱼ] - 3(N + 1)
```

### 步骤6：确定p值

**无结或结较少**：H统计量近似服从自由度为k-1的卡方分布

**存在结时**：修正H统计量：

```
H_c = H / C

C = 1 - Σ(tⱼ³ - tⱼ) / (N³ - N)
```

其中tⱼ是第j个结中相同值的个数

## 假设检验步骤

### 步骤1：建立假设

- **原假设（H₀）**：所有组来自相同的分布
- **备择假设（H₁）**：至少有一组分布与其他组不同

### 步骤2：选择显著性水平

通常选择α = 0.05或α = 0.01

### 步骤3：计算检验统计量

按上述步骤计算H值

### 步骤4：确定p值

使用卡方分布

### 步骤5：做出决策

- 如果p < α，拒绝H₀
- 否则，无法拒绝H₀

### 步骤6：事后检验

如果拒绝H₀，需要进行事后检验确定哪些组有差异。

## 事后检验

当Kruskal-Wallis检验拒绝原假设时，需要进行事后检验确定具体哪些组之间有显著差异。

### 1. Dunn检验

最常用的事后检验方法：

```
Z = (R̄ᵢ - R̄ⱼ) / √[N(N + 1)/12 × (1/nᵢ + 1/nⱼ)]
```

### 2. Nemenyi检验

类似于Tukey检验，但用于秩次数据。

### 3. 成对Wilcoxon检验

进行所有可能的成对Wilcoxon检验，并调整多重比较问题（如Bonferroni校正）。

### 4. Conover检验

基于t检验的配对比较方法。

## Python实现示例

### 基础Kruskal-Wallis检验

```python
import numpy as np
from scipy import stats

def kruskal_wallis_test(*groups, alpha=0.05):
    """
    Kruskal-Wallis检验

    参数:
        groups: 多个独立样本
        alpha: 显著性水平

    返回:
        result: 包含检验结果的字典
    """
    # 合并所有数据
    all_data = np.concatenate(groups)

    # 分配秩次（处理结）
    ranks = stats.rankdata(all_data)

    # 计算总样本量
    N = len(all_data)
    k = len(groups)

    # 计算每组的秩和
    start_idx = 0
    group_stats = []
    for i, group in enumerate(groups):
        n = len(group)
        end_idx = start_idx + n
        group_ranks = ranks[start_idx:end_idx]
        rank_sum = np.sum(group_ranks)
        mean_rank = rank_sum / n

        group_stats.append({
            'group': i + 1,
            'n': n,
            'rank_sum': rank_sum,
            'mean_rank': mean_rank
        })

        start_idx = end_idx

    # 计算H统计量
    sum_term = np.sum([stat['rank_sum']**2 / stat['n'] for stat in group_stats])
    H = (12 / (N * (N + 1))) * sum_term - 3 * (N + 1)

    # 计算p值（卡方分布）
    p_value = 1 - stats.chi2.cdf(H, df=k-1)

    reject = p_value < alpha

    return {
        'H_statistic': H,
        'p_value': p_value,
        'reject_null': reject,
        'df': k - 1,
        'group_stats': group_stats,
        'total_n': N
    }

# 示例1：比较三种教学方法的效果
np.random.seed(42)
method_A = np.array([78, 82, 75, 88, 90, 85, 79, 83, 77, 86])
method_B = np.array([70, 75, 72, 78, 80, 73, 71, 76, 74, 79])
method_C = np.array([85, 88, 82, 90, 87, 83, 84, 89, 86, 91])

result = kruskal_wallis_test(method_A, method_B, method_C, alpha=0.05)

print("Kruskal-Wallis检验结果（教学方法比较）:")
print(f"H统计量: {result['H_statistic']:.4f}")
print(f"p值: {result['p_value']:.4f}")
print(f"自由度: {result['df']}")
print(f"是否拒绝原假设: {result['reject_null']}")
print(f"\n各组统计:")
for stat in result['group_stats']:
    print(f"  方法{stat['group']}: n={stat['n']}, 秩和={stat['rank_sum']}, 平均秩={stat['mean_rank']:.2f}")
```

### 使用scipy的kruskal函数

```python
# 示例2：使用scipy的kruskal函数
H_stat, p_value = stats.kruskal(method_A, method_B, method_C)

print(f"\n使用scipy.kruskal的结果:")
print(f"H统计量: {H_stat:.4f}")
print(f"p值: {p_value:.4f}")
```

### 与ANOVA的比较

```python
# 示例3：比较Kruskal-Wallis检验与ANOVA
np.random.seed(42)

# 正态数据
normal_data1 = np.random.normal(50, 5, 20)
normal_data2 = np.random.normal(55, 5, 20)
normal_data3 = np.random.normal(60, 5, 20)

# 偏态数据
skewed_data1 = np.random.exponential(20, 20)
skewed_data2 = np.random.exponential(25, 20)
skewed_data3 = np.random.exponential(30, 20)

print("\n正态数据比较:")
print("单因素ANOVA:")
f_stat, f_p = stats.f_oneway(normal_data1, normal_data2, normal_data3)
print(f"p值: {f_p:.4f}")

print("\nKruskal-Wallis检验:")
kw_result = kruskal_wallis_test(normal_data1, normal_data2, normal_data3)
print(f"p值: {kw_result['p_value']:.4f}")

print("\n偏态数据比较:")
print("单因素ANOVA:")
f_stat2, f_p2 = stats.f_oneway(skewed_data1, skewed_data2, skewed_data3)
print(f"p值: {f_p2:.4f}")

print("\nKruskal-Wallis检验:")
kw_result2 = kruskal_wallis_test(skewed_data1, skewed_data2, skewed_data3)
print(f"p值: {kw_result2['p_value']:.4f}")
```

### 事后检验（Dunn检验）

```python
def dunn_posthoc(groups, ranks, alpha=0.05):
    """
    Dunn事后检验

    参数:
        groups: 各组数据
        ranks: 所有数据的秩次
        alpha: 显著性水平

    返回:
        comparisons: 比较结果列表
    """
    N = sum(len(group) for group in groups)
    k = len(groups)

    # 计算每组的平均秩
    group_mean_ranks = []
    start_idx = 0
    for group in groups:
        n = len(group)
        end_idx = start_idx + n
        group_ranks = ranks[start_idx:end_idx]
        mean_rank = np.mean(group_ranks)
        group_mean_ranks.append((mean_rank, n))
        start_idx = end_idx

    # 进行成对比较
    comparisons = []
    comparisons_count = k * (k - 1) / 2

    # Bonferroni校正
    adjusted_alpha = alpha / comparisons_count

    for i in range(k):
        for j in range(i + 1, k):
            mean_rank_i, n_i = group_mean_ranks[i]
            mean_rank_j, n_j = group_mean_ranks[j]

            # 计算Z统计量
            se = np.sqrt(N * (N + 1) / 12 * (1/n_i + 1/n_j))
            z_stat = (mean_rank_i - mean_rank_j) / se

            # 计算p值
            p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

            comparisons.append({
                'groups': (i + 1, j + 1),
                'z_statistic': z_stat,
                'p_value': p_value,
                'adjusted_alpha': adjusted_alpha,
                'significant': p_value < adjusted_alpha,
                'rank_diff': mean_rank_i - mean_rank_j
            })

    return comparisons

# 执行事后检验
if result['reject_null']:
    print("\n事后检验（Dunn检验）:")

    all_data = np.concatenate([method_A, method_B, method_C])
    ranks = stats.rankdata(all_data)

    comparisons = dunn_posthoc([method_A, method_B, method_C], ranks)

    for comp in comparisons:
        print(f"\n方法{comp['groups'][0]} vs 方法{comp['groups'][1]}:")
        print(f"  Z统计量: {comp['z_statistic']:.4f}")
        print(f"  p值: {comp['p_value']:.4f}")
        print(f"  校正后α: {comp['adjusted_alpha']:.4f}")
        print(f"  是否显著: {'是' if comp['significant'] else '否'}")
        print(f"  平均秩差: {comp['rank_diff']:.2f}")
```

### 效应量（Eta-squared）

```python
def calculate_eta_squared(H, N, k):
    """
    计算Kruskal-Wallis检验的效应量

    参数:
        H: H统计量
        N: 总样本量
        k: 组数

    返回:
        eta_squared: 效应量
    """
    eta_squared = (H - k + 1) / (N - k)
    return eta_squared

# 计算效应量
eta_sq = calculate_eta_squared(result['H_statistic'], result['total_n'], len(result['group_stats']))

print(f"\n效应量 η² = {eta_sq:.4f}")
print("效应量解释:")
print("  0.01: 小效应")
print("  0.06: 中等效应")
print("  0.14: 大效应")
```

### 可视化

```python
import matplotlib.pyplot as plt

def plot_kruskal_wallis(groups, labels=None, title="Kruskal-Wallis检验：多组比较"):
    """可视化多组数据"""
    if labels is None:
        labels = [f'组{i+1}' for i in range(len(groups))]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # 箱线图
    boxplot = axes[0].boxplot(groups, labels=labels, patch_artist=True)
    for patch, color in zip(boxplot['boxes'], ['skyblue', 'lightgreen', 'salmon']):
        patch.set_facecolor(color)
    axes[0].set_ylabel('值')
    axes[0].set_title(f'{title} - 箱线图')
    axes[0].grid(axis='y', alpha=0.3)

    # 小提琴图
    positions = range(1, len(groups) + 1)
    parts = axes[1].violinplot(groups, positions=positions, showmeans=True, showmedians=True)
    axes[1].set_xticks(positions)
    axes[1].set_xticklabels(labels)
    axes[1].set_title(f'{title} - 小提琴图')
    axes[1].grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()

# 可视化教学方法比较
plot_kruskal_wallis([method_A, method_B, method_C],
                    ['方法A', '方法B', '方法C'],
                    "教学方法效果比较")
```

## 注意事项

1. **独立性**：各样本之间必须相互独立
2. **随机抽样**：样本应该是随机抽取的
3. **样本量**：每组的样本量至少应为5
4. **结的处理**：存在结时需要使用平均秩次，并可能需要修正H统计量
5. **事后检验**：拒绝原假设后需要进行事后检验确定具体哪些组有差异

## Kruskal-Wallis检验的扩展

### 1. 中位数检验

另一种非参数方法，比较多个组的中位数。

### 2. Jonckheere-Terpstra检验

用于检验有序的组间趋势（如剂量-反应关系）。

### 3. Friedman检验

用于重复测量或配组设计的非参数方法。

## 参考资源

- 非参数统计学教材
- scipy.stats文档
- scipy.stats.kruskal文档
- Kruskal, W. H., & Wallis, W. A. (1952). Use of ranks in one-criterion variance analysis
- Conover, W. J. (1999). Practical nonparametric statistics