# 多元方差分析（MANOVA）

## 定义

多元方差分析（Multivariate Analysis of Variance, MANOVA）是单因素方差分析（ANOVA）在多变量情况下的扩展。它用于检验一个或多个分类自变量（因素）对两个或多个连续因变量组的均值向量是否存在显著差异。

与ANOVA比较单一因变量的组间差异不同，MANOVA同时分析多个因变量，能够：
- 控制I型错误率（Type I Error）
- 探究因变量之间的关系
- 检验因素对因变量组合的整体效应

## MANOVA 与 ANOVA 的比较

| 特征 | ANOVA | MANOVA |
|------|-------|--------|
| 因变量数量 | 1个 | 2个或更多 |
| 假设检验 | H₀: μ₁ = μ₂ = ... = μ_k | H₀: μ₁ = μ₂ = ... = μ_k（均值向量） |
| 检验统计量 | F统计量 | Wilks' Λ, Pillai's Trace, Hotelling's T², Roy's Largest Root |
| I型错误控制 | 每次检验独立 | 多重检验间控制 |
| 信息量 | 仅单一维度 | 多维信息，考虑因变量间关系 |
| 样本量要求 | 相对较小 | 需要更大的样本量 |
| 假设条件 | 正态性、方差齐性、独立性 | 多元正态性、协方差矩阵齐性、独立性 |

### 何时选择 MANOVA 而非 ANOVA

1. **研究问题涉及多个相关的因变量**
   - 例如：同时研究教学方法对学生数学成绩、物理成绩和化学成绩的影响

2. **因变量之间存在相关性**
   - MANOVA可以利用因变量间的相关信息提高检验功效

3. **控制实验错误率**
   - 避免对多个因变量分别进行ANOVA导致的I型错误膨胀

4. **探索因变量的组合模式**
   - 识别哪些因变量的组合最能区分不同组

## 基本原理

### 数据结构

假设有k个组，每组有n_i个观测，p个因变量：

$$X_{ij} = (x_{ij1}, x_{ij2}, ..., x_{ijp})^T$$

其中：
- i = 1, 2, ..., k（组别）
- j = 1, 2, ..., n_i（组内观测）
- p（因变量个数）

### 方差-协方差矩阵分解

MANOVA将总变异-协方差矩阵分解为组间和组内部分：

$$T = H + E$$

其中：
- T 是总平方和与交叉乘积矩阵（Total SSCP Matrix）
- H 是组间平方和与交叉乘积矩阵（Between-group SSCP Matrix）
- E 是组内平方和与交叉乘积矩阵（Within-group SSCP Matrix）

#### 总SSCP矩阵（T）

$$T = \sum_{i=1}^{k}\sum_{j=1}^{n_i}(X_{ij} - \bar{X}_{..})(X_{ij} - \bar{X}_{..})^T$$

其中 $\bar{X}_{..}$ 是总均值向量。

#### 组间SSCP矩阵（H）

$$H = \sum_{i=1}^{k}n_i(\bar{X}_{i.} - \bar{X}_{..})(\bar{X}_{i.} - \bar{X}_{..})^T$$

其中 $\bar{X}_{i.}$ 是第i组的组均值向量。

#### 组内SSCP矩阵（E）

$$E = \sum_{i=1}^{k}\sum_{j=1}^{n_i}(X_{ij} - \bar{X}_{i.})(X_{ij} - \bar{X}_{i.})^T$$

## 检验统计量

MANOVA有四种常用的检验统计量，它们基于H和E矩阵的不同特征值：

### 1. Wilks' Lambda（Λ）

最常用的检验统计量：

$$\Lambda = \frac{|E|}{|H + E|} = \frac{|E|}{|T|} = \prod_{j=1}^{s}\frac{1}{1 + \lambda_j}$$

其中：
- |·| 表示行列式
- λ_j 是 E^{-1}H 的特征值
- s = min(p, k-1)

**特点：**
- Λ值越小，组间差异越大
- 范围：[0, 1]
- Λ = 1 表示所有组均值向量相同
- Λ → 0 表示至少有一对组均值向量不同

**转换为F统计量：**
对于小样本，可以将Λ转换为F统计量：

$$F = \frac{1-\Lambda^{1/t}}{\Lambda^{1/t}} \cdot \frac{df_2}{df_1}$$

其中自由度取决于k, p, N。

### 2. Pillai's Trace（V）

$$V = \sum_{j=1}^{s}\frac{\lambda_j}{1 + \lambda_j} = \text{tr}[H(H+E)^{-1}]$$

**特点：**
- 最稳健的统计量，对违反假设不敏感
- 适用于非平衡设计
- V值越大，组间差异越大
- 范围：[0, s]

### 3. Hotelling-Lawley Trace（T²）

$$T^2 = \sum_{j=1}^{s}\lambda_j = \text{tr}[HE^{-1}]$$

**特点：**
- 也称为Hotelling's T²
- 适用于因变量数量较少的情况
- T²值越大，组间差异越大
- 在协方差矩阵齐性满足时有较高功效

### 4. Roy's Largest Root（θ）

$$\theta = \frac{\lambda_{max}}{1 + \lambda_{max}}$$

其中 λ_max 是 E^{-1}H 的最大特征值。

**特点：**
- 最有功效但最不稳健
- 适用于组间差异主要体现在一个方向的情况
- 仅考虑最大的特征值

### 检验统计量的选择

| 情况 | 推荐统计量 |
|------|-----------|
| 一般情况 | Wilks' Lambda |
| 假设可能违反 | Pillai's Trace |
| 因变量数量少 | Hotelling-Lawley Trace |
| 理论上最大功效（需假设满足） | Roy's Largest Root |
| 非平衡设计 | Pillai's Trace |

## 前提条件

### 1. 多元正态性（Multivariate Normality）

每个组的因变量向量应来自多元正态分布。

$$X_{ij} \sim N_p(\mu_i, \Sigma)$$

**检验方法：**

```python
# Shapiro-Wilk检验（每个因变量分别检验）
from scipy import stats
for var in dependent_vars:
    stat, p = stats.shapiro(data[var])
    print(f"{var}: Shapiro-Wilk p = {p:.4f}")

# Mardia检验（真正的多元正态性检验）
from scipy.stats import skew, kurtosis
# 需要自定义实现或使用特定包
```

**应对方法：**
- 大样本时（每组 n > 20）MANOVA对正态性偏离具有一定稳健性
- 数据转换（如对数转换、Box-Cox转换）
- 非参数替代方法（如PERMANOVA）

### 2. 协方差矩阵齐性（Homogeneity of Covariance Matrices）

各组的协方差矩阵应相等：

$$\Sigma_1 = \Sigma_2 = ... = \Sigma_k = \Sigma$$

**检验方法：**

```python
# Box's M检验
from scipy import stats
# 需要自定义实现或使用特定包

# Levene检验（每个因变量分别检验）
from scipy.stats import levene
for var in dependent_vars:
    stat, p = levene(*[group_data[var] for group_data in groups])
    print(f"{var}: Levene p = {p:.4f}")
```

**Box's M检验注意事项：**
- 对正态性假设敏感
- 大样本时可能过于敏感
- 建议同时观察实际协方差矩阵的差异

**应对方法：**
- Pillai's Trace统计量对方差不齐较稳健
- 数据转换
- 使用James检验等替代方法

### 3. 独立性

观测值之间相互独立。

**保证方法：**
- 通过研究设计保证
- 随机抽样
- 避免重复测量数据（除非使用重复测量MANOVA）

### 4. 无多重共线性（No Multicollinearity）

因变量之间不应存在极高的相关性（r > 0.9）。

**检验方法：**

```python
# 计算相关系数矩阵
correlation_matrix = data[dependent_vars].corr()
print(correlation_matrix)

# 计算方差膨胀因子（VIF）
from statsmodels.stats.outliers_influence import variance_inflation_factor
```

**应对方法：**
- 移除高度相关的因变量
- 主成分分析降维
- 因子分析

### 5. 线性关系

因变量之间应存在线性关系。

**检验方法：**
- 散点图矩阵
- 计算相关系数

### 6. 无异常值

各组的多元空间中不应有极端异常值。

**检验方法：**

```python
# 马氏距离（Mahalanobis Distance）
from scipy.spatial.distance import mahalanobis
from numpy.linalg import inv

def detect_outliers(data, dependent_vars):
    """使用马氏距离检测异常值"""
    X = data[dependent_vars].values
    cov_matrix = np.cov(X, rowvar=False)
    inv_cov = inv(cov_matrix)
    mean = np.mean(X, axis=0)

    distances = []
    for i in range(len(X)):
        d = mahalanobis(X[i], mean, inv_cov)
        distances.append(d)

    # 卡方分布临界值
    from scipy.stats import chi2
    critical_value = chi2.ppf(0.975, df=len(dependent_vars))

    outliers = np.where(np.array(distances) > critical_value)[0]
    return outliers, distances
```

## MANOVA的假设检验

### 单因素MANOVA（One-way MANOVA）

#### 假设

- H₀: μ₁ = μ₂ = ... = μ_k（所有组均值向量相等）
- H₁: 至少有一对组均值向量不相等

#### Python实现

```python
import numpy as np
import pandas as pd
from statsmodels.multivariate.manova import MANOVA
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 示例数据：三种教学方法对学生数学、物理、化学成绩的影响
np.random.seed(42)

n = 30  # 每组样本量
k = 3   # 组数
p = 3   # 因变量数量（数学、物理、化学）

# 生成数据
group_A = pd.DataFrame({
    'math': np.random.normal(85, 5, n),
    'physics': np.random.normal(82, 5, n),
    'chemistry': np.random.normal(80, 5, n),
    'method': ['A'] * n
})

group_B = pd.DataFrame({
    'math': np.random.normal(78, 5, n),
    'physics': np.random.normal(80, 5, n),
    'chemistry': np.random.normal(82, 5, n),
    'method': ['B'] * n
})

group_C = pd.DataFrame({
    'math': np.random.normal(75, 5, n),
    'physics': np.random.normal(76, 5, n),
    'chemistry': np.random.normal(78, 5, n),
    'method': ['C'] * n
})

# 合并数据
data = pd.concat([group_A, group_B, group_C], ignore_index=True)

# 1. 数据探索
print("数据概览:")
print(data.groupby('method').describe())

# 2. 可视化
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for i, subject in enumerate(['math', 'physics', 'chemistry']):
    sns.boxplot(x='method', y=subject, data=data, ax=axes[i])
    axes[i].set_title(f'{subject}成绩分布')
    axes[i].set_xlabel('教学方法')
    axes[i].set_ylabel('成绩')

plt.tight_layout()
plt.show()

# 3. 散点图矩阵
sns.pairplot(data, vars=['math', 'physics', 'chemistry'], hue='method', diag_kind='kde')
plt.suptitle('各科成绩的成对关系', y=1.02)
plt.show()

# 4. 计算相关系数矩阵
print("\n相关系数矩阵:")
correlation_matrix = data[['math', 'physics', 'chemistry']].corr()
print(correlation_matrix)

# 5. 正态性检验（Shapiro-Wilk）
print("\n正态性检验（Shapiro-Wilk）:")
for subject in ['math', 'physics', 'chemistry']:
    for method in ['A', 'B', 'C']:
        subset = data[data['method'] == method][subject]
        stat, p = stats.shapiro(subset)
        print(f"{subject} - 方法{method}: W = {stat:.4f}, p = {p:.4f}")

# 6. 方差齐性检验（Levene）
print("\n方差齐性检验（Levene）:")
for subject in ['math', 'physics', 'chemistry']:
    groups = [data[data['method'] == m][subject] for m in ['A', 'B', 'C']]
    stat, p = stats.levene(*groups)
    print(f"{subject}: W = {stat:.4f}, p = {p:.4f}")

# 7. 执行MANOVA
print("\n" + "="*50)
print("MANOVA结果")
print("="*50)

maov = MANOVA.from_formula('math + physics + chemistry ~ method', data=data)
print(maov.mv_test())
```

### 双因素MANOVA（Two-way MANOVA）

#### 用途

分析两个因素对多个因变量的影响，包括主效应和交互效应。

#### Python实现

```python
# 双因素MANOVA：教学方法×性别
np.random.seed(42)

n_per_cell = 15  # 每个单元格的样本量

data_2way = []
for method in ['A', 'B']:
    for gender in ['男', '女']:
        math_mean = 85 if method == 'A' else 78
        physics_mean = 82 if method == 'A' else 80
        chemistry_mean = 80 if method == 'A' else 82
        
        # 添加性别效应
        if gender == '女':
            math_mean += 2
            physics_mean += 1
        
        data_2way.append(pd.DataFrame({
            'math': np.random.normal(math_mean, 5, n_per_cell),
            'physics': np.random.normal(physics_mean, 5, n_per_cell),
            'chemistry': np.random.normal(chemistry_mean, 5, n_per_cell),
            'method': [method] * n_per_cell,
            'gender': [gender] * n_per_cell
        }))

data_2way = pd.concat(data_2way, ignore_index=True)

# 执行双因素MANOVA
maov_2way = MANOVA.from_formula(
    'math + physics + chemistry ~ C(method) * C(gender)', 
    data=data_2way
)
print("双因素MANOVA结果:")
print(maov_2way.mv_test())
```

## 事后检验（Post-hoc Tests）

当MANOVA的检验结果显著（拒绝H₀）时，需要进行事后检验以确定：
1. 哪些组之间存在差异
2. 哪些因变量对差异贡献最大

### 1. 单变量ANOVA事后检验

对每个因变量分别进行单因素ANOVA：

```python
print("\n" + "="*50)
print("单变量ANOVA事后检验")
print("="*50)

from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

for subject in ['math', 'physics', 'chemistry']:
    model = ols(f'{subject} ~ C(method)', data=data).fit()
    anova_table = anova_lm(model, typ=2)
    print(f"\n{subject} ANOVA:")
    print(anova_table)
```

### 2. 配对比较（Tukey HSD）

对每个因变量进行Tukey HSD检验：

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd

print("\n" + "="*50)
print("Tukey HSD配对比较")
print("="*50)

for subject in ['math', 'physics', 'chemistry']:
    tukey = pairwise_tukeyhsd(data[subject], data['method'])
    print(f"\n{subject}:")
    print(tukey)
```

### 3. 区分函数分析（Discriminant Function Analysis）

确定哪些因变量的组合最能区分各组：

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler

# 准备数据
X = data[['math', 'physics', 'chemistry']].values
y = data['method'].values

# 标准化
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# 线性判别分析
lda = LinearDiscriminantAnalysis()
X_lda = lda.fit_transform(X_std, y)

# 输出判别函数系数
print("\n" + "="*50)
print("判别函数分析")
print("="*50)
print("\n判别函数系数:")
for i, subject in enumerate(['math', 'physics', 'chemistry']):
    print(f"{subject}: {lda.coef_[0, i]:.4f}")

# 可视化
plt.figure(figsize=(10, 6))
colors = {'A': 'red', 'B': 'green', 'C': 'blue'}
for method in ['A', 'B', 'C']:
    mask = y == method
    plt.scatter(X_lda[mask, 0], np.zeros(np.sum(mask)),
                c=colors[method], label=f'方法{method}', alpha=0.6, s=100)

plt.xlabel('判别函数1')
plt.title('组间区分（判别函数）')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 4. 效应量

#### 偏Eta平方（Partial Eta-squared）

```python
def calculate_partial_eta_squared(anova_table, effect_name):
    """计算偏η²"""
    ss_effect = anova_table.loc[effect_name, 'sum_sq']
    ss_error = anova_table.loc['Residual', 'sum_sq']
    return ss_effect / (ss_effect + ss_error)

print("\n" + "="*50)
print("效应量（偏η²）")
print("="*50)

for subject in ['math', 'physics', 'chemistry']:
    model = ols(f'{subject} ~ C(method)', data=data).fit()
    anova_table = anova_lm(model, typ=2)
    
    eta_squared = calculate_partial_eta_squared(anova_table, 'C(method)')
    print(f"{subject}: 偏η² = {eta_squared:.4f}")
    
    # 解释
    if eta_squared < 0.01:
        interpretation = "小效应"
    elif eta_squared < 0.06:
        interpretation = "中等效应"
    elif eta_squared < 0.14:
        interpretation = "较大效应"
    else:
        interpretation = "大效应"
    print(f"  解释: {interpretation}")
```

## 重复测量MANOVA

### 定义

当同一被试在多个时间点或条件下被测量多个因变量时，使用重复测量MANOVA。

### Python实现（使用pingouin库）

```python
# 注意：需要安装 pingouin
# pip install pingouin

import pingouin as pg

# 示例：10名学生在3个时间点的数学、物理、化学成绩
np.random.seed(42)

n_subjects = 10
n_timepoints = 3

data_rm = []
for subject in range(n_subjects):
    # 每个学生有基础能力
    base_math = np.random.normal(80, 5)
    base_physics = np.random.normal(78, 5)
    base_chemistry = np.random.normal(76, 5)
    
    for time in ['T1', 'T2', 'T3']:
        # 时间效应：成绩随时间提高
        time_effect = {'T1': 0, 'T2': 3, 'T3': 6}[time]
        
        data_rm.append({
            'subject': subject,
            'time': time,
            'math': base_math + time_effect + np.random.normal(0, 2),
            'physics': base_physics + time_effect + np.random.normal(0, 2),
            'chemistry': base_chemistry + time_effect + np.random.normal(0, 2)
        })

data_rm = pd.DataFrame(data_rm)

# 重塑数据为宽格式
data_rm_wide = data_rm.pivot(index='subject', columns='time', 
                              values=['math', 'physics', 'chemistry'])

# 重复测量MANOVA
print("\n" + "="*50)
print("重复测量MANOVA")
print("="*50)

# 使用pingouin进行重复测量MANOVA
# 注意：需要根据实际API调整
# rm_manova = pg.rm_manova(data_rm, dv=['math', 'physics', 'chemistry'],
#                          within='time', subject='subject')
# print(rm_manova)
```

## 完整示例：教育研究案例

### 研究问题

比较三种不同教学方法对学生数学、物理、化学三科成绩的影响。

```python
import numpy as np
import pandas as pd
from statsmodels.multivariate.manova import MANOVA
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
from scipy.spatial.distance import mahalanobis
from numpy.linalg import inv
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler

# 设置随机种子和参数
np.random.seed(42)
n_per_group = 35  # 每组35人
methods = ['传统讲授', '互动讨论', '项目学习']
subjects = ['数学', '物理', '化学']

# 真实效应（均值）
true_means = {
    '传统讲授': {'数学': 75, '物理': 73, '化学': 71},
    '互动讨论': {'数学': 80, '物理': 78, '化学': 76},
    '项目学习': {'数学': 85, '物理': 83, '化学': 81}
}

# 协方差矩阵（各科成绩相关）
cov_matrix = np.array([
    [25, 16, 12],  # 数学
    [16, 25, 16],  # 物理
    [12, 16, 25]   # 化学
])

# 生成数据
data = []
for method in methods:
    means = [true_means[method][s] for s in subjects]
    group_data = np.random.multivariate_normal(means, cov_matrix, n_per_group)
    
    for i in range(n_per_group):
        row = {'方法': method}
        for j, subject in enumerate(subjects):
            row[subject] = group_data[i, j]
        data.append(row)

data = pd.DataFrame(data)

print("="*70)
print("研究案例：教学方法对学生多科成绩的影响")
print("="*70)

# 1. 描述性统计
print("\n【1. 描述性统计】")
print(data.groupby('方法').agg(['mean', 'std']))

# 2. 相关性分析
print("\n【2. 各科成绩相关系数矩阵】")
print(data[subjects].corr())

# 3. 可视化
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 箱线图
for i, subject in enumerate(subjects):
    sns.boxplot(x='方法', y=subject, data=data, ax=axes[0, i])
    axes[0, i].set_title(f'{subject}成绩分布')
    axes[0, i].set_xlabel('')
    axes[0, i].set_ylabel('成绩')

# 密度图
for i, subject in enumerate(subjects):
    for method in methods:
        subset = data[data['方法'] == method][subject]
        sns.kdeplot(subset, label=method, ax=axes[1, i], fill=True, alpha=0.3)
    axes[1, i].set_title(f'{subject}成绩密度分布')
    axes[1, i].set_xlabel('成绩')
    axes[1, i].legend()

plt.tight_layout()
plt.savefig('manova_descriptive.png', dpi=150, bbox_inches='tight')
plt.show()

# 4. 假设检验
print("\n【3. 假设检验】")

# 正态性检验
print("\n--- 正态性检验（Shapiro-Wilk）---")
for subject in subjects:
    print(f"\n{subject}:")
    for method in methods:
        subset = data[data['方法'] == method][subject]
        stat, p = stats.shapiro(subset)
        status = "✓" if p > 0.05 else "✗"
        print(f"  {method}: W={stat:.4f}, p={p:.4f} {status}")

# 方差齐性检验
print("\n--- 方差齐性检验（Levene）---")
for subject in subjects:
    groups = [data[data['方法'] == m][subject] for m in methods]
    stat, p = stats.levene(*groups)
    status = "✓" if p > 0.05 else "✗"
    print(f"{subject}: W={stat:.4f}, p={p:.4f} {status}")

# 5. 异常值检测（马氏距离）
print("\n【4. 异常值检测（马氏距离）】")
X = data[subjects].values
cov_matrix = np.cov(X, rowvar=False)
inv_cov = inv(cov_matrix)
mean = np.mean(X, axis=0)

# 计算马氏距离
distances = []
for i in range(len(X)):
    d = mahalanobis(X[i], mean, inv_cov)
    distances.append(d)

# 卡方临界值（α=0.025）
from scipy.stats import chi2
critical_value = chi2.ppf(0.975, df=len(subjects))
outliers = np.where(np.array(distances) > critical_value)[0]

print(f"马氏距离临界值（α=0.025）: {critical_value:.4f}")
print(f"检测到异常值数量: {len(outliers)}")

if len(outliers) > 0:
    print(f"异常值索引: {outliers}")
    # 不移除异常值，仅报告

# 6. 执行MANOVA
print("\n【5. MANOVA检验结果】")
print("="*70)
maov = MANOVA.from_formula('数学 + 物理 + 化学 ~ 方法', data=data)
manova_results = maov.mv_test()
print(manova_results)

# 解读MANOVA结果
print("\n--- 结果解读 ---")
# 从结果中提取p值（需要根据实际输出调整）
# 这里假设p < 0.05，进行后续分析
print("MANOVA检验结果显著（p < 0.05），表明至少有一对教学方法组在多科成绩上存在差异。")

# 7. 单变量ANOVA事后检验
print("\n【6. 单变量ANOVA】")
print("="*70)

for subject in subjects:
    model = ols(f'{subject} ~ C(方法)', data=data).fit()
    anova_table = anova_lm(model, typ=2)
    
    # 计算效应量
    ss_effect = anova_table.loc['C(方法)', 'sum_sq']
    ss_error = anova_table.loc['Residual', 'sum_sq']
    eta_squared = ss_effect / (ss_effect + ss_error)
    
    # 解释效应量
    if eta_squared < 0.01:
        interp = "小效应"
    elif eta_squared < 0.06:
        interp = "中等效应"
    elif eta_squared < 0.14:
        interp = "较大效应"
    else:
        interp = "大效应"
    
    print(f"\n{subject}:")
    print(f"  F = {anova_table.loc['C(方法)', 'F']:.4f}")
    print(f"  p = {anova_table.loc['C(方法)', 'PR(>F)']:.4f}")
    print(f"  偏η² = {eta_squared:.4f} ({interp})")

# 8. Tukey HSD配对比较
print("\n【7. Tukey HSD配对比较】")
print("="*70)

for subject in subjects:
    tukey = pairwise_tukeyhsd(data[subject], data['方法'])
    print(f"\n{subject}:")
    print(tukey)

# 9. 判别函数分析
print("\n【8. 判别函数分析】")
print("="*70)

# 准备数据
X = data[subjects].values
y = data['方法'].values

# 标准化
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# 线性判别分析
lda = LinearDiscriminantAnalysis()
X_lda = lda.fit_transform(X_std, y)

# 输出判别函数系数
print("\n判别函数系数（标准化后）:")
for i, subject in enumerate(subjects):
    print(f"  {subject}: {lda.coef_[0, i]:.4f}")

# 组中心
print("\n各组判别得分均值:")
for i, method in enumerate(methods):
    group_lda = X_lda[y == method]
    print(f"  {method}: {group_lda.mean():.4f}")

# 可视化判别结果
plt.figure(figsize=(12, 6))

# 子图1：判别得分分布
plt.subplot(1, 2, 1)
colors = {'传统讲授': 'red', '互动讨论': 'green', '项目学习': 'blue'}
for method in methods:
    mask = y == method
    plt.scatter(X_lda[mask, 0], np.zeros(np.sum(mask)),
                c=colors[method], label=method, alpha=0.6, s=100)
plt.xlabel('判别函数1得分')
plt.title('组间区分（判别函数）')
plt.legend()
plt.grid(True, alpha=0.3)
plt.yticks([])

# 子图2：判别得分箱线图
plt.subplot(1, 2, 2)
lda_df = pd.DataFrame({
    '判别得分': X_lda[:, 0],
    '方法': y
})
sns.boxplot(x='方法', y='判别得分', data=lda_df)
plt.title('各组判别得分分布')
plt.xlabel('')
plt.ylabel('判别函数1得分')
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('manova_discriminant.png', dpi=150, bbox_inches='tight')
plt.show()

# 10. 结论
print("\n【9. 研究结论】")
print("="*70)
print("""
基于上述分析，得出以下结论：

1. MANOVA检验结果显示，不同教学方法对学生多科成绩组合有显著影响
   （Wilks' Λ = [具体值], F = [具体值], p < 0.05）。

2. 单变量ANOVA结果表明：
   - 数学成绩：[具体p值]，[是否显著]
   - 物理成绩：[具体p值]，[是否显著]
   - 化学成绩：[具体p值]，[是否显著]

3. Tukey HSD事后检验显示：
   - [具体配对比较结果]

4. 判别函数分析表明，[哪科]对组间区分贡献最大。

5. 效应量分析显示，[具体效应量大小]。

建议：
- 根据研究结果，推荐[效果最好的]教学方法
- 考虑各科成绩的相关性，综合评估教学方法
- 后续研究可考虑增加样本量，控制其他变量
""")

print("\n" + "="*70)
print("分析完成！")
print("="*70)
```

## MANOVA的局限性与替代方法

### 局限性

1. **样本量要求高**
   - 需要较大的样本量以获得可靠的估计
   - 建议每组的样本量至少为因变量数量的5-10倍

2. **假设严格**
   - 多元正态性
   - 协方差矩阵齐性
   - 无多重共线性

3. **解释复杂**
   - 显著结果需要进一步的单变量分析
   - 判别函数的解释需要专业知识

4. **对异常值敏感**
   - 多元空间中的异常值影响较大

### 替代方法

| 情况 | 替代方法 |
|------|----------|
| 不满足正态性 | PERMANOVA（基于距离的多变量方差分析） |
| 不满足协方差齐性 | James检验，使用Pillai's Trace |
| 因变量高度相关 | 主成分分析（PCA）+ ANOVA |
| 重复测量设计 | 重复测量MANOVA，混合模型 |
| 分类因变量 | 多元Logistic回归 |
| 非参数数据 | 多元置换检验 |

## 总结

MANOVA是分析多组多变量数据的重要统计方法。

**核心要点：**
1. 同时分析多个因变量，控制I型错误
2. 利用四种检验统计量：Wilks' Λ, Pillai's Trace, Hotelling's T², Roy's Largest Root
3. 需要满足多元正态性、协方差矩阵齐性等假设
4. 显著后需进行单变量ANOVA和事后检验
5. 判别函数分析有助于理解组间差异的来源

**应用场景：**
1. 单因素MANOVA：一个因素多个水平对多个因变量的影响
2. 双因素MANOVA：两个因素的主效应和交互效应
3. 重复测量MANOVA：纵向研究或被试内设计

**最佳实践：**
1. 检验所有假设条件
2. 可视化多维数据
3. 报告MANOVA结果、单变量结果、事后检验和效应量
4. 使用稳健的检验统计量（如Pillai's Trace）
5. 考虑因变量间的相关性

**注意事项：**
1. 样本量要足够
2. 检测和处理异常值
3. 避免高度相关的因变量
4. 正确解释统计显著性和实际意义
5. 根据数据特点选择合适的检验统计量

理解MANOVA的原理、假设条件和应用场景，对于正确进行多变量多组比较分析至关重要。在社会科学、心理学、教育研究、医学研究等领域，MANOVA都是一个强大的分析工具。
