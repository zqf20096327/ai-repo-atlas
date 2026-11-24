# OpenLAIR/PremiseCheck

⭐ 6 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/OpenLAIR/PremiseCheck) · [官网](https://openlair.github.io/premisecheck/) · 组织维护

**为审稿意见做事实核查评分的研究工具**

PremiseCheck 是一个对同行评审意见（人类或 AI 生成）进行事实核查打分的 Python 包与 CLI：先将评论分解为显式前提，路由后由小型决策模型（默认 Kev-27B，开源权重自托管）逐条对照论文验证，取最低前提概率作为评论得分；分解器与整体基线走任意 OpenAI 兼容端点，只有决策模型读取论文文本。配套 ReviewFact 基准（NLP/机器学习/自然科学三部分，专家标注），提供 eval 命令输出 AUROC、成本与延迟，支持 JSONL 缓存续跑。基准仅限评估用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分解-路由-验证-聚合流水线，仅决策模型读取论文全文
- 默认决策模型 Kev-27B 开源权重，可自托管于本地 GPU；Jev 走 OpenRouter 端点
- ReviewFact 基准：三个数据源共 9,267 条专家标注评论
- CLI 与 Python API 均支持结果缓存、断点续跑，输出每条评论的成本与延迟

## 适用场景

- 审稿流程中筛查可能含事实错误的评审意见
- 在 ReviewFact 上复现论文中各设置的 AUROC 与成本指标
- 对自己收集的评论-论文数据批量打事实错误分

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L26: **TL;DR.** PremiseCheck scores how likely a peer-review comment contains a factual error about the paper it reviews
> L27: An LLM rewrites the comment as explicit premises without reading the paper. A small decision model then checks each
> L42: 1. **Decompose.** An LLM (GPT-5.5 in the paper) reads only the comment and lists the premises it relies on.

## 星数曲线

```mermaid
xychart-beta
    title "OpenLAIR/PremiseCheck 星数(近 3 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-11-24"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-10-22 5 → 2026-11-24 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `43ccb94b8fff` · [字段定义](../../DATASET.md)*
