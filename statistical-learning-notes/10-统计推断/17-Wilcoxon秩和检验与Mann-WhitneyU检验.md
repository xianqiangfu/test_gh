# Wilcoxon秩和检验与Mann-Whitney U检验

## 问题

统计推断部分缺少Wilcoxon秩和检验和Mann-Whitney U检验的学习笔记。这两个检验是分析两独立样本的重要非参数方法。

## 说明

Wilcoxon秩和检验和Mann-Whitney U检验是等价的，用于比较两个独立样本的分布，是t检验的非参数替代方法。

## 检验的定义和原理

### Wilcoxon秩和检验

Wilcoxon秩和检验（Wilcoxon Rank Sum Test）由Frank Wilcoxon于1945年提出，是比较两个独立样本的非参数检验方法。

**基本思想**：
1. 将两个样本的数据合并
2. 对所有数据进行排序并分配秩次
3. 分别计算两个样本的秩和
4. 比较两个秩和的差异是否显著

### Mann-Whitney U检验

Mann-Whitney U检验由H. B. Mann和D. R. Whitney于1947年提出，与Wilcoxon秩和检验完全等价。

**U统计量**：
```
U₁ = n₁n₂ + n₁(n₁ + 1)/2 - R₁
U₂ = n₁n₂ + n₂(n₂ + 1)/2 - R₂
```

其中：
- n₁, n₂：两个样本的样本量
- R₁, R₂：两个样本的秩和

**关系**：
```
U₁ + U₂ = n₁ × n₂
```

## 检验统计量的计算

### 步骤1：合并并排序

将两个样本的数据合并为一个样本，并从小到大排序。

### 步骤2：分配秩次

为每个观测值分配秩次。对于有相同值的观测值（结），使用平均秩次。

### 步骤3：计算秩和

计算每个样本的秩和：
```
R₁ = Σrank(Xᵢ)
R₂ = Σrank(Yⱼ)
```

### 步骤4：计算U统计量

```
U₁ = n₁n₂ + n₁(n₁ + 1)/2 - R₁
U₂ = n₁n₂ + n₂(n₂ + 1)/2 - R₂
```

检验统计量通常取较小的U值：
```
U = min(U₁, U₂)
```

### 步骤5：确定p值

**小样本**（n₁ ≤ 20或n₂ ≤ 20）：查Mann-Whitney U临界值表
**大样本**（n₁ > 20且n₂ > 20）：使用正态近似

#### 正态近似

正态近似的Z统计量：

```
μ_U = n₁n₂/2
σ_U² = n₁n₂(n₁ + n₂ + 1)/12

Z = (U - μ_U) / σ_U
```

**存在结时的修正**：

当存在结时，需要修正标准误：

```
σ_U² = [n₁n₂/(N(N-1))] × [N³ - N - Σ(tⱼ³ - tⱼ)]/12
```

其中：
- N = n₁ + n₂
- tⱼ：第j个结中相同值的个数

## 假设检验步骤

### 步骤1：建立假设

- **原假设（H₀）**：两个样本来自相同的分布
- **备择假设（H₁）**：
  - 两个样本分布不同（双侧）
  - 样本1倾向于有更大的值（右侧）
  - 样本1倾向于有更小的值（左侧）

### 步骤2：选择显著性水平

通常选择α = 0.05或α = 0.01

### 步骤3：计算检验统计量

按上述步骤计算U值或Z值

### 步骤4：计算p值

使用正态近似或查表

### 步骤5：做出决策

- 如果p < α，拒绝H₀
- 否则，无法拒绝H₀

### 步骤6：解释结果

在实际应用背景下解释

## 与t检验的比较

| 特征 | Wilcoxon秩和检验 | 独立样本t检验 |
|------|-----------------|--------------|
| 统计量 | 秩和 | 均值差 |
| 分布假设 | 无 | 正态分布 |
| 方差齐性 | 不需要 | 需要 |
| 检验功效 | 较低（正态时） | 较高（正态时） |
| 对异常值 | 不敏感 | 敏感 |
| 渐进效率 | 95.5% | 100%（正态时） |

**何时使用Wilcoxon秩和检验**：
1. 数据不满足正态性
2. 样本量较小
3. 存在异常值
4. 数据是序数而非等距

## Python实现示例

### 基础Wilcoxon秩和检验

```python
import numpy as np
from scipy import stats

def wilcoxon_rank_sum_test(sample1, sample2, alpha=0.05, alternative='two-sided'):
    """
    Wilcoxon秩和检验（Mann-Whitney U检验）

    参数:
        sample1, sample2: 两个独立样本
        alpha: 显著性水平
        alternative: 备择假设类型 ('two-sided', 'greater', 'less')

    返回:
        result: 包含检验结果的字典
    """
    sample1 = np.array(sample1)
    sample2 = np.array(sample2)
    n1, n2 = len(sample1), len(sample2)

    # 合并数据并排序
    combined = np.concatenate([sample1, sample2])
    sorted_indices = np.argsort(combined)

    # 分配秩次（处理结）
    ranks = np.zeros(len(combined))
    for i, idx in enumerate(sorted_indices):
        # 查找所有相同值的索引
        tied_indices = np.where(combined == combined[idx])[0]
        # 使用平均秩次
        avg_rank = np.mean(tied_indices + 1)
        ranks[idx] = avg_rank

    # 计算各样本的秩和
    R1 = np.sum(ranks[:n1])
    R2 = np.sum(ranks[n1:])

    # 计算U统计量
    U1 = n1 * n2 + n1 * (n1 + 1) / 2 - R1
    U2 = n1 * n2 + n2 * (n2 + 1) / 2 - R2
    U = min(U1, U2)

    # 计算期望和标准差
    mu_U = n1 * n2 / 2
    sigma_U = np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)

    # 计算Z统计量
    if sigma_U > 0:
        Z = (U - mu_U) / sigma_U
    else:
        Z = 0

    # 计算p值
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(Z)))
    elif alternative == 'greater':
        p_value = 1 - stats.norm.cdf(Z)
    elif alternative == 'less':
        p_value = stats.norm.cdf(Z)

    reject = p_value < alpha

    return {
        'U1': U1,
        'U2': U2,
        'U': U,
        'Z': Z,
        'p_value': p_value,
        'reject_null': reject,
        'R1': R1,
        'R2': R2,
        'mean1': np.mean(sample1),
        'mean2': np.mean(sample2)
    }

# 示例1：比较两种教学方法的效果
np.random.seed(42)
method_A = np.array([78, 82, 75, 88, 90, 85, 79, 83, 77, 86])
method_B = np.array([70, 75, 72, 78, 80, 73, 71, 76, 74, 79])

result = wilcoxon_rank_sum_test(method_A, method_B, alpha=0.05)

print("Wilcoxon秩和检验结果（教学方法比较）:")
print(f"方法A秩和 (R1): {result['R1']}")
print(f"方法B秩和 (R2): {result['R2']}")
print(f"U统计量: {result['U']:.2f}")
print(f"Z统计量: {result['Z']:.4f}")
print(f"p值: {result['p_value']:.4f}")
print(f"是否拒绝原假设: {result['reject_null']}")
```

### 使用scipy的mannwhitneyu函数

```python
# 示例2：使用scipy的mannwhitneyu函数
statistic, p_value = stats.mannwhitneyu(method_A, method_B, alternative='two-sided')

print(f"\n使用scipy.mannwhitneyu的结果:")
print(f"U统计量: {statistic:.2f}")
print(f"p值: {p_value:.4f}")
```

### 非正态数据的比较

```python
# 示例3：比较t检验和Wilcoxon检验
np.random.seed(42)

# 正态数据
normal_data1 = np.random.normal(50, 5, 30)
normal_data2 = np.random.normal(55, 5, 30)

# 偏态数据
skewed_data1 = np.random.exponential(20, 30)
skewed_data2 = np.random.exponential(25, 30)

print("\n正态数据比较:")
print("独立样本t检验:")
t_stat, t_p = stats.ttest_ind(normal_data1, normal_data2)
print(f"p值: {t_p:.4f}")

print("\nWilcoxon秩和检验:")
w_result = wilcoxon_rank_sum_test(normal_data1, normal_data2)
print(f"p值: {w_result['p_value']:.4f}")

print("\n偏态数据比较:")
print("独立样本t检验:")
t_stat2, t_p2 = stats.ttest_ind(skewed_data1, skewed_data2)
print(f"p值: {t_p2:.4f}")

print("\nWilcoxon秩和检验:")
w_result2 = wilcoxon_rank_sum_test(skewed_data1, skewed_data2)
print(f"p值: {w_result2['p_value']:.4f}")
```

### 效应量（r值）

```python
def calculate_effect_size_r(Z, n1, n2):
    """
    计算Wilcoxon检验的效应量r

    参数:
        Z: Z统计量
        n1, n2: 样本量

    返回:
        r: 效应量（0.1=小，0.3=中，0.5=大）
    """
    N = n1 + n2
    r = abs(Z) / np.sqrt(N)
    return r

# 计算效应量
r = calculate_effect_size_r(result['Z'], len(method_A), len(method_B))

print(f"\n效应量 r = {r:.4f}")
print("效应量解释:")
print("  0.1: 小效应")
print("  0.3: 中等效应")
print("  0.5: 大效应")
```

### 处理结（Tied Values）

```python
# 示例4：包含结的数据
data1 = np.array([1, 2, 2, 3, 4, 5])
data2 = np.array([2, 2, 3, 3, 4, 4])

result = wilcoxon_rank_sum_test(data1, data2)
print("\n包含结的数据:")
print(f"U统计量: {result['U']:.2f}")
print(f"p值: {result['p_value']:.4f}")

# 与scipy比较
stat, p = stats.mannwhitneyu(data1, data2, alternative='two-sided')
print(f"scipy结果 - U: {stat:.2f}, p: {p:.4f}")
```

### 可视化

```python
import matplotlib.pyplot as plt

def plot_wilcoxon_comparison(sample1, sample2, label1="样本1", label2="样本2", title="样本比较"):
    """可视化两个样本的分布"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # 箱线图
    axes[0].boxplot([sample1, sample2], labels=[label1, label2])
    axes[0].set_ylabel('值')
    axes[0].set_title(f'{title} - 箱线图')
    axes[0].grid(axis='y', alpha=0.3)

    # 小提琴图
    parts = axes[1].violinplot([sample1, sample2], positions=[1, 2],
                               showmeans=True, showmedians=True)
    axes[1].set_xticks([1, 2])
    axes[1].set_xticklabels([label1, label2])
    axes[1].set_title(f'{title} - 小提琴图')
    axes[1].grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()

# 可视化教学方法比较
plot_wilcoxon_comparison(method_A, method_B, "方法A", "方法B", "教学方法效果比较")
```

### 中位数差值的置信区间

```python
def wilcoxon_ci(sample1, sample2, confidence=0.95):
    """
    计算中位数差值的Hodges-Lehmann估计及其置信区间

    参数:
        sample1, sample2: 两个样本
        confidence: 置信水平

    返回:
        estimate: 中位数差值的估计
        ci_lower: 置信区间下限
        ci_upper: 置信区间上限
    """
    # 计算所有可能的差值
    diffs = np.array([x - y for x in sample1 for y in sample2])

    # Hodges-Lehmann估计：差值的中位数
    estimate = np.median(diffs)

    # 计算置信区间
    n1, n2 = len(sample1), len(sample2)
    sorted_diffs = np.sort(diffs)

    alpha = 1 - confidence
    critical_value = int(stats.norm.ppf(1 - alpha/2) * np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12))

    ci_lower = sorted_diffs[critical_value - 1]
    ci_upper = sorted_diffs[len(sorted_diffs) - critical_value]

    return estimate, ci_lower, ci_upper

# 计算中位数差值的置信区间
estimate, ci_lower, ci_upper = wilcoxon_ci(method_A, method_B)

print(f"\n中位数差值估计: {estimate:.2f}")
print(f"95%置信区间: [{ci_lower:.2f}, {ci_upper:.2f}]")
```

## 注意事项

1. **独立性**：两个样本必须相互独立
2. **随机抽样**：样本应该是随机抽取的
3. **结的处理**：存在结时需要使用平均秩次，并可能需要修正标准误
4. **样本量**：小样本时使用精确检验，大样本时使用正态近似
5. **与配对检验的区别**：Wilcoxon秩和检验用于独立样本，Wilcoxon符号秩检验用于配对样本

## Wilcoxon秩和检验 vs Wilcoxon符号秩检验

| 特征 | Wilcoxon秩和检验 | Wilcoxon符号秩检验 |
|------|----------------|-------------------|
| 样本类型 | 独立样本 | 配对样本 |
| 统计量 | 秩和 | 符号秩和 |
| 应用场景 | 比较两个独立组 | 比较配对数据 |
| 等价检验 | Mann-Whitney U检验 | 无 |

## 参考资源

- 非参数统计学教材
- scipy.stats文档
- scipy.stats.wilcoxon文档
- Mann, H. B., & Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically larger than the other
- Wilcoxon, F. (1945). Individual comparisons by ranking methods
