# buda-ai/bunny-agent

⭐ 29 · TypeScript · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/buda-ai/bunny-agent) · [官网](https://sandagent.dev/  ) · 组织维护

**多模型编程 agent CLI/SDK：本地或远程沙箱执行编码任务**

基于 Pi Coding Agent 的 TypeScript 编程 agent，支持三种用法：本地 CLI 编码助手、bunny remote 一键启动云沙箱（Sandock，$5/月起）、通过 SDK（LanguageModelV3 兼容 provider）嵌入 Next.js/Electron 等自有产品。stdout 即 AI SDK UI 流，可直接接 useChat() 前端。内置工具 harness（网页搜索、抓取、图像生成、bash、文件操作），支持 Claude/Gemini/OpenAI/Codex/Copilot 等多个 runner，沙箱可选 Sandock/E2B/Daytona/本地。附 GAIA 基准评测 harness。需自备模型 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- stdout 原生输出 AI SDK UI 流，useChat() 零胶水接入
- 多 runner 切换（Claude/Pi/Codex/Copilot/Gemini/OpenCode），无需改代码
- 内置工具 harness，技能文件自动发现
- SDK 提供 LanguageModelV3 兼容 provider，可嵌入自有产品

## 适用场景

- 把 CLI 当日常本地编码助手使用
- 在远程云沙箱中隔离运行 agent 任务并持久化会话
- 用 SDK 快速搭建自己的编程 agent SaaS 或桌面应用

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L19: **Bunny Agent** is a coding agent built on Pi Coding Agent — multi-model, harness-ready, and designed from the grou
> L27: It outputs a **native AI SDK UI stream** — meaning you can wire it directly into any `useChat()` frontend with zero

## 星数曲线

```mermaid
xychart-beta
    title "buda-ai/bunny-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7c274cb5c832` · [字段定义](../../DATASET.md)*
