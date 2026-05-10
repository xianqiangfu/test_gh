# 协方差分析（ANCOVA, Analysis of Covariance）

## 定义

协方差分析（Analysis of Covariance, ANCOVA）是一种结合了方差分析（ANOVA）和回归分析的统计方法。它通过在分析中包含协变量（Covariate），来控制可能影响因变量的混杂因素，从而更准确地检验不同组别之间在因变量上的差异。

**核心思想：** 在比较组间差异时，控制一个或多个连续型协变量的影响，减少误差变异，提高检验效能。

## ANCOVA与ANOVA的比较

| 特征 | ANOVA | ANCOVA |
|------|-------|--------|
| 仅考虑的因素 | 组别（分类变量） | 组别（分类变量）+ 协变量（连续变量） |
| 误差变异 | 总误差变异 | 调整协变量后的误差变异 |
| 检验效能 | 一般 | 更高（减少了误差变异） |
| 均值比较 | 粗均值 | 调整均值 |
| 应用场景 | 简单的组间比较 | 需要控制混杂因素的组间比较 |

### 为什么需要ANCOVA？

**问题示例：**
研究三种教学方法对学生成绩的影响：
- 方法A组：学生入学成绩较高（平均85分）
- 方法B组：学生入学成绩中等（平均80分）
- 方法C组：学生入学成绩较低（平均75分）

**如果直接用ANOVA比较：**
- 方法A组的后测成绩可能最高
- 但这可能是因为他们入学成绩本来就高
- 无法准确判断教学方法的效果

**使用ANCOVA：**
- 以入学成绩作为协变量
- 控制入学成绩的影响
- 比较调整后的组间差异（如果各组入学成绩相同，各组的平均成绩会是多少）

## ANCOVA模型

### 单因素ANCOVA模型

$$y_{ij} = \mu + \alpha_i + \beta(x_{ij} - \bar{x}_{..}) + \varepsilon_{ij}$$

其中：
- $y_{ij}$ 是第i组第j个被试的因变量观测值
- $\mu$ 是总体均值
- $\alpha_i$ 是第i组的处理效应
- $\beta$ 是协变量的回归系数
- $x_{ij}$ 是第i组第j个被试的协变量值
- $\bar{x}_{..}$ 是协变量的总均值
- $\varepsilon_{ij}$ 是随机误差项

### 双因素ANCOVA模型

$$y_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \gamma(x_{ijk} - \bar{x}_{...}) + \varepsilon_{ijk}$$

其中增加了两个因素的主效应和交互效应。

## ANCOVA的平方和分解

$$SS_{total} = SS_{between} + SS_{within} = SS_{treatment} + SS_{covariate} + SS_{error}$$

### 分解步骤

1. **总平方和（Total SS）：**
   $$SS_{total} = \sum_{i=1}^{k}\sum_{j=1}^{n_i}(y_{ij} - \bar{y}_{..})^2$$

2. **组间平方和（Between SS）：**
   $$SS_{between} = \sum_{i=1}^{k}n_i(\bar{y}_{i.} - \bar{y}_{..})^2$$

3. **协变量平方和（Covariate SS）：**
   由协变量解释的变异部分

4. **调整后的误差平方和（Adjusted Error SS）：**
   从组内平方和中扣除协变量解释的部分

## 前提条件

### 1. 回归斜率齐性（Homogeneity of Regression Slopes）

**最重要的前提条件：** 协变量与因变量的关系在不同组中相同。

即：各组中协变量对因变量的回归系数相等。

**检验方法：**
- 检验组别 × 协变量的交互效应是否显著
- 如果交互效应显著，说明回归斜率不同，不能使用ANCOVA

**数学表达：**
$$H_0: \beta_1 = \beta_2 = ... = \beta_k$$

### 2. 正态性

**要求：**
- 残差服从正态分布
- 各组因变量在给定协变量条件下服从正态分布

**检验方法：**
- 残差的Shapiro-Wilk检验
- Q-Q图
- 残差直方图

### 3. 方差齐性

**要求：**
- 调整后的组内方差相等

**检验方法：**
- Levene检验
- Bartlett检验

### 4. 独立性

**要求：**
- 观测值之间相互独立
- 通过研究设计保证

### 5. 线性关系

**要求：**
- 协变量与因变量之间呈线性关系

**检验方法：**
- 散点图
- 残差图
- 拟合线性回归模型

### 6. 协变量与因变量相关

**要求：**
- 协变量与因变量应该有显著的相关关系
- 相关性越强，ANCOVA减少误差变异的效果越好

**检验方法：**
- 相关系数
- 协变量的显著性检验

## 调整均值（Adjusted Means）

### 定义

调整均值是指在控制协变量影响后，各组在因变量上的估计均值。它回答的问题是："如果各组在协变量上的取值相同（通常取总均值），各组的因变量均值是多少？"

### 计算公式

$$\bar{y}_{i(adj)} = \bar{y}_{i.} - \hat{\beta}(\bar{x}_{i.} - \bar{x}_{..})$$

其中：
- $\bar{y}_{i(adj)}$ 是第i组的调整均值
- $\bar{y}_{i.}$ 是第i组的原始均值
- $\hat{\beta}$ 是协变量的回归系数估计
- $\bar{x}_{i.}$ 是第i组协变量的均值
- $\bar{x}_{..}$ 是协变量的总均值

### 调整均值的解释

**示例：**
- A组原始均值 = 85，A组协变量均值 = 85
- B组原始均值 = 80，B组协变量均值 = 75
- 协变量总均值 = 80
- 协变量回归系数 = 0.6

A组调整均值 = 85 - 0.6 × (85 - 80) = 85 - 3 = 82
B组调整均值 = 80 - 0.6 × (75 - 80) = 80 + 3 = 83

**解释：** 如果两组的协变量都等于总均值80，A组的期望因变量值是82，B组是83。

### 调整均值的标准误

$$SE(\bar{y}_{i(adj)}) = \sqrt{MS_{error} \left[\frac{1}{n_i} + \frac{(\bar{x}_{i.} - \bar{x}_{..})^2}{SS_{covariate}}\right]}$$

## ANCOVA的计算步骤

### 步骤1：检验回归斜率齐性

拟合包含组别、协变量和两者交互效应的模型：

$$y_{ij} = \mu + \alpha_i + \beta(x_{ij} - \bar{x}_{..}) + (\alpha\beta)_i(x_{ij} - \bar{x}_{..}) + \varepsilon_{ij}$$

检验交互效应是否显著：
- 如果p < 0.05，拒绝斜率齐性假设，不能使用标准ANCOVA
- 如果p ≥ 0.05，满足斜率齐性假设

### 步骤2：拟合ANCOVA模型

如果斜率齐性假设满足，拟合不含交互效应的ANCOVA模型：

$$y_{ij} = \mu + \alpha_i + \beta(x_{ij} - \bar{x}_{..}) + \varepsilon_{ij}$$

### 步骤3：检验组别效应

检验组别效应是否显著（即调整后的组间差异是否显著）：
- H₀: α₁ = α₂ = ... = α_k = 0
- H₁: 至少有一个α_i ≠ 0

### 步骤4：计算调整均值

根据公式计算各组调整均值及其置信区间。

### 步骤5：事后检验（如果显著）

如果组别效应显著，进行事后检验比较调整均值：
- Bonferroni校正
- Tukey HSD（需要调整）
- 其他配对比较方法

## ANCOVA表

| 变异来源 | 平方和(SS) | 自由度(df) | 均方(MS) | F值 | p值 |
|----------|-----------|-----------|----------|-----|-----|
| 组别（调整后） | SS_group_adj | k-1 | MS_group_adj | MS_group_adj/MS_error | - |
| 协变量 | SS_covariate | 1 | MS_covariate | MS_covariate/MS_error | - |
| 误差（调整后） | SS_error_adj | N-k-1 | MS_error_adj | | |
| 总计 | SS_total | N-1 | | | |

其中：
- k 是组数
- N 是总样本量

## 效应量

### 偏Eta-squared（Partial η²）

$$\eta^2_p = \frac{SS_{group\_adj}}{SS_{group\_adj} + SS_{error\_adj}}$$

**解释：** 在控制协变量后，组别解释的变异比例。

### Cohen's f

$$f = \sqrt{\frac{\eta^2_p}{1 - \eta^2_p}}$$

**解释：**
- f = 0.1: 小效应
- f = 0.25: 中等效应
- f = 0.4: 大效应

## 应用实例

### 实例1：教学方法研究

**研究问题：** 三种教学方法对学生成绩的影响

**设计：**
- 因变量：期末成绩
- 自变量：教学方法（A、B、C三组）
- 协变量：入学成绩（前测分数）

**数据示例：**

| 组别 | 入学成绩 | 期末成绩 |
|------|---------|---------|
| A | 85 | 88 |
| A | 83 | 86 |
| B | 80 | 84 |
| B | 78 | 82 |
| C | 75 | 80 |
| C | 73 | 78 |

**分析步骤：**
1. 检验入学成绩与期末成绩的线性关系
2. 检验回归斜率齐性（各组入学成绩对期末成绩的影响是否相同）
3. 进行ANCOVA，控制入学成绩影响
4. 比较调整后的组间差异

### 实例2：药物临床试验

**研究问题：** 比较三种药物对血压的影响

**设计：**
- 因变量：治疗后的血压值
- 自变量：药物类型（药物A、药物B、安慰剂）
- 协变量：治疗前血压值

**分析目标：** 控制治疗前血压差异，准确评估药物效果。

## Python实现示例

```python
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ==================== 1. 数据准备 ====================
np.random.seed(42)
n_per_group = 20

# 创建示例数据：教学方法研究
data = pd.DataFrame({
    'group': ['A']*n_per_group + ['B']*n_per_group + ['C']*n_per_group,
    'pre_score': np.concatenate([
        np.random.normal(85, 3, n_per_group),  # A组入学成绩较高
        np.random.normal(80, 3, n_per_group),  # B组入学成绩中等
        np.random.normal(75, 3, n_per_group)   # C组入学成绩较低
    ]),
    'post_score': np.concatenate([
        np.random.normal(88, 2, n_per_group),  # A组期末成绩
        np.random.normal(84, 2, n_per_group),  # B组期末成绩
        np.random.normal(80, 2, n_per_group)   # C组期末成绩
    ])
})

# 让post_score与pre_score相关
data['post_score'] = 40 + 0.5 * data['pre_score'] + np.random.normal(0, 1, len(data))

print("数据预览：")
print(data.head(10))
print(f"\n各组描述统计：")
print(data.groupby('group').describe())

# ==================== 2. 数据探索 ====================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 散点图：入学成绩 vs 期末成绩
colors = {'A': 'red', 'B': 'green', 'C': 'blue'}
for group in data['group'].unique():
    subset = data[data['group'] == group]
    axes[0, 0].scatter(subset['pre_score'], subset['post_score'],
                      label=f'Group {group}', color=colors[group], alpha=0.6)
axes[0, 0].set_xlabel('入学成绩（协变量）')
axes[0, 0].set_ylabel('期末成绩（因变量）')
axes[0, 0].set_title('入学成绩与期末成绩的关系')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 各组箱线图（原始期末成绩）
sns.boxplot(x='group', y='post_score', data=data, ax=axes[0, 1])
axes[0, 1].set_title('各组期末成绩分布（原始）')
axes[0, 1].set_xlabel('组别')
axes[0, 1].set_ylabel('期末成绩')

# 各组箱线图（入学成绩）
sns.boxplot(x='group', y='pre_score', data=data, ax=axes[1, 0])
axes[1, 0].set_title('各组入学成绩分布（协变量）')
axes[1, 0].set_xlabel('组别')
axes[1, 0].set_ylabel('入学成绩')

# 组均值比较
group_means = data.groupby('group').mean()
x_pos = np.arange(len(group_means))
axes[1, 1].bar(x_pos - 0.2, group_means['pre_score'], 0.4,
               label='入学成绩', alpha=0.8)
axes[1, 1].bar(x_pos + 0.2, group_means['post_score'], 0.4,
               label='期末成绩', alpha=0.8)
axes[1, 1].set_xlabel('组别')
axes[1, 1].set_ylabel('分数')
axes[1, 1].set_title('各组均值比较')
axes[1, 1].set_xticks(x_pos)
axes[1, 1].set_xticklabels(group_means.index)
axes[1, 1].legend()

plt.tight_layout()
plt.show()

# ==================== 3. 检查协变量与因变量的关系 ====================
correlation = data[['pre_score', 'post_score']].corr()
print(f"\n协变量与因变量的相关系数：")
print(correlation)

# 整体回归
model_simple = ols('post_score ~ pre_score', data=data).fit()
print(f"\n简单回归结果（协变量对因变量）：")
print(model_simple.summary())

# ==================== 4. 检验回归斜率齐性 ====================
print(f"\n{'='*60}")
print("步骤1：检验回归斜率齐性")
print(f"{'='*60}")

# 拟合包含交互效应的模型
model_interaction = ols('post_score ~ C(group) * pre_score', data=data).fit()
anova_interaction = sm.stats.anova_lm(model_interaction, typ=2)
print("\n交互效应检验（斜率齐性）：")
print(anova_interaction)

interaction_p = anova_interaction.loc['C(group):pre_score', 'PR(>F)']
if interaction_p > 0.05:
    print(f"\n✓ 回归斜率齐性假设满足 (p = {interaction_p:.4f})")
    print("  可以继续进行标准ANCOVA分析")
else:
    print(f"\n✗ 回归斜率齐性假设不满足 (p = {interaction_p:.4f})")
    print("  不能使用标准ANCOVA，需要考虑其他方法")

# 绘制各组的回归线
plt.figure(figsize=(10, 6))
for group in data['group'].unique():
    subset = data[data['group'] == group]
    x = subset['pre_score']
    y = subset['post_score']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.scatter(x, y, label=f'Group {group}', color=colors[group], alpha=0.6)
    plt.plot(x, p(x), color=colors[group], linewidth=2, alpha=0.8)

plt.xlabel('入学成绩（协变量）')
plt.ylabel('期末成绩（因变量）')
plt.title('各组的回归线（检查斜率齐性）')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ==================== 5. 比较ANOVA和ANCOVA ====================
print(f"\n{'='*60}")
print("步骤2：比较ANOVA（未调整）和ANCOVA（调整后）")
print(f"{'='*60}")

# ANOVA（未控制协变量）
model_anova = ols('post_score ~ C(group)', data=data).fit()
anova_table = sm.stats.anova_lm(model_anova, typ=2)
print("\nANOVA（未控制入学成绩）：")
print(anova_table)

# ANCOVA（控制协变量）
model_ancova = ols('post_score ~ C(group) + pre_score', data=data).fit()
ancova_table = sm.stats.anova_lm(model_ancova, typ=2)
print("\nANCOVA（控制入学成绩）：")
print(ancova_table)

# 比较结果
anova_p = anova_table.loc['C(group)', 'PR(>F)']
ancova_p = ancova_table.loc['C(group)', 'PR(>F)']

print(f"\n{'='*60}")
print("比较总结：")
print(f"{'='*60}")
print(f"ANOVA F值: {anova_table.loc['C(group)', 'F']:.4f}, p值: {anova_p:.4f}")
print(f"ANCOVA F值: {ancova_table.loc['C(group)', 'F']:.4f}, p值: {ancova_p:.4f}")
print(f"\n调整前后的p值变化：{anova_p:.4f} → {ancova_p:.4f}")

# ==================== 6. 计算调整均值 ====================
print(f"\n{'='*60}")
print("步骤3：计算调整均值")
print(f"{'='*60}")

# 获取模型参数
beta = model_ancova.params['pre_score']
overall_pre_mean = data['pre_score'].mean()

# 计算各组调整均值
group_stats = data.groupby('group').agg({
    'pre_score': 'mean',
    'post_score': 'mean'
}).rename(columns={'pre_score': 'pre_mean', 'post_score': 'raw_mean'})

group_stats['adj_mean'] = group_stats['raw_mean'] - beta * (group_stats['pre_mean'] - overall_pre_mean)

print("\n原始均值与调整均值比较：")
print(group_stats)

# 计算调整均值的标准误
def calculate_adj_mean_se(model, data, group):
    """计算调整均值的标准误"""
    group_data = data[data['group'] == group]
    n = len(group_data)
    group_pre_mean = group_data['pre_score'].mean()
    overall_pre_mean = data['pre_score'].mean()

    # 残差均方
    mse = model.mse_resid

    # 协变量的平方和
    ss_covariate = ((data['pre_score'] - data['pre_score'].mean())**2).sum()

    se = np.sqrt(mse * (1/n + (group_pre_mean - overall_pre_mean)**2 / ss_covariate))
    return se

for group in group_stats.index:
    se = calculate_adj_mean_se(model_ancova, data, group)
    ci_95 = 1.96 * se
    group_stats.loc[group, 'adj_mean_se'] = se
    group_stats.loc[group, 'adj_mean_ci_lower'] = group_stats.loc[group, 'adj_mean'] - ci_95
    group_stats.loc[group, 'adj_mean_ci_upper'] = group_stats.loc[group, 'adj_mean'] + ci_95

print("\n调整均值及95%置信区间：")
print(group_stats[['adj_mean', 'adj_mean_se', 'adj_mean_ci_lower', 'adj_mean_ci_upper']])

# ==================== 7. 可视化调整均值 ====================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 原始均值
x_pos = np.arange(len(group_stats))
bars1 = axes[0].bar(x_pos, group_stats['raw_mean'],
                    yerr=[group_stats['raw_mean'] - data.groupby('group')['post_score'].mean() - 1.96 * data.groupby('group')['post_score'].sem(),
                          data.groupby('group')['post_score'].mean() + 1.96 * data.groupby('group')['post_score'].sem() - group_stats['raw_mean']],
                    capsize=5, alpha=0.8, color='lightcoral')
axes[0].set_xlabel('组别')
axes[0].set_ylabel('期末成绩')
axes[0].set_title('原始均值（未控制入学成绩）')
axes[0].set_xticks(x_pos)
axes[0].set_xticklabels(group_stats.index)
axes[0].grid(True, alpha=0.3, axis='y')

# 添加数值标签
for i, (idx, row) in enumerate(group_stats.iterrows()):
    axes[0].text(i, row['raw_mean'] + 0.5, f"{row['raw_mean']:.2f}",
                ha='center', va='bottom')

# 调整均值
bars2 = axes[1].bar(x_pos, group_stats['adj_mean'],
                    yerr=[group_stats['adj_mean'] - group_stats['adj_mean_ci_lower'],
                          group_stats['adj_mean_ci_upper'] - group_stats['adj_mean']],
                    capsize=5, alpha=0.8, color='lightblue')
axes[1].set_xlabel('组别')
axes[1].set_ylabel('调整后的期末成绩')
axes[1].set_title('调整均值（控制入学成绩后）')
axes[1].set_xticks(x_pos)
axes[1].set_xticklabels(group_stats.index)
axes[1].grid(True, alpha=0.3, axis='y')

# 添加数值标签
for i, (idx, row) in enumerate(group_stats.iterrows()):
    axes[1].text(i, row['adj_mean'] + 0.5, f"{row['adj_mean']:.2f}",
                ha='center', va='bottom')

plt.tight_layout()
plt.show()

# ==================== 8. 效应量 ====================
print(f"\n{'='*60}")
print("步骤4：效应量计算")
print(f"{'='*60}")

# 偏Eta-squared
ss_group_adj = ancova_table.loc['C(group)', 'sum_sq']
ss_error_adj = ancova_table.loc['Residual', 'sum_sq']
partial_eta_squared = ss_group_adj / (ss_group_adj + ss_error_adj)

print(f"偏Eta-squared (η²p) = {partial_eta_squared:.4f}")

# Cohen's f
cohens_f = np.sqrt(partial_eta_squared / (1 - partial_eta_squared))
print(f"Cohen's f = {cohens_f:.4f}")

# 解释效应量
if partial_eta_squared < 0.01:
    effect_interpretation = "小效应"
elif partial_eta_squared < 0.06:
    effect_interpretation = "中等效应"
else:
    effect_interpretation = "大效应"

print(f"\n效应量解释：{effect_interpretation}")

# 协变量的效应量
ss_covariate = ancova_table.loc['pre_score', 'sum_sq']
partial_eta_squared_cov = ss_covariate / (ss_covariate + ss_error_adj)
print(f"\n协变量的偏Eta-squared = {partial_eta_squared_cov:.4f}")
print(f"协变量解释了 {partial_eta_squared_cov*100:.2f}% 的变异")

# ==================== 9. 假设检验 ====================
print(f"\n{'='*60}")
print("步骤5：假设检验")
print(f"{'='*60}")

# 残差分析
residuals = model_ancova.resid

# 正态性检验
stat, p = stats.shapiro(residuals)
print(f"\n残差正态性检验 (Shapiro-Wilk):")
print(f"  统计量 = {stat:.4f}, p值 = {p:.4f}")
if p > 0.05:
    print("  ✓ 残差服从正态分布")
else:
    print("  ✗ 残差不服从正态分布，考虑数据转换")

# 方差齐性检验
group_residuals = [model_ancova.resid[data['group'] == g] for g in data['group'].unique()]
stat, p = stats.levene(*group_residuals)
print(f"\n调整后残差的方差齐性检验 (Levene):")
print(f"  统计量 = {stat:.4f}, p值 = {p:.4f}")
if p > 0.05:
    print("  ✓ 满足方差齐性假设")
else:
    print("  ✗ 不满足方差齐性假设，使用稳健方法")

# 残差可视化
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 残差直方图
axes[0, 0].hist(residuals, bins=15, edgecolor='black', alpha=0.7)
axes[0, 0].set_title('残差分布')
axes[0, 0].set_xlabel('残差')
axes[0, 0].set_ylabel('频数')
axes[0, 0].grid(True, alpha=0.3)

# Q-Q图
stats.probplot(residuals, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('残差Q-Q图')
axes[0, 1].grid(True, alpha=0.3)

# 残差vs拟合值
axes[1, 0].scatter(model_ancova.fittedvalues, residuals, alpha=0.6)
axes[1, 0].axhline(y=0, color='r', linestyle='--')
axes[1, 0].set_xlabel('拟合值')
axes[1, 0].set_ylabel('残差')
axes[1, 0].set_title('残差 vs 拟合值')
axes[1, 0].grid(True, alpha=0.3)

# 各组残差箱线图
data_with_residuals = data.copy()
data_with_residuals['residuals'] = residuals
sns.boxplot(x='group', y='residuals', data=data_with_residuals, ax=axes[1, 1])
axes[1, 1].axhline(y=0, color='r', linestyle='--')
axes[1, 1].set_xlabel('组别')
axes[1, 1].set_ylabel('残差')
axes[1, 1].set_title('各组残差分布')

plt.tight_layout()
plt.show()

# ==================== 10. 事后检验 ====================
print(f"\n{'='*60}")
print("步骤6：事后检验")
print(f"{'='*60}")

# 如果ANCOVA的组别效应显著，进行事后检验
if ancova_table.loc['C(group)', 'PR(>F)'] < 0.05:
    print("\n组别效应显著，进行配对比较：")

    # 注意：标准Tukey HSD不适用于ANCOVA，需要使用其他方法
    # 这里使用简单的Bonferroni校正作为示例

    # 计算各组配对比较
    groups = data['group'].unique()
    comparisons = []

    for i in range(len(groups)):
        for j in range(i+1, len(groups)):
            group1 = groups[i]
            group2 = groups[j]

            # 调整均值差值
            diff = group_stats.loc[group1, 'adj_mean'] - group_stats.loc[group2, 'adj_mean']

            # 标准误计算（简化版）
            n1 = len(data[data['group'] == group1])
            n2 = len(data[data['group'] == group2])
            se = np.sqrt(mse * (1/n1 + 1/n2))

            # t统计量
            t_stat = diff / se
            df = N - len(groups) - 1

            # p值（双尾）
            p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

            # Bonferroni校正
            num_comparisons = len(groups) * (len(groups) - 1) / 2
            p_adjusted = min(p_value * num_comparisons, 1.0)

            comparisons.append({
                'group1': group1,
                'group2': group2,
                'diff': diff,
                'se': se,
                't': t_stat,
                'p_raw': p_value,
                'p_adjusted': p_adjusted,
                'significant': p_adjusted < 0.05
            })

    comparison_df = pd.DataFrame(comparisons)
    print("\n配对比较结果（Bonferroni校正）：")
    print(comparison_df.to_string(index=False))

else:
    print("\n组别效应不显著，无需进行事后检验")

# ==================== 11. 完整模型摘要 ====================
print(f"\n{'='*60}")
print("ANCOVA模型完整摘要")
print(f"{'='*60}")
print(model_ancova.summary())

# ==================== 12. 预测可视化 ====================
plt.figure(figsize=(12, 8))

# 为每组绘制平行回归线
for group in data['group'].unique():
    subset = data[data['group'] == group]
    # 平行线，使用共同的斜率（模型中的beta）
    intercept_group = model_ancova.params[f'C(group)[T.{group}]']
    # 对于参照组，intercept是模型截距
    if group == model_ancova.params.index[model_ancova.params.index.str.contains('C(group)').tolist()[0]].split('.')[1].replace(']', ''):
        intercept = model_ancova.params['Intercept']
    else:
        intercept = model_ancova.params['Intercept'] + model_ancova.params[f'C(group)[T.{group}]']

    x_range = np.linspace(subset['pre_score'].min(), subset['pre_score'].max(), 100)
    y_pred = intercept + beta * x_range

    plt.scatter(subset['pre_score'], subset['post_score'],
                label=f'Group {group}', color=colors[group], alpha=0.6, s=50)
    plt.plot(x_range, y_pred, color=colors[group], linewidth=2,
             linestyle='-', label=f'Group {group} 回归线')

# 标记总均值线
plt.axvline(x=overall_pre_mean, color='black', linestyle='--',
            linewidth=2, label='协变量总均值')

plt.xlabel('入学成绩（协变量）')
plt.ylabel('期末成绩（因变量）')
plt.title('ANCOVA平行回归线（各组具有共同斜率）')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## ANCOVA的优势与局限

### 优势

1. **提高检验效能：** 通过控制协变量，减少误差变异，更容易检测到组间差异
2. **消除混杂偏倚：** 控制可能影响结果的混淆因素
3. **提高精度：** 调整均值比原始均值更准确地反映组间差异
4. **平衡设计：** 即使各组在协变量上不平衡，ANCOVA也可以调整

### 局限性

1. **假设严格：** 特别是回归斜率齐性假设难以满足
2. **协变量选择：** 不恰当的协变量可能引入新的偏倚
3. **因果解释：** 不能替代随机化设计
4. **过度调整：** 如果协变量是中介变量，过度调整会削弱真实效应

## ANCOVA的误用

### 1. 将中介变量作为协变量

**错误：** 将因变量的中介变量作为协变量
- 例如：研究教学方法→兴趣→成绩，将兴趣作为协变量
- 这样会削弱教学方法对成绩的真实效应

**正确做法：** 使用中介分析而非ANCOVA

### 2. 将受处理影响的变量作为协变量

**错误：** 将受自变量影响的变量作为协变量
- 例如：研究药物对血压的影响，将受药物影响的指标作为协变量
- 这样会调整掉处理效应

**正确做法：** 只使用处理前的变量作为协变量

### 3. 不满足斜率齐性假设时使用标准ANCOVA

**错误：** 在交互效应显著时仍使用标准ANCOVA
- 这会导致错误的结论

**正确做法：**
- 报告交互效应
- 考虑分层分析
- 使用多水平模型

## 替代方法

### 1. 多层线性模型（HLM）

当存在嵌套结构或随机效应时使用。

### 2. 倾向性得分匹配

当存在多个协变量时，倾向性得分匹配比ANCOVA更灵活。

### 3. 分层分析

当回归斜率不同时，可以分层分析。

### 4. 协变量调整的回归

当只有两组时，可以使用协变量调整的回归。

## 总结

ANCOVA是控制协变量影响的重要统计方法。

**核心要点：**
1. 控制协变量可以减少误差变异，提高检验效能
2. 调整均值是在协变量取值相同时的估计均值
3. 必须检验回归斜率齐性假设
4. 协变量应该是处理前的变量，与因变量相关但不受处理影响

**应用场景：**
1. 研究中有混淆因素需要控制
2. 各组在协变量上不平衡
3. 前后测研究（以前测为协变量）
4. 非随机化设计

**注意事项：**
1. 检验所有假设条件
2. 选择适当的协变量
3. 检验回归斜率齐性
4. 报告调整均值及其置信区间
5. 谨慎解释因果关系

**最佳实践：**
1. 可视化协变量与因变量的关系
2. 检验回归斜率齐性
3. 比较ANOVA和ANCOVA的结果
4. 报告调整均值和效应量
5. 如果显著，进行适当的事后检验

理解ANCOVA的原理、假设条件和适用场景，对于正确控制混杂因素、提高研究质量至关重要。ANCOVA是连接ANOVA和回归的桥梁，为研究者提供了更精确的分析工具。