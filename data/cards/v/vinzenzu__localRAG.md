# vinzenzu/localRAG

⭐ 14 · Python · 推送 2026-06-17 · [GitHub](https://github.com/vinzenzu/localRAG) · 个人维护

**本地离线 RAG 问答：用 Mistral 7B 对自有文档提问**

基于 Python 3.12 的本地 RAG 问答应用：用户将 PDF 或 TXT 文件放入指定目录，程序首次运行时用 ChromaDB 构建向量数据库，通过 Ollama 拉取并运行 Mistral 7B（默认 mistral:instruct，可在代码中切换模型），在浏览器打开本地 IP 的 Gradio 网页界面对文档提问并获取 LLM 回答。全部组件在本地运行，无需付费 API。README 由个人维护，作者自述实现性能有改进空间（重排序、换嵌入模型等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PDF/TXT 本地文档导入，首次运行自动构建 ChromaDB 向量库
- 通过 Ollama 运行 Mistral 7B，默认模型可在代码中更换
- Gradio 本地网页界面，浏览器中与文档对话
- 全流程本地免费，无需外部 API

## 适用场景

- 在本地对自己的 PDF/TXT 资料提问
- 离线环境下搭建私人文档问答
- 不想付费 API 的轻量 RAG 试用

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: ## Fully free, local and open-source Q&A RAG with Mistral 7B, using local documents
> L18: 9. In the console, a local IP address will be printed. Copy it, paste it into a browser, and you can interact with 
> L24: 3. Type in your question. Web interface for the RAG app

## 星数曲线

```mermaid
xychart-beta
    title "vinzenzu/localRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `682ea9320ec2` · [字段定义](../../DATASET.md)*
