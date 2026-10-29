# surmon-china/surmon.me.ai

⭐ 22 · TypeScript · MIT · 推送 2026-03-22 · [GitHub](https://github.com/surmon-china/surmon.me.ai) · 个人维护 · 中文 README

**surmon.me 博客生态的 AI Agent 对话服务**

运行在 Cloudflare Workers 上的自包含 AI Agent 服务，将 CMS 内容（NodePress）、前端博客网站与外部知识源统一接入智能对话能力；采用 Tool-driven 的 Agent 架构，模型为 Gemini 2.5 Flash，并使用 RAG 检索。面向个人博客生态（surmon.me）的访客与管理场景，依赖 Cloudflare D1/R2 等资源，通过 wrangler 配置密钥后以 pnpm 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tool-driven 的 Agent 架构
- Gemini 2.5 Flash + RAG 驱动对话
- 统一接入 NodePress CMS、前端网站与外部知识源
- 构建于 Cloudflare Workers，含 D1/R2 资源

## 适用场景

- 在我的博客上提供基于站点内容的智能问答
- 把 CMS 文章与外部知识源接入统一的对话界面

## 场景标签

`RAG` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L11: **The AI Agent service for the surmon.me ecosystem, built on Cloudflare Workers. It connects CMS content (NodePress
> L15: **为 surmon.me 生态构建的自包含 AI Agent 服务。基于 Tool-driven 的 Agent 架构，将 CMS 内容（NodePress）、前端网站（Surmon.me）与外部知识源统一接入智能对话能力。**

## 星数曲线

```mermaid
xychart-beta
    title "surmon-china/surmon.me.ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f054ab171947` · [字段定义](../../DATASET.md)*
