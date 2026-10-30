# liu673/skill-studio

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-05-07 · [GitHub](https://github.com/liu673/skill-studio) · [官网](https://github.com/liu673/skill-studio/releases) · 个人维护 · 中文 README

**管理 AI Agent 技能资产的本地优先桌面工具**

基于 Tauri（Rust 后端 + React 前端）的桌面应用，面向使用 AI Agent 的开发者和团队：把散落的本地 Skill 文件（skill.md 及相关文件）整合为可追踪的资产，提供创建、导入（本地目录/Git 仓库/市场/模板）、快照版本化、版本差异对比与回滚、生效版本设定，以及向 45+ 种 Agent 平台目录的同步（目录复制或符号链接）。内置团队空间的提交、评审、合并与拉取流程。默认纯本地存储于 ~/.skill-studio/，仅市场浏览和 Git 导入产生网络请求，不自动执行导入的 Skill。当前为 v0.1.0 未签名预览版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 快照式版本管理：创建、对比差异、回滚、设定生效版本
- 内置 45+ 种 Agent 平台的目录识别规则并支持自定义平台
- 团队空间提供 Skill 库提交、差异评审、合并与拉取流程
- 默认纯本地存储，不依赖云服务，不自动执行导入的 Skill

## 适用场景

- 把我散落在各平台目录的 Skill 文件统一管理和版本化
- 为不同项目编排 Skill 集合并同步到对应 Agent 平台目录
- 团队协作维护 Skill 库，通过评审和合并发布稳定版本

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L14: Skill Studio 是一个本地优先的桌面端 Skill 资产管理工具，用于创建、导入、组织、版本化、对比和同步 AI Agent 技能。它把个人 Skill 工作区、版本快照、外部市场、平台目录、项目空间和团队交付流程整合到
> L16: 支持的平台包括 Cursor、Claude Code、Codex、Windsurf、Roo Code 等 45+ 种 Agent 平台。

## 星数曲线

```mermaid
xychart-beta
    title "liu673/skill-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `9e9d6b337002` · [字段定义](../../DATASET.md)*
