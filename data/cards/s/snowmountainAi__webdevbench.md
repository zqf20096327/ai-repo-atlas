# snowmountainAi/webdevbench

⭐ 15 · TypeScript · 推送 2026-05-07 · [GitHub](https://github.com/snowmountainAi/webdevbench) · [官网](https://webdevbench.com) · 组织维护

**评测 AI 应用生成平台的基准：按软件代理角色打分**

面向 vibe coding 平台（用自然语言生成全栈应用的系统）的评测基准：将平台视为端到端软件代理，从 PM（需求理解）、Engineering（代码质量/架构）、Ops（部署/可靠性）三个角色维度评估。覆盖应用创建（ACR）与应用修改（AMR）两种交互模式、T4/T5 复杂度层级，采用 68 项指标（25 主指标+43 诊断指标）分 7 组，并嵌入 80 条金丝雀需求用于区分真实推理与模板匹配。README 报告了对 6 个平台、3 个领域的初步研究结论，未给出安装运行方式。

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

- PM/Engineering/Ops 三角色的软件代理评测框架
- 68 项指标（25 主指标+43 诊断指标）分 7 组
- 80 条金丝雀需求区分真实推理与模式匹配
- 首次区分应用创建（ACR）与应用修改（AMR）评测

## 适用场景

- 对比评测 AI 应用生成平台的工程与生产能力
- 研究 AI 生成代码在安全性与迭代修改上的表现
- 作为应用级软件工程评测的研究数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: SWE-WebDev-Bench is a benchmark designed to evaluate vibe coding platforms - systems that generate full-stack applic
> L45: |Dimension|Description|
> L53: - 25 Primary Metrics (what was built)

## 星数曲线

```mermaid
xychart-beta
    title "snowmountainAi/webdevbench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2e9a808ca140` · [字段定义](../../DATASET.md)*
