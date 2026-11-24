# mibazarow/bitrix-mcp-public-server

⭐ 3 · TypeScript · MIT · 推送 2026-11-07 · [GitHub](https://github.com/mibazarow/bitrix-mcp-public-server) · 个人维护

**为 AI 代理提供 Bitrix Framework 代码与文档查询的自托管 MCP 服务器**

自部署的 MCP 服务器（Node.js，端口 3100），供 Cursor、Claude Desktop、PhpStorm、Kilo 等 AI 代理客户端连接，从本机 Bitrix 安装的 PHP 源码和 markdown 文档中读取信息。提供 24 个工具：列出模块/组件/事件、按名称/命名空间/接口搜索函数与类、读取函数源码、语义搜索文档；语义检索由独立的 Python 嵌入服务承担，运行 google/embeddinggemma-2（CPU fp32，无需 GPU），索引随 Bitrix 更新增量重建，通过 cron 或管理接口触发。原公开实例已下线，仓库只含自行部署套件；服务器无鉴权，公开部署需在 nginx 层做访问限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 24 个 MCP 工具覆盖模块、组件、ORM、类、函数与文档查询
- 直接解析本机 Bitrix PHP 源文件，索引与安装版本一致
- EmbeddingGemma 2 语义文档搜索，CPU fp32 运行无需 GPU
- Streamable HTTP 传输（MCP spec 2025-03-26），无状态

## 适用场景

- 让 AI 代理基于当前安装的真实源码回答 Bitrix API 用法
- 在 IDE 中查询模块事件、类继承和函数调用位置
- 对 Bitrix 文档做语义检索并引用原文

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: **MCP-сервер, который вы разворачиваете сами.** Он даёт AI-агентам (Cursor, Claude Desktop,
> L11: Сервер полностью независим от движка: это отдельный сервис, а не модуль Bitrix. Он ничего
> L68: ## Инструменты (24 шт.)

## 星数曲线

```mermaid
xychart-beta
    title "mibazarow/bitrix-mcp-public-server 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-18 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `1e75acf7a439` · [字段定义](../../DATASET.md)*
