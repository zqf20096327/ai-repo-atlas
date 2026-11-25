# marcusquinn/aidevops

⭐ 471 · Shell · MIT · 推送 2026-11-24 · [GitHub](https://github.com/marcusquinn/aidevops) · [官网](https://www.aidevops.sh) · 个人维护

**OpenCode 插件式 AI DevOps 框架：从意图到可验证交付的 agent 自动化**

以 OpenCode 插件形式分发的 AI DevOps 框架，内含 17 个主 agent、2,250+ 子 agent、2,210+ 辅助脚本与 111 个斜杠命令，覆盖软件交付、基础设施、业务、营销、内容与研究等领域的任务编排。关键机制包括按需加载的上下文、模型路由（simple/standard/thinking 三档）、Pulse 每 2 分钟调度无头 worker、密钥不出聊天与 Git 的安全约束、以及带证据门控的 Git 工作流。经 Homebrew 或 npm 全局安装，依赖 OpenCode 运行时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 个主 agent 与 2,250+ 可单独寻址的子 agent、111 个斜杠命令
- Pulse 调度器每 2 分钟派发无头 worker，处理 auto-dispatch 标签的 issue
- provider-neutral 的 simple/standard/thinking 三档模型路由
- 密钥与受保护数据隔离于聊天与 Git 之外，含 prompt-injection 防御

## 适用场景

- 让 AI agent 自主完成从规划到 PR 的完整软件交付流程
- 7×24 无人值守地调度 worker 处理仓库任务与例行工作
- 为团队提供统一的 agent 操作规范与证据留存机制
- 集中管理服务凭据与安全审计

## 场景标签

`模型网关` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **aidevops.sh** is an OpenCode
> L12: Instead of treating every job as an isolated chat, aidevops gives people and AI
> L170: - **Routing:** provider-neutral `simple`, `standard`, and `thinking` workload tiers

## 星数曲线

```mermaid
xychart-beta
    title "marcusquinn/aidevops 星数(近 21 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-28", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 415 --> 476
    line [420, 422, 421, 422, 423, 425, 434, 435, 421, 441, 445, 451, 452, 454, 455, 456, 467, 468, 469, 470, 471]
```

2026-10-23 420 → 2026-11-25 471（+51）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `691662d12db3` · [字段定义](../../DATASET.md)*
