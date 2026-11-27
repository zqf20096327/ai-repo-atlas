# axoviq-ai/synthadoc

⭐ 2,001 · Python · AGPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/axoviq-ai/synthadoc) · [官网](https://axoviq.com/resources/synthadoc) · 组织维护

**面向个人与企业的本地知识编译引擎，将文档编译为可审计的 Markdown wiki**

Synthadoc 读取 PDF、表格、PPT、网页、音视频等源文档，用 LLM 在摄取阶段将其合成为持久化的结构化 wiki：自动建立交叉引用、检测矛盾、标记孤页，每条声明附 ^[file:L-L] 行级引用。提供 CLI、REST API、12 工具 MCP 服务器、Obsidian 插件与 Web UI 四类接口；内置不可变 audit.db 审计日志、成本软警告/硬门槛、三层缓存、五态页面生命周期，以及九种需人工确认的会话式维护工作流。输出为纯本地 Markdown，兼容 OKF。AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 摄取时编译知识而非查询时检索，矛盾检测与五态页面生命周期
- 每条声明带 ^[file:L-L] 行级引用，Obsidian Source Viewer 可核验
- audit.db 审计日志、成本阈值硬门槛、三层缓存控制重复摄取开销
- REST API、MCP 服务器、Docker 镜像与本地 Ollama/Gemini 等多后端

## 适用场景

- 为个人或团队把散落的 PDF/网页/会议记录编译成可检索的本地知识库
- 合规敏感场景下在本地维护带审计与成本上限的知识平台
- 按部门部署多端口 wiki 并跨库联合查询
- 长期积累文档时自动发现矛盾、孤页与过期页面并修复

## 场景标签

`知识库管理` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L33: Synthadoc reads your raw source documents — PDFs, spreadsheets, PPTs, web pages, images, videos, Word files, TXTs, 
> L98: Most knowledge-management tools retrieve and summarize at query time. Synthadoc inverts this: it **compiles knowled

## 星数曲线

```mermaid
xychart-beta
    title "axoviq-ai/synthadoc 星数(近 24 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 1521 --> 2079
    line [1567, 1568, 1574, 1577, 1578, 1615, 1650, 1688, 1725, 1567, 1957, 1997, 2018, 2031, 2030, 2031, 2032, 2033, 2002, 1999, 2001, 2003, 2002, 2001]
```

2026-10-25 1,567 → 2026-11-27 2,001（+434）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `90cba12017ba` · [字段定义](../../DATASET.md)*
