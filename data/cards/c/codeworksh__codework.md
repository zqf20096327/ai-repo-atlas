# codeworksh/codework

⭐ 24 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/codeworksh/codework) · [官网](https://www.codework.sh) · 组织维护

**开源编码 agent CLI：任意模型驱动的代码任务执行工具**

以 npm 包 @codeworksh/cli 分发的命令行编码代理：在本地仓库或隔离沙箱（daytona/vercel/memory/sqldb）中运行会话，支持 OpenAI、Anthropic、Google、xAI、OpenRouter 等多供应商模型，并可订阅登录（OpenAI Codex、GitHub Copilot）。会话状态持久化于本地数据库，可按 ID 恢复；提供 server 模式与插件机制扩展工具、提示词和沙箱驱动。底层拆分为 harness 运行时、plugin SDK 与 aikit 统一 LLM API 四个包，开发需 Node.js 24.14.1+ 与 pnpm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多供应商模型目录与订阅登录（codex/copilot）
- 持久化会话，按 ID 恢复
- 本地或 daytona/vercel/memory/sqldb 沙箱运行
- 插件机制扩展工具、提示词与沙箱驱动

## 适用场景

- 在仓库或沙箱中让 AI agent 执行代码检查与修复任务
- 用同一 CLI 切换不同 LLM 供应商运行编码任务
- 通过插件为自己的 agent 会话添加工具和沙箱

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: An open-source coding agent for code & work: run sessions in your repo or an isolated sandbox, on any model, extend
> L24: codework run --provider openai --model gpt-6-luna "Inspect and fix the failing tests"

## 星数曲线

```mermaid
xychart-beta
    title "codeworksh/codework 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-28 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `df33e150e4f4` · [字段定义](../../DATASET.md)*
