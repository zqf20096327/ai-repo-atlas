# quchangle1/MatchTIR

⭐ 20 · Python · 推送 2026-07-27 · [GitHub](https://github.com/quchangle1/MatchTIR) · [官网](https://arxiv.org/abs/2601.10712) · 组织维护 · 中文 README

**工具集成推理的细粒度监督训练框架（ACL 2026 论文实现）**

ACL 2026 论文 MatchTIR 的官方实现：通过二部匹配做轮次级奖励分配与双层优势估计，为工具集成推理提供细粒度监督。基于 VeRL 框架训练，提供 KM（Hard）与 OT（Soft）两种奖励函数实现，发布 Qwen3-4B/8B 的四组模型检查点与 FTRL 训练数据；训练用 FTRL，域外评测用 BFCL 与 ToolHop。面向做 LLM 工具调用/推理强化学习训练的科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 二部匹配的轮次级奖励分配与双层优势估计
- 提供 KM（Hard）与 OT（Soft）两种奖励函数
- 发布 Qwen3-4B/8B 四组检查点与 FTRL 数据集
- 基于 VeRL 0.3.1.dev 框架，脚本化训练/合并/评测流程

## 适用场景

- 训练工具集成推理能力的 LLM
- 在 FTRL/BFCL/ToolHop 上评测工具调用与泛化能力
- 复现论文实验或使用已发布的检查点做后续研究

## 场景标签

`强化学习` `微调` · 领域:训练与推理

## 证据(README 行号)

> L32: We propose **MatchTIR**, a framework that introduces fine-grained supervision via bipartite matching-based turn-lev
> L119: We employ the VeRL 0.3.1.dev framework for training.

## 星数曲线

```mermaid
xychart-beta
    title "quchangle1/MatchTIR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1bef33b7d263` · [字段定义](../../DATASET.md)*
