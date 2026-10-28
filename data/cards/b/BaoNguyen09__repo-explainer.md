# BaoNguyen09/repo-explainer

⭐ 22 · TypeScript · MIT · 推送 2026-08-03 · [GitHub](https://github.com/BaoNguyen09/repo-explainer) · [官网](http://repex.thienbao.dev) · 个人维护

**输入 GitHub 仓库 URL 即生成 AI 解读与追问聊天的应用**

面向开发者的 AI 应用：粘贴 GitHub 仓库链接后，由 AI 代理自主选择并并行读取仓库文件，生成概览、架构图、目录树与技术栈说明，并支持针对该仓库的流式追问聊天（含 normal/caveman 两种风格）。支持通过环境变量在 Claude 与 Gemini 间切换提供商，可用 MODEL 覆盖默认模型。后端为 FastAPI+Postgres，前端为 Vite，提供 Docker Compose 一键部署；概述每次现生成、后端不缓存，历史存于浏览器 localStorage，对超大仓库返回明确错误。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 代理自主选文件并并行抓取，输出概览/架构图/目录树/技术栈
- 单一环境变量 AI_PROVIDER 切换 Claude 与 Gemini
- SSE 流式状态更新与 WebSocket 仓库追问聊天
- Docker Compose 一键运行前后端与 Postgres

## 适用场景

- 快速了解陌生仓库的整体架构与技术栈
- 就具体文件与实现细节向 AI 追问某个仓库
- 脚本调用一次性 JSON 接口获取仓库解读

## 场景标签

`文档问答` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: An AI app that explains GitHub repositories through agentic file exploration.
> L8: - **AI-powered summaries** -- Paste a GitHub repo URL and get an overview, architecture diagram, directory tree, and
> L9: - **Multiple AI providers** -- Switch between Claude (Anthropic) and Gemini (Google) with a single env var (`AI_PROV

## 星数曲线

```mermaid
xychart-beta
    title "BaoNguyen09/repo-explainer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ed41aa93820a` · [字段定义](../../DATASET.md)*
