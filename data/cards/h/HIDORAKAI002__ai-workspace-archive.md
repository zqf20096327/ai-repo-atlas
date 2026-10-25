# HIDORAKAI002/ai-workspace-archive

⭐ 37 · 推送 2026-10-24 · [GitHub](https://github.com/HIDORAKAI002/ai-workspace-archive) · 个人维护

**本地离线 AI 工具归档仓库：聚合技能、MCP、规则与提示词**

一个由机器人每 6 小时自动同步、聚合上游开源仓库的本地归档：收录 29,746 个带 YAML frontmatter 的技能/提示词文件（20 个子域、23 个来源仓库）、23 个 MCP server 仓库（11 类）、3,348 条 IDE 规则、系统提示词集合、12 家 API provider、15 个可本地 Docker 运行的无代码平台与 1,400+ 公共 API 目录。面向已使用 Claude、Cursor、Copilot 等工具的开发者：离线浏览目录、复制技能文件作为系统提示词、按说明安装 MCP server 或本地运行 n8n 等平台。本体是内容归档而非软件产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 29,746 个结构化技能文件，20 个子域分类、23 个来源仓库
- 23 个 MCP server 仓库（含官方 SDK、浏览器自动化、数据库、云平台等 11 类）
- VPS 机器人每 6 小时检查上游并同步，GitHub Actions 每日备份
- 技能文件可直接粘贴为 Claude/Cursor/Copilot 的系统提示词

## 适用场景

- 离线浏览和挑选 AI 技能提示词，装进日常使用的编辑器或助手
- 查找并本地安装 MCP server 接入 Claude Desktop 或 Cursor
- 获取 Cursor/Cline 等 IDE 规则文件复制到自己的项目
- 本地 Docker 运行收录的无代码自动化平台（如 n8n）

## 场景标签

`提示工程` `精选清单` · 领域:Agent 开发

## 证据(README 行号)

> L12: > **Stop collecting tabs.** 29,746 skill files. 3,348 IDE rules. 23 MCP servers. 8 system-prompt collections. 12 AP
> L61: > **`/ai_skills_library/`** -- 29,746 structured YAML-frontmatted skill files, deep-categorized across 20 sub-domai
> L209: > **`/mcps/`** -- 23 fully cloned Model Context Protocol server repositories across 11 categories -- all installab

## 星数曲线

```mermaid
xychart-beta
    title "HIDORAKAI002/ai-workspace-archive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `087d2922012b` · [字段定义](../../DATASET.md)*
