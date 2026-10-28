# raiyanyahya/build-pipe

⭐ 22 · JavaScript · MIT · 推送 2026-08-11 · [GitHub](https://github.com/raiyanyahya/build-pipe) · [官网](https://buildpipe.com) · 个人维护

**本地优先的桌面流水线自动化应用，供开发者编排含 AI 调用的多步工作流**

Electron 桌面应用，供开发者可视化编排与运行多步工作流（本地 Zapier/n8n 定位）：步骤类型含 Shell 命令、AI 语言模型调用（OpenAI/Anthropic，可在设置中切换）、HTTP 请求、文件读写、条件分支、循环与通知，步骤间以 {{step_id.output}} 模板传递输出。支持 cron 定时、文件变更监听与本地 Webhook 触发。AI 还可用于以自然语言生成流水线（Build with AI）及作为各模板中的分析步骤。附带 43 个流水线模板。所有数据存于本地 ~/.buildpipe，无遥测与云同步；AI 功能依赖 OpenAI 或 Anthropic API key（加密存储）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 种步骤类型（CODE/AI/HTTP/FILE/IF/LOOP/NOTIFY）+ 模板变量串联输出
- 定时（内置 cron）、文件监听、本地 Webhook 三种触发方式
- 自然语言描述生成完整流水线（Build with AI）
- 43 个即用模板与运行历史记录（每流水线保留最近 100 次）

## 适用场景

- 把 Shell 命令、AI 摘要与文件写入串成每日自动化流水线
- 文件变更或 Webhook 触发本地开发任务
- 用内置模板快速搭建晨间简报、日志监控等自动化

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L13: **buildpipe** is a standalone desktop app that lets you compose, run, and automate multi-step developer workflows —
> L15: Think of it as a local Zapier or n8n, built specifically for developers who want to chain shell commands, AI calls,
> L40: #### `AI` — Language model call

## 星数曲线

```mermaid
xychart-beta
    title "raiyanyahya/build-pipe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2612a6ab53a8` · [字段定义](../../DATASET.md)*
