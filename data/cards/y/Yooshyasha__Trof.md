# Yooshyasha/Trof

⭐ 21 · Kotlin · MIT · 推送 2026-07-28 · [GitHub](https://github.com/Yooshyasha/Trof) · 个人维护

**面向 Vikunja 的 AI 任务生成器：自然语言拆解为任务并经确认入库**

自托管的 Kotlin 应用，连接 Vikunja 任务追踪器：用户用自然语言描述项目，AI 生成结构化任务集，并可在拆解前提出澄清问题；所有变更需经用户逐项审核确认后才写入 Vikunja。支持创建与编辑项目，可修改任务名称、描述、评论、标签或删除生成项。AI 提供方可选 OpenAI、Anthropic、Google、OpenRouter、DeepSeek 或本地 Ollama。通过 Gradle 构建并以 Docker Compose 启动，nginx 提供 HTTPS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言描述项目，AI 拆解为结构化 Vikunja 任务
- AI 可提出澄清问题以细化拆解
- 所有变更需用户审核确认后才写入 Vikunja
- 支持 6 种 AI 提供方，含本地 Ollama（无需 API key）

## 适用场景

- 用自然语言把项目想法拆解成 Vikunja 任务清单
- 在任务入库前审核并修正 AI 生成的任务
- 在自托管环境中为 Vikunja 补充 AI 辅助的项目规划能力

## 场景标签

 · 领域:任务管理/生产力工具

## 证据(README 行号)

> L3: > AI task generation for Vikunja — it intercepts bad tasks before they hit your board. Describe a project in plain l
> L14: - **AI-assisted breakdown** — the AI turns your description into a structured set of tasks.

## 星数曲线

```mermaid
xychart-beta
    title "Yooshyasha/Trof 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a7c9fbeb55e5` · [字段定义](../../DATASET.md)*
