# Xnurta/Xnurta-MCP

⭐ 14 · 推送 2026-10-27 · [GitHub](https://github.com/Xnurta/Xnurta-MCP) · 组织维护

**将 Xnurta 亚马逊广告能力接入 AI 助手的 MCP 服务器**

面向亚马逊广告卖家的 MCP 服务器：授权后可在 Claude Code、ChatGPT 等 MCP 兼容客户端中用自然语言查询广告绩效数据（ACOS/ROAS/TACOS 等）、结合自有成本利润计算真实盈利、创建 SP 广告活动、编辑线上广告实体（预算/竞价/否定投放）、管理 AI 托管组，并提供 6 个可选分析 Skill（周报/月报/结构分析/搜索词诊断等）。写操作直接作用于线上账户，需显式确认；不支持 SB/SD 活动创建。安装通过插件市场或 Skills 目录上传完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言查询广告绩效、实体配置与操作日志
- 8 个必需 Skill + 6 个可选分析 Skill 的分层设计
- 写操作采用两阶段确认并要求回读结果
- 支持 OAuth 与 MCP Token 两种授权方式

## 适用场景

- 在 Claude Code 或 ChatGPT 中用自然语言查询亚马逊广告数据并生成周报
- 让 AI 结合自有利润数据判断哪些广告活动亏损
- 通过对话创建 SP 广告活动或修改预算与竞价

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: Bring Xnurta's advertising capabilities into your own AI agent (Claude, ChatGPT, and more) and make your data part o
> L30: Xnurta MCP works with any MCP-compatible AI assistant. Recommended and fully tested:
> L41: 1. **Choose an authorization method and connect MCP** — Xnurta MCP supports both OAuth and MCP Token; choose based 

## 星数曲线

```mermaid
xychart-beta
    title "Xnurta/Xnurta-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5b231fe47897` · [字段定义](../../DATASET.md)*
