# thesysdev/genui-widget

⭐ 21 · TypeScript · 推送 2026-01-16 · [GitHub](https://github.com/thesysdev/genui-widget) · [官网](https://www.thesys.dev/) · 组织维护

**可嵌入网页的生成式 UI 聊天组件，连接 LangGraph/n8n 后端**

由 Thesys 构建的嵌入式聊天 widget，让 AI 聊天机器人渲染按钮、表单、图表等富交互 UI 而非纯文本。面向在自己的应用中接入 AI 对话的开发者：通过单个 script 标签或 npm 包安装，后端可接 LangGraph/LangChain 部署（云端或自托管）、n8n、Make.com 或自定义 webhook；支持 SSE 流式响应、会话与线程管理，存储可选 localStorage、LangGraph 服务端或内存；提供全页/侧栏/底部托盘三种布局与明暗主题。限制：需自行配置后端，Node.js 20.9.0+ 用于开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个 script 标签或 npm 包即可嵌入
- 后端支持 LangGraph、n8n、Make.com 及自定义 webhook
- SSE 实时流式响应与线程管理（创建/切换/删除）
- 三种存储模式：内存/localStorage/LangGraph 服务端

## 适用场景

- 给网站快速嵌入 AI 聊天窗口
- 把 LangGraph 或 n8n 工作流的输出渲染为交互式 UI
- 跨设备同步对话历史的服务端部署

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: An embeddable chat widget that lets your AI chatbots render rich, interactive UI like buttons, forms, charts, cards 
> L16: - 🔌 **Multi-Provider** - LangGraph, n8n, Make.com, or custom webhooks

## 星数曲线

```mermaid
xychart-beta
    title "thesysdev/genui-widget 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `159e3af7630e` · [字段定义](../../DATASET.md)*
