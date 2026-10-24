# Debapriya-source/nyaya-gpt

⭐ 83 · Python · 推送 2026-03-25 · [GitHub](https://github.com/Debapriya-source/nyaya-gpt) · [官网](https://nyaya-gpt.streamlit.app/) · 个人维护

**面向印度宪法与 BNS 的 ReAct+RAG 法律问答聊天机器人**

Nyaya-GPT 是一个法律问答应用：用户通过 Streamlit 界面就印度宪法（Indian Constitution）与 Bharatiya Nyaya Sanhita（BNS）提问，系统由 ReAct agent 驱动——LLM 先对查询推理，再决定是否调用 PDF 查询工具从 FAISS 向量数据库中做语义检索，多步精炼后合成回答。技术栈为 LangChain + ChatGroq（Groq API）+ FAISS + Streamlit，PDF 文档被切块并嵌入 FAISS。README 以概念讲解与代码走读为主，未给出完整的安装运行命令；定位偏教程式项目，用户可修改文档与代码构建自己的助手。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct agent 循环：先推理再调用工具检索，多步精炼回答
- FAISS 向量数据库存储文档嵌入并做语义检索
- LangChain + ChatGroq（Groq API）+ Streamlit 技术栈
- 支持印度宪法与 BNS 两类法律 PDF 的查询工具

## 适用场景

- 查询印度宪法与 BNS 的具体条文与概念
- 作为模板替换文档构建自己的个性化法律/文档问答助手
- 学习 ReAct + RAG + 向量数据库的组合实现方式

## 场景标签

`文档问答` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L5: Let’s dive into some advanced AI concepts with a real-world problem like building a smart legal assistant, **Nyaya-G
> L53: 3. **RAG & Vector Database**: It fetches relevant legal text from the FAISS(Facebook AI Similarity Search) vector d

## 星数曲线

```mermaid
xychart-beta
    title "Debapriya-source/nyaya-gpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-24 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e3905f3de078` · [字段定义](../../DATASET.md)*
