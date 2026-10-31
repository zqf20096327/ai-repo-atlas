# The-AgenticFlow/openflows

⭐ 44 · Rust · MIT · 推送 2026-10-30 · [GitHub](https://github.com/The-AgenticFlow/openflows) · [官网](https://openflows.dev) · 组织维护

**在自托管 Coder 上运行的自治 AI 开发团队：GitHub issue 转合并 PR**

部署在自托管 Coder 环境中的多 agent 软件开发系统：NEXUS 编排、FORGE 写代码、SENTINEL 对抗式评审、VESSEL 合并 PR、LORE 记录文档，将 GitHub issue 处理为经评审的合并 PR。通过门控规划审批、类型化 SharedStore 状态契约、reconcile() 失败恢复与 Coder RBAC 多租户隔离运行；工作区内不暴露 LLM key。一条 setup.sh 脚本完成 Coder、Redis、GitHub App 与模型配置；技能/MCP/模型可通过 registry.json 注册扩展。当前 v1.2.x，声称已可端到端交付合并 PR。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五 agent 流水线：issue → 规划门 → 实现 → 对抗评审 → 合并 PR
- reconcile() 失败恢复：孤儿/过期 worker 检测、退避重试、未合并 PR 续跑
- 基于 Coder RBAC 与 Redis keyspace 前缀的多租户隔离
- 技能/MCP/模型可插拔注册，SKILL.md 目录即加技能

## 适用场景

- 把 GitHub issue 自动变成经过评审的合并 PR
- 在企业现有工程流程中引入受治理、可审计的 AI 交付
- 在自托管环境中隔离运行 AI 编码 agent 而不暴露 LLM key

## 场景标签

`编码 Agent` `代码审查` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L6: **OpenFlows is an autonomous AI software team that turns GitHub issues into reviewed, production-ready pull requests
> L29: You create a GitHub issue → NEXUS picks it up → FORGE writes code → SENTINEL reviews adversarially
> L35: OpenFlows also enforces a **gated planning checkpoint** — FORGE writes a plan and halts until SENTINEL reviews and 

## 星数曲线

```mermaid
xychart-beta
    title "The-AgenticFlow/openflows 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-31 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fbf5714d3203` · [字段定义](../../DATASET.md)*
