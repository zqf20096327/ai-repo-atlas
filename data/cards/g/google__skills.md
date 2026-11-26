# google/skills

⭐ 24,678 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/google/skills) · 组织维护

**为 AI agent 提供 Google 产品与技术的技能集合**

Google 官方维护的 Agent Skills 仓库，收录覆盖 Google Cloud 全线的技能条目，按入门、AI/ML、基础设施、数据库、开发者工具、安全等十余个类别组织。通过 skills.sh 的 npx 命令安装到目标 agent，可选择具体技能、目标 agent 与安装范围（项目级或全局），并支持更新与移除过期技能。另捆绑面向 Claude Code、Codex、Antigravity CLI 等 agent harness 的插件（Skills + MCP server）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.5 天,年发版 0,7 位贡献者
- 涨星:近 1 天 **+27**(自 20261016 起算)
- 安装:npm 包 `skills` 月下载 23,786,800
- 平台:— · 协议:MCP

## 能力要点

- 按 10+ 类别组织的大量 Google Cloud/产品技能条目
- npx skills add 支持按技能、agent、安装范围（项目/全局）选择安装
- npx skills update 支持更新并移除过期技能
- 捆绑 Skills + MCP server 形式的产品插件，适配多种 agent harness

## 适用场景

- 让编码 agent 具备操作 Google Cloud（GKE、BigQuery、IAM 等）的领域知识
- 为 agent 安装 Google Ads、Analytics 等 API 的使用技能
- 在 Claude Code/Codex 等 harness 中以插件形式接入 Google 技能与 MCP server

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: This repository contains Agent Skills for Google
> L11: npx skills add google/skills
> L277: This repo also bundles Google product plugins (Skills + MCP servers) for agent harnesses.

## 星数曲线

```mermaid
xychart-beta
    title "google/skills 星数(近 27 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 21173 --> 24996
    line [21491, 21522, 21541, 21566, 21594, 21617, 21638, 21677, 21699, 21721, 21764, 21541, 23683, 23924, 24053, 24125, 24242, 24328, 24368, 24393, 24432, 24453, 24479, 24516, 24548, 24587, 24678]
```

2026-10-23 21,491 → 2026-11-26 24,678（+3,187）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a8971eecbd73` · [字段定义](../../DATASET.md)*
