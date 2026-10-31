# wende/mobileclaw

⭐ 22 · TypeScript · 推送 2026-07-15 · [GitHub](https://github.com/wende/mobileclaw) · [官网](https://mobileclaw.vercel.app?demo) · 个人维护

**移动优先的 OpenClaw/LM Studio 聊天界面（PWA）**

面向 OpenClaw 与 LM Studio 的移动端优先聊天前端：通过 WebSocket 连接 OpenClaw 后端，LM Studio 走 OpenAI 兼容 API 自动获取本地模型列表。支持流式 Markdown 渲染、工具调用实时状态展示、编辑差异（diff）内联视图、可展开的思维链（reasoning）块、子智能体（sub-agent）活动流。另提供可嵌入的 iframe 小部件（?detached 参数）、命令面板、暗色模式、文件上传、推送通知与可选 Cloudflare Turnstile 防护。Next.js 16 + TypeScript 构建，git clone 源码 pnpm 启动，无桌面安装包。

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

- 流式输出 + 富 Markdown 渲染（代码高亮、一键复制）
- 工具调用实时状态与红绿内联 diff 视图
- LM Studio 本地模型支持，无需云端
- iframe 嵌入模式（?detached）免配置连接后端

## 适用场景

- 手机上给 OpenClaw/ LM Studio 提供可用的聊天界面
- 把聊天小部件嵌入任意网页连接自有后端
- 在移动端查看智能体（agent）工具调用与推理过程

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L2: A mobile-first chat UI for OpenClaw and LM Studio
> L51: Run local models with full chat UI support. Auto-fetches available models, parses `<think>` tags for reasoning disp
> L57: Drop MobileClaw into any page as an iframe. The `?detached` query param renders a compact, chromeless chat widget —

## 星数曲线

```mermaid
xychart-beta
    title "wende/mobileclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `b652946867e7` · [字段定义](../../DATASET.md)*
