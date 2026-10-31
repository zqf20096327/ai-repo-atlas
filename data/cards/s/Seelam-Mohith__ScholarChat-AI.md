# Seelam-Mohith/ScholarChat-AI

⭐ 14 · Python · 推送 2026-09-25 · [GitHub](https://github.com/Seelam-Mohith/ScholarChat-AI) · [官网](https://scholarchat-ai.streamlit.app) · 个人维护

**学生上传课程大纲 PDF，用文字或语音提问获得基于文档的回答**

面向学生的 RAG 学术问答应用：上传课程大纲 PDF 后，经 PyPDFLoader 提取文本、递归分块、Gemini 嵌入向量化存入内存向量库，检索相关片段后由 Gemini 2.5 Flash 生成回答；语音输入使用浏览器 Web Speech API 转文字。以 Streamlit 应用形式提供，需配置 GOOGLE_API_KEY，支持部署到 Streamlit Community Cloud，向量存储与会话缓存在内存中，重启后不保留。多文档支持、测验生成等列为未来功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 流水线：PyPDFLoader 提取→分块→Gemini 嵌入→内存向量库检索→Gemini 2.5 Flash 生成
- 支持文字与语音提问（Web Speech API 语音转文字）
- 会话级缓存与临时文件自动清理
- 提供 Streamlit Community Cloud 部署步骤

## 适用场景

- 上传课程大纲 PDF 后查询作业、考试与评分要求
- 通过语音免手操作向文档提问
- 在浏览器中本地或云端运行个人课程问答工具

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: ScholarChat AI is an AI-powered academic assistant that helps students interact with syllabus documents using natura
> L5: The application uses Retrieval-Augmented Generation (RAG) with Google's Gemini models to retrieve relevant informati

## 星数曲线

```mermaid
xychart-beta
    title "Seelam-Mohith/ScholarChat-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3bb475e89598` · [字段定义](../../DATASET.md)*
