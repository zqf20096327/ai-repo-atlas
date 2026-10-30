# SteveTANTAN/HydraRAG

⭐ 56 · Python · Apache-2.0 · 推送 2025-11-12 · [GitHub](https://github.com/SteveTANTAN/HydraRAG) · [官网](https://stevetantan.github.io/HydraRAG/) · 组织维护 · 中文 README

**EMNLP 2025 论文系统：跨知识图谱/维基文档/网页检索增强 LLM 推理问答**

EMNLP 2025 主会论文 HydraRAG 的官方实现：将 Freebase/Wikidata 结构化知识图谱、Wikipedia 文档检索与 SerpAPI 在线搜索统一进迭代扩展的推理流程，让 LLM 基于多源证据生成 KGQA 问答预测。支持 GPT-3.5/GPT-4/Llama-3.1-8B/70B/DeepSeek-v3 作为后端，可在 CWQ、AdvHotpotQA、QALD10-en、SimpleQA 等 7 个基准上运行与评测。运行前需本地部署 Freebase 与 Wikidata，并自备 LLM API 与 SerpAPI key，以源码方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 KG、Wikipedia 文档与在线搜索三类证据源的推理框架
- 支持 gpt3/gpt4/llama/llama70b/deepseek 五种 LLM 后端
- 覆盖 CWQ、AdvHotpotQA、QALD10-en、SimpleQA 等 7 个基准数据集
- 提供子图加载、消融开关（--no-freebase/--no-web 等）与准确率评测脚本

## 适用场景

- 在 KGQA 基准上复现论文实验与消融研究
- 研究不完整知识图谱与多源证据对 LLM 推理的影响
- 作为跨源 RAG 推理方法的参考实现

## 场景标签

`知识图谱` `RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L101: |`--model {gpt3,gpt4,llama,deepseek,llama70b}`|LLM backend.<be> `gpt3` = GPT-3.5-Turbo, `gpt4` = GPT-4-Turbo, `lla

## 星数曲线

```mermaid
xychart-beta
    title "SteveTANTAN/HydraRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-30 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `d0e64f480df0` · [字段定义](../../DATASET.md)*
