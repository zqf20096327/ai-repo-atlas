# nakasyou/hono-typedstream

⭐ 42 · TypeScript · MIT · 推送 2025-10-31 · [GitHub](https://github.com/nakasyou/hono-typedstream) · [官网](https://npmjs.org/package/hono-typedstream) · 个人维护

**Hono 的类型安全 JSON 流式响应工具库**

面向使用 Hono 框架的 TypeScript 开发者的轻量辅助库：服务端将 ReadableStream 或 AsyncGenerator 逐行序列化为 JSON 并以流式响应发送，客户端通过 receiveTypedStream 重建为带类型的对象，借助 TypedResponse 在服务端与客户端之间共享同一泛型类型，实现端到端类型安全。无手动管道代码，支持与 streamText 和 testClient 配合。通过 npm 与 jsr 发布安装。

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

- 服务端 typedStream 读取 ReadableStream/AsyncGenerator 并逐行流式输出 JSON
- 客户端 receiveTypedStream 将每行 JSON 重建为类型化对象
- 基于 TypedResponse 实现服务端与客户端类型共享

## 适用场景

- 在 Hono 应用中实现类型安全的流式 JSON 接口
- 前后端共享泛型类型，避免流式数据的手动类型维护
- 为流式输出场景（如模型生成内容）提供传输层支持

## 场景标签

 · 领域:Web 开发/流式传输

## 证据(README 行号)

> L5: `hono-typedstream` is a lightweight helper that lets Hono handlers stream JSON values line by line while keeping end
> L11: - **Built for Hono**: Leverages `streamText`, works smoothly with `testClient`, and fits naturally into existing Ho

## 星数曲线

```mermaid
xychart-beta
    title "nakasyou/hono-typedstream 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `89ea6c3de08c` · [字段定义](../../DATASET.md)*
