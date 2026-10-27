# BodaFu/auto-rednote

⭐ 37 · TypeScript · MIT · 推送 2026-03-10 · [GitHub](https://github.com/BodaFu/auto-rednote) · [官网](https://github.com/BodaFu/auto-rednote) · 个人维护 · 中文 README

**OpenClaw 插件：给 AI Agent 提供小红书网页端 28 个操作工具**

以 TypeScript 编写的 OpenClaw 扩展插件，向 AI Agent 暴露 xhs_* 系列共 28 个工具，覆盖账号查询、内容搜索浏览、评论点赞收藏关注、通知处理与图文视频发布；另含仅限 macOS 的桌面私信回复与桌面 Feed 工具（分别经 peekaboo CLI 与 Ghost OS 操作小红书 App）。机制上复用 OpenClaw 管理的已登录 Chrome 会话，通过 Playwright 与页面 __INITIAL_STATE__ 提取数据，无需 API Key 与逆向工程。安装需 git clone 至 OpenClaw extensions 目录并 npm install，要求 Node.js ≥ 22 与 OpenClaw Gateway 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 28 个 xhs_* 工具覆盖内容、互动、通知、发布全域操作
- 复用 OpenClaw 已登录 Chrome 会话，无需 API Key 与逆向工程
- 通知处理状态用 node:sqlite 持久化到本地数据库
- macOS 桌面 IM/Feed 工具通过 peekaboo 与 Ghost OS 操作小红书 App GUI

## 适用场景

- 让 Agent 自动检查并回复小红书新评论
- 自动回复小红书私信（需 macOS 桌面 App）
- 按关键词搜索笔记并批量点赞、收藏或关注作者
- 通过 Agent 定时发布图文或视频笔记

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: 复用你已登录的 Chrome（通过 OpenClaw browser control），让 AI Agent 获得完整的小红书网页端操作能力——无需独立浏览器进程，无需 API Key，无需逆向工程。
> L13:   → xhs_* 工具调用

## 星数曲线

```mermaid
xychart-beta
    title "BodaFu/auto-rednote 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3bcdf76a1f67` · [字段定义](../../DATASET.md)*
