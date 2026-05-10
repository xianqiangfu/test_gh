# Wilcoxon符号秩检验

## 问题

统计推断部分缺少Wilcoxon符号秩检验的学习笔记。这是处理配对样本的重要非参数方法。

## 说明

Wilcoxon符号秩检验用于比较配对样本（如同一对象的前后测量）的差异，是配对t检验的非参数替代方法。

## 检验的定义和原理

Wilcoxon符号秩检验（Wilcoxon Signed-Rank Test）由Frank Wilcoxon于1945年提出，是比较配对样本的非参数检验方法。

### 基本思想

1. 计算每对数据的差值
2. 去除零差值
3. 对差值的绝对值进行排序并分配秩次
4. 根据差值的符号分配正秩和负秩
5. 比较正秩和与负秩的差异

### 与符号检验的比较

| 特征 | 符号检验 | Wilcoxon符号秩检验 |
|------|---------|-------------------|
| 利用信息 | 只用符号 | 同时利用符号和大小 |
| 检验功效 | 较低 | 较高 |
| 计算 | 简单 | 稍复杂 |
| 异常值影响 | 无 | 较小 |
| 效率 | 63% | 95%（对正态分布） |

### 与配对t检验的比较

| 特征 | Wilcoxon符号秩检验 | 配对t检验 |
|------|-------------------|-----------|
| 统计量 | 秩和 | 差值均值 |
| 分布假设 | 差值对称分布 | 差值正态分布 |
| 检验功效 | 较低（正态时） | 较高（正态时） |
| 对异常值 | 不敏感 | 敏感 |

## 统计量的计算

### 步骤1：计算差值

对于n对数据 (Xᵢ, Yᵢ)，计算差值：
```
Dᵢ = Xᵢ - Yᵢ
```

### 步骤2：去除零差值

去除差值为0的对，记有效样本量为n*

### 步骤3：对绝对值排序

对\|Dᵢ\|进行排序，分配秩次（最小的绝对值秩为1）

### 步骤4：分配符号秩

- 正差值：正秩
- 负差值：负秩

### 步骤5：计算秩和

```
W⁺ = Σrank(Dᵢ), for Dᵢ > 0
W⁻ = Σrank(Dᵢ), for Dᵢ < 0
```

### 步骤6：确定检验统计量

检验统计量T通常取较小的秩和：
```
T = min(W⁺, W⁻)
```

### 步骤7：确定p值

**小样本**（n* ≤ 25）：查Wilcoxon符号秩检验临界值表
**大样本**（n* > 25）：使用正态近似

#### 正态近似

```
μ_T = n*(n* + 1)/4
σ_T² = n*(n* + 1)(2n* + 1)/24

Z = (T - μ_T) / σ_T
```

**存在结时的修正**：

```
σ_T² = [n*(n* + 1)(2n* + 1)/24] - [Σ(tⱼ³ - tⱼ)/48]
```

其中tⱼ是第j个结中相同值的个数

## 假设检验步骤

### 步骤1：建立假设

- **原假设（H₀）**：差值的中位数为0
- **备择假设（H₁）**：
  - 差值的中位数不为0（双侧）
  - 差值的中位数大于0（右侧）
  - 差值的中位数小于0（左侧）

### 步骤2：选择显著性水平

通常选择α = 0.05或α = 0.01

### 步骤3：计算检验统计量

按上述步骤计算T值或Z值

### 步骤4：计算p值

使用正态近似或查表

### 步骤5：做出决策

- 如果p < α，拒绝H₀
- 否则，无法拒绝H₀

### 步骤6：解释结果

在实际应用背景下解释

## Python实现示例

### 基础Wilcoxon符号秩检验

```python
import numpy as np
from scipy import stats

def wilcoxon_signed_rank_test(x, y=None, mu=0, alpha=0.05, alternative='two-sided'):
    """
    Wilcoxon符号秩检验

    参数:
        x: 第一组数据，或差值数据（当y=None时）
        y: 第二组数据（配对样本）
        mu: 检验的中位数（单样本时）
        alpha: 显著性水平
        alternative: 备择假设类型 ('two-sided', 'greater', 'less')

    返回:
        result: 包含检验结果的字典
    """
    if y is None:
        # 单样本检验：检验中位数是否为mu
        d = np.array(x) - mu
    else:
        # 配对样本检验
        d = np.array(x) - np.array(y)

    # 去除零差值
    d = d[d != 0]
    n = len(d)

    if n == 0:
        return {
            'statistic': 0,
            'p_value': 1.0,
            'reject_null': False,
            'n_pairs': 0
        }

    # 计算绝对值的秩
    abs_d = np.abs(d)
    ranks = stats.rankdata(abs_d)

    # 分配符号秩
    signed_ranks = ranks * np.sign(d)

    # 计算正秩和与负秩和
    W_plus = np.sum(signed_ranks[signed_ranks > 0])
    W_minus = abs(np.sum(signed_ranks[signed_ranks < 0]))

    # 检验统计量（取较小的）
    T = min(W_plus, W_minus)

    # 计算期望和标准差
    mu_T = n * (n + 1) / 4
    sigma_T = np.sqrt(n * (n + 1) * (2 * n + 1) / 24)

    # 计算Z统计量
    if sigma_T > 0:
        Z = (T - mu_T) / sigma_T
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
        'W_plus': W_plus,
        'W_minus': W_minus,
        'T': T,
        'Z': Z,
        'p_value': p_value,
        'reject_null': reject,
        'n_pairs': n,
        'mean_diff': np.mean(d)
    }

# 示例1：配对样本检验（某药物效果）
np.random.seed(42)
before = np.array([85, 78, 92, 88, 76, 90, 82, 79, 91, 87])
after = np.array([88, 80, 95, 86, 78, 93, 84, 82, 94, 89])

result = wilcoxon_signed_rank_test(before, after, alpha=0.05)

print("Wilcoxon符号秩检验结果（药物治疗效果）:")
print(f"正秩和 (W⁺): {result['W_plus']}")
print(f"负秩和 (W⁻): {result['W_minus']}")
print(f"检验统计量T: {result['T']}")
print(f"Z统计量: {result['Z']:.4f}")
print(f"p值: {result['p_value']:.4f}")
print(f"是否拒绝原假设: {result['reject_null']}")
```

### 使用scipy的wilcoxon函数

```python
# 示例2：使用scipy的wilcoxon函数
statistic, p_value = stats.wilcoxon(before, after, alternative='two-sided')

print(f"\n使用scipy.wilcoxon的结果:")
print(f"统计量: {statistic}")
print(f"p值: {p_value:.4f}")
```

### 与配对t检验的比较

```python
# 示例3：比较Wilcoxon检验与配对t检验
np.random.seed(42)

# 正态数据
normal_data1 = np.random.normal(50, 5, 30)
normal_data2 = normal_data1 + np.random.normal(2, 3, 30)

# 偏态数据
skewed_data1 = np.random.exponential(20, 30)
skewed_data2 = skewed_data1 + np.random.exponential(5, 30)

print("\n正态数据比较:")
print("配对t检验:")
t_stat, t_p = stats.ttest_rel(normal_data1, normal_data2)
print(f"p值: {t_p:.4f}")

print("\nWilcoxon符号秩检验:")
w_result = wilcoxon_signed_rank_test(normal_data1, normal_data2)
print(f"p值: {w_result['p_value']:.4f}")

print("\n偏态数据比较:")
print("配对t检验:")
t_stat2, t_p2 = stats.ttest_rel(skewed_data1, skewed_data2)
print(f"p值: {t_p2:.4f}")

print("\nWilcoxon符号秩检验:")
w_result2 = wilcoxon_signed_rank_test(skewed_data1, skewed_data2)
print(f"p值: {w_result2['p_value']:.4f}")
```

### 单样本中位数检验

```python
# 示例4：单样本中位数检验
np.random.seed(42)
weights = np.array([68, 72, 65, 70, 75, 69, 71, 67, 73, 68, 74, 70])

# 检验中位数是否显著大于70
result = wilcoxon_signed_rank_test(weights, mu=70, alpha=0.05, alternative='greater')

print("\n单样本Wilcoxon符号秩检验结果（体重中位数）:")
print(f"有效样本量: {result['n_pairs']}")
print(f"正秩和 (W⁺): {result['W_plus']}")
print(f"负秩和 (W⁻): {result['W_minus']}")
print(f"Z统计量: {result['Z']:.4f}")
print(f"p值: {result['p_value']:.4f}")
print(f"是否拒绝原假设: {result['reject_null']}")
```

### 效应量（r值）

```python
def calculate_effect_size_r(Z, n):
    """
    计算Wilcoxon检验的效应量r

    参数:
        Z: Z统计量
        n: 有效样本量

    返回:
        r: 效应量（0.1=小，0.3=中，0.5=大）
    """
    r = abs(Z) / np.sqrt(n)
    return r

# 计算效应量
r = calculate_effect_size_r(result['Z'], result['n_pairs'])

print(f"\n效应量 r = {r:.4f}")
print("效应量解释:")
print("  0.1: 小效应")
print("  0.3: 中等效应")
print("  0.5: 大效应")
```

### 可视化

```python
import matplotlib.pyplot as plt

def plot_wilcoxon_differences(x, y, title="Wilcoxon符号秩检验：差值分析"):
    """可视化配对差值"""
    differences = np.array(x) - np.array(y)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 差值直方图
    axes[0, 0].hist(differences, bins=10, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 0].axvline(x=0, color='red', linestyle='--', linewidth=2, label='零线')
    axes[0, 0].axvline(x=np.median(differences), color='green', linestyle='-', linewidth=2, label='中位数')
    axes[0, 0].set_xlabel('差值')
    axes[0, 0].set_ylabel('频数')
    axes[0, 0].set_title(f'{title} - 差值直方图')
    axes[0, 0].legend()

    # 配对数据点
    axes[0, 1].scatter(range(len(x)), x, color='blue', label='组1', alpha=0.7)
    axes[0, 1].scatter(range(len(y)), y, color='red', label='组2', alpha=0.7)
    for i in range(len(x)):
        axes[0, 1].plot([i, i], [x[i], y[i]], 'gray', alpha=0.5)
    axes[0, 1].set_xlabel('配对编号')
    axes[0, 1].set_ylabel('值')
    axes[0, 1].set_title(f'{title} - 配对数据点')
    axes[0, 1].legend()

    # 差值条形图
    axes[1, 0].bar(range(len(differences)), differences, color='skyblue', edgecolor='black')
    axes[1, 0].axhline(y=0, color='red', linestyle='--', linewidth=2)
    axes[1, 0].set_xlabel('配对编号')
    axes[1, 0].set_ylabel('差值')
    axes[1, 0].set_title(f'{title} - 差值条形图')

    # Q-Q图（检验正态性）
    stats.probplot(differences, dist="norm", plot=axes[1, 1])
    axes[1, 1].set_title(f'{title} - Q-Q图')

    plt.tight_layout()
    plt.show()

# 可视化配对样本差值
plot_wilcoxon_differences(before, after, "药物治疗前后对比")
```

### Hodges-Lehmann中位数估计

```python
def hodges_lehmann_estimate(x, y=None):
    """
    计算Hodges-Lehmann中位数估计

    参数:
        x: 第一组数据
        y: 第二组数据（可选）

    返回:
        estimate: 中位数估计
    """
    if y is None:
        # 单样本：中位数
        return np.median(x)
    else:
        # 配对样本：所有可能对的平均值的中位数
        d = np.array(x) - np.array(y)
        # 计算所有可能的均值
        means = [(d[i] + d[j]) / 2 for i in range(len(d)) for j in range(i, len(d))]
        return np.median(means)

# 计算Hodges-Lehmann估计
estimate = hodges_lehmann_estimate(before, after)

print(f"\nHodges-Lehmann中位数估计: {estimate:.2f}")
print(f"普通中位数: {np.median(before - after):.2f}")
```

## 注意事项

1. **对称性假设**：差值分布应该关于中位数对称
2. **独立性**：配对之间应该相互独立
3. **随机抽样**：样本应该是随机抽取的
4. **零差值**：零差值不计入检验，减少有效样本量
5. **结的处理**：存在结时需要使用平均秩次，并可能需要修正标准误

## Wilcoxon符号秩检验的适用条件

1. **配对数据**：必须是配对样本设计
2. **连续或有序数据**：数据至少是有序的
3. **差值对称分布**：差值的分布应该对称（但不要求正态）
4. **样本量**：小样本和大样本都可以使用

## 参考资源

- 非参数统计学教材
- scipy.stats文档
- scipy.stats.wilcoxon文档
- Wilcoxon, F. (1945). Individual comparisons by ranking methods
- Conover, W. J. (1999). Practical nonparametric statistics