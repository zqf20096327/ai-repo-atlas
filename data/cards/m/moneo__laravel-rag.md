# moneo/laravel-rag

⭐ 40 · PHP · MIT · 推送 2026-06-21 · [GitHub](https://github.com/moneo/laravel-rag) · [官网](https://moneo.com.tr/blog/rag-pipelines-now-native-to-laravel) · 个人维护

**Laravel 应用的驱动式 RAG 管道包：检索增强生成全流程**

基于 Prism PHP 的 Laravel RAG 软件包，面向使用 Laravel 11+ 的 PHP 开发者。提供驱动式向量存储（pgvector 用于生产、sqlite-vec 用于本地开发，经 .env 切换）、流式 SSE 响应、Agentic 迭代检索、RRF 混合搜索、LLM 重排序、对话记忆、RAG 评测框架、MCP 服务器、Filament 管理面板与 Livewire 组件。通过 composer 安装，自定义向量存储需实现 VectorStoreContract。sqlite-vec 选项不支持 macOS Herd/Homebrew PHP，需 Docker 或 Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pgvector/sqlite-vec 双向量存储驱动，.env 切换
- 混合搜索（RRF）、LLM 重排序与 Agentic 迭代检索
- RAG 评测框架（Faithfulness/Relevancy/Context Recall）
- MCP Server 可将 RAG 暴露为 Claude Desktop、Cursor 等的工具

## 适用场景

- 在 Laravel 应用中为文档模型添加向量检索与问答
- 对已有知识库做带来源的流式聊天组件
- 通过 MCP 让 Claude Desktop/Cursor 查询自己的知识库

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L11: A complete, driver-based RAG (Retrieval-Augmented Generation) pipeline for Laravel. Built on Prism PHP for provider
> L26: - **RAG Evals** — First Laravel-native evaluation framework (Faithfulness, Relevancy, Context Recall)

## 星数曲线

```mermaid
xychart-beta
    title "moneo/laravel-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-26 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `44814c6c2a70` · [字段定义](../../DATASET.md)*
