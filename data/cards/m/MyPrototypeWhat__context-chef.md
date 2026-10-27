# MyPrototypeWhat/context-chef

⭐ 31 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/MyPrototypeWhat/context-chef) · [官网](https://myprototypewhat.github.io/context-chef/) · 个人维护 · 中文 README

**面向 TS/JS AI agent 的上下文编译器：压缩历史、裁剪工具、适配多提供商**

TypeScript/JavaScript 库，在每次 LLM 调用前将 agent 状态编译为适配目标提供商的载荷：自动压缩对话历史（summarize/anchored/reset 策略，可后台执行）、按任务裁剪工具列表、Zod 校验的动态状态注入、约束消息 pinning、统一 context:// 存储与单一 context 工具检索、快照回滚。同一提示架构可编译到 OpenAI/Anthropic/Gemini 适配格式。以 npm monorepo 提供 core 及 AI SDK/TanStack AI 中间件三个包，面向 agent 开发者，零配置两行接入。

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

- 历史压缩（含约束 pinning 与后台压缩）与溢出策略可组合/可自定义
- 工具裁剪与双层命名空间架构降低工具幻觉，KV-cache 友好
- 五轴架构：选择/放置/持久化/检索/适配，统一 StorageBackend 与单一 context 工具
- Vercel AI SDK 与 TanStack AI 中间件包零代码改动接入

## 适用场景

- 长对话 agent 上线后自动压缩历史且不丢失约束
- 工具过多导致模型选错工具时按任务动态裁剪
- 同一套 prompt 架构在 OpenAI/Anthropic/Gemini 间切换
- 长任务中保持状态注入与快照回滚

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L15: Context compiler for TypeScript/JavaScript AI agents.
> L17: ContextChef solves the most common context engineering problems in AI agent development: conversations too long for
> L25: |`@context-chef/core`|Core context compiler — overflow strategies, tool pruning, one addressed context store, pipel

## 星数曲线

```mermaid
xychart-beta
    title "MyPrototypeWhat/context-chef 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `795bb8eea14c` · [字段定义](../../DATASET.md)*
