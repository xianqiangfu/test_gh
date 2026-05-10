# p-value（p值）

## 定义

p-value（probability value，概率值）是在假设检验中，假定原假设H₀为真的条件下，获得至少与观测结果同样极端的结果的概率。它是衡量证据反对原假设程度的量化指标。

## p值的数学定义

对于检验统计量T，p值定义为：

$$p = P(|T| \geq |t_{obs}| | H_0 \text{为真})$$

其中：
- $t_{obs}$ 是观测到的检验统计量值
- 条件概率表示在H₀为真时，观测到至少如此极端的统计量的概率

## p值的计算

### 双侧检验

$$p = 2 \times P(T \geq |t_{obs}| | H_0)$$

### 单侧检验

- 右侧检验（H₁: θ > θ₀）：
  $$p = P(T \geq t_{obs} | H_0)$$

- 左侧检验（H₁: θ < θ₀）：
  $$p = P(T \leq t_{obs} | H_0)$$

## p值的解释

### 正确理解

1. **条件概率：** p值是在H₀为真的前提下计算的，不是H₀为真的概率
2. **证据强度：** p值越小，反对H₀的证据越强
3. **重复抽样：** p值描述的是在重复抽样中，获得当前或更极端结果的概率

### 常见错误理解

| 错误理解 | 纠正 |
|----------|------|
| p值是H₀为真的概率 | p值是P(数据\|H₀)，不是P(H₀\|数据) |
| 小p值意味着效应很重要 | p值衡量统计显著性，不等于实际重要性 |
| p=0.05有意义的分界线 | 没有神奇的p值分界线，不应绝对化 |
| 显著结果意味着研究假设正确 | 拒绝H₀不等于证明H₁正确 |
| 非显著结果意味着H₀为真 | 不拒绝H₀不等于证明H₀为真 |

## 显著性水平（α）

显著性水平是事先设定的拒绝H₀的概率阈值，通常取α = 0.05。

### 决策规则

- 如果 p < α，拒绝H₀（结果显著）
- 如果 p ≥ α，不拒绝H₀（结果不显著）

### α值的选择

| α值 | 应用场景 |
|-----|----------|
| 0.10 | 初步探索性研究 |
| 0.05 | **最常用**，社会科学、医学研究标准 |
| 0.01 | 严格标准，高风险领域 |
| 0.001 | 极严格标准，如物理学发现 |

### α与p值的关系

- α是决策阈值，p值是计算结果
- α在检验前设定，p值在检验后计算
- α控制第一类错误率

## p值与第一类、第二类错误

### 第一类错误（Type I Error）

- **定义：** H₀为真时拒绝H₀
- **概率：** α（显著性水平）
- **解释：** "假阳性"，"虚惊"

### 第二类错误（Type II Error）

- **定义：** H₀为假时不拒绝H₀
- **概率：** β
- **解释：** "假阴性"，"漏报"

### 统计功效（Power）

- **定义：** H₀为假时拒绝H₀的能力
- **公式：** Power = 1 - β
- **意义：** 检测真实效应的能力

### 关系

$$\alpha + Power \neq 1$$

α和β之间是权衡关系，降低α会增加β，降低β需要增大样本量。

## p值的分布

### H₀为真时p值的分布

当H₀为真时，p值在[0, 1]区间上均匀分布：

$$P(p \leq x) = x, \quad \forall x \in [0, 1]$$

这意味着：
- P(p < 0.05) = 0.05
- P(p < 0.01) = 0.01
- 小p值在H₀为真时很少出现

### H₀为假时p值的分布

当H₀为假时，p值向小值偏移，偏移程度取决于：
- 效应大小
- 样本量
- 检验功效

## p值与置信区间

p值与置信区间有密切关系：

### 双侧检验与置信区间

- 95%置信区间包含H₀中的假设值 ↔ p > 0.05
- 95%置信区间不包含H₀中的假设值 ↔ p < 0.05

### 优势

置信区间提供更多信息：
- 不仅知道是否显著
- 还知道效应量的可能范围
- 可以评估实际重要性

## p值的局限性

### 1. 样本量依赖

**问题：** 大样本时，微小效应也会产生极小的p值。

```python
# 大样本示例
n = 10000
effect_size = 0.01  # 很小的效应
p值 ≈ 0.0001  # 非常显著，但实际意义有限
```

### 2. 不包含效应大小

p值只告诉你结果是否显著，不告诉你效应有多大。

**解决方案：** 报告效应量（如Cohen's d、R²）

### 3. 不包含实际意义

统计显著性不等于实际重要性。

**示例：**
- 某药物降低血压0.5 mmHg，p < 0.001（统计显著）
- 但临床效果微不足道（实际无意义）

### 4. 多重比较问题

进行多次检验时，第一类错误率增加。

**问题：** 如果做20次检验，α = 0.05，至少出现一次假阳性的概率约为1 - 0.95²⁰ ≈ 0.64

**校正方法：**
- Bonferroni校正：α' = α/k（k是检验次数）
- False Discovery Rate (FDR)
- Holm-Bonferroni方法

### 5. P-hacking问题

研究者通过多种方式"寻找"显著结果。

**常见P-hacking方法：**
- 分析多次，只报告显著的结果
- 根据数据选择检验方法
- 去除"异常值"使结果显著
- 分层分析直到找到显著的子组

**解决方案：**
- 预注册研究方案
- 数据和代码公开
- 报告所有分析结果

## p值报告规范

### ASA关于p值的声明（2016）

美国统计协会（ASA）发布的重要指导原则：

1. **p值可以表明数据与特定统计模型的相容程度**
2. **p值不能衡量假设为真的概率**
3. **科学结论不应仅基于p值是否超过阈值**
4. **合理的推断需要完整的报告和透明度**
5. **p值或统计显著性并不衡量效应大小或重要性**
6. **p值本身不提供好的证据**

### 最佳实践

1. **不要只报告p < 0.05**
   - 报告精确p值（如p = 0.032）

2. **不要将p值作为唯一证据**
   - 报告效应量和置信区间

3. **不要过分强调p值**
   - 考虑实际意义、研究设计、效应大小

4. **避免二值思维**
   - 不应把结果简单分为"显著"和"不显著"

## Python实现示例

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 1. 计算p值示例
# 单样本t检验
sample = np.array([25, 27, 24, 26, 25, 26, 28, 24, 25, 27])
mu0 = 25
t_stat, p_value = stats.ttest_1samp(sample, mu0)
print(f"t = {t_stat:.4f}, p = {p_value:.4f}")

# 2. p值分布示例（H₀为真）
def simulate_p_values(n_sim=10000, n=20, mu=0, sigma=1):
    p_values = []
    for _ in range(n_sim):
        sample = np.random.normal(mu, sigma, n)
        _, p_value = stats.ttest_1samp(sample, 0)
        p_values.append(p_value)
    return np.array(p_values)

p_values = simulate_p_values()
print(f"H₀为真时，p < 0.05的比例: {np.mean(p_values < 0.05):.3f}")

# 3. 效应大小与p值的关系
def power_analysis(effect_size, n, alpha=0.05):
    """计算统计功效"""
    from statsmodels.stats.power import ttest_power
    return ttest_power(effect_size, n, alpha, alternative='two-sided')

# 不同效应大小的功效
effect_sizes = [0.2, 0.5, 0.8]  # 小、中、大效应
sample_sizes = np.arange(10, 200, 10)

for es in effect_sizes:
    powers = [power_analysis(es, n) for n in sample_sizes]
    print(f"效应大小 {es}: n=50时功效={power_analysis(es, 50):.3f}")

# 4. 多重比较校正
from statsmodels.stats.multitest import multipletests

# 假设有10个p值
p_values = [0.01, 0.03, 0.12, 0.04, 0.002, 0.08, 0.05, 0.15, 0.07, 0.003]

# Bonferroni校正
reject, p_corrected, _, _ = multipletests(p_values, method='bonferroni')
print("Bonferroni校正:")
for i, (p_orig, p_corr, rej) in enumerate(zip(p_values, p_corrected, reject)):
    print(f"检验{i}: 原p={p_orig:.4f}, 校正后p={p_corr:.4f}, 拒绝H₀: {rej}")

# FDR校正
reject, p_corrected, _, _ = multipletests(p_values, method='fdr_bh')
print("\nFDR校正:")
for i, (p_orig, p_corr, rej) in enumerate(zip(p_values, p_corrected, reject)):
    print(f"检验{i}: 原p={p_orig:.4f}, 校正后p={p_corr:.4f}, 拒绝H₀: {rej}")

# 5. 效应量计算
from statsmodels.stats import power as pw

# Cohen's d（双样本）
group1 = np.array([85, 82, 88, 79, 86, 84, 87, 83, 85, 81])
group2 = np.array([82, 80, 85, 78, 81, 83, 80, 82, 79, 84])

n1, n2 = len(group1), len(group2)
var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)

# 合并标准差
pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1 + n2 - 2))
cohen_d = (np.mean(group1) - np.mean(group2)) / pooled_std

print(f"\nCohen's d = {cohen_d:.3f}")
print("效应大小解释:")
if abs(cohen_d) < 0.2:
    print("小效应")
elif abs(cohen_d) < 0.8:
    print("中等效应")
else:
    print("大效应")
```

## Bayes因子与p值

作为p值的替代，Bayes因子提供另一种证据度量：

$$BF_{10} = \frac{P(数据|H_1)}{P(数据|H_0)}$$

### Bayes因子解释

| BF值 | 证据强度 |
|------|----------|
| > 100 | 极强支持H₁ |
| 30-100 | 非常强支持H₁ |
| 10-30 | 强支持H₁ |
| 3-10 | 中等支持H₁ |
| 1/3-3 | 证据不明确 |
| 1/10-1/3 | 中等支持H₀ |
| 1/30-1/10 | 强支持H₀ |
| < 1/100 | 极强支持H₀ |

### 优势

- 直接比较两个假设
- 支持备择假设的证据
- 更符合直觉

### 缺点

- 需要先验分布
- 计算复杂

## 总结

p值是统计学中最重要但也最容易被误解的概念之一。

**关键要点：**

1. **p值的正确理解：**
   - p = P(至少如此极端的结果 | H₀为真)
   - 不是P(H₀为真)

2. **显著性水平α：**
   - α是决策阈值，不是分界线
   - α控制第一类错误率

3. **p值的局限性：**
   - 依赖样本量
   - 不反映效应大小
   - 容易被滥用（P-hacking）

4. **最佳实践：**
   - 报告精确p值
   - 报告效应量和置信区间
   - 考虑实际意义
   - 避免过度依赖p值

5. **替代方法：**
   - 置信区间提供更多信息
   - Bayes因子提供不同视角
   - 效应量衡量实际重要性

理解p值的正确含义和局限性，对于进行科学、严谨的统计分析至关重要。