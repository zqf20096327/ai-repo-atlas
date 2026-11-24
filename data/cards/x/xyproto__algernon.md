# xyproto/algernon

⭐ 3,028 · JavaScript · BSD-3-Clause · 推送 2026-11-22 · [GitHub](https://github.com/xyproto/algernon) · [官网](https://algernon.roboticoverlords.org) · 个人维护

**给开发者的自包含 Go Web 服务器：内置 Lua/模板渲染与 LLM 内容生成**

单个可执行文件的 Go Web 服务器，内置 HTTP/2、HTTP/3 (QUIC)、Lua/Teal 脚本处理、Markdown/Pongo2/Amber 模板渲染、Sass/GCSS 样式处理、npm-less React 19/JSX/TSX 转译，以及 Redis、内置 BoltDB、PostgreSQL、SQLite、MariaDB/MySQL、MSSQL 多种数据库后端。支持用户权限、限流、插件（JSON-RPC）、自动刷新预览和 REPL。其中 LLM 相关功能为 index.prompt 文件：指定内容类型、Ollama 模型与提示词后生成内容。默认 Redis，无 Redis 时回退到内置 Bolt，无需配置即可启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件自包含可执行，无外部依赖，覆盖 Linux/macOS/64 位 Windows
- 内置 Lua/Teal 脚本、Markdown/Pongo2/Amber 渲染、JSX/TSX 转译等多种文件类型处理
- 支持 HTTP/2 与 HTTP/3 (QUIC)、限流、插件、用户权限系统
- index.prompt 文件可通过 Ollama 模型生成页面内容

## 适用场景

- 零配置快速搭建 Lua 脚本驱动的动态网站
- 本地预览 Markdown 文件与静态页面开发（auto-refresh）
- 无需 npm 构建 React/JSX/TypeScript 前端页面
- 轻量环境下（如树莓派）运行带数据库后端的 Web 服务

## 场景标签

 · 领域:Web 开发/基础设施

## 证据(README 行号)

> L9: Web server with built-in support for HTTP/2, HTTP/3 (QUIC), Lua, Teal, Markdown, Pongo2, HyperApp, Amber, Sass(SCSS)
> L73:  * index.prompt is a content-type, an Ollama model, a blank line and a prompt, for generating content with LLMs.

## 星数曲线

```mermaid
xychart-beta
    title "xyproto/algernon 星数(近 8 点)"
    x-axis ["2026-10-22", "2026-10-28", "2026-11-06", "2026-11-08", "2026-11-13", "2026-11-15", "2026-11-20", "2026-11-24"]
    y-axis "stars" 3027 --> 3033
    line [3031, 3032, 3031, 3032, 3031, 3030, 3028, 3028]
```

2026-10-22 3,031 → 2026-11-24 3,028（-3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `1435c20745bd` · [字段定义](../../DATASET.md)*
