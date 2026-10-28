# horenbergerb/BernoulliDiffusion

⭐ 22 · Python · MIT · 推送 2026-09-27 · [GitHub](https://github.com/horenbergerb/BernoulliDiffusion) · 个人维护

**面向二值数据的 Bernoulli 扩散模型实现，训练并生成样本**

实现论文 Deep Unsupervised Learning using Nonequilibrium Thermodynamics 所述扩散算法，用 Bernoulli 分布（而非 Gaussian）生成噪声，训练于固定长度的二值数据并学习生成同分布样本。2026 更新重构训练以修复收敛问题：反向模型加入跳连接、每样本采样单个时间步、可选 x_0 预测。提供配置化训练/生成脚本、基础验证与可视化；验证程序较粗糙。以 Python 源码仓库形式提供，经 requirements.txt 安装依赖后运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Bernoulli 分布为噪声源的二值数据扩散模型
- 2026 更新：跳连接、单时间步采样损失、可选 x_0 预测
- 提供 train.py / generate.py 脚本与 config.yaml 三段配置
- 含单元测试与训练演化 GIF、损失曲线等可视化

## 适用场景

- 学习/复现离散扩散模型算法
- 在二值序列数据上训练生成模型并采样
- 研究离散扩散的训练技巧与收敛问题

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: This is an implementation of the diffusion machine learning algorithm described in Deep Unsupervised Learning using 
> L7: This model can be trained on any binary-valued data of fixed length. It will learn to generate samples which appear 

## 星数曲线

```mermaid
xychart-beta
    title "horenbergerb/BernoulliDiffusion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `72da1ca7c587` · [字段定义](../../DATASET.md)*
