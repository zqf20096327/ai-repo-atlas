# CommandCodeAI/langbase-sdk

⭐ 65 · TypeScript · NOASSERTION · 推送 2026-05-15 · [GitHub](https://github.com/CommandCodeAI/langbase-sdk) · [官网](https://langbase.com/docs/sdk) · 组织维护

**Langbase 平台的 TypeScript SDK，用于调用其 Pipes 生成/流式文本**

面向开发者的 npm 包，封装 Langbase 平台 API：通过 langbase.pipes.run() 以声明式方式生成或流式输出 LLM 文本，需配置 LANGBASE_API_KEY。README 提供安装命令与 Node.js、Next.js 示例（含 React 展示组件与 API Route），细节引导至官方文档。内容较薄，未见本地运行时或离线能力说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- langbase.pipes.run() 支持生成与流式两种输出模式
- 提供 Node.js 与 Next.js 示例工程
- npm/pnpm/yarn 三种包管理器安装方式

## 适用场景

- 在 Node/Next.js 应用中调用 Langbase Pipes 生成文本
- 通过 React 组件展示流式 LLM 响应

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: The AI SDK for building declarative and composable AI-powered LLM products.
> L35: You can `langbase.pipes.run()` to generate or stream from a Pipe.

## 星数曲线

```mermaid
xychart-beta
    title "CommandCodeAI/langbase-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-31 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `d92ef01c3e5d` · [字段定义](../../DATASET.md)*
