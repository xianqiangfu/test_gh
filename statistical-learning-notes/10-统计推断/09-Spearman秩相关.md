# Spearman秩相关系数

## 定义

Spearman秩相关系数（Spearman's rank correlation coefficient），又称Spearman's ρ（rho），是一种非参数统计量，用于衡量两个变量之间的单调关系强度。它由Charles Spearman于1904年提出。

### 核心特点

- **非参数方法：** 不需要数据服从特定分布（如正态分布）
- **基于秩次：** 使用数据的秩次而非原始值
- **衡量单调关系：** 检测变量间的单调（递增或递减）关系，而非严格线性关系
- **适用于定序数据：** 可用于有序分类数据

## 与皮尔逊相关的比较

| 特征 | 皮尔逊相关系数（r） | Spearman秩相关系数（ρ） |
|------|---------------------|-------------------------|
| **类型** | 参数统计量 | 非参数统计量 |
| **数据要求** | 连续变量，近似正态 | 连续或定序变量，无分布要求 |
| **关系类型** | 线性关系 | 单调关系 |
| **敏感度** | 对异常值敏感 | 对异常值稳健 |
| **计算基础** | 原始数据值 | 数据的秩次 |
| **适用场景** | 线性关系，正态数据 | 非线性单调关系，非正态数据 |
| **功效** | 满足假设时功效更高 | 不满足正态性时更可靠 |

### 选择原则

1. **使用皮尔逊相关：**
   - 数据服从正态分布
   - 变量间存在线性关系
   - 数据为连续型
   - 无明显异常值

2. **使用Spearman秩相关：**
   - 数据不服从正态分布
   - 变量间存在单调但非线性关系
   - 数据为定序型（如评分等级）
   - 存在明显异常值
   - 样本量较小

## Spearman秩相关系数的计算

### 方法一：使用秩次差（无结时）

当没有重复值（无结）时：

$$\rho = 1 - \frac{6\sum d_i^2}{n(n^2 - 1)}$$

其中：
- $d_i = R_{xi} - R_{yi}$ 是第i对观测值的秩次差
- $n$ 是样本量
- $R_{xi}$ 和 $R_{yi}$ 分别是X和Y的第i个观测值的秩次

### 方法二：使用皮尔逊公式（适用于有结）

Spearman秩相关系数实际上是对数据秩次计算皮尔逊相关系数：

$$\rho = \frac{\sum (R_{xi} - \bar{R}_x)(R_{yi} - \bar{R}_y)}{\sqrt{\sum (R_{xi} - \bar{R}_x)^2 \sum (R_{yi} - \bar{R}_y)^2}}$$

其中：
- $\bar{R}_x$ 和 $\bar{R}_y$ 是秩次的均值

### 秩次的计算

#### 基本步骤

1. **排序：** 分别对X和Y的数据从小到大排序
2. **赋秩：** 给每个观测值赋予秩次（1, 2, 3, ..., n）
3. **处理结：** 对相同值赋予平均秩次

#### 结（Tie）的处理

当数据中有重复值时，使用平均秩次：

**示例：**
```
原始数据：[5, 8, 8, 10, 12]
排序后：[5, 8, 8, 10, 12]
赋秩：   [1, 2.5, 2.5, 4, 5]  # 两个8的平均秩次是(2+3)/2 = 2.5
```

#### 计算示例

| X | Y | X的秩(R_x) | Y的秩(R_y) | d = R_x - R_y | d² |
|---|---|------------|------------|---------------|-----|
| 12 | 15 | 3 | 3 | 0 | 0 |
| 8  | 10 | 2 | 1 | 1 | 1 |
| 15 | 18 | 4 | 4 | 0 | 0 |
| 5  | 12 | 1 | 2 | -1 | 1 |
| ∑ |   |    |    |   | 2 |

$$\rho = 1 - \frac{6 \times 2}{4(4^2 - 1)} = 1 - \frac{12}{60} = 1 - 0.2 = 0.8$$

## 系数的解释

### 取值范围

Spearman秩相关系数 ρ 的取值范围是 [-1, 1]

### 解释规则

| ρ值范围 | 相关强度 | 解释 |
|---------|----------|------|
| ρ = 1 | 完全正相关 | 完全单调递增关系 |
| 0.7 ≤ ρ < 1 | 强正相关 | 强单调递增关系 |
| 0.3 ≤ ρ < 0.7 | 中度正相关 | 中度单调递增关系 |
| 0 < ρ < 0.3 | 弱正相关 | 弱单调递增关系 |
| ρ = 0 | 无相关 | 无单调关系 |
| -0.3 < ρ < 0 | 弱负相关 | 弱单调递减关系 |
| -0.7 < ρ ≤ -0.3 | 中度负相关 | 中度单调递减关系 |
| -1 < ρ ≤ -0.7 | 强负相关 | 强单调递减关系 |
| ρ = -1 | 完全负相关 | 完全单调递减关系 |

### 单调关系的理解

**正相关（ρ > 0）：**
- X增加时，Y倾向于增加
- 但不一定是线性关系

**负相关（ρ < 0）：**
- X增加时，Y倾向于减少
- 但不一定是线性关系

**零相关（ρ = 0）：**
- X和Y之间没有单调关系
- 但可能存在其他复杂关系（如U型关系）

### 与皮尔逊相关的差异

| 数据模式 | 皮尔逊 r | Spearman ρ |
|----------|----------|------------|
| 线性关系 | 高（接近±1） | 高（接近±1） |
| 单调非线性关系 | 低 | 高（接近±1） |
| U型/倒U型关系 | 低（接近0） | 低（接近0） |
| 有异常值的线性关系 | 受影响大 | 受影响小 |

**示例：非线性单调关系**

```
X: [1, 2, 3, 4, 5]
Y: [1, 4, 9, 16, 25]  # Y = X²（完全单调递增）

皮尔逊 r ≈ 0.97（接近1但不完全）
Spearman ρ = 1.0（完全单调）
```

## 假设检验

### 检验目的

检验总体Spearman秩相关系数是否显著不为零，即判断两个变量之间是否存在显著的秩相关关系。

### 假设

- **零假设（H₀）：** ρ = 0（两个变量之间不存在秩相关）
- **备择假设（H₁）：** ρ ≠ 0（两个变量之间存在秩相关）

也可以进行单侧检验：
- H₁: ρ > 0（存在正秩相关）
- H₁: ρ < 0（存在负秩相关）

### 检验统计量

#### 小样本情况（n ≤ 30）

使用临界值表进行判断。

#### 大样本情况（n > 30）

使用正态近似：

$$t = \rho \sqrt{\frac{n-2}{1-\rho^2}}$$

该统计量服从自由度为 n-2 的 t 分布。

或使用 z 统计量：

$$z = \rho \sqrt{n-1}$$

该统计量近似服从标准正态分布。

### p值计算

根据检验统计量的值和自由度（或标准正态分布）计算p值。

### 决策规则

- 如果 p < α（通常α = 0.05），拒绝H₀，认为存在显著的相关关系
- 如果 p ≥ α，不拒绝H₀，认为没有足够的证据表明存在相关关系

### 置信区间

对于大样本，Spearman秩相关系数的置信区间可以使用Fisher's z变换：

$$z = \frac{1}{2} \ln\left(\frac{1+\rho}{1-\rho}\right) = \text{arctanh}(\rho)$$

$$SE_z = \frac{1}{\sqrt{n-3}}$$

$$z_{lower} = z - z_{\alpha/2} \times SE_z$$
$$z_{upper} = z + z_{\alpha/2} \times SE_z$$

$$\rho_{lower} = \tanh(z_{lower}) = \frac{e^{z_{lower}} - e^{-z_{lower}}}{e^{z_{lower}} + e^{-z_{lower}}}$$
$$\rho_{upper} = \tanh(z_{upper})$$

## 假设检验的Python实现

### 使用 scipy.stats.spearmanr

```python
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 示例数据：学生数学和物理成绩的秩次关系
math_scores = np.array([85, 92, 78, 88, 95, 72, 90, 83, 87, 91])
physics_scores = np.array([82, 90, 75, 85, 93, 70, 88, 80, 84, 89])

# 1. 计算Spearman秩相关系数和p值
rho, p_value = stats.spearmanr(math_scores, physics_scores)
print(f"Spearman秩相关系数: ρ = {rho:.4f}")
print(f"p值: p = {p_value:.4f}")

# 判断显著性
alpha = 0.05
if p_value < alpha:
    print(f"在α = {alpha}水平下，拒绝零假设")
    print("结论：数学成绩和物理成绩之间存在显著的秩相关关系")
else:
    print(f"在α = {alpha}水平下，不拒绝零假设")
    print("结论：没有足够证据表明数学成绩和物理成绩之间存在秩相关关系")

# 2. 置信区间计算（大样本近似）
def spearman_ci(rho, n, alpha=0.05):
    """计算Spearman秩相关系数的置信区间"""
    z = np.arctanh(rho)
    se = 1 / np.sqrt(n - 3)
    z_crit = stats.norm.ppf(1 - alpha/2)
    
    z_lower = z - z_crit * se
    z_upper = z + z_crit * se
    
    rho_lower = np.tanh(z_lower)
    rho_upper = np.tanh(z_upper)
    
    return rho_lower, rho_upper

ci_lower, ci_upper = spearman_ci(rho, len(math_scores))
print(f"\n95%置信区间: [{ci_lower:.4f}, {ci_upper:.4f}]")

# 3. 手动计算（验证理解）
def calculate_spearman(x, y):
    """手动计算Spearman秩相关系数"""
    # 计算秩次
    rank_x = stats.rankdata(x)
    rank_y = stats.rankdata(y)
    
    # 计算秩次差
    d = rank_x - rank_y
    
    # Spearman公式
    n = len(x)
    rho = 1 - (6 * np.sum(d**2)) / (n * (n**2 - 1))
    
    return rho, rank_x, rank_y, d

rho_manual, rank_x, rank_y, d = calculate_spearman(math_scores, physics_scores)
print(f"\n手动计算验证:")
print(f"Spearman秩相关系数: ρ = {rho_manual:.4f}")
print(f"X的秩次: {rank_x}")
print(f"Y的秩次: {rank_y}")
print(f"秩次差: {d}")
print(f"秩次差平方和: {np.sum(d**2)}")

# 4. 与皮尔逊相关比较
pearson_r, pearson_p = stats.pearsonr(math_scores, physics_scores)
print(f"\n与皮尔逊相关比较:")
print(f"皮尔逊相关系数: r = {pearson_r:.4f}, p = {pearson_p:.4f}")
print(f"Spearman秩相关系数: ρ = {rho:.4f}, p = {p_value:.4f}")

# 5. 可视化
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 散点图（原始数据）
axes[0].scatter(math_scores, physics_scores, alpha=0.6, s=100)
axes[0].set_xlabel('数学成绩', fontsize=12)
axes[0].set_ylabel('物理成绩', fontsize=12)
axes[0].set_title(f'原始数据散点图\nSpearman ρ = {rho:.4f}, p = {p_value:.4f}', fontsize=14)
axes[0].grid(True, alpha=0.3)

# 添加趋势线
z = np.polyfit(math_scores, physics_scores, 1)
p = np.poly1d(z)
axes[0].plot(math_scores, p(math_scores), "r--", alpha=0.8, linewidth=2)

# 秩次散点图
axes[1].scatter(rank_x, rank_y, alpha=0.6, s=100, color='green')
axes[1].set_xlabel('数学成绩秩次', fontsize=12)
axes[1].set_ylabel('物理成绩秩次', fontsize=12)
axes[1].set_title(f'秩次散点图\nSpearman ρ = {rho:.4f}', fontsize=14)
axes[1].grid(True, alpha=0.3)

# 添加对角线（完美正相关）
axes[1].plot([0, max(rank_x)], [0, max(rank_y)], 'r--', alpha=0.5, linewidth=2, label='完美正相关线')
axes[1].legend()

plt.tight_layout()
plt.show()

# 6. 处理有结的情况
print("\n=== 处理有结的情况 ===")

# 有重复值的数据
x_tied = np.array([10, 15, 15, 20, 20, 20, 25, 30])
y_tied = np.array([12, 18, 18, 22, 24, 22, 28, 32])

print(f"X数据: {x_tied}")
print(f"Y数据: {y_tied}")

# 计算秩次
rank_x_tied = stats.rankdata(x_tied)
rank_y_tied = stats.rankdata(y_tied)

print(f"\nX的秩次: {rank_x_tied}")
print(f"Y的秩次: {rank_y_tied}")

rho_tied, p_tied = stats.spearmanr(x_tied, y_tied)
print(f"\nSpearman秩相关系数: ρ = {rho_tied:.4f}")
print(f"p值: p = {p_tied:.4f}")

# 7. 示例：非线性单调关系
print("\n=== 非线性单调关系示例 ===")

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_nonlinear = x ** 2  # 完全单调递增，但是非线性关系

pearson_r_nl, pearson_p_nl = stats.pearsonr(x, y_nonlinear)
spearman_rho_nl, spearman_p_nl = stats.spearmanr(x, y_nonlinear)

print(f"数据: Y = X²（完全单调递增，非线性）")
print(f"皮尔逊相关: r = {pearson_r_nl:.4f}, p = {pearson_p_nl:.4f}")
print(f"Spearman秩相关: ρ = {spearman_rho_nl:.4f}, p = {spearman_p_nl:.4f}")

# 可视化
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].scatter(x, y_nonlinear, alpha=0.6, s=100, color='purple')
axes[0].set_xlabel('X', fontsize=12)
axes[0].set_ylabel('Y = X²', fontsize=12)
axes[0].set_title(f'非线性单调关系（原始数据）\n皮尔逊 r = {pearson_r_nl:.4f}', fontsize=14)
axes[0].grid(True, alpha=0.3)

axes[1].scatter(x, y_nonlinear, alpha=0.6, s=100, color='orange')
axes[1].set_xlabel('X', fontsize=12)
axes[1].set_ylabel('Y = X²', fontsize=12)
axes[1].set_title(f'非线性单调关系（原始数据）\nSpearman ρ = {spearman_rho_nl:.4f}', fontsize=14)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 8. 示例：异常值的影响
print("\n=== 异常值影响示例 ===")

# 正常数据
x_normal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_normal = np.array([1.1, 2.0, 2.9, 4.2, 5.1, 5.9, 7.0, 8.1, 9.2, 10.0])

# 添加异常值
x_outlier = np.append(x_normal, [50])  # 添加一个异常的X值
y_outlier = np.append(y_normal, [2])   # 对应的Y值不匹配

# 计算相关系数
pearson_r_normal, _ = stats.pearsonr(x_normal, y_normal)
spearman_rho_normal, _ = stats.spearmanr(x_normal, y_normal)

pearson_r_outlier, _ = stats.pearsonr(x_outlier, y_outlier)
spearman_rho_outlier, _ = stats.spearmanr(x_outlier, y_outlier)

print("正常数据:")
print(f"  皮尔逊 r = {pearson_r_normal:.4f}")
print(f"  Spearman ρ = {spearman_rho_normal:.4f}")

print("\n添加异常值后:")
print(f"  皮尔逊 r = {pearson_r_outlier:.4f} (变化: {pearson_r_outlier - pearson_r_normal:.4f})")
print(f"  Spearman ρ = {spearman_rho_outlier:.4f} (变化: {spearman_rho_outlier - spearman_rho_normal:.4f})")

print(f"\n结论: 皮尔逊相关对异常值更敏感，Spearman秩相关更稳健")

# 可视化
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].scatter(x_normal, y_normal, alpha=0.6, s=100)
axes[0].set_xlabel('X', fontsize=12)
axes[0].set_ylabel('Y', fontsize=12)
axes[0].set_title(f'正常数据\n皮尔逊 r = {pearson_r_normal:.4f}, Spearman ρ = {spearman_rho_normal:.4f}', fontsize=14)
axes[0].grid(True, alpha=0.3)

axes[1].scatter(x_outlier, y_outlier, alpha=0.6, s=100)
axes[1].scatter([50], [2], color='red', s=200, label='异常值', zorder=5)
axes[1].set_xlabel('X', fontsize=12)
axes[1].set_ylabel('Y', fontsize=12)
axes[1].set_title(f'包含异常值\n皮尔逊 r = {pearson_r_outlier:.4f}, Spearman ρ = {spearman_rho_outlier:.4f}', fontsize=14)
axes[1].grid(True, alpha=0.3)
axes[1].legend()

plt.tight_layout()
plt.show()
```

## 应用场景

### 1. 教育评估

分析不同科目成绩之间的关系：

```python
# 学生在多门课程的成绩
chinese = np.array([85, 90, 78, 88, 92, 75, 87, 83, 89, 91])
math = np.array([82, 88, 76, 85, 90, 73, 86, 80, 87, 89])
english = np.array([80, 85, 77, 82, 88, 74, 84, 79, 85, 87])

# 计算各科目之间的Spearman秩相关
subjects = {
    '语文': chinese,
    '数学': math,
    '英语': english
}

print("各科目之间的Spearman秩相关:")
for i, (name1, scores1) in enumerate(subjects.items()):
    for name2, scores2 in list(subjects.items())[i+1:]:
        rho, p = stats.spearmanr(scores1, scores2)
        print(f"{name1} - {name2}: ρ = {rho:.4f}, p = {p:.4f}")
```

### 2. 医学研究

分析疾病严重程度与治疗效果的秩次关系：

```python
# 疾病严重程度评分（1-5分）
severity = np.array([2, 3, 1, 4, 5, 2, 3, 4, 1, 5])

# 治疗效果评分（1-5分）
effectiveness = np.array([3, 4, 2, 5, 4, 3, 4, 5, 2, 5])

rho, p = stats.spearmanr(severity, effectiveness)
print(f"疾病严重程度与治疗效果: ρ = {rho:.4f}, p = {p:.4f}")
```

### 3. 市场调研

分析消费者满意度与购买意愿的秩次关系：

```python
# 消费者满意度评分（1-10分）
satisfaction = np.array([7, 9, 6, 8, 10, 5, 8, 7, 9, 8])

# 购买意愿评分（1-5分）
purchase_intent = np.array([4, 5, 3, 4, 5, 2, 4, 4, 5, 4])

rho, p = stats.spearmanr(satisfaction, purchase_intent)
print(f"满意度与购买意愿: ρ = {rho:.4f}, p = {p:.4f}")
```

## 注意事项与局限性

### 注意事项

1. **样本量要求：**
   - 小样本时检验功效较低
   - 一般建议 n ≥ 10

2. **结的影响：**
   - 大量重复值会降低检验功效
   - 应报告结的数量和比例

3. **单调关系 vs 因果关系：**
   - 相关不意味着因果
   - 需要结合领域知识解释

4. **异常值处理：**
   - Spearman对异常值较稳健
   - 但极端异常值仍可能影响结果

5. **多重比较问题：**
   - 同时检验多个变量对时需要校正α
   - 可使用Bonferroni校正

### 局限性

1. **只能检测单调关系：**
   - 无法检测U型、倒U型等非单调关系

2. **信息损失：**
   - 使用秩次会丢失原始数据的信息
   - 当数据满足正态性时，皮尔逊相关更优

3. **功效相对较低：**
   - 当数据满足正态性时，Spearman的功效低于皮尔逊

4. **对结敏感：**
   - 大量结会降低相关系数的可靠性

## 与其他非参数相关系数的比较

| 相关系数 | 符号 | 数据类型 | 特点 |
|----------|------|----------|------|
| Spearman | ρ | 连续或定序 | 检测单调关系，常用 |
| Kendall | τ | 连续或定序 | 检测一致性，适合小样本 |
| Goodman-Kruskal | γ | 定序 | 专门用于定序数据 |

### Kendall's τ 与 Spearman's ρ 的选择

- **样本量极小（n < 10）：** 优先使用 Kendall's τ
- **存在大量结：** Kendall's τ 更合适
- **一般情况：** 两者结果通常相似，Spearman更常用

## 总结

Spearman秩相关系数是重要的非参数相关分析方法。

**核心要点：**
1. 基于秩次，不要求正态分布
2. 检测单调关系，而非线性关系
3. 对异常值稳健
4. 适用于定序数据和非正态数据

**应用场景：**
1. 非正态分布数据
2. 定序数据（如评分等级）
3. 非线性但单调的关系
4. 存在异常值的数据

**优势：**
1. 无需分布假设
2. 对异常值稳健
3. 适用范围广

**局限：**
1. 只能检测单调关系
2. 满足正态性时功效低于皮尔逊
3. 对结较敏感

**实践建议：**
1. 先进行数据探索，检查分布和关系形态
2. 满足正态性且为线性关系时使用皮尔逊
3. 否则使用Spearman秩相关
4. 同时报告相关系数、p值和置信区间
5. 结合可视化解释结果

理解Spearman秩相关的原理、适用条件和局限性，对于正确进行相关分析至关重要。
