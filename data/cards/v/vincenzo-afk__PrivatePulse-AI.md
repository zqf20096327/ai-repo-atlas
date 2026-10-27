# vincenzo-afk/PrivatePulse-AI

⭐ 40 · TypeScript · MIT · 推送 2026-09-19 · [GitHub](https://github.com/vincenzo-afk/PrivatePulse-AI) · 个人维护

**隐私优先的 RAG 文档问答应用：本地处理+引用溯源**

面向处理敏感文件（医疗记录、财务报表、法律合同等）的 RAG 文档问答应用：用户上传 PDF/DOCX/TXT/图片/扫描件，通过自然语言对话获取带文档与页码引用的回答。机制包括本地文档处理、检索增强生成、会话隔离工作区、SSN/信用卡/邮箱实体掩码、审计日志；嵌入默认用 Ollama nomic-embed-text 本地生成，生成走 Groq Llama 3.2 90B Vision（需 GROQ_API_KEY）。FastAPI 后端 + Next.js 14 前端，支持 uv/npm 或 Docker Compose 本地运行。README 声明为本地优先开发项目，不保证合规性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PDF/DOCX/TXT/图片/扫描件多格式摄取，含视觉与 OCR 回退路径
- 回答内联文档与页码引用，检索上下文用于落地生成
- 会话隔离工作区、实体掩码（SSN/信用卡/邮箱）与审计日志
- 嵌入默认走 Ollama nomic-embed-text 本地生成，可配置 OpenAI 兼容嵌入

## 适用场景

- 对医疗、法律、财务等机密文档做自然语言问答且要求引用来源
- 在本地环境处理敏感文件以减少原始文档外露
- 扫描件与图片文档的 OCR 问答

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: PrivatePulse AI lets you ask natural-language questions about medical records, financial statements, legal contracts
> L23: |Retrieval-augmented answers|Relevant chunks are retrieved from the document index before generation.|
> L52: |Generation|Groq Llama 3.2 90B Vision|

## 星数曲线

```mermaid
xychart-beta
    title "vincenzo-afk/PrivatePulse-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-27 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `91fc997a901c` · [字段定义](../../DATASET.md)*
