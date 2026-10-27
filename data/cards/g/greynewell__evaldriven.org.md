# greynewell/evaldriven.org

⭐ 30 · Nunjucks · CC0-1.0 · 推送 2026-06-22 · [GitHub](https://github.com/greynewell/evaldriven.org) · [官网](https://evaldriven.org) · 个人维护

**评测驱动开发方法论站点：先建评测再交付功能**

阐述 Eval-Driven Development 实践原则的文档型站点：主张每个概率性系统先定义正确性规格，为每个任务建立带阈值与依据的评测，在 CI 中随每次变更运行评测，用统计证明（样本量、置信区间、回归基线）替代单次通过测试，并将 token 开销与延迟纳入评测指标。内容为十条原则陈述，面向构建 AI 系统的工程与运维人员。仓库未提供可安装的代码、命令或数据集，仅为理念阐述。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 十条 Eval-Driven Development 原则文本
- 主张评测在 CI 中与 lint、类型检查、构建并列运行
- 将成本（token 开销、延迟、算力）定义为评测指标
- 要求评测定义、数据集、阈值与结果全部纳入版本控制

## 适用场景

- 为 AI 系统团队制定评测规范时参考原则清单
- 在设计概率性系统前建立正确性规格的检查思路
- 推动评测进入 CI/CD 流程时引用方法论依据

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: AI writes code. The engineer defines "working," measures it, enforces it. **Eval-Driven Development**: every probabi
> L21: ### 4. Evals run in CI

## 星数曲线

```mermaid
xychart-beta
    title "greynewell/evaldriven.org 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `94bba98b5911` · [字段定义](../../DATASET.md)*
