# DeepShah1406/College_RAG_Chatbot

⭐ 14 · Python · MIT · 推送 2025-12-18 · [GitHub](https://github.com/DeepShah1406/College_RAG_Chatbot) · 个人维护

**面向高校知识库的 RAG 聊天机器人，基于院校文档回答提问**

面向高校场景的 RAG 对话应用：将院校 PDF 文档切块、生成 HuggingFace 嵌入并存入 Chroma 向量库，检索相关片段后由 Groq（llama-3.3-70b-versatile）LLM 生成回答，README 注明生产部署应换用其他可信 LLM 提供商。支持多轮对话记忆、聊天历史浏览、PDF 导出、敏感话题处理，提供 Streamlit 界面与 FastAPI REST 端点双形态。使用前需替换代码中的院校名占位符并配置 Groq API key；Tesseract OCR 为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PDF 文档向量化入库（2000 字符块/500 重叠）后检索生成回答
- Streamlit UI 与 FastAPI REST /chat 端点双接口
- 多轮对话记忆与聊天历史 PDF 导出
- 新增文档可增量入库且不丢失已有数据

## 适用场景

- 搭建基于本校手册等文档的学生咨询问答
- 通过 REST API 将问答能力接入已有系统
- 导出对话记录用于留档

## 场景标签

`聊天机器人` `RAG` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: A production-ready **Retrieval-Augmented Generation (RAG) chatbot solution** designed to provide accurate, context-a
> L75: 6. **Generation**: LLM generates response using retrieved context + prompt

## 星数曲线

```mermaid
xychart-beta
    title "DeepShah1406/College_RAG_Chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c9d2aa5dfeca` · [字段定义](../../DATASET.md)*
