# hooshyar/flutter_streaming_text_markdown

⭐ 38 · Dart · MIT · 推送 2026-10-26 · [GitHub](https://github.com/hooshyar/flutter_streaming_text_markdown) · [官网](https://hooshyar.github.io/flutter_streaming_text_markdown/) · 个人维护

**Flutter 组件：将 LLM 流式输出实时渲染为 markdown**

面向 Flutter 开发者的 pub 包：接收来自 ChatGPT、Claude、Gemini 或任意模型的 Stream<String>，以打字机/淡入等动画逐段揭示渲染 markdown，并容忍未闭合的语法（半截加粗、未闭合代码块、残缺表格）。内置 ChatGPT/Claude 风格动画预设、LaTeX 渲染、RTL 支持、暂停/跳过控制器与无障碍选项；附 OpenAI 与 Anthropic SSE 转 Stream 的桥接示例。底层 markdown 渲染由 gpt_markdown 完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Stream<String> 直接输入，随缓冲增长重新解析 markdown 与 LaTeX
- ChatGPT/Claude/typewriter/instant 四种动画预设，支持 catchUp 变速平滑突发 token
- 暂停/恢复/跳过/重启的 StreamingTextController 程序化控制
- 对半完成 markdown 语法的容错渲染，不闪现原始标记

## 适用场景

- 在 Flutter 聊天应用中流畅展示 LLM 流式回复
- 为支持 RTL 语言（如阿拉伯语）的 AI 助手渲染回复
- 等待首个 token 时显示骨架屏（TTFT shimmer）的对话界面

## 场景标签

 · 领域:LLM 前端 UI 组件

## 证据(README 行号)

> L3: Render LLM replies as they stream. Pass in a `Stream<String>` from ChatGPT, Claude, Gemini or any model and get smoo
> L30: To use a real model, replace `fakeLlmReply()` with your model's token stream. Streaming from an LLM API has ready-m
> L56: Under the hood the markdown is rendered by `gpt_markdown`; this package adds the streaming engine, reveal animation

## 星数曲线

```mermaid
xychart-beta
    title "hooshyar/flutter_streaming_text_markdown 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-27 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `aff5b4056151` · [字段定义](../../DATASET.md)*
