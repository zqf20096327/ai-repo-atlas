# Youhai020616/xiaohongshu

⭐ 31 · Python · MIT · 推送 2026-09-12 · [GitHub](https://github.com/Youhai020616/xiaohongshu) · 个人维护 · 中文 README

**面向 AI Agent 的小红书命令行工具：搜索、发布、互动与数据分析**

以 Python CLI（xhs 命令）驱动小红书网页端，覆盖关键词搜索、图文/视频发布、点赞收藏评论、创作者数据看板导出与通知读取。采用 MCP 服务（Go 二进制）+ CDP（Chrome DevTools Protocol）双引擎自动切换。几乎所有命令支持 --json-output 输出统一 JSON 信封，stdout 只含数据、进度走 stderr，附 SCHEMA.md 与 SKILL.md 供 AI Agent 作为技能调用；另可用 FastAPI 以 REST API 暴露全部能力。通过 pip、源码或 Docker 安装，需 Python≥3.10，CDP 功能需本地 Chrome。项目自述处于 Alpha 阶段，自动化操作存在账号风控风险。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MCP + CDP 双引擎自动切换，MCP 不可用时回退 Chrome 自动化
- --json-output 统一 JSON 信封，成功与失败结构一致，供 Agent 解析
- 短索引机制：xhs search → xhs read 1 → xhs like 1，无需复制 ID
- REST API（FastAPI）以 HTTP 暴露搜索、发布、互动等全部能力

## 适用场景

- 让 AI Agent 通过命令行操作小红书账号进行搜索与发布
- 批量搜索并导出小红书内容为 CSV/JSON 做分析
- 创作者导出后台数据看板与互动通知

## 场景标签

`网页抓取` `工作流自动化` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L67: - 🤖 **Agent 友好** — `--json-output` 成功与失败都输出统一信封；stdout 只有数据，进度走 stderr
> L131: ## 面向 AI Agent 的结构化输出
> L240: - SKILL.md — 作为 AI Agent Skill 使用

## 星数曲线

```mermaid
xychart-beta
    title "Youhai020616/xiaohongshu 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-26 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ca2cf15988b6` · [字段定义](../../DATASET.md)*
