# glincker/claude-code-marketplace

⭐ 37 · Shell · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/glincker/claude-code-marketplace) · [官网](https://www.glincker.com/) · 组织维护

**面向 Claude Code 的社区技能/Agent 市场，覆盖开发全流程**

社区维护的 Claude Code 插件市场：以 SKILL.md 格式提供 23+ 个专用 agent/技能，覆盖代码审查（5 个并行 agent：安全/性能/测试/架构/风格）、YAML 工作流编排、自然语言数据库查询（PostgreSQL/MySQL/MongoDB/SQLite/Redis）、代码迁移与 100+ API 集成；通过 Claude Code 的 /plugin marketplace 与 /plugin install 命令安装，另提供 7 个 slash 命令。技能会在本机执行代码，README 提示安装前审查源码与权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个并行 agent 的多 agent 代码审查系统
- YAML 配置的技能编排框架（条件逻辑与并行执行）
- 自然语言查询 5 种数据库并生成优化与索引建议
- 自然语言接口接入 100+ API（OAuth/JWT 认证处理）

## 适用场景

- 用多 agent 审查 PR 的安全、性能与测试覆盖
- 通过 YAML 串联技能构建自动化流水线
- 用自然语言查询数据库或调用第三方 API
- 自动化代码迁移并生成风险评级与测试

## 场景标签

`多智能体` `代码审查` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **Community-Driven Agent Marketplace** - A comprehensive collection of specialized agents, automation workflows, a
> L62: /plugin marketplace add https://github.com/GLINCKER/claude-code-marketplace
> L203: ├── SKILL.md           # Required: Skill definition with YAML frontmatter

## 星数曲线

```mermaid
xychart-beta
    title "glincker/claude-code-marketplace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ce8a81647b88` · [字段定义](../../DATASET.md)*
