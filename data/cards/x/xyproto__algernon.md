# xyproto/algernon

⭐ 3,028 · JavaScript · BSD-3-Clause · 推送 2026-11-25 · [GitHub](https://github.com/xyproto/algernon) · [官网](https://algernon.roboticoverlords.org) · 个人维护

**自包含纯 Go Web 服务器：Lua/Markdown/HTTP2/3 与多数据库内置支持**

用 Go 编写的单可执行文件 Web 服务器，内置 HTTP/2、HTTP/3 (QUIC)、Lua/Teal 脚本处理、Markdown、Pongo2/Amber 模板、Sass/GCSS、JSX/TSX 转译（npm-less React 19），并支持 BoltDB（内置）、Redis、Valkey、PostgreSQL、SQLite、MariaDB、MySQL、MSSQL 作为数据库后端。特色机制包括 index.* 特殊文件名约定、auto-refresh 实时预览、用户权限系统、限流、插件（JSON-RPC）与 Ollama LLM 内容生成（.prompt 文件）。无外部依赖，可通过 go install、brew、pacman、Docker 或预编译包安装。

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

- 单可执行文件，无外部依赖，支持 Linux/macOS/64 位 Windows
- 内置 Lua/Teal 脚本处理与 index.* 文件名约定，修改后可自动刷新页面
- 支持多种数据库后端：内置 BoltDB、Redis、PostgreSQL、SQLite、MariaDB/MySQL 等
- .prompt 文件可指定 Ollama 模型与提示词以生成页面内容

## 适用场景

- 本地快速预览 Markdown/网页并实时刷新
- 用 Lua 脚本作为 HTTP handler 搭建小型动态站点
- 无需配置数据库主机即可启动（内置 BoltDB）
- 通过 .prompt 文件让 LLM 生成页面内容

## 场景标签

 · 领域:Web 开发/服务器基础设施

## 证据(README 行号)

> L9: Web server with built-in support for HTTP/2, HTTP/3 (QUIC), Lua, Teal, Markdown, Pongo2, HyperApp, Amber, Sass(SCSS)
> L73:  * index.prompt is a content-type, an Ollama model, a blank line and a prompt, for generating content with LLMs.
> L172: The idea is that web pages can be written in Markdown, Pongo2, Amber, HTML or JSX (+React or HyperApp), depending 

## 星数曲线

```mermaid
xychart-beta
    title "xyproto/algernon 星数(近 8 点)"
    x-axis ["2026-10-24", "2026-10-28", "2026-11-06", "2026-11-08", "2026-11-13", "2026-11-15", "2026-11-20", "2026-11-26"]
    y-axis "stars" 3027 --> 3033
    line [3031, 3032, 3031, 3032, 3031, 3030, 3028, 3028]
```

2026-10-24 3,031 → 2026-11-26 3,028（-3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `72ecd68bd4da` · [字段定义](../../DATASET.md)*
