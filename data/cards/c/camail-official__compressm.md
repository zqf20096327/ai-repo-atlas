# camail-official/compressm

⭐ 34 · Python · MIT · 推送 2026-02-23 · [GitHub](https://github.com/camail-official/compressm) · [官网](https://openreview.net/pdf?id=LtzmeSMBTW) · 组织维护

**训练中压缩状态空间模型（LRU）的研究代码，ICLR 2026 论文配套**

ICLR 2026 论文 The Curious Case of In-Training Compression of State Space Models 的官方代码库，实现 CompreSSM：在训练过程中对 LRU 模型施加平衡截断，依据 Hankel 奇异值识别并移除低影响状态，从大状态维度训练收缩至小维度。覆盖 sMNIST 与 LRA 五个任务的基线、容差压缩、pragmatic 变体与消融实验，提供配置文件与多种子复现脚本。Mamba 实验在另一仓库 CompreSSMamba。基于 Python 3.10+ 与 JAX，源码经 conda 环境安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 训练中基于 Hankel 奇异值的平衡截断状态移除
- 支持 tolerance/fixed/pragmatic 多种压缩模式与自动回滚
- sMNIST 与 LRA 五任务的完整复现配置与多种子脚本
- 提供各压缩容差下的预期结果表

## 适用场景

- 复现论文中的 SSM 训练中压缩实验
- 研究状态维度对 SSM 性能与计算成本的影响
- 将平衡截断压缩方法移植到自己的 LRU/SSM 模型

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L12: This is the main repository accompanying the ICLR 2026 paper The Curious Case of In-Training Compression of State S
> L16: State Space Models (SSMs) offer parallelizable training and fast inference for long sequence modeling. At their cor

## 星数曲线

```mermaid
xychart-beta
    title "camail-official/compressm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a19f341742c4` · [字段定义](../../DATASET.md)*
