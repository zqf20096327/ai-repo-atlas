# ProfessionalWiki/MediaWiki-MCP-Server

⭐ 138 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server) · [官网](https://professional.wiki/en/mediawiki-mcp-server) · 组织维护

**让 LLM 客户端通过 MCP 读写任意 MediaWiki 的服务器**

面向开发者与企业的 Model Context Protocol (MCP) 服务器，使 Claude Code、Cursor 等 LLM 客户端能够对任意 MediaWiki 站点进行读取与写入。读取工具覆盖页面抓取、搜索、历史、分类成员、文件字节内联等；写入工具（需认证）包括创建/更新/删除/移动/保护页面与文件上传，OAuth 与 bot password 两种认证路径。另提供 Semantic MediaWiki、Cargo、Wikibase、NeoWiki 等扩展包工具，仅在装了对应扩展的 wiki 上注册。支持 stdio 与 HTTP 两种传输，多 wiki 配置，经 npm 安装并按客户端逐项给出接入配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 页面读取/写入/搜索/文件上传等完整 MediaWiki 工具集，支持多 wiki 与默认 wiki
- OAuth（浏览器流/托管代理/手动 token）与 bot password 认证
- Semantic MediaWiki、Cargo、Wikibase、NeoWiki、Bucket 扩展包工具，按扩展安装情况注册
- stdio 与 HTTP 两种 MCP 传输，含内容大小上限等环境变量调节

## 适用场景

- 让 AI 编程助手直接查询和编辑 MediaWiki 站点内容
- 企业内部 wiki 接入 LLM 客户端做知识问答与内容维护
- 对 Wikibase/Cargo 等 wiki 运行结构化查询

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L4: An MCP (Model Context Protocol) server that enables Large Language Model (LLM) clients to interact with any MediaWik
> L180: ### Claude Code

## 星数曲线

```mermaid
xychart-beta
    title "ProfessionalWiki/MediaWiki-MCP-Server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 136 --> 139
    line [137, 138]
```

2026-10-18 137 → 2026-10-22 138（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e6104711c678` · [字段定义](../../DATASET.md)*
