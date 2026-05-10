# Meta分析（Meta-Analysis）

## 定义

Meta分析（Meta-Analysis）是一种统计方法，通过定量方法综合多个独立研究的结果，提供更可靠的证据。它将多个研究的结果合并为一个综合的效应量估计，提高统计功效和结论的可靠性。

## 基本概念

### 为什么要进行Meta分析

1. **提高统计功效：** 单个研究样本量可能不足，合并多个研究可提高检测真实效应的能力
2. **解决矛盾：** 不同研究结果可能不一致，Meta分析可探究原因并给出综合结论
3. **提高精确度：** 合并研究结果可减少估计的不确定性
4. **发现规律：** 可发现单个研究难以发现的趋势和模式
5. **指导实践：** 为政策制定和临床决策提供更可靠的证据

### 系统综述与Meta分析

- **系统综述（Systematic Review）：** 使用明确、系统的方法识别、筛选、评价和综合所有相关研究
- **Meta分析：** 在系统综述基础上，使用统计方法合并研究结果

## Meta分析的步骤

### 1. 提出研究问题

明确研究问题，通常使用PICO格式：
- **P（Population）：** 研究人群
- **I（Intervention）：** 干预措施
- **C（Comparison）：** 对照组
- **O（Outcome）：** 结局指标

### 2. 文献检索

- 制定检索策略
- 检索多个数据库（如PubMed、Web of Science、CNKI等）
- 检索灰色文献（未发表的研究、会议论文等）
- 追踪参考文献

### 3. 研究筛选

根据纳入和排除标准筛选研究：
- 题目和摘要筛选
- 全文筛选
- 记录筛选过程（如使用PRISMA流程图）

### 4. 数据提取

提取关键信息：
- 研究特征（作者、年份、样本量等）
- 研究设计
- 结局指标
- 效应量及其置信区间
- 基线特征

### 5. 质量评价

评价纳入研究的质量：
- 随机对照试验：使用Cochrane偏倚风险评估工具
- 观察性研究：使用NOS量表等
- 根据质量进行敏感性分析

### 6. 数据分析

- 选择效应量指标
- 选择效应模型
- 合并效应量
- 检验异质性
- 进行亚组分析或Meta回归
- 评估发表偏倚

### 7. 结果解释和报告

- 解释合并结果
- 讨论异质性来源
- 评价证据质量（如使用GRADE系统）
- 报告局限性和建议

## 效应量（Effect Size）

### 常用效应量指标

#### 1. 连续变量

**均值差（Mean Difference, MD）：**
- 适用于结局指标单位相同的研究
- $$MD = \bar{x}_1 - \bar{x}_2$$

**标准化均值差（Standardized Mean Difference, SMD）：**
- 适用于结局指标单位不同的研究
- $$SMD = \frac{\bar{x}_1 - \bar{x}_2}{S_{pooled}}$$
- 其中$S_{pooled}$为合并标准差

常用形式：
- Cohen's d
- Hedges' g（对小样本校正）

#### 2. 二分类变量

**风险比（Risk Ratio, RR）或相对风险（Relative Risk）：**
- $$RR = \frac{p_1}{p_2}$$
- 其中$p_1$和$p_2$分别为两组的事件发生率

**比值比（Odds Ratio, OR）：**
- $$OR = \frac{p_1/(1-p_1)}{p_2/(1-p_2)} = \frac{a/b}{c/d} = \frac{ad}{bc}$$
- 通常在Log尺度上进行合并：$\ln(OR)$

**风险差（Risk Difference, RD）：**
- $$RD = p_1 - p_2$$

#### 3. 生存数据

**风险比（Hazard Ratio, HR）：**
- 基于生存分析
- 在Log尺度上合并

### 效应量的权重

在Meta分析中，每个研究的权重取决于：
- **样本量：** 样本量越大，权重越大
- **效应量的方差：** 方差越小（精确度越高），权重越大
- **模型类型：** 固定效应和随机效应模型的权重计算不同

## 效应模型

### 固定效应模型（Fixed-Effect Model）

**基本假设：**
- 所有研究测量同一个真实的效应量
- 观察到的变异仅由随机误差引起
- 不存在异质性

**合并效应量：**
$$\hat{\theta}_{FE} = \frac{\sum_{i=1}^{k} w_i \hat{\theta}_i}{\sum_{i=1}^{k} w_i}$$

其中权重：
$$w_i = \frac{1}{\hat{\sigma}_i^2}$$

**适用情况：**
- 研究间异质性小（I² < 25%）
- 研究设计、人群、干预措施高度相似

### 随机效应模型（Random-Effects Model）

**基本假设：**
- 真实效应量在不同研究间存在变异
- 总变异 = 研究内变异 + 研究间变异

**合并效应量：**
$$\hat{\theta}_{RE} = \frac{\sum_{i=1}^{k} w_i^* \hat{\theta}_i}{\sum_{i=1}^{k} w_i^*}$$

其中权重：
$$w_i^* = \frac{1}{\hat{\sigma}_i^2 + \tau^2}$$

$\tau^2$是研究间方差分量。

**$\tau^2$的估计方法：**
- DerSimonian-Laird方法（最常用）
- REML（限制性最大似然）方法
- Paule-Mandel方法

**适用情况：**
- 研究间存在异质性（I² > 25%）
- 研究设计、人群或干预措施存在差异
- 需要将结果推广到更广泛的人群

### 模型选择

| 情况 | 推荐模型 |
|------|----------|
| I² < 25%，p > 0.10 | 固定效应模型 |
| I² ≥ 25%，p ≤ 0.10 | 随机效应模型 |
| 研究高度同质 | 固定效应模型 |
| 研究存在临床异质性 | 随机效应模型 |

## 异质性检验

异质性指研究间结果的变异超出随机误差所能解释的范围。

### 异质性检验方法

#### 1. Q检验（Cochran's Q）

$$Q = \sum_{i=1}^{k} w_i (\hat{\theta}_i - \hat{\theta})^2$$

其中：
- $\hat{\theta}_i$是第i个研究的效应量
- $\hat{\theta}$是合并效应量
- $w_i$是权重

Q服从自由度为k-1的卡方分布。

**局限：**
- 检验功效受研究数量影响
- 研究数量少时，即使异质性大也可能不显著
- 研究数量多时，即使异质性小也可能显著

#### 2. I²统计量

$$I^2 = \frac{Q - (k-1)}{Q} \times 100\%$$

**解释：**
- I² = 0%：无异质性
- I² = 25%：轻度异质性
- I² = 50%：中度异质性
- I² = 75%：重度异质性

**优势：**
- 不受研究数量影响
- 直观易懂
- 可用于比较不同Meta分析的异质性

#### 3. τ²统计量

研究间方差分量，表示真实效应量的方差。

**估计方法：**
- DerSimonian-Laird：$\tau^2 = \max\left(0, \frac{Q - (k-1)}{\sum w_i - \frac{\sum w_i^2}{\sum w_i}}\right)$
- REML：更精确但计算复杂

### 异质性的来源

#### 1. 临床异质性
- 研究人群不同（年龄、性别、疾病严重程度等）
- 干预措施不同（剂量、给药途径、疗程等）
- 结局指标不同（测量方法、随访时间等）

#### 2. 方法学异质性
- 研究设计不同（RCT vs 观察性研究）
- 偏倚风险不同
- 统计分析方法不同

#### 3. 统计学异质性
- 效应量的变异超出随机误差

### 处理异质性的方法

#### 1. 不合并
- 异质性过大时，不进行Meta分析
- 改为定性描述

#### 2. 亚组分析
- 按研究特征分组
- 分别合并各亚组
- 比较亚组间差异

#### 3. Meta回归
- 探讨异质性与协变量的关系
- 识别异质性的来源

#### 4. 敏感性分析
- 逐一排除研究
- 评估单个研究对结果的影响
- 按研究质量分组分析

#### 5. 使用随机效应模型
- 考虑研究间变异
- 提供更保守的置信区间

## 发表偏倚（Publication Bias）

发表偏倚指具有统计学显著性的结果比不显著的结果更容易发表的现象。

### 发表偏倚的来源

1. **研究者：** 倾向于提交阳性结果
2. **期刊：** 倾向于发表阳性结果
3. **赞助者：** 可能影响结果的发表
4. **语言：** 英语期刊更易被检索

### 检测发表偏倚的方法

#### 1. 漏斗图（Funnel Plot）

以效应量为横轴，标准误（或样本量）为纵轴的散点图。

**特征：**
- 对称：无发表偏倚
- 不对称：存在发表偏倚

**不对称的原因：**
- 发表偏倚
- 小样本研究质量低
- 真实的异质性
- 机会
- 造假

#### 2. Egger's检验

线性回归检验漏斗图的不对称性。

$$\frac{\hat{\theta}_i}{SE_i} = a + b \cdot \frac{1}{SE_i} + \varepsilon_i$$

检验截距a是否为0。

**局限：**
- 研究数量少时检验功效低（至少需要10个研究）
- 对异质性敏感

#### 3. Begg's检验

基于秩相关的方法检验漏斗图不对称性。

**局限：**
- 检验功效较低
- 现在较少使用

#### 4. 剪补法（Trim and Fill）

估计漏掉的研究并调整效应量。

**步骤：**
1. 剪掉漏斗图不对称一侧的研究
2. 估计真实的中心
3. 补上对称的研究
4. 重新估计效应量

### 减少发表偏倚的方法

1. **全面的文献检索：**
   - 检索多个数据库
   - 检索灰色文献
   - 追踪参考文献

2. **注册研究：**
   - 临床试验注册（如ClinicalTrials.gov）
   - 系统综述注册（如PROSPERO）

3. **联系研究者：**
   - 获取未发表的数据

4. **谨慎解释：**
   - 承认发表偏倚的可能影响
   - 评估结果的稳健性

## 亚组分析与Meta回归

### 亚组分析

将研究按特定特征分组，分别进行Meta分析。

**常用亚组：**
- 研究设计
- 人群特征
- 干预措施
- 随访时间
- 研究质量

**注意事项：**
- 亚组数量不宜过多
- 避免数据挖掘
- 事先规定亚组分析计划
- 检验亚组间差异的显著性

### Meta回归

探讨研究水平特征（协变量）与效应量的关系。

**模型：**
$$\hat{\theta}_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} + \varepsilon_i + u_i$$

其中：
- $\beta$是回归系数
- $\varepsilon_i$是研究内误差
- $u_i$是研究间误差（随机效应模型）

**注意事项：**
- 研究数量至少是协变量数的10倍
- 注意生态学谬误
- 考虑研究间的相关性

## 敏感性分析

评估结果对某些假设或决策的稳健性。

### 常用方法

1. **逐一排除法：** 每次排除一个研究，重新合并
2. **按研究质量分组：** 比较高质量和低质量研究的结果
3. **按样本量分组：** 比较大样本和小样本研究的结果
4. **使用不同模型：** 比较固定效应和随机效应模型的结果
5. **使用不同效应量：** 比较不同效应量的结果

### 解释

如果敏感性分析结果一致，说明结果稳健。如果结果变化很大，需要谨慎解释。

## Meta分析的质量评价

### AMSTAR 2量表

评价系统综述的方法学质量。

### PRISMA声明

报告系统综述和Meta分析的标准。

### GRADE系统

评价证据质量。

**证据质量等级：**
- **高质量：** 非常确信真实效应接近效应估计
- **中等质量：** 对效应估计有中等程度信心
- **低质量：** 对效应估计的信心有限
- **极低质量：** 对效应估计的信心很少

**降级因素：**
- 研究局限性
- 不一致性
- 间接性
- 不精确性
- 发表偏倚

## Python实现示例

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.meta_analysis import (
    combine_effects,
    effectsize_smd,
    effectsize_2x2,
    heterogeneity,
    publish_results
)

# 1. 基本Meta分析 - 连续变量（标准化均值差）
# =============================================================

# 示例数据：5个研究的两组均值和标准差
studies_continuous = pd.DataFrame({
    'study': ['Study 1', 'Study 2', 'Study 3', 'Study 4', 'Study 5'],
    'n1': [50, 60, 45, 55, 40],      # 干预组样本量
    'mean1': [8.5, 7.8, 9.2, 8.1, 8.9],  # 干预组均值
    'sd1': [2.1, 1.9, 2.3, 2.0, 2.2],    # 干预组标准差
    'n2': [48, 58, 43, 53, 38],      # 对照组样本量
    'mean2': [6.2, 5.9, 6.8, 6.1, 6.5],  # 对照组均值
    'sd2': [2.0, 1.8, 2.1, 1.9, 2.0]     # 对照组标准差
})

# 计算每个研究的效应量（Cohen's d）和方差
def calculate_cohen_d(n1, mean1, sd1, n2, mean2, sd2):
    """计算Cohen's d及其方差"""
    # 合并标准差
    pooled_sd = np.sqrt(((n1 - 1) * sd1**2 + (n2 - 1) * sd2**2) / (n1 + n2 - 2))
    
    # Cohen's d
    d = (mean1 - mean2) / pooled_sd
    
    # Hedges' g（小样本校正）
    correction_factor = 1 - 3 / (4 * (n1 + n2) - 9)
    g = d * correction_factor
    
    # 方差
    var_d = (n1 + n2) / (n1 * n2) + g**2 / (2 * (n1 + n2))
    
    return d, g, var_d

# 计算效应量
results = []
for idx, row in studies_continuous.iterrows():
    d, g, var_d = calculate_cohen_d(
        row['n1'], row['mean1'], row['sd1'],
        row['n2'], row['mean2'], row['sd2']
    )
    results.append({
        'study': row['study'],
        'n1': row['n1'],
        'n2': row['n2'],
        'd': d,
        'g': g,
        'se': np.sqrt(var_d),
        'ci_lower': g - 1.96 * np.sqrt(var_d),
        'ci_upper': g + 1.96 * np.sqrt(var_d)
    })

results_df = pd.DataFrame(results)
print("各研究效应量（Hedges' g）：")
print(results_df[['study', 'g', 'se', 'ci_lower', 'ci_upper']])

# 固定效应模型Meta分析
def fixed_effect_meta(effect_sizes, variances):
    """固定效应模型Meta分析"""
    weights = 1 / np.array(variances)
    pooled_effect = np.sum(weights * effect_sizes) / np.sum(weights)
    pooled_var = 1 / np.sum(weights)
    pooled_se = np.sqrt(pooled_var)
    
    # 95%置信区间
    ci_lower = pooled_effect - 1.96 * pooled_se
    ci_upper = pooled_effect + 1.96 * pooled_se
    
    # Z检验
    z_stat = pooled_effect / pooled_se
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    
    return {
        'effect': pooled_effect,
        'se': pooled_se,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'z': z_stat,
        'p': p_value,
        'weights': weights
    }

# 随机效应模型Meta分析（DerSimonian-Laird方法）
def random_effects_meta(effect_sizes, variances):
    """随机效应模型Meta分析"""
    k = len(effect_sizes)
    weights = 1 / np.array(variances)
    
    # 固定效应的合并效应
    pooled_effect_fe = np.sum(weights * effect_sizes) / np.sum(weights)
    
    # Q统计量
    Q = np.sum(weights * (effect_sizes - pooled_effect_fe)**2)
    df = k - 1
    
    # tau²估计（DerSimonian-Laird）
    C = np.sum(weights) - np.sum(weights**2) / np.sum(weights)
    tau_squared = max(0, (Q - df) / C)
    
    # 随机效应权重
    weights_re = 1 / (np.array(variances) + tau_squared)
    
    # 随机效应合并效应
    pooled_effect = np.sum(weights_re * effect_sizes) / np.sum(weights_re)
    pooled_var = 1 / np.sum(weights_re)
    pooled_se = np.sqrt(pooled_var)
    
    # 95%置信区间
    ci_lower = pooled_effect - 1.96 * pooled_se
    ci_upper = pooled_effect + 1.96 * pooled_se
    
    # Z检验
    z_stat = pooled_effect / pooled_se
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    
    # I²统计量
    I_squared = max(0, (Q - df) / Q) * 100 if Q > df else 0
    
    return {
        'effect': pooled_effect,
        'se': pooled_se,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'z': z_stat,
        'p': p_value,
        'weights': weights_re,
        'Q': Q,
        'df': df,
        'tau_squared': tau_squared,
        'I_squared': I_squared
    }

# 进行Meta分析
effect_sizes = results_df['g'].values
variances = results_df['se'].values ** 2

fe_results = fixed_effect_meta(effect_sizes, variances)
re_results = random_effects_meta(effect_sizes, variances)

print("\n固定效应模型结果：")
print(f"合并效应量 (Hedges' g): {fe_results['effect']:.3f}")
print(f"95% CI: [{fe_results['ci_lower']:.3f}, {fe_results['ci_upper']:.3f}]")
print(f"Z = {fe_results['z']:.3f}, p = {fe_results['p']:.4f}")

print("\n随机效应模型结果：")
print(f"合并效应量 (Hedges' g): {re_results['effect']:.3f}")
print(f"95% CI: [{re_results['ci_lower']:.3f}, {re_results['ci_upper']:.3f}]")
print(f"Z = {re_results['z']:.3f}, p = {re_results['p']:.4f}")
print(f"Q = {re_results['Q']:.3f}, df = {re_results['df']}, p = {1 - stats.chi2.cdf(re_results['Q'], re_results['df']):.4f}")
print(f"I² = {re_results['I_squared']:.1f}%")
print(f"τ² = {re_results['tau_squared']:.4f}")

# 2. 二分类数据Meta分析（OR）
# =============================================================

# 示例数据：5个研究的2x2表
studies_binary = pd.DataFrame({
    'study': ['Study 1', 'Study 2', 'Study 3', 'Study 4', 'Study 5'],
    'a': [45, 52, 38, 48, 35],  # 干预组事件数
    'b': [5, 8, 7, 7, 5],       # 干预组非事件数
    'c': [30, 35, 25, 32, 22],  # 对照组事件数
    'd': [18, 23, 18, 21, 16]   # 对照组非事件数
})

def calculate_or(a, b, c, d):
    """计算Odds Ratio及其方差"""
    # OR
    or_value = (a * d) / (b * c)
    
    # Log OR
    log_or = np.log(or_value)
    
    # Log OR的方差
    var_log_or = 1/a + 1/b + 1/c + 1/d
    
    # 95% CI
    se = np.sqrt(var_log_or)
    ci_lower = np.exp(log_or - 1.96 * se)
    ci_upper = np.exp(log_or + 1.96 * se)
    
    return {
        'or': or_value,
        'log_or': log_or,
        'se': se,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper
    }

# 计算每个研究的OR
or_results = []
for idx, row in studies_binary.iterrows():
    or_result = calculate_or(row['a'], row['b'], row['c'], row['d'])
    or_result['study'] = row['study']
    or_results.append(or_result)

or_df = pd.DataFrame(or_results)
print("\n各研究Odds Ratio：")
print(or_df[['study', 'or', 'ci_lower', 'ci_upper']])

# OR的Meta分析（在Log尺度上进行）
log_or_values = or_df['log_or'].values
log_or_variances = or_df['se'].values ** 2

fe_or = fixed_effect_meta(log_or_values, log_or_variances)
re_or = random_effects_meta(log_or_values, log_or_variances)

print("\n固定效应模型结果（OR）：")
print(f"合并OR: {np.exp(fe_or['effect']):.3f}")
print(f"95% CI: [{np.exp(fe_or['ci_lower']):.3f}, {np.exp(fe_or['ci_upper']):.3f}]")
print(f"Z = {fe_or['z']:.3f}, p = {fe_or['p']:.4f}")

print("\n随机效应模型结果（OR）：")
print(f"合并OR: {np.exp(re_or['effect']):.3f}")
print(f"95% CI: [{np.exp(re_or['ci_lower']):.3f}, {np.exp(re_or['ci_upper']):.3f}]")
print(f"Z = {re_or['z']:.3f}, p = {re_or['p']:.4f}")
print(f"Q = {re_or['Q']:.3f}, df = {re_or['df']}, p = {1 - stats.chi2.cdf(re_or['Q'], re_or['df']):.4f}")
print(f"I² = {re_or['I_squared']:.1f}%")

# 3. 森林图（Forest Plot）
# =============================================================

def forest_plot(studies, effects, ci_low, ci_high, pooled_effect,
                pooled_ci_low, pooled_ci_high, weights=None,
                title="Forest Plot", effect_label="Effect Size"):
    """绘制森林图"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    y_pos = np.arange(len(studies))
    
    # 绘制各研究
    for i, (study, effect, ci_l, ci_h) in enumerate(zip(studies, effects, ci_low, ci_high)):
        # 效应量点
        ax.scatter(effect, i, s=100, zorder=3)
        # 置信区间
        ax.plot([ci_l, ci_h], [i, i], 'k-', linewidth=1.5, zorder=2)
        # 研究名称和效应量
        weight_text = f" ({weights[i]*100:.1f}%)" if weights is not None else ""
        ax.text(ci_l - 0.1, i, f"{study}{weight_text}",
                va='center', ha='right', fontsize=9)
        ax.text(effect, i + 0.3, f"{effect:.2f} [{ci_l:.2f}, {ci_h:.2f}]",
                va='bottom', ha='center', fontsize=8)
    
    # 绘制合并效应量
    y_pooled = len(studies) + 1
    ax.scatter(pooled_effect, y_pooled, s=150, c='red', marker='diamond', zorder=3)
    ax.plot([pooled_ci_low, pooled_ci_high], [y_pooled, y_pooled],
            'r-', linewidth=2, zorder=2)
    ax.text(pooled_ci_low - 0.1, y_pooled, "Pooled",
            va='center', ha='right', fontsize=10, fontweight='bold')
    ax.text(pooled_effect, y_pooled + 0.3,
            f"{pooled_effect:.2f} [{pooled_ci_low:.2f}, {pooled_ci_high:.2f}]",
            va='bottom', ha='center', fontsize=9)
    
    # 垂直线（无效线）
    ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5, zorder=1)
    
    # 设置图表
    ax.set_xlabel(effect_label, fontsize=12)
    ax.set_ylabel('Study', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_yticks(list(y_pos) + [y_pooled])
    ax.set_yticklabels(list(studies) + ['Pooled'])
    ax.grid(True, axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# 绘制森林图（连续变量）
forest_plot(
    studies=results_df['study'].tolist(),
    effects=results_df['g'].tolist(),
    ci_low=results_df['ci_lower'].tolist(),
    ci_high=results_df['ci_upper'].tolist(),
    pooled_effect=re_results['effect'],
    pooled_ci_low=re_results['ci_lower'],
    pooled_ci_high=re_results['ci_upper'],
    weights=re_results['weights'] / np.sum(re_results['weights']),
    title="Forest Plot - Continuous Outcome (Random Effects)",
    effect_label="Hedges' g"
)

# 4. 漏斗图（Funnel Plot）
# =============================================================

def funnel_plot(effects, standard_errors, title="Funnel Plot"):
    """绘制漏斗图"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 散点图
    ax.scatter(effects, standard_errors, s=100, alpha=0.6)
    
    # 添加研究编号
    for i, (effect, se) in enumerate(zip(effects, standard_errors)):
        ax.text(effect, se, str(i+1), fontsize=8, ha='center', va='bottom')
    
    # 绘制95%置信区间漏斗
    x_range = np.linspace(min(effects) - 1, max(effects) + 1, 100)
    y_95 = 1.96 / np.abs(x_range)  # 近似
    ax.plot(x_range, y_95, 'r--', alpha=0.5, label='95% CI')
    ax.plot(x_range, -y_95, 'r--', alpha=0.5)
    
    # 垂直线（合并效应量）
    pooled_effect = np.average(effects, weights=1/standard_errors**2)
    ax.axvline(x=pooled_effect, color='gray', linestyle='-', alpha=0.5)
    
    # 设置图表
    ax.set_xlabel('Effect Size', fontsize=12)
    ax.set_ylabel('Standard Error', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# 绘制漏斗图
funnel_plot(
    effects=results_df['g'].tolist(),
    standard_errors=results_df['se'].tolist(),
    title="Funnel Plot - Assessment of Publication Bias"
)

# 5. Egger's检验
# =============================================================

def eggers_test(effects, standard_errors):
    """Egger's检验发表偏倚"""
    # 标准化效应量
    standardized_effects = effects / standard_errors
    precision = 1 / standard_errors
    
    # 线性回归
    X = sm.add_constant(precision)
    model = sm.OLS(standardized_effects, X).fit()
    
    # 检验截距是否为0
    intercept = model.params[0]
    intercept_se = model.bse[0]
    t_stat = intercept / intercept_se
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=len(effects)-2))
    
    return {
        'intercept': intercept,
        'se': intercept_se,
        't': t_stat,
        'p': p_value,
        'model': model
    }

egger_result = eggers_test(results_df['g'].values, results_df['se'].values)
print("\nEgger's检验结果：")
print(f"截距 = {egger_result['intercept']:.4f} (SE = {egger_result['se']:.4f})")
print(f"t = {egger_result['t']:.4f}, p = {egger_result['p']:.4f}")
if egger_result['p'] < 0.05:
    print("结论：存在发表偏倚（p < 0.05）")
else:
    print("结论：未检测到显著发表偏倚（p >= 0.05）")

# 6. 敏感性分析
# =============================================================

def sensitivity_analysis(effect_sizes, variances):
    """敏感性分析：逐一排除研究"""
    n = len(effect_sizes)
    results = []
    
    for i in range(n):
        # 排除第i个研究
        idx_exclude = np.arange(n) != i
        effects_excluded = effect_sizes[idx_exclude]
        variances_excluded = variances[idx_exclude]
        
        # 重新计算
        re_result = random_effects_meta(effects_excluded, variances_excluded)
        
        results.append({
            'excluded_study': i + 1,
            'effect': re_result['effect'],
            'ci_lower': re_result['ci_lower'],
            'ci_upper': re_result['ci_upper'],
            'p': re_result['p']
        })
    
    return pd.DataFrame(results)

sensitivity_df = sensitivity_analysis(effect_sizes, variances)
print("\n敏感性分析结果：")
print(sensitivity_df)

# 7. 亚组分析
# =============================================================

# 假设按研究设计分组
subgroup_info = pd.DataFrame({
    'study': results_df['study'],
    'design': ['RCT', 'RCT', 'Observational', 'RCT', 'Observational']
})

subgroup_results = {}
for design in subgroup_info['design'].unique():
    mask = subgroup_info['design'] == design
    effects_sub = effect_sizes[mask]
    vars_sub = variances[mask]
    
    re_sub = random_effects_meta(effects_sub, vars_sub)
    subgroup_results[design] = re_sub
    
    print(f"\n{design}亚组结果：")
    print(f"效应量: {re_sub['effect']:.3f} [{re_sub['ci_lower']:.3f}, {re_sub['ci_upper']:.3f}]")
    print(f"I² = {re_sub['I_squared']:.1f}%")

# 8. Meta回归
# =============================================================

def meta_regression(effect_sizes, variances, covariates):
    """Meta回归"""
    # 随机效应权重
    re_result = random_effects_meta(effect_sizes, variances)
    tau2 = re_result['tau_squared']
    
    # 权重
    weights = 1 / (variances + tau2)
    
    # 加权回归
    X = sm.add_constant(covariates)
    model = sm.WLS(effect_sizes, X, weights=weights).fit()
    
    return model

# 示例：效应量与样本量的关系
sample_sizes = studies_continuous['n1'].values + studies_continuous['n2'].values
model = meta_regression(effect_sizes, variances, sample_sizes)

print("\nMeta回归结果：")
print(model.summary())
```

## Meta分析报告

### 报告内容

1. **研究问题：** 清晰的研究问题和纳入标准
2. **文献检索：** 检索策略和数据库
3. **研究选择：** 纳入和排除过程
4. **研究特征：** 纳入研究的基本特征
5. **质量评价：** 纳入研究的质量评估
6. **结果：**
   - 合并效应量及其置信区间
   - 异质性检验结果
   - 亚组分析和Meta回归结果
   - 敏感性分析结果
   - 发表偏倚评估
7. **讨论：**
   - 结果的解释
   - 局限性
   - 对实践的意义

### 报告格式示例

```
# Meta分析标题

## 摘要

## 引言
- 研究背景
- 研究问题

## 方法
- 纳入和排除标准
- 文献检索策略
- 数据提取
- 质量评价
- 统计分析方法

## 结果
- 研究选择流程（PRISMA流程图）
- 纳入研究特征
- 质量评价结果
- Meta分析结果（包括森林图）
- 异质性分析
- 发表偏倚评估

## 讨论
- 主要发现
- 与其他研究的比较
- 局限性
- 对实践和未来研究的意义

## 结论
```

## Meta分析的局限性与注意事项

### 局限性

1. **垃圾进，垃圾出（GIGO）：**
   - 纳入低质量研究会影响结果
   - 需要严格的质量评价

2. **异质性：**
   - 过大异质性使合并结果无意义
   - 需要探讨异质性来源

3. **发表偏倚：**
   - 可能夸大效应量
   - 需要全面检索和评估

4. ** apples and oranges：**
   - 合并不同质的研究可能不恰当
   - 需要谨慎判断

5. **重复发表：**
   - 同一数据被多次分析
   - 需要识别和排除

### 注意事项

1. **事先注册研究方案**
2. **遵循PRISMA报告规范**
3. **全面检索文献**
4. **严格评价研究质量**
5. **适当处理异质性**
6. **评估发表偏倚**
7. **进行敏感性分析**
8. **谨慎解释结果**

## 总结

Meta分析是循证医学和循证决策的重要工具。

**核心要点：**
1. 综合多个研究结果，提高统计功效
2. 选择合适的效应量和效应模型
3. 检验和处理异质性
4. 评估发表偏倚
5. 进行敏感性分析验证结果稳健性

**应用场景：**
1. 临床干预效果评价
2. 流行病学病因研究
3. 诊断试验准确性
4. 预后因素研究

**最佳实践：**
1. 事先注册研究方案
2. 全面检索文献
3. 严格评价研究质量
4. 选择合适的统计方法
5. 遵循报告规范

**质量保证：**
1. 使用AMSTAR 2评价方法学质量
2. 遵循PRISMA报告规范
3. 使用GRADE系统评价证据质量

理解Meta分析的原理、方法和局限性，对于正确进行和解释Meta分析至关重要。Meta分析不是简单的统计汇总，而是一个系统的、严谨的研究过程，需要仔细的规划、执行和解释。
