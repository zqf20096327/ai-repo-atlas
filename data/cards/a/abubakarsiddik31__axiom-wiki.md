# abubakarsiddik31/axiom-wiki

⭐ 112 · TypeScript · NOASSERTION · 推送 2026-11-08 · [GitHub](https://github.com/abubakarsiddik31/axiom-wiki) · [官网](https://abubakarsiddik31.github.io/axiom-wiki/) · 个人维护

**把文档与代码库编译成可供 Agent 查询的自更新 Markdown wiki**

一个以 CLI 与 MCP 服务器形式提供的知识编译工具：将 PDF、DOCX、HTML、网页、YouTube 字幕乃至整个代码库摄入并编译为带 YAML frontmatter 与双向 wiki-link 的 Markdown 页面。以 SHA-256 哈希做增量编译，引用带页码/时间戳/行号定位器，可用 lint --forensic 做机器校验；内置 Orama 混合检索（BM25+向量）、本地 Web UI、JSON API 与 16 个 MCP agent 工具。支持 9 家 LLM 提供商，含 Ollama 离线路径；npm 分发，许可证为 ELv2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 增量编译：SHA-256 内容哈希跳过未变更文件，sync 按 Git diff 更新
- 取证式引用：页码/时间戳/行号定位器，lint --forensic 机械校验，query --forensic 屏蔽参数记忆
- MCP 服务器提供 16 个 agent 工具，setup-agent 自动配置开发工具
- Orama 混合检索（BM25+向量）与本地 BGE cross-encoder 重排

## 适用场景

- 把散落的 PDF、文章、视频整理成互链的个人知识库
- 为项目代码库生成架构目录与模块指南并随代码演进同步
- 让 Claude Code / Cursor 等 IDE agent 通过 MCP 读写 wiki 作为外部记忆
- 需要可验证出处的资料问答与引用审计

## 场景标签

`知识库管理` `文档解析` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L8:  An AI-powered knowledge compiler that transforms unstructured documents and codebases into an interconnected, self-
> L28: > *"Instead of repeatedly querying a raw database with RAG, what if an AI continuously reads, extracts, synthesizes
> L159: |**Ollama** *(100% Local / Offline)*|`llama3.3`, `qwen2.5`, `mistral`, custom|✅ (nomic/bge)|**Free**|ollama.com|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `ac40448ee6ef` · [字段定义](../../DATASET.md)*
