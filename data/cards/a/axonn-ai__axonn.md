# axonn-ai/axonn

⭐ 76 · Python · Apache-2.0 · 推送 2026-04-28 · [GitHub](https://github.com/axonn-ai/axonn) · [官网](https://axonn.readthedocs.io) · 组织维护

**并行训练与微调深度神经网络的分布式框架**

AxoNN 是一个用于训练深度神经网络的并行框架，面向需要在多 GPU/大规模环境下做模型训练与微调的开发者与科研人员。安装要求先装好 PyTorch，再通过 pip 安装 axonn；项目采用 Black 代码风格，提供 Slack 与文档入口，配套论文发表于 IPDPS '22，主题为异步、消息驱动的极大规模深度学习。以 Apache 2.0 许可分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 异步、消息驱动的并行深度学习训练框架
- 支持深度神经网络的大规模并行训练与微调
- pip 安装，前置依赖 PyTorch

## 适用场景

- 在多 GPU 集群上并行训练大规模神经网络
- 微调深度模型并利用并行计算加速

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L8: AxoNN is a parallel framework for training deep neural networks.
> L11: Prior to the installation, PyTorch must already be installed.

## 星数曲线

```mermaid
xychart-beta
    title "axonn-ai/axonn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-24 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `5409a175b80a` · [字段定义](../../DATASET.md)*
