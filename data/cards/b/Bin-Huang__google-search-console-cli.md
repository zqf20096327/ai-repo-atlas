# Bin-Huang/google-search-console-cli

⭐ 24 · TypeScript · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/Bin-Huang/google-search-console-cli) · 个人维护

**面向 AI agent 的 Google Search Console 命令行工具与技能包**

封装 Google Search Console 官方 API 的 CLI：支持按查询、页面、国家、设备等维度检索搜索分析数据，检查 URL 索引状态，列出/添加/删除站点，管理（列出/查询/提交/删除）站点地图。基于 googleapis Node.js 客户端，处理服务账号认证与请求签名，所有命令输出结构化 JSON 到 stdout 供 agent 直接解析。可通过 npm 全局安装，或以 skills/plugin 形式安装到 Claude Code、Cursor、Codex 等 agent 环境。需自备 Google Cloud 服务账号或 OAuth 凭据，写操作需 Full 权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Search Console API v1 与 Webmasters API v3（query/sites/sitemaps/inspect 等）
- 所有命令输出结构化 JSON，供 agent 免处理解析
- 提供 AI agent skills 安装方式（npx skills add / Claude Code 插件市场）
- 支持服务账号与应用默认凭据（ADC）两种认证路径

## 适用场景

- 让 Claude Code/Cursor/Codex 等 agent 直接查询站点搜索表现与索引状态
- SEO 分析：按查询词、页面、国家、设备维度拉取搜索数据
- 通过脚本或 agent 管理站点地图的提交与删除

## 场景标签

 · 领域:SEO/开发者工具

## 证据(README 行号)

> L3: Google Search Console CLI & Skills for AI agents (and humans). Analyze search performance by query, page, country, a
> L5: **Works with:** OpenClaw, Claude Code, Cursor, Codex, and any agent that can run shell commands.
> L40: Built on Google's official APIs. Handles service account authentication and request signing. Every command outputs 

## 星数曲线

```mermaid
xychart-beta
    title "Bin-Huang/google-search-console-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a20c1c10629f` · [字段定义](../../DATASET.md)*
