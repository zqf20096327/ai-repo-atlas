# dannote/phoenix_streamdown

⭐ 26 · Elixir · MIT · 推送 2026-05-03 · [GitHub](https://github.com/dannote/phoenix_streamdown) · 个人维护

**Phoenix LiveView 的流式 markdown 渲染组件，面向 LLM 输出**

Elixir/Phoenix LiveView 组件库：在服务端渲染 markdown，token 流式到达时仅重渲染最后一个块，已完成块以 phx-update=ignore 冻结；自动闭合不完整语法（未闭合加粗、围栏、链接），底层用 Rust 支持的 MDEx 渲染 HTML，客户端零 JavaScript。支持词级淡入等流式动画。示例为使用 ReqLLM 流式输出的聊天应用。供在 LiveView 中展示 LLM 流式回复的开发者使用。

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

- 服务端渲染 + 块级 diff，仅重渲染活动块
- Remend 自动闭合不完整 markdown 语法
- 零客户端 JavaScript，支持词级流式动画

## 适用场景

- LiveView 聊天应用中流式展示 LLM 回复
- 需要稳定已渲染内容、仅更新尾部的 markdown 流渲染

## 场景标签

 · 领域:Web 前端/LLM 界面组件

## 证据(README 行号)

> L3: Streaming markdown renderer for Phoenix LiveView, optimized for LLM output.
> L25: That's it. Pass `content` as a markdown string, set `streaming` to `true` while tokens are arriving. Completed bloc

## 星数曲线

```mermaid
xychart-beta
    title "dannote/phoenix_streamdown 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ea5efd77778b` · [字段定义](../../DATASET.md)*
