# Hoyant-Su/Agentic-RL-A3

⭐ 19 · Python · 推送 2026-10-12 · [GitHub](https://github.com/Hoyant-Su/Agentic-RL-A3) · 组织维护

**NeurIPS 2026 论文：CLI agent 的结构化动作信用分配强化学习方法**

研究代码仓库，实现 A3（Action Advantage Assignment）方法：基于可执行 shell 动作计算 episode/turn/trajectory-tree 级优势，对 CLI agent 做策略优化，并提出预算化工作区上下文选择（σ-Reveal harness）与 ShellOps/ShellOps-Pro 基准。支持混合基准训练、推理与评测（JSONL 轨迹评分），发布 A3-Qwen3-14B 检查点并附带 H100 上验证的演示。研究实现为 docker-free，基于 verl/verl-agent 代码基础设施构建；部分重建数据因上游许可需联系作者获取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- A3：从可执行 shell 动作推导 episode/turn/trajectory-tree 优势做信用分配
- ShellOps 与 ShellOps-Pro（OOD infer-only）两个自建基准数据集
- 发布 A3-Qwen3-14B 检查点，演示脚本可在单张 CUDA GPU 上复现
- docker-free 研究实现，训练/推理/评测共用同一入口

## 适用场景

- 复现论文中的 agentic RL 训练与评测流程
- 在自建 CLI 任务基准上训练自定义 agent 策略
- 研究结构化动作信用分配与选择性观测（σ-Reveal）harness 的效果

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L13: **A 3 (Action Advantage Assignment)**
> L16: - Structured CLI code credit for policy optimization
> L57: ```bash

## 星数曲线

```mermaid
xychart-beta
    title "Hoyant-Su/Agentic-RL-A3 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [20, 19, 19]
```

2026-10-18 20 → 2026-10-31 19（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `9d1ccfbc7d9d` · [字段定义](../../DATASET.md)*
