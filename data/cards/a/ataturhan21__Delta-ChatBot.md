# ataturhan21/Delta-ChatBot

⭐ 24 · Python · GPL-3.0 · 推送 2026-10-31 · [GitHub](https://github.com/ataturhan21/Delta-ChatBot) · 个人维护

**基于 Streamlit 的本地 PDF/文本文档问答聊天机器人**

一个 Streamlit 应用：上传 PDF 或 UTF-8 TXT 文档后，经文档加载、按 256 字符（重叠 32）分块、嵌入与 Chroma 检索，再由会话式 LangChain 链生成回答，可展开查看检索到的原文片段。侧边栏可选 OpenAI 或 Hugging Face 模型，API key 以掩码字段传入各 provider 客户端，每个上传文档集使用独立 Chroma 集合。通过 git clone 加 Poetry 安装依赖从源码运行，面向本地单用户会话；provider 访问与兼容性需部署前自行验证，附离线单元测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上传 PDF/UTF-8 TXT 后的分块、嵌入与 Chroma 检索问答流程
- 侧边栏选择 OpenAI 或 Hugging Face 模型，API key 传入 provider 客户端而非进程级环境变量
- 每个上传文档集使用独立临时目录与独立 Chroma 集合
- 提供离线单元测试（fake provider clients）

## 适用场景

- 上传自己的 PDF 或文本文件后提问并获得带原文出处的回答
- 在本地单用户会话中测试不同 OpenAI/Hugging Face 模型的文档问答效果

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: A Streamlit application for asking questions about uploaded PDF and plain-text documents. It combines document loadi
> L20: 1. Choose an OpenAI or Hugging Face model in the sidebar.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6fc14172ff04` · [字段定义](../../DATASET.md)*
