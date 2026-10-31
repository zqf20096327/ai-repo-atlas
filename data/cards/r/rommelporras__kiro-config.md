# rommelporras/kiro-config

⭐ 14 · Shell · MIT · 推送 2026-04-24 · [GitHub](https://github.com/rommelporras/kiro-config) · [官网](https://rommelporras.com) · 个人维护

**Kiro CLI 的多 agent 编排配置：orchestrator+专家模式与安全钩子**

为 Kiro CLI 提供的个人配置仓库：采用 orchestrator-and-specialists 模式，devops-orchestrator 作为默认 agent 负责规划、对话、协调与 git 操作，并将代码编写等工作委派给 9 个专家 agent（Python/TypeScript/shell/前端/Terraform 等）。含 12 份 steering 文档、20 个技能、11 个 hooks，以及自我学习知识管道（纠正自动捕获、关键词追踪、规则自动晋升）。三层安全设计：hooks、deniedPaths、deniedCommands；基础设施命令只读，禁止执行变更类操作。通过 git clone 后运行 setup.sh 符号链接到 ~/.kiro/ 完成安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- orchestrator + 9 专家 agent 的委派式多 agent 架构
- 11 个 hooks：密钥扫描、敏感文件保护、破坏性命令拦截、纠正检测等
- 自我学习管道：纠正自动捕获→episode 记录→规则自动晋升
- 三层安全与基础设施只读策略（Terraform/kubectl/AWS CLI 等仅允许只读命令）

## 适用场景

- 为 Kiro CLI 搭建多 agent 协作的 DevOps 开发环境
- 团队按 3 步在约 5 分钟内完成成员入职配置
- 以钩子与命令黑名单约束 agent 的危险操作

## 场景标签

`多智能体` `提示工程` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: Personal Kiro CLI configuration with multi-agent orchestrator, multi-domain steering (Python, TypeScript, shell, inf
> L8: User ↔ devops-orchestrator (plans, converses, coordinates, git ops)

## 星数曲线

```mermaid
xychart-beta
    title "rommelporras/kiro-config 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `49a885f56032` · [字段定义](../../DATASET.md)*
