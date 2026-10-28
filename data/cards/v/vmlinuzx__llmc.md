# vmlinuzx/llmc

⭐ 36 · Python · MIT · 推送 2026-02-17 · [GitHub](https://github.com/vmlinuzx/llmc) · 个人维护

**面向代码库的本地优先 RAG 引擎与 LLM 智能路由器**

面向开发者在使用 LLM 处理代码库场景的工具：本地建立 SQLite 索引，用 TreeSitter 解析多种语言的代码与文档，按查询检索相关片段（函数/类/文档）并发送所需上下文而非整个代码库；支持 GraphRAG 代码结构分析、小模型本地富化标注、MCP server（可接入 Claude Desktop）、本地→廉价云→高端模型的级联路由与预算控制。安全上提供受信客户端 Hybrid Mode 与不受信输入的 Docker/nsjail 容器隔离。通过 curl 安装脚本或 pip（自 git 仓库）安装，附带 CLI 与 TUI 仪表盘（官方标注仍在开发中）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 SQLite 索引 + TreeSitter 多语言代码解析的 RAG 检索
- MCP server 支持，可接入 Claude Desktop
- Local → Cheap Cloud → Premium 的级联路由与预算上限/限流
- Docker/nsjail 容器隔离与 Hybrid Mode 两种安全模式

## 适用场景

- 在代码项目中本地检索相关片段，减少发给 LLM 的 token 量
- 通过 MCP 让 Claude Desktop 等客户端访问本地代码索引
- 对不受信的 LLM 输出做沙箱化远程代码执行

## 场景标签

`RAG` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13: LLMC is a **local-first RAG (Retrieval Augmented Generation) engine** and intelligent router designed to drasticall
> L61: |**🔌 MCP Support**|Full Model Context Protocol server to integrate seamlessly with Claude Desktop.|
> L80: * **Intelligent Failover:** Cascades from Local → Cheap Cloud → Premium Models.

## 星数曲线

```mermaid
xychart-beta
    title "vmlinuzx/llmc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2fbbceabb45a` · [字段定义](../../DATASET.md)*
