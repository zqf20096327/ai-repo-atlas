# informatique-cdc/retro-doc

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/informatique-cdc/retro-doc) · 组织维护

**面向存量代码库的自动化逆向文档生成与分析平台**

由 Caisse des Dépôts Informatique 开发的代码库分析应用：上传源码 zip 后，后端通过 Azure Durable Functions 工作流逐文件抽取 AST、CFG、DFG 图，生成文档与结构洞察；结果以 Angular SPA 呈现，支持 Cytoscape 图浏览、基于 LangChain 与 Azure AI Search 的 RAG 问答聊天机器人，以及使用 DeepAgents 的自主多步深度分析（可导出 PDF）。限制：LLM 端点、嵌入模型与 Azure AI Search 无法本地模拟，为必需外部服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上传 zip 源码后自动抽取 AST/CFG/DFG 图并生成文档
- RAG 聊天机器人基于 LangChain + Azure AI Search 回答代码库问题
- DeepAgents 自主多步深度分析，支持 PDF 导出
- Microsoft Entra ID 认证的多用户支持与实时流水线跟踪

## 适用场景

- 接手遗留项目时快速生成文档并浏览代码结构
- 通过对话向 AI 询问代码库的实现细节
- 对代码库提交自由形式问题获得多步自主分析报告

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L15: Retro-Doc analyzes existing codebases to automatically generate documentation and structural insights. Upload a zip
> L25: - **RAG chatbot** — Ask questions about the analyzed codebase in a conversational interface, powered by LangChain w
> L26: - **Deep analysis** — Submit free-form queries for autonomous multi-step code analysis using DeepAgents, with PDF e

## 星数曲线

```mermaid
xychart-beta
    title "informatique-cdc/retro-doc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7e5499167713` · [字段定义](../../DATASET.md)*
