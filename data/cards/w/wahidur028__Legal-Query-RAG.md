# wahidur028/Legal-Query-RAG

⭐ 14 · Python · 推送 2026-09-01 · [GitHub](https://github.com/wahidur028/Legal-Query-RAG) · [官网](https://doi.org/10.1109/ACCESS.2025.3542125) · 组织维护

**法律问答 RAG 研究代码：混合检索加评测引导的迭代精炼**

IEEE Access 2025 论文 Legal Query RAG 的研究代码仓库：对法律 PDF 建索引，用 BM25 加稠密检索做混合搜索，经重排序后由 Groq 托管的 LLaMA 模型生成回答，再由 TruLens 评测 agent 度量上下文相关性、接地性与答案相关性；未达标时反馈给提示工程 agent 改写查询并迭代。以 Gradio 本地界面运行，需 Groq 与 OpenAI API key。仓库明言为研究原型而非法律建议，且不含 LICENSE 文件，不提供论文全部结果的一键复现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- BM25+稠密检索的混合搜索与交叉编码器重排序
- TruLens 评测 agent 驱动的迭代查询精炼回路
- Gradio 本地 UI：上传 PDF、索引、问答与评测展示
- 未达标回答默认扣留，禁用无接地回退

## 适用场景

- 在本地对法律 PDF 做带评测与溯源的问答实验
- 研究评测引导查询精炼的 RAG 流程
- 复现论文中描述的原型流程并检查其证据边界

## 场景标签

`RAG` `文档问答` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: LQ-RAG explicitly incorporates an agent-based iterative refinement mechanism during inference. It first generates an
> L43: 5. Retrieve candidate passages through hybrid search: BM25 supplies lexical matches and dense passage retrieval sup
> L154: python app.py

## 星数曲线

```mermaid
xychart-beta
    title "wahidur028/Legal-Query-RAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `56ebf05f5a1d` · [字段定义](../../DATASET.md)*
