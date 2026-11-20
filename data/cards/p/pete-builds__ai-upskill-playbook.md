# pete-builds/ai-upskill-playbook

⭐ 10 · MIT · 推送 2026-11-13 · [GitHub](https://github.com/pete-builds/ai-upskill-playbook) · [官网](https://pete-builds.github.io/ai-upskill-playbook/) · 个人维护

**个人 AI 系统自学路线图：在自有硬件上构建与运维 AI 栈**

作者（系统管理员背景）记录八个月从 Claude 订阅加一台闲置 PC 到家庭服务器、自建 MCP 服务器、约六十个 agent 技能与 CI 门禁的学习路径，按月份分三阶段：Claude Code 基础与 homelab、agents/MCP/自托管 AI 栈、自动化测试部署监控。形式为路线图而非教程，每节含 'What bit me' 踩坑记录与可运行的 'Done when' 验收测试。明确不覆盖模型训练、ML 理论、微调与大规模生产 RAG。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按月分阶段的学习路线，每节附可运行的 Done when 验收测试
- Claude Code 工作流：plan mode、CLAUDE.md、context 管理、模型分层
- 按领域拆分的 agents/skills/subagents 设计与路由机制
- 自托管服务实操：Pi-hole DNS、Docker 容器安全规则、备份恢复验证

## 适用场景

- 想在自有硬件上从零搭建 AI 开发与运维环境的个人
- 学习 Claude Code 的 skills、subagents 与 MCP server 构建
- 为家庭服务器规划容器化服务与安全运维流程

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: **How I learned to build and run AI systems on my own hardware, in the order I would do it again.**
> L9: It is a map, not a tutorial. Each section says what to set up, why, and the mistake that taught me the lesson. Every
> L21: **Not covered:** model training, ML theory, fine-tuning, production RAG at scale. This is the integration and opera

## 星数曲线

```mermaid
xychart-beta
    title "pete-builds/ai-upskill-playbook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `a6fd4072a3e8` · [字段定义](../../DATASET.md)*
