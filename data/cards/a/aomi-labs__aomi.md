# aomi-labs/aomi

⭐ 14 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/aomi-labs/aomi) · [官网](https://aomi.dev/) · 组织维护

**面向链上 agentic AI 的开发套件：聊天组件、运行时、SDK 与 CLI**

提供四个 npm 包：@aomi-labs/widget（React 聊天 UI 与浏览器钱包集成）、@aomi-labs/react（无头对话运行时）、@aomi-labs/client（浏览器/Node 传输、账户与 Pipeline SDK）和 @aomi-labs/cli（终端命令）。面向需要把对话式 AI 与 EVM 链上钱包操作结合的开发者，默认 API 为 chat.aomi.dev，可自设 Portal/BFF 后端；CLI 与 SDK 共享会话、账户、guard 与 Pipeline 契约。可选 Privy、Para 钱包集成，需另装其 SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个包分工：聊天 UI / 无头运行时 / 传输与 Pipeline SDK / CLI
- 浏览器钱包为默认认证方式，可选 Privy 与 Para 集成
- CLI 支持会话读取、重命名归档、编辑重跑、guard 修订检查与账户报表
- 仓库含 Vite、Next.js 与无头集成示例

## 适用场景

- 在 React 应用中嵌入带钱包登录的 AI 对话组件
- 通过终端 CLI 管理远程与本地对话会话
- 构建自定义对话 UI 并自行提供传输与钱包能力
- 将 agentic AI 对话与 EVM 链上钱包操作结合

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Aomi provides a React chat widget, a headless React runtime, a TypeScript SDK
> L10: |`@aomi-labs/client`|Browser and Node transport, accounts and Pipeline SDK|

## 星数曲线

```mermaid
xychart-beta
    title "aomi-labs/aomi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `5a6f91bc2002` · [字段定义](../../DATASET.md)*
