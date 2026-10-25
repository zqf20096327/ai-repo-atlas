# davis7dotsh/river

⭐ 228 · TypeScript · MIT · 推送 2026-03-27 · [GitHub](https://github.com/davis7dotsh/river) · [官网](https://useriver.dev) · 个人维护

**为全栈 TypeScript 应用提供类型安全、可恢复的 AI agent 流式传输库**

面向 SvelteKit 与 TanStack Start 开发者的流式传输库：提供类似 tRPC 的服务端创建/写入流与客户端消费流 API，对每个流块实现全栈类型安全；通过 Redis provider 支持可恢复/持久化流；框架无关，可与 AI SDK、Mastra 或自定义流搭配使用。安装为 bun 添加 river-core 与对应框架适配器包，peer 依赖 zod 与 neverthrow。README 标注完整文档尚在编写中，路线图包含文档页与 S2 provider。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 流块的全栈类型安全与 tRPC 风格客户端/服务端 API
- Redis provider 下开箱即用的可恢复/持久化流
- 库无关：兼容 AI SDK、Mastra 与自定义流
- 提供 SvelteKit 与 TanStack Start 适配器包

## 适用场景

- 在 SvelteKit/TanStack Start 应用中构建类型安全的 agent 流式接口
- 需要断线后可恢复的持久化流式输出场景
- 在不同 AI 框架之间复用同一套流式基础设施

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: - full stack type safety on stream chunks
> L8: - library agnostic, works with ai sdk, mastra, custom streams, or anything you want
> L9: - resumable/durable streams work out of the box with the redis provider

## 星数曲线

```mermaid
xychart-beta
    title "davis7dotsh/river 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 227 --> 229
    line [228, 228]
```

2026-10-18 228 → 2026-10-25 228（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `31faa48a7b72` · [字段定义](../../DATASET.md)*
