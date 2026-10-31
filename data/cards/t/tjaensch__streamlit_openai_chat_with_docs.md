# tjaensch/streamlit_openai_chat_with_docs

⭐ 13 · Python · 推送 2026-04-11 · [GitHub](https://github.com/tjaensch/streamlit_openai_chat_with_docs) · 个人维护

**已弃用的 Streamlit 文档问答 POC：上传文本与 OpenAI 模型对话**

基于 Streamlit 的实验性概念验证应用：用户上传文本文件，文件被分块后用 LangChain OpenAIEmbeddings 嵌入并暂存于 Chroma 向量库，随后可就文件内容提问，由 OpenAI gpt-4o-mini 模型生成回答。需自备 OpenAI API key，API 调用按 token 计费，界面显示 token 用量与嵌入成本估算。README 明确声明该应用已弃用、不再维护且不可运行，且提示结果可能不准确。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 上传文件分块、嵌入并暂存 Chroma 向量库
- gpt-4o-mini 模型基于文件内容生成回答
- 界面显示 token 用量与嵌入成本估算

## 适用场景

- （已弃用，不可用）曾用于与自备文本文档进行问答
- 作为 Streamlit + LangChain + Chroma 的 POC 参考结构

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L6: The application is using OpenAI's gpt-4o-mini model to answer questions about the content of one or more files that 
> L7: The user can then ask questions about the content of the data and the application will return an answer. You will ne

## 星数曲线

```mermaid
xychart-beta
    title "tjaensch/streamlit_openai_chat_with_docs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ff24779ff806` · [字段定义](../../DATASET.md)*
