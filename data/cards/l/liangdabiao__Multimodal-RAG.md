# liangdabiao/Multimodal-RAG

⭐ 41 · Python · 推送 2026-05-12 · [GitHub](https://github.com/liangdabiao/Multimodal-RAG) · [官网](https://skillhub.cn/skills/user_8bb4b4f5/glm53-flash-pdf-rag) · 个人维护 · 中文 README

**面向 PDF 的多模态 RAG 问答系统：整页转图检索并生成回答**

上传 PDF 后以自然语言提问的应用：不做文本提取与 OCR，用 PyMuPDF 将页面渲染为图片，经云端多模态 Embedding（Cohere embed-v4.0 或 DashScope）编码后写入 Zilliz Serverless 向量库，检索命中页面再做 ±2 页扩展，交由 DashScope Qwen 或 OpenRouter 视觉大模型生成回答。Embedding 与 LLM 引擎均可独立切换，全部计算走云端 API，无需本地 GPU。提供 Flask Web 界面（7860 端口）与独立问答 API 服务（7861 端口）。限制：依赖 DashScope/Cohere/OpenRouter API Key 与 Zilliz Cloud 账号，本地离线仅作为扩展方向提及。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 不做 OCR，PDF 整页作为图片做多模态 Embedding，保留表格/图表/手写批注等视觉信息
- Embedding（Cohere/DashScope）与 LLM（DashScope/OpenRouter）双引擎可独立切换
- 检索命中页 ±2 页扩展，自动去重与边界检查
- Flask Web 服务 + 独立 API 问答服务双入口，可同时运行

## 适用场景

- 对扫描件、图文混排或含公式表格的 PDF 做问答
- 国内网络环境下全用 DashScope（一个 Key 同时跑 Embedding 与视觉理解）
- 通过独立 API（7861 端口）将 PDF 问答能力接入外部程序

## 场景标签

`文档问答` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L3: 基于多模态 Embedding + Zilliz + Qwen 视觉理解的多模态 RAG 系统。支持 **Cohere / DashScope Embedding** 和 **DashScope / OpenRouter LLM**
> L5: 与传统 RAG 不同，本系统**不做文本提取和 OCR**，而是直接将 PDF 页面当作图片处理，通过视觉 Embedding 模型编码，完整保留表格、图表、排版、手写批注等所有视觉信息。
> L59: |POST|`/api/search`|检索相关页面并生成回答|`{"question": "...", "doc_name": "xxx.pdf"}`|

## 星数曲线

```mermaid
xychart-beta
    title "liangdabiao/Multimodal-RAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5b20bd92e00a` · [字段定义](../../DATASET.md)*
