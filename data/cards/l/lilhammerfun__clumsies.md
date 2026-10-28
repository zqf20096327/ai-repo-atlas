# lilhammerfun/clumsies

⭐ 19 · Rust · MIT · 推送 2026-10-14 · [GitHub](https://github.com/lilhammerfun/clumsies) · [官网](https://clumsies.ai/) · 组织维护 · 中文 README

**团队共享 AI 编码记忆的管理平台：为 agent 提供经审核的 Markdown 指引**

面向使用编码 agent 的团队：组织维护已发布的 Memory（架构决策、项目约束、流程），各 Project 绑定本地仓库并选用 Memory；agent 工作时检索相关指引，用户要求时可提出变更草稿，须经组织所有者/管理员审核后发布，检索不会自动改写 Memory。提供 macOS 原生应用（DMG 安装、Apple Silicon M1+、macOS 14+），含记忆增长与检索活动的面板；Windows/Linux 走 CLI 流程，桌面开发已暂停并移出活动代码树。集成 Codex App、Claude Code、opencode、DeepSeek Harness、Google Antigravity，首次使用会下载检索模型；可自部署 Rust Server + PostgreSQL + OIDC。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 组织级 Memory 发布与人工审核（Draft→Review→Publish）流程
- macOS 面板展示记忆增长、检索活动与覆盖情况
- 集成 Codex/Claude Code/opencode/DeepSeek Harness/Google Antigravity 五种 agent 宿主
- 支持自部署 Rust Server + PostgreSQL + 自有 OIDC 身份提供方

## 适用场景

- 团队沉淀架构决策与编码规范供 agent 检索
- 为多个项目绑定不同的组织级记忆
- 对 agent 提出的记忆变更做人工审核后发布

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L12: Clumsies helps teams maintain shared Markdown guidance for coding agents: architecture decisions, project constrain
> L58: Clumsies includes integrations for the macOS Codex App, Claude Code, opencode, DeepSeek Harness (`dsh`), and Google

## 星数曲线

```mermaid
xychart-beta
    title "lilhammerfun/clumsies 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a2f39aa50124` · [字段定义](../../DATASET.md)*
