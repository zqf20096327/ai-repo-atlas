# microsoft/fabric-task-flows

⭐ 50 · Python · MIT · 推送 2026-05-22 · [GitHub](https://github.com/microsoft/fabric-task-flows) · 组织维护

**用 AI agent 生成 Microsoft Fabric 解决方案的 Task Flow 仓库**

微软开源的 Microsoft Fabric 解决方案生成框架：通过 @fabric-advisor agent（依托 GitHub Copilot agent 模式）引导用户经历 Discover→Design→Test→Sign-Off→Deploy→Validate→Document 七个阶段，将业务问题描述转化为架构决策记录、测试计划与 CI/CD 就绪的部署脚本，产出一份项目简报和一个部署目录。内置 13 个预定义 Task Flow、7 个决策指南、45 种 Fabric 项类型注册表及模板，并提供可选的 Copilot hooks 做策略校验与审计日志。需 Python 3.11+ 与 GitHub Copilot agent 模式。

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

- 七阶段自动化管线（含 Sign-Off 与 Deploy 人工确认点，最多 3 轮修订）
- 产出 CI/CD 就绪的依赖排序部署脚本与单一项目简报
- 内置 13 个 Task Flow、7 个决策指南、45 种 Fabric 项类型注册表
- 可选 Copilot hooks 提供策略拦截与运行时审计日志

## 适用场景

- 不会 Fabric 的团队用自然语言描述业务问题并得到可部署方案
- 架构师复用预验证模式而非从零搭建
- 新接触 Fabric 的用户按引导式流程完成端到端交付

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L15: With the `@fabric-advisor` agent, you describe the problem. After a few prompts, the whole solution is mapped, ever
> L83: .github/agents/         → The @fabric-advisor orchestrator

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/fabric-task-flows 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-25 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4ab0794b3184` · [字段定义](../../DATASET.md)*
