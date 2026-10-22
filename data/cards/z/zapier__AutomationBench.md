# zapier/AutomationBench

⭐ 352 · Python · NOASSERTION · 推送 2026-08-04 · [GitHub](https://github.com/zapier/AutomationBench) · [官网](https://zapier.com/benchmarks) · 组织维护

**评估 AI agent 完成真实业务流程能力的基准**

由 Zapier 维护的评测基准：在覆盖 CRM、日历、收件箱等 47 个模拟 SaaS 工具的仿真业务环境中，检验 AI agent 能否将销售、营销、运营、客服、财务、HR 六大领域（各 100 个任务）的业务流程执行到正确状态。任务全部可程序化验证，按断言式评分规则给出 partial_credit 与严格通过率两个指标；另有 200 个简单域任务不计分。官方榜单基于未公开的私有任务集，本地分数仅方向性一致。通过 git clone 源码加 CLI 运行，也可在 Prime Intellect 托管环境执行，附带网页版结果可视化器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 大业务领域 ×100 任务，跨 47 个模拟 SaaS 工具的仿真环境验证
- 全部任务可程序化验证，按断言 rubric 对比最终状态与期望状态
- partial_credit（密集奖励信号）与 task_completed_correctly（严格通过）双指标
- 附带可比较多轮运行的网页可视化器

## 适用场景

- 我需要评测各家模型在真实业务流程自动化上的通过率
- 我想在 RL 训练中使用 partial_credit 作为环境奖励信号
- 我想对比不同模型或不同 reasoning effort 的评测结果

## 场景标签

 · 领域:AI 评测/基准测试

## 证据(README 行号)

> L3: A benchmark for evaluating AI agents on realistic business workflows.
> L13: AutomationBench evaluates how well AI models complete realistic business workflows—the kind of tasks that happen da

## 星数曲线

```mermaid
xychart-beta
    title "zapier/AutomationBench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 340 --> 343
    line [341, 342, 342]
```

2026-10-18 341 → 2026-10-21 342（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d2246e212e96` · [字段定义](../../DATASET.md)*
