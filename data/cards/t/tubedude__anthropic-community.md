# tubedude/anthropic-community

⭐ 15 · Elixir · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/tubedude/anthropic-community) · 个人维护

**Elixir 开发者访问 Anthropic API 的非官方客户端库**

以 Hex 包 anthropropic_community 发布的非官方 Anthropic API Elixir 客户端：提供 Client 结构体、Messages/Models/Batches 资源模块、类型化内容块、原生工具调用（ToolRunner 驱动完整 agentic 循环）、流式 SSE、指数退避自动重试与统一错误结构。支持服务器端工具（WebSearch/CodeExecution 等，Computer use 与 MCP 连接器为 beta 未支持）、提示缓存、扩展思考、结构化输出、图片/PDF 文档、引用、文件上传（beta）与 token 计数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 类型化内容块（Text/ToolUse/Thinking/Image 等）替代裸 map
- ToolRunner 驱动完整工具调用 agentic 循环
- 流式返回惰性 Stream，429/5xx 指数退避自动重试
- 支持引用（5 种类型）、结构化输出、提示缓存与文件上传（beta）

## 适用场景

- 在 Elixir 应用中接入 Claude 模型完成对话与生成
- 构建带工具调用的 agent，由 ToolRunner 执行循环
- 批量处理请求（Batches）并引用 PDF 出处

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L1: # Anthropic Elixir API Client
> L3: An unofficial Elixir client for the Anthropic API, built around the same shape as Anthropic's official SDKs: an expl

## 星数曲线

```mermaid
xychart-beta
    title "tubedude/anthropic-community 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `eb7fe56992c8` · [字段定义](../../DATASET.md)*
