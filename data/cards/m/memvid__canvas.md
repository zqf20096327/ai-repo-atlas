# memvid/canvas

⭐ 23 · TypeScript · 推送 2026-01-05 · [GitHub](https://github.com/memvid/canvas) · [官网](https://memvid.com) · 组织维护

**基于 Memvid 构建知识库搜索/聊天/仪表盘界面的 React UI 套件**

Canvas 是构建在 Memvid（视频化 AI 记忆格式）之上的知识库 UI 套件，以三个 npm 包提供：core（引擎、记忆客户端、LLM providers）、react（组件与模板）、server（Next.js 路由工具）。开发者将其嵌入 Next.js 应用，即可获得语义/词法/混合搜索、带来源引用的 RAG 聊天、记忆统计仪表盘与文件摄取（PDF/DOCX/XLSX 等），并生成 /api/canvas/* 系列端点。LLM 后端支持 OpenAI、Anthropic、Google，需配置 API key；通过 slots、hooks 与 CSS 变量定制。MIT 许可。

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

- 三个 npm 包：core 引擎 / React 组件 / Next.js 服务端工具
- 语义、词法与混合搜索；RAG 聊天附来源引用
- 摄取 PDF/DOCX/XLSX/PPTX/JSON 等文件到 Memvid 记忆
- 生成 /api/canvas/* API 端点；slots/hooks/CSS 变量定制

## 适用场景

- 在自己的 Next.js 应用里加上基于自有文档的搜索与聊天界面
- 搭建带仪表盘与文件上传的知识库前端
- 复用现成组件快速构建 Memvid 记忆的管理界面

## 场景标签

`RAG` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L3: **AI-powered Knowledge Base UI Kit** built on Memvid - the video-based memory format for AI.
> L5: Canvas provides drop-in React components and server utilities to build search, chat, and dashboard interfaces powere
> L11: |`@memvid/canvas-core`|Core engine, memory client, LLM providers|npm|

## 星数曲线

```mermaid
xychart-beta
    title "memvid/canvas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2d49cca8033e` · [字段定义](../../DATASET.md)*
