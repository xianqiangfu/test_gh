# MCMC方法简介

## 定义

马尔可夫链蒙特卡洛（Markov Chain Monte Carlo，MCMC）是一类用于从复杂的概率分布中抽样的算法。MCMC是贝叶斯计算的核心技术，特别适用于高维参数空间和复杂后验分布的情况。

## MCMC的基本思想

### 核心概念

MCMC方法的核心思想是构造一个马尔可夫链，使其平稳分布就是我们要抽样的目标分布（如贝叶斯分析中的后验分布）。通过运行这个马尔可夫链足够长的时间，我们就可以获得来自目标分布的样本。

### 为什么需要MCMC？

1. **贝叶斯推断的挑战：**
   - 后验分布通常很复杂，没有解析解
   - 高维空间的积分计算极其困难
   - 直接采样不可行

2. **MCMC的优势：**
   - 可以处理高维参数空间
   - 适用于各种复杂分布
   - 只需要知道分布的核函数（不需要归一化常数）

## 马尔可夫链基础

### 定义

马尔可夫链是一个随机过程，具有"无记忆性"：下一状态只依赖于当前状态，与历史状态无关。

数学表示：
$$P(X_{t+1} | X_t, X_{t-1}, ..., X_0) = P(X_{t+1} | X_t)$$

### 转移概率矩阵

对于离散状态空间，转移概率矩阵P定义了从一个状态转移到另一个状态的概率：
$$P_{ij} = P(X_{t+1} = j | X_t = i)$$

性质：
1. 每行元素之和为1：$$\sum_j P_{ij} = 1$$
2. 所有元素非负：$$P_{ij} \geq 0$$

### 平稳分布

如果存在分布π，满足：
$$\pi_j = \sum_i \pi_i P_{ij}$$

或向量形式：$$\pi = \pi P$$

则π是马尔可夫链的平稳分布。

### 不可约性和遍历性

**不可约性：** 任何状态都可以从其他状态以正概率到达

**周期性：** 状态是否只能在特定时间步返回

**遍历性：** 不可约且非周期的马尔可夫链称为遍历链

遍历马尔可夫链保证从任何初始状态出发，最终会收敛到平稳分布。

## Metropolis-Hastings算法

### 算法原理

Metropolis-Hastings（MH）算法是最基本的MCMC算法，通过构造一个满足细致平衡条件的转移核来生成样本。

### 细致平衡条件

如果转移核P满足：
$$\pi(x)P(x \rightarrow y) = \pi(y)P(y \rightarrow x)$$

则π是平稳分布。

### 算法步骤

1. **初始化：** 选择初始状态x^(0)

2. **迭代：** 对于t = 0, 1, 2, ..., N-1：
   
   a. **提议：** 从提议分布q(x^(t)·)中生成候选状态y
   
   b. **接受概率：** 计算接受概率
      $$\alpha(x^{(t)}, y) = \min\left(1, \frac{\pi(y)q(y, x^{(t)})}{\pi(x^{(t)})q(x^{(t)}, y)}\right)$$
   
   c. **接受/拒绝：** 生成u ~ Uniform(0,1)
      - 如果u ≤ α，接受：x^(t+1) = y
      - 否则，拒绝：x^(t+1) = x^(t)

### 特殊情况

**对称提议：** 如果q(y, x) = q(x, y)，则：
$$\alpha(x, y) = \min\left(1, \frac{\pi(y)}{\pi(x)}\right)$$

这是经典的Metropolis算法。

### 提议分布选择

常见的提议分布：
1. **正态分布：** q(y|x) = N(y; x, σ²I)
2. **均匀分布：** q(y|x) = Uniform(x-δ, x+δ)
3. **自适应提议：** 根据链的运行情况调整参数

提议分布的选择影响收敛速度：
- 方差太小：接受率高，但探索空间慢
- 方差太大：接受率低，经常拒绝

最佳接受率通常在20%-50%之间。

### Python实现示例

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def metropolis_hastings(target_dist, proposal_dist, initial_state, n_iter):
    """
    Metropolis-Hastings算法实现
    
    参数:
    target_dist: 目标分布的密度函数（可以是不归一化的）
    proposal_dist: 提议分布函数，返回候选状态
    initial_state: 初始状态
    n_iter: 迭代次数
    
    返回:
    samples: 采样序列
    acceptance_rate: 接受率
    """
    current_state = initial_state
    samples = [current_state]
    accept_count = 0
    
    for _ in range(n_iter):
        # 提议新状态
        proposed_state = proposal_dist(current_state)
        
        # 计算接受概率
        acceptance_prob = min(1, 
            target_dist(proposed_state) / target_dist(current_state))
        
        # 接受或拒绝
        if np.random.rand() < acceptance_prob:
            current_state = proposed_state
            accept_count += 1
        
        samples.append(current_state)
    
    acceptance_rate = accept_count / n_iter
    return np.array(samples), acceptance_rate

# 示例：从标准正态分布中采样
def target_normal(x):
    """标准正态分布（不归一化）"""
    return np.exp(-0.5 * x**2)

def proposal_normal(x):
    """正态提议分布，标准差为1"""
    return x + np.random.normal(0, 1)

# 运行MCMC
samples, ar = metropolis_hastings(target_normal, proposal_normal, 0, 10000)

# 去除burn-in期
burnin = 1000
samples_post_burnin = samples[burnin:]

# 绘制结果
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 迹线图
axes[0].plot(samples[:1000])
axes[0].set_title('Trace Plot')
axes[0].set_xlabel('Iteration')
axes[0].set_ylabel('Value')

# 直方图与真实分布对比
axes[1].hist(samples_post_burnin, bins=50, density=True, alpha=0.7, label='MCMC Samples')
x_true = np.linspace(-4, 4, 100)
axes[1].plot(x_true, stats.norm.pdf(x_true, 0, 1), 'r-', label='True Distribution')
axes[1].set_title('Histogram vs True Distribution')
axes[1].legend()

# 自相关函数
from statsmodels.tsa.stattools import acf
acf_values = acf(samples_post_burnin, nlags=50)
axes[2].plot(acf_values)
axes[2].set_title('Autocorrelation Function')
axes[2].set_xlabel('Lag')
axes[2].set_ylabel('ACF')

plt.tight_layout()
plt.show()

print(f"接受率: {ar:.3f}")
print(f"样本均值: {np.mean(samples_post_burnin):.3f}")
print(f"样本标准差: {np.std(samples_post_burnin):.3f}")
```

## Gibbs采样

### 算法原理

Gibbs采样是MH算法的特殊情况，适用于多元分布。它通过依次从每个变量的条件分布中抽样来生成样本。

### 适用条件

当目标分布π(x₁, x₂, ..., xₙ)的条件分布π(xᵢ|x₋ᵢ)可以轻松抽样时，Gibbs采样特别有效。

### 算法步骤

1. **初始化：** 选择初始状态x^(0) = (x₁^(0), x₂^(0), ..., xₙ^(0))

2. **迭代：** 对于t = 0, 1, 2, ..., N-1：
   
   x₁^(t+1) ~ π(x₁ | x₂^(t), x₃^(t), ..., xₙ^(t))
   
   x₂^(t+1) ~ π(x₂ | x₁^(t+1), x₃^(t), ..., xₙ^(t))
   
   ...
   
   xₙ^(t+1) ~ π(xₙ | x₁^(t+1), x₂^(t+1), ..., xₙ₋₁^(t+1))

### 优势与限制

**优势：**
- 不需要提议分布和接受概率
- 每次迭代都接受
- 对于高相关变量更高效

**限制：**
- 需要知道所有条件分布
- 变量强相关时收敛可能很慢
- 难以并行化

### Python实现示例

```python
import numpy as np
from scipy import stats

def gibbs_sampling_joint_normal(n_iter, rho, initial_state=(0, 0)):
    """
    从二元正态分布中进行Gibbs采样
    
    参数:
    n_iter: 迭代次数
    rho: 相关系数
    initial_state: 初始状态
    
    返回:
    samples: 采样序列
    """
    x1, x2 = initial_state
    samples = np.zeros((n_iter, 2))
    
    for i in range(n_iter):
        # 从x1的条件分布中采样
        x1 = np.random.normal(rho * x2, np.sqrt(1 - rho**2))
        
        # 从x2的条件分布中采样
        x2 = np.random.normal(rho * x1, np.sqrt(1 - rho**2))
        
        samples[i] = [x1, x2]
    
    return samples

# 生成样本
samples = gibbs_sampling_joint_normal(10000, rho=0.8)

# 去除burn-in期
burnin = 1000
samples_post_burnin = samples[burnin:]

# 绘制结果
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 迹线图
axes[0, 0].plot(samples_post_burnin[:500, 0])
axes[0, 0].set_title('Trace Plot - X1')
axes[0, 0].set_xlabel('Iteration')

axes[0, 1].plot(samples_post_burnin[:500, 1])
axes[0, 1].set_title('Trace Plot - X2')
axes[0, 1].set_xlabel('Iteration')

# 散点图
axes[1, 0].scatter(samples_post_burnin[:, 0], samples_post_burnin[:, 1], alpha=0.5)
axes[1, 0].set_title('Joint Distribution')
axes[1, 0].set_xlabel('X1')
axes[1, 0].set_ylabel('X2')

# 边际分布
axes[1, 1].hist(samples_post_burnin[:, 0], bins=50, density=True, alpha=0.5, label='X1')
axes[1, 1].hist(samples_post_burnin[:, 1], bins=50, density=True, alpha=0.5, label='X2')
axes[1, 1].plot(np.linspace(-3, 3, 100), stats.norm.pdf(np.linspace(-3, 3, 100)), 'r-', label='True N(0,1)')
axes[1, 1].set_title('Marginal Distributions')
axes[1, 1].legend()

plt.tight_layout()
plt.show()

# 检验估计的均值、协方差
print(f"估计的均值: {np.mean(samples_post_burnin, axis=0)}")
print(f"估计的协方差矩阵:\n{np.cov(samples_post_burnin.T)}")
```

## 收敛诊断

### 为什么需要收敛诊断？

1. **Burn-in期：** 链需要时间达到平稳分布
2. **混合效率：** 链探索参数空间的能力
3. **样本独立性：** 自相关问题影响有效样本量

### 诊断方法

#### 1. 迹线图（Trace Plot）

**目的：** 可视化检查链的收敛情况

**特征：**
- 良好的链：像"毛毛虫"，在稳定值周围波动
- 不收敛：有趋势、周期性或突然跳跃

```python
def plot_trace(samples, variable_names=None):
    """绘制迹线图"""
    n_vars = samples.shape[1]
    fig, axes = plt.subplots(n_vars, 1, figsize=(10, 2*n_vars))
    
    if n_vars == 1:
        axes = [axes]
    
    for i, ax in enumerate(axes):
        ax.plot(samples[:, i], alpha=0.7)
        if variable_names:
            ax.set_ylabel(variable_names[i])
        ax.set_xlabel('Iteration')
    
    plt.tight_layout()
    plt.show()
```

#### 2. 自相关函数（ACF）

**目的：** 评估样本间的自相关程度

**特征：**
- 自相关衰减快：链混合良好
- 自相关衰减慢：链混合差，需要更多迭代

**有效样本量：**
$$ESS = \frac{N}{1 + 2\sum_{k=1}^{\infty}\rho_k}$$

其中ρₖ是滞后k的自相关系数。

#### 3. Gelman-Rubin诊断

**目的：** 比较多条链的收敛情况

**方法：**
1. 运行多条链（至少2条）从不同初始值
2. 计算链内方差和链间方差
3. 计算$\hat{R}$（潜在尺度缩减因子）

**判断标准：**
- $\hat{R} < 1.1$：收敛良好
- $\hat{R} > 1.1$：可能未收敛

```python
def gelman_rubin(chains):
    """
    计算Gelman-Rubin诊断统计量
    
    参数:
    chains: (n_chains, n_samples) 数组
    
    返回:
    r_hat: 潜在尺度缩减因子
    """
    n_chains, n_samples = chains.shape
    
    # 链内均值和方差
    chain_means = np.mean(chains, axis=1)
    chain_vars = np.var(chains, axis=1, ddof=1)
    
    # 链间方差
    overall_mean = np.mean(chain_means)
    between_var = n_samples * np.var(chain_means, ddof=1) / (n_chains - 1)
    
    # 链内方差
    within_var = np.mean(chain_vars)
    
    # 潜在尺度缩减因子
    r_hat = np.sqrt((n_samples - 1) / n_samples + between_var / within_var)
    
    return r_hat

# 示例：运行多条链
n_chains = 4
n_samples = 10000
chains = np.zeros((n_chains, n_samples))

for i in range(n_chains):
    samples, _ = metropolis_hastings(target_normal, proposal_normal, 
                                     initial_state=np.random.normal(0, 5), 
                                     n_iter=n_samples)
    chains[i] = samples

# 计算R_hat
r_hat = gelman_rubin(chains.T)
print(f"Gelman-Rubin R-hat: {r_hat:.3f}")
```

#### 4. 其他诊断方法

**Geweke诊断：** 比较早段和晚段样本的均值差异

**Heidelberger-Welch检验：** 检验链是否达到平稳

**Raftery-Lewis诊断：** 估计所需的迭代次数

### 实用建议

1. **预烧期：** 通常丢弃前10%-50%的样本
2. **稀疏化：** 只保留每k个样本以减少自相关
3. **运行多条链：** 从不同初始值开始
4. **视觉检查：** 结合多种诊断方法

## 应用示例：贝叶斯线性回归

```python
import numpy as np
import pymc3 as pm
import matplotlib.pyplot as plt

# 生成模拟数据
np.random.seed(42)
n = 100
x = np.linspace(0, 10, n)
true_slope = 2.5
true_intercept = 1.0
y = true_intercept + true_slope * x + np.random.normal(0, 2, n)

# 贝叶斯线性回归模型
with pm.Model() as linear_model:
    # 先验分布
    intercept = pm.Normal('intercept', mu=0, sd=10)
    slope = pm.Normal('slope', mu=0, sd=10)
    sigma = pm.HalfNormal('sigma', sd=5)
    
    # 似然函数
    mu = intercept + slope * x
    likelihood = pm.Normal('y', mu=mu, sd=sigma, observed=y)
    
    # MCMC采样
    trace = pm.sample(2000, tune=1000, chains=4, cores=2)

# 诊断图
pm.traceplot(trace)
plt.show()

# 总结结果
print(pm.summary(trace))

# 后验预测
with linear_model:
    ppc = pm.sample_posterior_predictive(trace, samples=500)

# 绘制结果
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 回归线和不确定性
axes[0].scatter(x, y, alpha=0.5, label='Data')
for i in range(0, len(trace['slope']), 50):
    axes[0].plot(x, trace['intercept'][i] + trace['slope'][i] * x, 
                 'r-', alpha=0.05)
axes[0].plot(x, true_intercept + true_slope * x, 'k--', label='True line')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].legend()
axes[0].set_title('Posterior Regression Lines')

# 参数分布
axes[1].hist(trace['intercept'], bins=50, alpha=0.7, label='Intercept')
axes[1].hist(trace['slope'], bins=50, alpha=0.7, label='Slope')
axes[1].axvline(true_intercept, color='red', linestyle='--', label='True intercept')
axes[1].axvline(true_slope, color='green', linestyle='--', label='True slope')
axes[1].legend()
axes[1].set_title('Parameter Distributions')

plt.tight_layout()
plt.show()
```

## 注意事项

### 1. 初始值选择

- 选择合理的初始值可以加速收敛
- 从先验分布中抽样作为初始值
- 避免从零概率区域开始

### 2. 参数调优

- 提议分布的参数影响效率
- 自适应MCMC可以自动调优参数
- 常见目标接受率：20%-50%

### 3. 计算成本

- MCMC可能需要大量迭代
- 高维问题计算成本更高
- 考虑使用现代MCMC方法（如NUTS）

### 4. 局限性

- 可能收敛到局部模式
- 多峰分布可能有问题
- 缺乏标准化的收敛诊断

### 5. 现代替代方法

**Hamiltonian Monte Carlo (HMC):**
- 利用物理系统的哈密顿动力学
- 比传统MCMC效率更高

**No-U-Turn Sampler (NUTS):**
- HMC的自适应版本
- PyMC3和Stan中的默认采样器

**变分推断:**
- 确定性近似方法
- 速度快但可能有偏差

## 总结

MCMC是贝叶斯统计的核心工具，使我们能够从复杂的后验分布中抽样。主要要点：

1. **基本原理：** 构造马尔可夫链，使其平稳分布为目标分布
2. **核心算法：** Metropolis-Hastings和Gibbs采样
3. **收敛诊断：** 使用迹线图、自相关、Gelman-Rubin等诊断方法
4. **实际应用：** 贝叶斯回归、层次模型等复杂模型
5. **现代发展：** HMC、NUTS等高效算法

理解MCMC对于现代贝叶斯分析至关重要，它使得我们能够解决传统方法无法处理的复杂统计问题。

## 参考资源

- Gelman, A., et al. (2013). "Bayesian Data Analysis"
- Robert, C. P., & Casella, G. (2004). "Monte Carlo Statistical Methods"
- PyMC3 Documentation: https://docs.pymc.io/
- Stan Manual: https://mc-stan.org/users/documentation/
- Betancourt, M. (2017). "A Conceptual Introduction to Hamiltonian Monte Carlo"
