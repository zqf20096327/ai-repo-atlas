# google/skills

⭐ 21,396 · Python · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/google/skills) · 组织维护

**为 AI agent 提供谷歌产品与技术的技能集合**

谷歌官方维护的 Agent Skills 仓库，收录面向 Google 产品与技术（含 Google Cloud）的技能，按 Google Cloud 入门、AI/ML、基础设施、数据库与分析、开发者工具、安全与身份、广告等类别组织，覆盖 GKE、BigQuery、Agent Platform、Cloud Run、SecOps 等产品。通过 skills.sh 的 npx 命令安装，可选择具体技能与作用范围；另为 Claude Code、Codex、Antigravity CLI 等 agent harness 提供包含 MCP server 的插件包。

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

## 动量与使用信号

- 维护:`active` — 距上次 push 1.5 天,年发版 0,7 位贡献者
- 涨星:近 1 天 **+27**(自 20261016 起算)
- 安装:npm 包 `skills` 月下载 23,786,800
- 平台:— · 协议:MCP

## 能力要点

- 按 12+ 类别组织的 Agent Skills 清单（AI/ML、基础设施、数据库、安全等）
- 通过 npx skills add 安装，支持选择性安装与项目/全局作用域
- 提供 skills update 命令更新并移除过时技能
- 为 Claude Code、Codex、Antigravity CLI 打包产品插件（Skills + MCP servers）

## 适用场景

- 让 AI agent 获取操作 Google Cloud 资源的领域技能
- 为 Claude Code 等工具安装谷歌产品插件
- 按类别查找 GKE、BigQuery、SecOps 等产品的使用指南技能

## 场景标签

`精选清单` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: This repository contains Agent Skills for Google
> L11: npx skills add google/skills
> L223: This repo also bundles Google product plugins (Skills + MCP servers) for agent harnesses.

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `b4580fdd6842` · [字段定义](../../DATASET.md)*
