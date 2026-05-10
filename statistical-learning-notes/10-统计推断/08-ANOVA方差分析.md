# ANOVA方差分析（Analysis of Variance）

## 定义

方差分析（Analysis of Variance, ANOVA）是由Ronald Fisher发展的统计方法，用于分析两个或多个组均值之间是否存在显著差异。尽管名称是"方差分析"，但其本质是比较组间变异和组内变异，从而推断组均值是否相等。

## 基本原理

### 方差分解

ANOVA的核心思想是将总变异（Total Variance）分解为两个部分：

$$SS_{total} = SS_{between} + SS_{within}$$

其中：
- $SS_{total}$ 是总平方和
- $SS_{between}$ 是组间平方和
- $SS_{within}$ 是组内平方和

### 自由度分解

$$df_{total} = df_{between} + df_{within}$$

$$df_{total} = N - 1$$
$$df_{between} = k - 1$$
$$df_{within} = N - k$$

其中：
- N 是总样本量
- k 是组数

## 单因素ANOVA（One-way ANOVA）

### 用途

检验一个因素（分类变量）对连续变量的影响。即检验k个组的均值是否相等。

### 假设

- H₀: μ₁ = μ₂ = ... = μ_k（所有组均值相等）
- H₁: 至少有一对组均值不相等

### 平方和计算

#### 1. 总平方和（Total Sum of Squares）

$$SS_{total} = \sum_{i=1}^{k}\sum_{j=1}^{n_i}(y_{ij} - \bar{y}_{..})^2$$

其中：
- $y_{ij}$ 是第i组第j个观测值
- $\bar{y}_{..}$ 是总均值

#### 2. 组间平方和（Between-group Sum of Squares）

$$SS_{between} = \sum_{i=1}^{k}n_i(\bar{y}_{i.} - \bar{y}_{..})^2$$

其中：
- $\bar{y}_{i.}$ 是第i组的组均值
- $n_i$ 是第i组的样本量

#### 3. 组内平方和（Within-group Sum of Squares）

$$SS_{within} = \sum_{i=1}^{k}\sum_{j=1}^{n_i}(y_{ij} - \bar{y}_{i.})^2$$

### 均方（Mean Squares）

$$MS_{between} = \frac{SS_{between}}{df_{between}} = \frac{SS_{between}}{k-1}$$

$$MS_{within} = \frac{SS_{within}}{df_{within}} = \frac{SS_{within}}{N-k}$$

### F统计量

$$F = \frac{MS_{between}}{MS_{within}}$$

### ANOVA表

| 变异来源 | 平方和(SS) | 自由度(df) | 均方(MS) | F值 | p值 |
|----------|-----------|-----------|----------|-----|-----|
| 组间 | $SS_{between}$ | k-1 | $MS_{between}$ | $MS_{between}/MS_{within}$ | - |
| 组内 | $SS_{within}$ | N-k | $MS_{within}$ | | |
| 总计 | $SS_{total}$ | N-1 | | | |

### 决策规则

- 如果 F > F_{α}(k-1, N-k) 或 p < α，拒绝H₀
- 否则，不拒绝H₀

### 前提条件

1. **正态性：** 每组数据应来自正态分布
   - 可用Shapiro-Wilk检验检验

2. **独立性：**
   - 组内观测值相互独立
   - 不同组之间相互独立

3. **方差齐性（Homoscedasticity）：**
   - 各组方差相等
   - 可用Levene检验或Bartlett检验检验

### 应用实例

研究三种教学方法对学生成绩的影响：

| 方法A | 方法B | 方法C |
|-------|-------|-------|
| 85 | 82 | 78 |
| 87 | 80 | 79 |
| 83 | 84 | 80 |
| 86 | 83 | 77 |
| 84 | 81 | 78 |

检验三种方法的效果是否有显著差异。

## 双因素ANOVA（Two-way ANOVA）

### 用途

分析两个因素（分类变量）对连续变量的影响，包括主效应和交互效应。

### 模型

$$y_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \varepsilon_{ijk}$$

其中：
- $\mu$ 是总体均值
- $\alpha_i$ 是因素A第i水平的主效应
- $\beta_j$ 是因素B第j水平的主效应
- $(\alpha\beta)_{ij}$ 是因素A第i水平和因素B第j水平的交互效应
- $\varepsilon_{ijk}$ 是误差项

### 平方和分解

$$SS_{total} = SS_A + SS_B + SS_{AB} + SS_{error}$$

其中：
- $SS_A$ 是因素A的主效应
- $SS_B$ 是因素B的主效应
- $SS_{AB}$ 是A和B的交互效应
- $SS_{error}$ 是误差项

### 双因素ANOVA表

| 变异来源 | 平方和(SS) | 自由度(df) | 均方(MS) | F值 |
|----------|-----------|-----------|----------|-----|
| 因素A | $SS_A$ | a-1 | $MS_A = SS_A/(a-1)$ | $MS_A/MS_{error}$ |
| 因素B | $SS_B$ | b-1 | $MS_B = SS_B/(b-1)$ | $MS_B/MS_{error}$ |
| 交互AB | $SS_{AB}$ | (a-1)(b-1) | $MS_{AB} = SS_{AB}/[(a-1)(b-1)]$ | $MS_{AB}/MS_{error}$ |
| 误差 | $SS_{error}$ | ab(n-1) | $MS_{error} = SS_{error}/[ab(n-1)]$ | |
| 总计 | $SS_{total}$ | abn-1 | | |

其中：
- a 是因素A的水平数
- b 是因素B的水平数
- n 是每个单元格的重复次数

### 交互效应的含义

交互效应表示一个因素的效果依赖于另一个因素的水平。

- **显著交互：** 因素A的效应在不同B水平下不同
- **不显著交互：** 因素A的效应独立于B的水平

### 应用实例

研究教学方法（A）和学生性别（B）对成绩的影响。

## 重复测量ANOVA（Repeated Measures ANOVA）

### 用途

分析同一被试在不同条件下的差异，适用于纵向研究或被试内设计。

### 特点

1. **减少误差：** 控制个体差异，提高检验功效
2. **需要球形假设：** 各时间点/条件的方差相等，协方差相等（Mauchly检验）

### 单因素重复测量ANOVA

$$y_{ij} = \mu + \pi_i + \tau_j + \varepsilon_{ij}$$

其中：
- $\pi_i$ 是被试i的效应（随机效应）
- $\tau_j$ 是时间/条件j的效应

### 前提条件

1. **球形假设（Sphericity）：**
   - 各时间点方差相等
   - 各时间点间协方差相等
   - 可用Mauchly检验检验

2. **不满足球形假设时的修正：**
   - Greenhouse-Geisser修正
   - Huynh-Feldt修正

## 事后检验（Post-hoc Tests）

当F检验显著（拒绝H₀）时，需要进行事后检验确定具体哪些组之间存在差异。

### 常用方法

#### 1. Tukey HSD（Honestly Significant Difference）

**特点：**
- 控制家族错误率（Family-wise Error Rate, FWER）
- 适用于所有配对比较
- 比较保守

**检验统计量：**
$$HSD = q_{\alpha,k,df_{error}} \cdot \sqrt{\frac{MS_{error}}{n}}$$

其中q是学生化范围分布的临界值。

#### 2. Bonferroni校正

**特点：**
- 简单易用
- 非常保守
- 调整显著性水平：$\alpha' = \alpha / m$（m是比较次数）

#### 3. Scheffé方法

**特点：**
- 最保守
- 适用于任何线性比较
- 适用于复杂的比较

#### 4. Dunnett检验

**特点：**
- 专门用于比较各组与对照组
- 更有功效
- 适用于多个实验组对一个对照组的比较

### 选择事后检验的原则

| 情况 | 推荐方法 |
|------|----------|
| 所有组两两比较 | Tukey HSD |
| 只与对照组比较 | Dunnett |
| 特定的复杂比较 | Scheffé |
| 比较次数较少 | Bonferroni |

## 效应量

### Eta-squared (η²)

$$\eta^2 = \frac{SS_{between}}{SS_{total}}$$

**解释：**
- 因素解释的变异占总变异的比例
- η² = 0.01: 小效应
- η² = 0.06: 中等效应
- η² = 0.14: 大效应

**注意：** η²有偏差，倾向于高估效应量。

### Partial Eta-squared (偏η²)

$$\eta^2_p = \frac{SS_{effect}}{SS_{effect} + SS_{error}}$$

**解释：**
- 消除其他因素影响后，该因素解释的变异比例

**优势：** 更适合多因素ANOVA。

### Omega-squared (ω²)

$$\omega^2 = \frac{SS_{between} - (k-1)MS_{error}}{SS_{total} + MS_{error}}$$

**优势：** 比η²更精确的无偏估计。

## ANOVA的假设检验

### 1. 正态性检验

```python
# Shapiro-Wilk检验
from scipy import stats

for group in groups:
    statistic, p_value = stats.shapiro(group)
    print(f"Shapiro-Wilk: p = {p_value:.4f}")
```

**应对方法：**
- 转换数据（如对数转换）
- 使用非参数方法（Kruskal-Wallis检验）

### 2. 方差齐性检验

```python
# Levene检验
statistic, p_value = stats.levene(*groups)

# Bartlett检验
statistic, p_value = stats.bartlett(*groups)
```

**应对方法：**
- Welch ANOVA（方差不齐时）
- 数据转换
- Brown-Forsythe检验

### 3. 独立性

通过研究设计保证，统计上难以检验。

## 方差不齐时的替代方法

### Welch ANOVA

当方差齐性假设不满足时使用：

$$F^* = \frac{\sum_{i=1}^{k}w_i(\bar{y}_i - \tilde{y})^2/(k-1)}{1 + \frac{2(k-2)}{k^2-1}\sum_{i=1}^{k}\frac{(1-w_i/\bar{w})^2}{n_i-1}}$$

其中：
- $w_i = n_i/s_i^2$
- $\tilde{y} = \frac{\sum w_i\bar{y}_i}{\sum w_i}$

### Brown-Forsythe检验

使用中位数而不是均值，更稳健：

$$F_{BF} = \frac{\sum_{i=1}^{k}n_i(\tilde{y}_i - \tilde{y}_{..})^2/(k-1)}{\sum_{i=1}^{k}\sum_{j=1}^{n_i}|y_{ij} - \tilde{y}_i|/(N-k)}$$

其中$\tilde{y}$表示中位数。

## Python实现示例

```python
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import AnovaRM
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 单因素ANOVA
# 示例：三种教学方法的效果
group_A = np.array([85, 87, 83, 86, 84, 86, 82, 88, 84, 85])
group_B = np.array([82, 80, 84, 83, 81, 82, 79, 84, 81, 80])
group_C = np.array([78, 79, 80, 77, 78, 79, 76, 80, 78, 79])

# 使用scipy
f_stat, p_value = stats.f_oneway(group_A, group_B, group_C)
print(f"单因素ANOVA: F = {f_stat:.4f}, p = {p_value:.4f}")

# 使用statsmodels
data = pd.DataFrame({
    'score': np.concatenate([group_A, group_B, group_C]),
    'method': ['A']*10 + ['B']*10 + ['C']*10
})

model = ols('score ~ C(method)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("\nANOVA表:")
print(anova_table)

# 2. 事后检验（Tukey HSD）
tukey = pairwise_tukeyhsd(data['score'], data['method'])
print("\nTukey HSD事后检验:")
print(tukey)

# 3. 双因素ANOVA
# 示例：教学方法×性别
np.random.seed(42)
data_2way = pd.DataFrame({
    'score': np.concatenate([
        np.random.normal(85, 3, 10),  # A-男
        np.random.normal(83, 3, 10),  # A-女
        np.random.normal(80, 3, 10),  # B-男
        np.random.normal(78, 3, 10)   # B-女
    ]),
    'method': ['A']*10 + ['A']*10 + ['B']*10 + ['B']*10,
    'gender': ['男']*10 + ['女']*10 + ['男']*10 + ['女']*10
})

model_2way = ols('score ~ C(method) * C(gender)', data=data_2way).fit()
anova_table_2way = sm.stats.anova_lm(model_2way, typ=2)
print("\n双因素ANOVA表:")
print(anova_table_2way)

# 4. 重复测量ANOVA
# 示例：4个时间点的测量
np.random.seed(42)
n_subjects = 10
n_timepoints = 4

data_rm = pd.DataFrame({
    'subject': np.repeat(range(n_subjects), n_timepoints),
    'time': np.tile(['T1', 'T2', 'T3', 'T4'], n_subjects),
    'score': np.concatenate([
        np.random.normal(75, 3, n_subjects),  # T1
        np.random.normal(78, 3, n_subjects),  # T2
        np.random.normal(82, 3, n_subjects),  # T3
        np.random.normal(85, 3, n_subjects)   # T4
    ])
})

aovrm = AnovaRM(data_rm, 'score', 'subject', within=['time'])
res = aovrm.fit()
print("\n重复测量ANOVA:")
print(res)

# 5. 效应量计算
def calculate_eta_squared(anova_table):
    """计算效应量 eta-squared"""
    ss_between = anova_table.loc['C(method)', 'sum_sq']
    ss_total = anova_table['sum_sq'].sum()
    return ss_between / ss_total

eta_squared = calculate_eta_squared(anova_table)
print(f"\n效应量 η² = {eta_squared:.4f}")

# 6. 假设检验
# 正态性检验
print("\n正态性检验:")
for name, group in [('A', group_A), ('B', group_B), ('C', group_C)]:
    stat, p = stats.shapiro(group)
    print(f"组{name}: Shapiro-Wilk p = {p:.4f}")

# 方差齐性检验
stat, p = stats.levene(group_A, group_B, group_C)
print(f"\n方差齐性 (Levene): p = {p:.4f}")

# 7. 可视化
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 箱线图
sns.boxplot(x='method', y='score', data=data, ax=axes[0])
axes[0].set_title('各组分数分布')
axes[0].set_xlabel('教学方法')
axes[0].set_ylabel('分数')

# 均值条形图
sns.barplot(x='method', y='score', data=data, ax=axes[1], ci=95)
axes[1].set_title('各组均值与95%置信区间')
axes[1].set_xlabel('教学方法')
axes[1].set_ylabel('分数')

plt.tight_layout()
plt.show()

# 8. 残差分析
residuals = model.resid
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 残差直方图
axes[0].hist(residuals, bins=15, edgecolor='black')
axes[0].set_title('残差分布')
axes[0].set_xlabel('残差')
axes[0].set_ylabel('频数')

# Q-Q图
stats.probplot(residuals, dist="norm", plot=axes[1])
axes[1].set_title('残差Q-Q图')
axes[1].grid(True)

plt.tight_layout()
plt.show()
```

## ANOVA与t检验的关系

| 特征 | t检验 | ANOVA |
|------|-------|-------|
| 比较组数 | 2组 | 2组或更多 |
| 假设检验 | H₀: μ₁ = μ₂ | H₀: μ₁ = μ₂ = ... = μ_k |
| 检验统计量 | t | F |
| 关系 | t² = F (两组时) | 包含t检验 |

当k = 2时：
- ANOVA的F统计量等于t检验的t统计量的平方
- 两种方法等价

## ANOVA的局限性与替代方法

### 局限性

1. **假设敏感：** 对正态性和方差齐性敏感
2. **组间比较：** F检验只告诉我们存在差异，不告诉哪里有差异
3. **设计限制：** 只适用于平衡设计或不平衡但分析正确的设计
4. **效应大小：** 大样本时微小效应也可能显著

### 替代方法

| 条件 | 替代方法 |
|------|----------|
| 非正态数据 | Kruskal-Wallis检验（非参数ANOVA） |
| 方差不齐 | Welch ANOVA, Brown-Forsythe检验 |
| 重复测量且不满足球形假设 | 多层线性模型, 广义估计方程 |
| 分类因变量 | Logistic回归 |
| 计数数据 | Poisson回归 |

## 总结

ANOVA是比较多个组均值的重要统计方法。

**核心要点：**
1. 方差分解：总变异 = 组间变异 + 组内变异
2. F检验：比较组间均方和组内均方
3. 显著后需要事后检验确定具体差异
4. 需要检查前提条件

**应用场景：**
1. 单因素ANOVA：一个因素多个水平
2. 双因素ANOVA：两个因素的主效应和交互效应
3. 重复测量ANOVA：纵向研究或被试内设计

**注意事项：**
1. 检查正态性和方差齐性
2. F检验显著后进行事后检验
3. 报告效应量而非仅p值
4. 方差不齐时使用Welch ANOVA

**最佳实践：**
1. 可视化数据（箱线图、均值图）
2. 检验假设条件
3. 报告ANOVA表、效应量、事后检验结果
4. 解释实际意义而非仅统计显著性

理解ANOVA的原理、假设条件和局限性，对于正确进行多组比较分析至关重要。