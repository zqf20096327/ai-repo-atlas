# DracoBlue/a2a-ai-provider

⭐ 31 · TypeScript · NOASSERTION · 推送 2026-06-12 · [GitHub](https://github.com/DracoBlue/a2a-ai-provider) · [官网](https://npmjs.com/package/a2a-ai-provider) · 个人维护

**为 Vercel AI SDK 提供 A2A 协议 Provider 的适配库**

面向使用 Vercel AI SDK（ai v5+）的开发者，提供 @ai-sdk 兼容的 A2A 协议 Provider 实现：通过 @a2a-js/sdk 支持 A2A JSON-RPC 2.0 API，使 LLM 调用、工具、流式输出与基于文件的 artifacts 之间实现互操作。可作为 drop-in Provider 使用，支持 generateText 与 streamText 两种调用方式，并提供 idGenerator 可配置项。以 pnpm 安装 npm 包形式分发，MIT 许可。README 自述处于 alpha 阶段，功能未完整，不建议用于生产环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- @ai-sdk 兼容的 A2A Protocol Provider（ai v5+ drop-in）
- 基于 @a2a-js/sdk 支持 A2A JSON-RPC 2.0 API
- 支持 generateText 与 streamText 调用方式
- 可替换默认 IdGenerator 的 Provider 配置项

## 适用场景

- 在 Vercel AI SDK 应用中接入 A2A 协议的 agent 服务
- 将 A2A 工具/流式输出/artifacts 纳入 ai SDK 调用链
- 实验性探索 A2A 与 AI SDK 的互操作

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: An `@ai-sdk` compatible AI provider implementation for the A2A Protocol, enabling universal interoperability between
> L9: - 🔌 Drop-in `ai` Provider (v5 and later)

## 星数曲线

```mermaid
xychart-beta
    title "DracoBlue/a2a-ai-provider 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bad6ed918333` · [字段定义](../../DATASET.md)*
