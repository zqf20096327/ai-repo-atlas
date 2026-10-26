# QiYao-Wang/AutoPatent

⭐ 220 · JavaScript · 推送 2026-01-04 · [GitHub](https://github.com/QiYao-Wang/AutoPatent) · [官网](https://autopatent.wangqiyao.me/) · 组织维护 · 中文 README

**多智能体框架：从草稿自动生成完整专利文档（附 D2P 基准）**

论文配套仓库（JCIP 2026 / arXiv:2412.09796），提出 Draft2Patent 任务与 D2P 基准：基于初始草稿生成平均 17K token 的完整专利。框架 AutoPatent 使用 LLM 驱动的 planner、writer 与 examiner 三类 agent，结合 PGTree 与 RRAG 生成专利文档；评测含 BLEU/ROUGE、自提出的 IRR 指标与三位专利专家盲评。目前数据与代码声明将在论文录用后发布，仓库内已放出 10 个生成样例（example 目录）与演示视频。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- planner/writer/examiner 多智能体结合 PGTree 与 RRAG 生成完整专利
- 提出 Draft2Patent 任务与 D2P 基准
- 提出 IRR（逆重复率）评测指标
- 仓库已发布 10 个生成专利样例与演示视频

## 适用场景

- 从技术草稿自动生成长篇专利文档
- 评估 LLM 在专利生成任务上的表现（D2P 基准）
- 复现论文中的零样本/少样本/微调对比实验

## 场景标签

`多智能体` `模型评测` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L55: We introduce a novel and practical task known as **Draft2Patent**, along with its corresponding **D2P benchmark**, 
> L57: We propose a multi-agent framework called **AutoPatent** which leverages the LLM-based planner agent, writer agents

## 星数曲线

```mermaid
xychart-beta
    title "QiYao-Wang/AutoPatent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 218 --> 221
    line [219, 220, 220]
```

2026-10-18 219 → 2026-10-26 220（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `05c5834a92fe` · [字段定义](../../DATASET.md)*
