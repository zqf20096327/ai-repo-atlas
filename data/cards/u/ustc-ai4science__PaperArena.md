# ustc-ai4science/PaperArena

⭐ — · [GitHub]() · 组织维护

**科学文献工具增强 agent 的评测基准与平台**

面向科学文献场景的 LLM agent 评测基准：任务要求 agent 跨多篇论文整合多模态信息（文本/图表/公式），并调用解析、检索、计算等工具生成有依据的回答。配套 PaperArena-Hub 模块化评测平台，支持单 agent 与多 agent 系统，由 LLM Judge 对照 Ph.D. 专家基线评分。数据集经 Hugging Face / Google Drive 发布。实验显示最强 agent 平均准确率仅 38.78%。安装走 Conda 环境 + 下载数据集 + 运行评估脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨论文多步推理与多模态理解评测（文本/图表/公式/表格）
- 提供多模态解析、上下文检索、程序化计算工具环境
- PaperArena-Hub 支持单 agent 与多 agent 系统评测
- QA 对经半自动校验（问题混淆/答案标准化/人工审查）构建

## 适用场景

- 评测自研 LLM agent 在科学文献任务上的工具调用与推理能力
- 研究 agent 多步规划与工具使用效率
- 作为科学发现 agent 的标准化评测平台

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L20: Existing benchmarks inadequately test LLM agents on realistic scientific tasks. We introduce **PaperArena**, a new 
> L56: - **On the right**, the **PaperArena-Hub platform** serves as a modular framework for agent evaluation. It features
> L60: This guide provides step-by-step instructions to set up the environment, download the necessary datasets, and run t

## 星数曲线

```mermaid
xychart-beta
    title "ustc-ai4science/PaperArena 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `c980bf269ae3` · [字段定义](../../DATASET.md)*
