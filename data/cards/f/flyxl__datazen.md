# flyxl/datazen

⭐ 117 · Rust · GPL-3.0 · 推送 2026-10-24 · [GitHub](https://github.com/flyxl/datazen) · [官网](https://flyxl.github.io/datazen/) · 个人维护 · 中文 README

**开源跨平台数据库桌面客户端，支持 AI 与 MCP agent 接入**

基于 Tauri + Rust 的 GPL-3.0 桌面数据库工作台，安装包小于 15MB，覆盖 18 种数据库驱动（PostgreSQL/MySQL/MariaDB/SQLite/Redis 等）。功能包括 schema 感知 SQL 编辑器、可视化查询构建、ER 图、图表与运维仪表盘、备份/Data Sync/Data Transfer/Schema Diff、YAML 工作流、SSH/代理/WebSocket 隧道。AI 部分为可选功能：自然语言生成 SQL、错误诊断、EXPLAIN 分析，可配置 OpenAI/Anthropic/DeepSeek/Ollama 或任意 OpenAI 兼容端点；同时作为 MCP server 与 client 运行，支持 headless stdio 模式。无账号、无遥测，凭据 AES-256-GCM 加密。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 种数据库驱动，既是 MCP server 也是 MCP client，支持 headless stdio 模式
- AI 可选：OpenAI/Anthropic/DeepSeek/Ollama 及 OpenAI 兼容端点，基于已连接 schema 生成 SQL 与诊断
- Data Sync/Data Transfer/Schema Diff 等数据迁移操作均提供可审查预览
- MIT 许可的 Driver API 支持独立仓库开发驱动，工作流以 YAML 描述并可在 UI/MCP/headless 下运行

## 适用场景

- 在一个桌面应用中完成数据库浏览、查询、迁移与监控的完整流程
- 用自然语言针对真实 schema 生成 SQL 或诊断报错
- 让外部 AI agent 通过 MCP 驱动数据库操作或运行工作流
- 定时备份与跨库自动化任务的编排执行

## 场景标签

 · 领域:数据库工具/桌面应用

## 证据(README 行号)

> L47: A first-run wizard walks you through the first connection and seeds a sample SQLite database, so you can try everyt
> L101: AI is optional and yours to configure: OpenAI, Anthropic, DeepSeek, Ollama for fully local models, or any OpenAI-c

## 星数曲线

```mermaid
xychart-beta
    title "flyxl/datazen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 116 --> 118
    line [117, 117]
```

2026-10-18 117 → 2026-10-24 117（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `d149f9a54a76` · [字段定义](../../DATASET.md)*
