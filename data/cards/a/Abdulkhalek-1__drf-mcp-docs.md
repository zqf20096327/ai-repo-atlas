# Abdulkhalek-1/drf-mcp-docs

⭐ 16 · Python · MIT · 推送 2026-03-09 · [GitHub](https://github.com/Abdulkhalek-1/drf-mcp-docs) · [官网](http://abdulkhalek-1.github.io/drf-mcp-docs/) · 个人维护

**通过 MCP 向 AI 编码代理暴露 Django REST API 文档**

面向 Django REST Framework 项目的 MCP 服务器：读取 drf-spectacular、drf-yasg 或 DRF 内置生成器产出的 OpenAPI schema，转换为结构化数据后以 MCP Resources 与 Tools 形式暴露，供 Claude Code、Cursor 等 AI 编码代理浏览端点、查询 schema、获取请求/响应示例并生成前端集成代码（fetch/axios/requests/cURL）。只读暴露文档，不改数据；支持 stdio 与 streamable-http 两种传输。

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

- 三种 schema 适配器：drf-spectacular / drf-yasg / DRF 内置，自动检测
- MCP Resources 浏览 API 结构，Tools 支持搜索端点与生成集成代码
- 只读文档暴露，无数据变更
- stdio 与 streamable-http 两种传输，可挂载到 ASGI 应用

## 适用场景

- 让 Claude Code / Cursor 等代理读取我的 DRF API 文档并编写正确的前端集成代码
- 在 AI 工具中按关键字搜索 API 端点与查看 schema 详情
- 通过 MCP 生成各语言的请求示例代码

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L11: **drf-mcp-docs** exposes your Django REST Framework API **documentation** through the Model Context Protocol (MCP) 
> L15: > Packages like `django-mcp-server` and `django-rest-framework-mcp` expose DRF **actions** as MCP tools — the AI ag
> L190: │  AI Agent   │────>│  MCP Server  │────>│ Schema Processor │────>│  Adapter  │

## 星数曲线

```mermaid
xychart-beta
    title "Abdulkhalek-1/drf-mcp-docs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `29fe04e53b9c` · [字段定义](../../DATASET.md)*
