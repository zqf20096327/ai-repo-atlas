# kuluruvineeth/openbeam

⭐ 18 · TypeScript · AGPL-3.0 · 推送 2026-05-04 · [GitHub](https://github.com/kuluruvineeth/openbeam) · [官网](https://kuluruvineeth.com/essays/three-retrievers-one-answer/) · 个人维护

**面向企业与物理世界的开源企业搜索与自主 agent 平台**

自托管的企业知识搜索平台，将 SaaS 工具（Slack、GitHub、Notion 等）与物理系统（IoT 传感器、MQTT/OPC-UA/BACnet 工业协议）统一到一个可搜索、可被 agent 调用的层，提供 87 个连接器、混合语义+关键词搜索（基于 Vespa BM25+HNSW）、带引用溯源的 RAG 管道、MCP 服务器以及 6 个基于 Temporal 定时调度的自主 agent（写入需审批）。跨平台 Go CLI 提供 Homebrew 与二进制安装，服务端通过 Docker Compose 或源码 make 部署，AGPL-3.0 许可，数据留在本地服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 87 个连接器覆盖 SaaS、IoT 平台与工业协议
- 混合语义+关键词搜索，宣称 p99 延迟低于 200ms
- 6 个基于 Temporal 的预置自主 agent，写操作需审批
- 一等 MCP 服务器支持 Claude Code、Cursor 等 MCP 客户端

## 适用场景

- 在一个查询中同时搜索企业 SaaS 文档与 IoT 传感器数据
- 为 Claude Code、Cursor 等 MCP 客户端接入统一知识库
- 定时运行内容摘要、合规审查等自主 agent 任务
- 在自有基础设施上自托管企业搜索，数据不出网

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L26: - **AI Agents** — Tool-use agents that search, analyze, and act across your entire knowledge base with 100+ composa
> L30: - **MCP Server** — First-class Model Context Protocol server for Claude Code, Cursor, Codex, and any MCP client
> L31: - **RAG Pipeline** — Grounded AI answers with citation and source attribution

## 星数曲线

```mermaid
xychart-beta
    title "kuluruvineeth/openbeam 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `deee94b7ecce` · [字段定义](../../DATASET.md)*
