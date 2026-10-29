# imsai-sh/open-claude-design

⭐ 18 · TypeScript · Apache-2.0 · 推送 2026-05-15 · [GitHub](https://github.com/imsai-sh/open-claude-design) · [官网](https://www.imsai.cc/) · 个人维护 · 中文 README

**开源复刻 Claude Design：浏览器内对话生成多文件 React 原型**

对 Anthropic Claude Design（claude.ai/design）的开源复刻，纯 Web 应用形态：用户对话生成多文件 React 原型（.jsx/.html/.css），配 Tweaks·Comment·Edit·Draw 四种预览内就地编辑工具。Agent 循环（Vercel AI SDK ToolLoopAgent）运行在浏览器标签页内，BYOK 直连 OpenRouter 等 10 个提供商；存储走单个 Cloudflare Worker（D1 元数据 + R2 内容寻址 blob），Worker 不经手提示词。自称 pre-alpha，可能破坏性变更；verifier 子代理、本地文件夹桥接与第三方 MCP 尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 对话流式生成多文件 React 项目，Babel Standalone 沙箱 iframe 预览
- Tweaks/Comment/Edit/Draw 四种预览内就地编辑工具
- Agent 循环在浏览器运行，BYOK 直连 OpenRouter 等 10 个提供商
- 单个 Cloudflare Worker（D1+R2）做存储，可导入 Claude Design ZIP 导出

## 适用场景

- 用对话快速生成并迭代多文件 React 界面原型
- 在预览中直接调整设计令牌、内联样式并回写源码
- 自托管一个不依赖桌面端/本地守护进程的 AI 原型工具

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L122: - **Chat → generate** a multi-file React prototype, streamed token-by-token into the project workspace.
> L135: - **AI** — Vercel AI SDK `ToolLoopAgent` running in the browser, calling OpenRouter or any of 10 first-party provi

## 星数曲线

```mermaid
xychart-beta
    title "imsai-sh/open-claude-design 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5911aea32839` · [字段定义](../../DATASET.md)*
