# griver/Q-RAG

⭐ 66 · Jupyter Notebook · 推送 2026-09-04 · [GitHub](https://github.com/griver/Q-RAG) · 组织维护

**ICLR 2026 论文官方库：RL 训练嵌入器实现多步检索的 RAG 方法**

Q-RAG 论文的训练与评测代码：在文本块嵌入的潜空间中用价值型强化学习（时序差分）训练轻量嵌入器 agent 完成多步检索，保持 LLM 冻结、不做 LLM 微调。覆盖 BabiLong、RULER、HotpotQA、Musique 基准的复现流程，使用 Contriever/E5/GTE 嵌入模型与 Qwen 系列作为阅读 LLM，全部训练在单张 A100-80GB 上 12 小时内完成。以 Python 仓库形式提供，需 Python 3.12 与 CUDA GPU，Linux 环境推荐。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 价值型 RL（时序差分）在嵌入潜空间训练多步检索 agent，LLM 保持冻结
- 覆盖 BabiLong/RULER/HotpotQA/Musique 四个基准的训练与评测脚本
- 单张 A100-80GB、12 小时内完成每个模型的训练
- 支持 Contriever、E5、GTE 三类嵌入模型，评测阅读用 QwQ-32B/Qwen3-4B

## 适用场景

- 复现论文中长上下文多步检索的实验结果
- 在自有多跳问答数据上训练轻量检索器
- 研究潜空间强化学习训练嵌入器的方法

## 场景标签

`RAG` `强化学习` · 领域:知识与检索

## 证据(README 行号)

> L11: **Q-RAG** is a resource-efficient method for **multi-step retrieval** trained with reinforcement learning directly 
> L13: Q-RAG achieves **state-of-the-art results** on long-context benchmarks (**BabiLong**, **RULER**) for contexts up to

## 星数曲线

```mermaid
xychart-beta
    title "griver/Q-RAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-26 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4b03053f5196` · [字段定义](../../DATASET.md)*
