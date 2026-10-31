# machinelearningZH/document-research-tool

⭐ 13 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/machinelearningZH/document-research-tool) · 组织维护

**面向文档集合的混合检索+LLM 研究工具，供领域专家检索与起草答案**

基于 Python Shiny 的 Web 应用：对文档集合做词法+语义混合检索，按 chunk 检索但以完整文档作为 LLM 上下文，用户可勾选提交给 LLM 的文档并切换 OpenRouter 上数百个商用/开源模型。自带数百份瑞士州议会记录开放数据开箱可用，通过 notebook 预处理自有数据并建 Weaviate 索引。定位为辅助领域专家搜索与答案起草的快速原型模板，强调用户控制与本地自托管；安装走 git clone + uv，需配置 OpenRouter API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 词法+语义混合检索，chunk 检索、整文档生成
- 用户自选提交给 LLM 的文档，检索与生成分离
- 经 OpenRouter 切换数百个商用/开源模型
- 支持 mps/cuda/cpu 嵌入平台与本地自托管部署

## 适用场景

- 在大量混合来源的政府或行政文档中做智能检索
- 让领域专家挑选来源后由 LLM 协助起草答案
- 对保密文档做本地自托管的 RAG 原型验证

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L19: - **Hybrid search**: Combines lexical and semantic search.
> L20: - **Retrieve with chunks, generate with documents**: Finds relevant documents via chunks but lets you chat with who
> L66: - LLMs make mistakes, so we focus on **assistive systems that help domain experts with search and answer drafting**

## 星数曲线

```mermaid
xychart-beta
    title "machinelearningZH/document-research-tool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `22d5445de549` · [字段定义](../../DATASET.md)*
