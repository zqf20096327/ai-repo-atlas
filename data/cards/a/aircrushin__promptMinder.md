# aircrushin/promptMinder

⭐ 113 · JavaScript · 推送 2026-10-23 · [GitHub](https://github.com/aircrushin/promptMinder) · [官网](https://prompt-minder.com) · 个人维护 · 中文 README

**面向团队的提示词版本管理与协作平台**

基于 Next.js + Neon PostgreSQL + Clerk 的提示词管理平台：提供版本管理与回溯、类 Git diff 的版本对比、可配置的团队审批流（提交/审批/拒绝/撤回、评论与 @提及）、标签分类、公私有模式与社区贡献。集成 AI 模型做提示词智能生成与对话方法提炼，内置 Agent Skills 目录（浏览/同步/导出 ZIP），并提供 CLI 与版本评测功能（用例对比、规则断言、成本估算）。限制：需自行配置 Clerk、Neon 数据库等多项环境变量；评测依赖用户在 Playground 保存的服务商密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提示词版本管理、diff 对比与可配置团队审批流
- Agent Skills 专区：目录同步、浏览、导出 Skill ZIP、CLI 操作
- 版本评测：保存用例并以同一模型配置对比两个版本，支持规则断言与 JSON 导出
- 配套 CLI（npm 安装）与面向 Cursor/Claude Code 等 agent 的独立 CLI skill

## 适用场景

- 团队统一管理提示词版本并走审批流程后发布
- 把 AI 对话中的方法提炼成可复用的提示词
- 发现和复用公开 Agent Skills 并导入工作区
- 发布前用用例评测对比新旧两个提示词版本

## 场景标签

`提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L8: 一个专业的提示词管理平台，让 AI 提示词管理更简单、更高效
> L23: - ✅ **AI 智能生成** - 集成 AI 模型，智能生成优质提示词
> L376: 保存 1–5 个用例（输入、字符串变量和规则/人工标准），再以同一模型配置对比两个具体版本。

## 星数曲线

```mermaid
xychart-beta
    title "aircrushin/promptMinder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-28 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `77681a823103` · [字段定义](../../DATASET.md)*
