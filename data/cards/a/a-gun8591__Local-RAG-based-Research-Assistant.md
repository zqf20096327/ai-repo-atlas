# a-gun8591/Local-RAG-based-Research-Assistant

⭐ 3 · Python · 推送 2026-11-16 · [GitHub](https://github.com/a-gun8591/Local-RAG-based-Research-Assistant) · 个人维护

**本地离线 RAG 问答助手：对自己的 PDF/文本提问**

三个 Python 脚本组成的终端 RAG 问答工具：extract_pdf.py 将 PDF 转为文本，ingest.py 分块并用 sentence-transformer 嵌入存为 npz 索引，chat.py 检索相关片段后交由本地 Ollama（llama3.2）生成带来源标注的回答。数据全程不离开本机，无需数据库服务器。提供 Docker 构建与运行方式（容器仅跑聊天，Ollama 留在宿主机）。限制包括扫描版 PDF 需先 OCR、仅终端界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 100% 本地运行，无云端 API 调用
- 每条回答附 (sources: ...) 来源标注
- 一条命令将 PDF 转文本并建立向量索引
- 提供 Docker 构建与 PowerShell / Docker Desktop 两种运行方式

## 适用场景

- 在本地私有文档上做离线问答检索
- 不希望数据上传云端的资料查询
- 用个人 PDF 做研究资料整理提问

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: Ask questions about your own PDF and text files, fully offline. The assistant retrieves the most relevant passages f
> L22: 1. **Ingest**: documents are split into chunks and embedded with a sentence-transformer model.
> L25: 4. **Generate**: the best chunks are passed to llama3.2 as context to produce the answer.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `0fc5021ef6c7` · [字段定义](../../DATASET.md)*
