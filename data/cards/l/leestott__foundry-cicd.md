# leestott/foundry-cicd

⭐ 25 · MIT · 推送 2026-05-22 · [GitHub](https://github.com/leestott/foundry-cicd) · 个人维护

**给企业开发团队：Microsoft Foundry AI agent 的 CI/CD 参考流水线**

面向在 Microsoft Foundry 上构建 AI agent 的团队，提供两套平行的参考流水线（GitHub Actions 与 Azure DevOps）：实现构建验证、基于评估数据集的质量门禁、以及 Dev→Test/QA→Production 的带审批晋级。CI 阶段包含 ruff 静态检查、bandit 安全扫描、agent.yaml 配置校验、pytest 测试与评估结果发布；CD 阶段包含 Dev 冒烟测试、Test 场景与安全评估、生产环境审批门禁与部署后冒烟。凭证通过 secrets/变量组引用，仓库为参考实现而非可直接安装的产品。

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

- GitHub Actions 与 Azure DevOps 两套平行流水线实现同一生命周期
- 基于评估数据集的质量门禁与结果制品发布
- Dev/Test/Production 带环境审批的受控晋级
- ruff/bandit/pytest 静态检查、安全扫描与测试集成

## 适用场景

- 为 Microsoft Foundry 上的 AI agent 搭建 CI/CD 流水线
- 在 agent 晋级生产前执行评估质量门禁
- 参照双平台流水线配置企业级 LLMOps 流程

## 场景标签

`模型评测` `MLOps` · 领域:评测与运维

## 证据(README 行号)

> L5: Reference pipelines for building, validating, evaluating, and promoting AI agent versions across Dev, Test, and Prod
> L31: 2. Evaluation quality gates

## 星数曲线

```mermaid
xychart-beta
    title "leestott/foundry-cicd 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ec3477667b0c` · [字段定义](../../DATASET.md)*
