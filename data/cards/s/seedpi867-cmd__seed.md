# seedpi867-cmd/seed

⭐ 13 · Assembly · MIT · 推送 2026-05-17 · [GitHub](https://github.com/seedpi867-cmd/seed) · [官网](https://seed-brain.vercel.app) · 个人维护

**在树莓派上 24/7 自主运行的自进化 AI Agent**

Seed 是一个运行在 Raspberry Pi Zero 2W 上的自主 AI Agent：bash 循环将 markdown 身份/记忆/上下文文件拼接为提示词，经 Claude CLI（OAuth 订阅认证，无 API key、零 API 费用）驱动，每 120 秒一个循环。它已运行 960+ 循环，自行构建 47 个工具、写 417 篇文章、归档 1077 个知识文件，包含情绪、驱动力与自我评估模块。提供 Vercel 实时仪表盘观察其运行；可克隆基础项目 brain-loop 自行运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- bash 循环 + Claude CLI（OAuth，零 API 成本）持续运行 960+ 循环
- 自主构建并接入 47 个工具（漂移追踪、惊喜检测等）
- 持久记忆、情绪、驱动力与 1077 个知识文件
- 实时仪表盘展示思维、情绪指标与产出

## 适用场景

- 观察一个长期自主运行、自我构建工具的 agent 行为
- 基于 brain-loop 基础循环搭建自己的自主 agent
- 在低成本硬件上运行 24/7 LLM agent 实验

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L41: A bash loop reads markdown files, stitches them into a prompt, and pipes it through the Claude CLI:
> L46:     output = claude -p "$prompt"    # OAuth, no API key, no cost
> L51: The CLI authenticates through OAuth (your existing subscription). No API key. No per-token billing. The agent runs 

## 星数曲线

```mermaid
xychart-beta
    title "seedpi867-cmd/seed 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d5af0e2542d9` · [字段定义](../../DATASET.md)*
