# bitgineer/artificial-analysis-skill

⭐ 3 · JavaScript · 推送 2026-10-21 · [GitHub](https://github.com/bitgineer/artificial-analysis-skill) · 个人维护

**Agent 技能与 CLI：按固定可审计尺度对比 LLM 基准、价格与速度**

以 SKILL.md 加 Node 脚本形式交付的技能与小型 CLI，从 ArtificialAnalysis.ai 抓取 LLM 模型数据，套用固定对比尺度后输出 JSON，由运行技能的 agent 生成报告。核心机制是指标注册表（声明单位与优劣方向）与用例画像（按相关指标平均排名排序）。无需 API key 与账户，仅依赖 Node.js 18+ 内置模块，仅向 artificialanalysis.ai 发起请求。数据来自抓取公开页面，页面可能变更；与 Artificial Analysis 无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 指标注册表声明单位与方向，形成单一可审计对比口径
- 按用例（软件开发、agent 自动化、科研、通用、QA）输出模型排名
- 无 API key、无账户、无第三方依赖，仅依赖 Node.js 内置模块
- 兼容 OpenCode 原生技能格式及其他 agent harness

## 适用场景

- 为 agent harness 选型时按固定尺度对比模型的基准、价格与速度
- 按软件开发或 agent 自动化等具体用例查看模型排名
- 获取带来源 URL 与采集时间的模型数据 JSON

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: An agent skill and small CLI that collect LLM model data from ArtificialAnalysis.ai, apply a fixed comparison scale,
> L9: Model comparisons drift: one report ranks by intelligence, the next by price, a third by whatever the model felt lik
> L71: Metrics cover intelligence, benchmarks, price, performance and capabilities. Each declares a direction, so lower pr


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `9dff3bec1c35` · [字段定义](../../DATASET.md)*
