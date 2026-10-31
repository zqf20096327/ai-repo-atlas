# lucidrains/discrete-distribution-network

⭐ 38 · Python · MIT · 推送 2026-08-02 · [GitHub](https://github.com/lucidrains/discrete-distribution-network) · 个人维护 · 中文 README

**离散分布网络（DDN）的 PyTorch 实现库**

lucidrains 对 Lei Yang（北京）提出的 Discrete Distribution Network 的探索性实现，提供 DDN 与论文中的 GuidedSampler 两个 PyTorch 模块，支持 split-and-prune 之外可选 crossover（混合 top 2 节点替换被剪枝节点）选项。附 Oxford flowers 数据集上的训练脚本，通过 pip/uv 安装运行，供研究与实验复现使用。

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

- 提供 DDN 模块的 PyTorch 实现
- 包含论文提出的 GuidedSampler 实现
- 支持 crossover 选项（混合 top 2 节点替换被剪枝节点）
- 附带 Oxford flowers 训练脚本

## 适用场景

- 复现或实验 Discrete Distribution Network 论文方法
- 研究生成建模中的离散分布机制
- 在 Oxford flowers 数据集上训练示例模型

## 场景标签

 · 领域:深度学习/生成建模

## 证据(README 行号)

> L19: from discrete_distribution_network import DDN
> L28: from discrete_distribution_network import GuidedSampler

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/discrete-distribution-network 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-31 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `587de30aefef` · [字段定义](../../DATASET.md)*
