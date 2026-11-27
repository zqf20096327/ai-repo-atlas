# egehank1/deepscholar

⭐ 17 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/egehank1/deepscholar) · [官网](https://www.egehankilic.com/) · 个人维护

**本地 RAG 问答系统：对研究论文提问并给出可核查引用**

基于 FastAPI 后端与 Next.js 前端的自托管论文问答系统：上传 PDF 后经 PyMuPDF 抽取文本、分块嵌入存入 pgvector，回答采用检索受限生成——每句带 [N] 标记，后处理剔除未引用句并从标记重建引用列表。检索管线含向量+关键词混合搜索（RRF 融合）、BM25 重排、逐论文检索与覆盖率检查；另提供论文对比、知识图谱（方法/数据集/任务节点）与回答质量指标（检索精度、引用正确性、忠实度）记录。默认配合 Ollama 本地运行，无 OCR，无鉴权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每句回答附 [N] 引用标记，未引用句在后处理中被剔除
- 混合检索：向量+关键词 RRF 融合后 BM25 重排，多论文问题逐论文检索
- 知识图谱展示论文、方法、数据集、任务及类型化边
- 内置三项启发式质量指标并按问题记录日志

## 适用场景

- 向自己上传的一批研究论文提问并获得可核查出处的回答
- 对比多篇论文的方法、数据集与局限
- 通过知识图谱发现共享基准的论文
- 本地环境处理 PDF，数据不出机器

## 场景标签

`RAG` `科研工具` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L11: Ask questions about a pile of research papers and get answers you can actually check. Every sentence points back to
> L27: So the rule for DeepScholar is simple: the model only gets to say what's in the retrieved passages, with a `[N]` ma
> L93: 1. **Hybrid search.** Vector search misses exact names (a dataset, a metric); keyword search misses paraphrases. Bo


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `2c158661fd9b` · [字段定义](../../DATASET.md)*
