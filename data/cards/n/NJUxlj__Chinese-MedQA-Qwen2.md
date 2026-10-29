# NJUxlj/Chinese-MedQA-Qwen2

⭐ 90 · Python · 推送 2026-04-29 · [GitHub](https://github.com/NJUxlj/Chinese-MedQA-Qwen2) · 个人维护 · 中文 README

**Qwen2 后训练全流水线的医疗问答系统，含 RAG 与多 Agent 会诊**

以 Qwen2/Qwen3 为基座的医疗问答完整流水线项目：覆盖训练数据生成、SFT 微调（HuggingFace Trainer）、手写 DPOTrainer 的 DPO 训练、基于 VeRL 框架的 PPO/GRPO/TRPO 等强化学习，再经 vLLM 部署推理。模型通过 API 接入 embedder+Reranker 的 RAG 系统（Milvus/FAISS/Neo4j 知识库、BM25 与向量混合检索），并实现基于 MDAgents 论文的多专科智能体会诊系统。提供 FastAPI+Gradio 服务、多种评估器（BLEU/ROUGE/医疗 QA/数学/代码）与 YAML 配置入口。限制：面向中文医疗问答的垂直场景，需自备模型权重与数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SFT/DPO/DAPO/GSPO/TRPO/PPO/GRPO 多种微调算法，含手写 DPOTrainer
- vLLM、XInference、Ollama、Transformers 多种推理后端
- 混合检索 RAG：相似度、BM25、L2 距离、KNN，支持 Milvus+FAISS+Neo4j
- 基于 MDAgents 的多专科医疗多 Agent 会诊系统

## 适用场景

- 微调并部署一个西医疾病诊疗的垂直 Qwen 模型
- 为医疗问答系统叠加知识库检索（RAG）能力
- 构建多专科 AI 会诊问诊流程

## 场景标签

`RAG` `多智能体` `微调` `强化学习` · 领域:Agent 开发

## 证据(README 行号)

> L10: 本项目是一个基于 **Qwen2 + Agent + RAG** 的医疗问答系统，旨在打通从 SFT/Embedding 训练数据生成，到 SFT 微调、奖励模型微调，再到 DPO/DAPO/GSPO/TRPO 强化学习微调，最终
> L12: 最终目标：基于上述后训练方式，微调出一个使用西医知识进行疾病诊疗的垂直 Qwen2 模型。
> L20: - 🤖 **Multi-Agent 会诊**：基于 MDAgents 的多专科医疗会诊系统

## 星数曲线

```mermaid
xychart-beta
    title "NJUxlj/Chinese-MedQA-Qwen2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 89 --> 91
    line [90, 90]
```

2026-10-18 90 → 2026-10-29 90（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d1a195848fb2` · [字段定义](../../DATASET.md)*
