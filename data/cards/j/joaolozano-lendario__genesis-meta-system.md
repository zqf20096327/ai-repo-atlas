# joaolozano-lendario/genesis-meta-system

⭐ 16 · Shell · MIT · 推送 2026-01-18 · [GitHub](https://github.com/joaolozano-lendario/genesis-meta-system) · 个人维护

**面向 Claude Code 的元系统：从领域描述生成完整 Claude Code 系统**

GENESIS 是基于 Claude Code 的元系统生成器：输入领域文字简述，经 8 阶段流水线（含 5 个人工确认门）生成包含 slash 命令、CLAUDE.md、skills、agents、STATE.yaml 的完整 Claude Code 原生系统，支持 COGNITIVE/TECHNICAL/CREATIVE/OPERATIONAL/HYBRID 五类系统。提供 11 个 slash 命令用于生成、验证、导出、恢复与测试，验证用 Glob/Grep 计算实际得分而非估算，附 20 项自动化测试。需已安装 Claude Code CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 领域描述→完整 Claude Code 系统的 8 阶段生成流水线
- 11 个 slash 命令覆盖生成/验证/导出/恢复/测试
- Glob/Grep 实际计数评分（完整性/一致性/原则分加权）
- 生成合成专家团队（THINKER/HYBRID/EXECUTOR 认知类型）

## 适用场景

- 我用一句领域描述让 Claude Code 生成营销、DevOps 等完整系统
- 对已生成的 Claude Code 系统做量化验证与评分
- 管理、导出或恢复多个生成的系统

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L18: **GENESIS is a meta-system** — a system that generates other systems.
> L31: GENESIS generates systems designed specifically for **Claude Code's architecture**:
> L232: - **Claude Code CLI** installed

## 星数曲线

```mermaid
xychart-beta
    title "joaolozano-lendario/genesis-meta-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5f7e231117e5` · [字段定义](../../DATASET.md)*
