# cisco-ai-defense/adversarial-hubness-detector

⭐ 19 · Python · NOASSERTION · 推送 2026-03-17 · [GitHub](https://github.com/cisco-ai-defense/adversarial-hubness-detector) · [官网](https://blogs.cisco.com/ai/your-models-memory-has-been-compromised-adversarial-hubness-in-rag-systems) · 组织维护

**检测 RAG/向量库中对抗性枢纽文档的安全扫描器**

Cisco AI Defense 维护的开源安全扫描器，审计向量索引与嵌入，识别以异常高频率出现在多样化查询 top-k 结果中的对抗性枢纽（adversarial hubs），用于发现操纵检索、注入内容的恶意文档。提供全局、概念感知、模态感知三种检测模式，支持 FAISS/Pinecone/Qdrant/Weaviate 四种向量库的统一接口，客户端 BM25/TF-IDF 融合实现任意数据库上的混合检索，并通过插件系统扩展自定义检索、重排与检测器。以 CLI（ahd scan）与 Python SDK 两种形式提供，输出 JSON 与 HTML 报告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 median/MAD z-score 的统计异常检测，区分恶意枢纽与正常热门内容
- 全局/概念感知/模态感知三种检测模式
- FAISS、Pinecone、Qdrant、Weaviate 统一接口，客户端 BM25/TF-IDF 混合检索适配任意向量库
- 插件系统支持自定义检索、重排与检测器，输出 JSON/HTML 报告

## 适用场景

- 审计 RAG 系统向量库中是否存在操纵检索结果的恶意文档
- 多模态图像-文本检索系统做跨模态枢纽检测
- 安全团队生成 JSON/HTML 格式的检测报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L6: Adversarial Hubness Detector is an open-source security scanner that audits vector indices and embeddings to detect 
> L55: - **Vector Database Support**: FAISS, Pinecone, Qdrant, Weaviate with unified interface

## 星数曲线

```mermaid
xychart-beta
    title "cisco-ai-defense/adversarial-hubness-detector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `cbad346e315e` · [字段定义](../../DATASET.md)*
