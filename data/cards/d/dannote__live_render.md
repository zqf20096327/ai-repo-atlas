# dannote/live_render

⭐ 65 · Elixir · MIT · 推送 2026-03-14 · [GitHub](https://github.com/dannote/live_render) · 个人维护

**为 Phoenix LiveView 提供 AI 生成 UI 的 Elixir 库**

面向 Elixir/Phoenix 开发者的 server-driven generative UI 库：LLM 生成 UI spec，LiveView 在服务端将其解析为函数组件，仅通过 WebSocket 推送 HTML 差异。AI 只能使用目录中注册的组件形成约束；支持 JSON Patch、JSON Object、YAML、OpenUI Lang、A2UI 五种 spec 格式，其中 OpenUI Lang 声称比 JSON 少约 50% token。可搭配 ReqLLM、Jido 或任意产生 spec map 的客户端。以 Hex 依赖安装，含 18 个内置组件与示例聊天应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 只能调用目录中注册的组件，服务端解析 spec 并仅推送 HTML diff
- 五种 spec 格式（JSON Patch/JSON Object/YAML/OpenUI Lang/A2UI），支持流式渐进渲染
- 多轮编辑模式：LLM 仅输出变更键，按 RFC 7396 深度合并
- 内置 18 个组件与含工具调用的 ReAct 示例应用

## 适用场景

- 在 Phoenix LiveView 应用中让 LLM 动态生成受约束的界面
- 构建聊天式工具（天气/加密行情/GitHub 等）的生成式 UI
- 接入 A2UI 协议的 agent 输出到 LiveView 渲染

## 场景标签

 · 领域:Web 前端/LLM 应用框架

## 证据(README 行号)

> L5: AI generates a UI spec → LiveView resolves it to function components server-side → pushes only HTML diffs over the W
> L17: - **Bring your own LLM** — works with ReqLLM, Jido, or any client that produces a spec map

## 星数曲线

```mermaid
xychart-beta
    title "dannote/live_render 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-30 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6f9953ba1e9c` · [字段定义](../../DATASET.md)*
