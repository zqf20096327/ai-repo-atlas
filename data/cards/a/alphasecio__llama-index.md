# alphasecio/llama-index

⭐ 54 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/alphasecio/llama-index) · [官网](https://go.alphasec.io/llama-index) · 组织维护

**基于 LlamaIndex 的 Streamlit 示例应用集：PDF 问答与网页摘要**

alphasecio 维护的 LlamaIndex 示例应用集合，含两个 Streamlit 应用：chat-with-pdf 用 LlamaParse 解析 PDF、构建 VectorStoreIndex 后用 OpenAI 问答（需 OpenAI、LlamaCloud 密钥）；summarize-url 用 SimpleWebPageReader 抓取网页、构建 SummaryIndex 后用 Google Gemini 摘要（需 Google AI Studio 密钥）。API 密钥仅在浏览器会话中输入，不做服务端存储。支持 Railway 一键部署，或本地以 Python 3.12 虚拟环境逐应用运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- chat-with-pdf：LlamaParse 解析 + VectorStoreIndex + OpenAI 问答
- summarize-url：网页抓取 + SummaryIndex + Gemini 摘要
- API 密钥仅存于浏览器会话，无服务端存储
- Railway 一键部署模板

## 适用场景

- 学习 LlamaIndex 构建数据问答应用的写法
- 快速部署一个 PDF 对话或网页摘要演示
- 作为自建 RAG 应用的起点代码

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L19: A collection of Streamlit apps powered by LlamaIndex, the open-source framework for building LLM applications over 
> L23: |chat-with-pdf|Parse a PDF with LlamaParse, index it in a `VectorStoreIndex` and ask questions with OpenAI|OpenAI, 
> L24: |summarize-url|Fetch a web page with `SimpleWebPageReader`, build a `SummaryIndex` and summarize it with Google Gem

## 星数曲线

```mermaid
xychart-beta
    title "alphasecio/llama-index 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-26 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `4973d1ca9f57` · [字段定义](../../DATASET.md)*
