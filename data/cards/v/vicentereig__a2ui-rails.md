# vicentereig/a2ui-rails

⭐ 14 · Ruby · 推送 2026-01-06 · [GitHub](https://github.com/vicentereig/a2ui-rails) · 个人维护

**Rails 引擎：LLM 生成类型安全的交互式 UI 组件树**

Google A2UI 规范的 Ruby/Rails 移植，基于 DSPy.rb 与 Turbo Streams 实现 LLM 驱动的 UI 生成。AI agent 输出带类型的组件结构体邻接表、Turbo Stream 操作与数据更新，而非可执行代码；组件映射到可信的 ViewComponent 目录（15 种），数据模型与动作上下文使用 Sorbet T::Struct 做服务端类型强制。面向 Rails 开发者，以 gem/Rails Engine 形式提供，含生成器、Stimulus 控制器与独立 JS 渲染包 @a2ui/core。状态为早期开发，API 会变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 经 ChainOfThought 输出类型化组件树、流操作与数据更新，不生成代码
- 15 种组件类型映射到 ViewComponent 目录
- T::Struct + DSPy TypeCoercion 的服务端类型安全数据绑定
- 提供 Rails Engine、生成器与独立浏览器端 JS 包 @a2ui/core

## 适用场景

- 在 Rails 应用中用自然语言生成/增量更新表单等交互界面
- AI agent 通过 Turbo Streams 交付结构化 UI 更新
- 无 Rails 场景下用 @a2ui/core 在浏览器渲染 Surface

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Ruby port of Google's A2UI (Agent-to-User Interface) for Rails, using Turbo Streams and DSPy.rb for LLM-driven UI 
> L55: The LLM never generates code—only typed data structures that map to trusted ViewComponents.

## 星数曲线

```mermaid
xychart-beta
    title "vicentereig/a2ui-rails 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `96099874ce8c` · [字段定义](../../DATASET.md)*
