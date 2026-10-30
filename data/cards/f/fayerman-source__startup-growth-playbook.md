# fayerman-source/startup-growth-playbook

⭐ 30 · MIT · 推送 2026-10-08 · [GitHub](https://github.com/fayerman-source/startup-growth-playbook) · 个人维护

**给 LLM agent 的创业增长策略手册：按产品阶段自动生成营销计划**

以 Markdown 文档形式提供的一套分发策略手册：克隆到任意项目目录后，由 LLM agent 读取 AGENT.md 协议，扫描代码库识别产品与受众，按产品阶段从 10 种分发策略中选取适配项（通常 2-3 个，PMF 前可能更少或为零），生成含任务与指标的 plan.md，并产出推文、SEO 页面、外联文案等营销产物。涉及应用代码改动的下一步转为实施交接文档而非由 agent 直接修改。策略 1-7 与 9-10 摘自 Greg Isenberg 等公开材料，并声明与原作者无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 种分发策略（MCP Servers、程序化 SEO、AEO、病毒式产物等）
- AGENT.md 自举协议：agent 从代码库自动发现产品阶段并选策略
- 产出限定在 marketing/ 目录，应用代码改动转为实施交接
- 策略内容注明来源（Greg Isenberg、Caleb Dean 公开材料）

## 适用场景

- 让 Claude Code 等 agent 基于我的代码库自动生成营销计划
- 独立开发者按产品阶段挑选获客策略
- 批量生成社媒内容与 SEO 页面草稿

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L33: |`AGENT.md`|Self-bootstrapping protocol. The agent reads this first|
> L34: |`playbook.md`|10 distribution strategies with implementation steps and agent tasks|

## 星数曲线

```mermaid
xychart-beta
    title "fayerman-source/startup-growth-playbook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4b06712a337a` · [字段定义](../../DATASET.md)*
