# timazed/CodexKit

⭐ 33 · Swift · 推送 2026-10-28 · [GitHub](https://github.com/timazed/CodexKit) · 个人维护

**在 iOS/macOS 应用中嵌入 OpenAI Codex 风格 agent 的 Swift SDK**

面向 iOS 17+/macOS 14+ 应用的 Swift SDK，提供 ChatGPT 登录（浏览器 OAuth 与设备码）、可恢复会话线程（SQLite 或 Realm 持久化）、流式类型化输出、应用自定义工具（带审批门与并行限制）、人设/技能/本地记忆等能力。配套的可选 npm 包 @timazed/codexkit 供 Node.js 后端执行 SDK 预备的文本、结构化 JSON 与图像生成/编辑请求，后端需自行负责鉴权、队列与存储。npm 包不支持工具调用与完整 agent 运行时，每次调用仅一次提供商尝试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ChatGPT 浏览器 OAuth 与设备码登录，macOS 可复用本地 Codex 会话
- SQLite/Realm 双持久化适配器的可恢复线程与上下文压缩
- 应用自定义工具带审批门、技能策略限制与有界并行执行
- npm 包在 Node 后端执行预备的文本/JSON/图像请求，零运行时依赖

## 适用场景

- 在 iOS/macOS 应用内构建带 ChatGPT 账号登录的对话 agent
- 让后端执行 App 预备的结构化 JSON 或图像生成请求
- 为 agent 添加带审批门的自定义工具与本地记忆

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: `CodexKit` is a Swift SDK for embedding Codex-style agents in **iOS 17+ and macOS 14+** apps. It provides ChatGPT si
> L8: The optional `@timazed/codexkit` npm package lets Node.js backends execute CodexKit-prepared **text, structured JSON

## 星数曲线

```mermaid
xychart-beta
    title "timazed/CodexKit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-29 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6509df61b396` · [字段定义](../../DATASET.md)*
