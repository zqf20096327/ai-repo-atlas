# google-deepmind/loft

⭐ 239 · Python · Apache-2.0 · 推送 2026-04-13 · [GitHub](https://github.com/google-deepmind/loft) · 组织维护

**百万级 token 长上下文评测基准（35 数据集，4 模态）**

Google DeepMind 发布的 LOFT 长上下文基准，配套论文《Can Long-Context Language Models Subsume Retrieval, RAG, SQL, and More?》。覆盖 6 大任务类别（文本/视觉/音频检索、RAG、SQL、Many-Shot ICL），共 35 个数据集、4 种模态，支持 128k 等长度设置。提供数据下载脚本、Corpus-in-Context 提示示例、推理与评测代码；推理当前支持 VertexAI 上的 Gemini 模型，需 Google Cloud PROJECT_ID。多模态部分数据集需自行从原网站下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 大任务类别、35 个数据集、4 种模态（文本/图像/音频/视频）
- 提供 CiC 提示示例与按 task_type 输出多指标的评测代码
- LOFT-Hard 子集（MuSiQue/QAMPARI/QUEST）推荐用于迭代
- 推理支持 VertexAI 上的 Gemini（如 gemini-1.5-flash-002）

## 适用场景

- 评测长上下文模型在检索、RAG、SQL 等任务上的表现
- 获取第三方评测所需的提示文件（3P evaluation）
- 对比长上下文模型与检索系统的能力边界

## 场景标签

 · 领域:LLM 评测/长上下文

## 证据(README 行号)

> L3: This repository houses the resources for LOFT, the Long Context Frontiers benchmark, introduced in the research pape
> L4: LOFT consists of 6 long-context task categories spanning retrieval, multi-hop
> L5: compositional reasoning, and more, totaling 35 datasets and 4 modalities.

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/loft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 238 --> 240
    line [239, 239]
```

2026-10-18 239 → 2026-10-22 239（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `12e8941f7c5f` · [字段定义](../../DATASET.md)*
