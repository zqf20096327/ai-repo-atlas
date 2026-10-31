# DweskZ/EcuDataMCP

⭐ 14 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/DweskZ/EcuDataMCP) · 个人维护

**让 AI 助手检索分析厄瓜多尔政府开放数据的 MCP 服务器**

通过 Model Context Protocol 把 Claude、ChatGPT、Cursor 等 AI 客户端接入厄瓜多尔官方数据源（CKAN 目录、SRI、Gob.ec、SERCOP、INEC、BCE、Superintendencia 等），支持自然语言搜索、trámites 查询、在内存中 preview CSV/Excel/JSON 数据及查询 CKAN DataStore，公共数据源无需 API key。部署方式含 PyPI 包（uvx）、Docker（stdio/HTTP，HTTP 可配 Bearer 认证、限流、TLS）与手动安装（Python 3.11+ 与 uv）。README 声明部分工具定义由 AI 生成或协助，可能不完整或过时，需对照来源核验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一接入 SRI、INEC、BCE、SERCOP 等多个厄瓜多尔官方数据源，无需 API key
- preview_resource_data 在内存解析 CSV/TSV、JSON/GeoJSON、Excel 与部分压缩文件
- Docker 部署支持 HTTP Streamable、Bearer 认证、限流、TLS 与 /health /usage 端点
- 提供 Claude Desktop、Cursor、VS Code、ChatGPT、Codex、Gemini CLI 等十余种客户端接入配置

## 适用场景

- 在 Claude 或 ChatGPT 中直接查询厄瓜多尔政府办事流程与公共数据
- 记者与研究人员跨机构交叉检索 SRI、INEC、BCE 等数据集并预览数据
- 开发者把厄瓜多尔开放数据作为 AI agent 的数据后端

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L10: **Infraestructura abierta de datos públicos para Ecuador.** EcuDataMCP conecta asistentes de IA, investigadores, pe
> L12: Utiliza el Model Context Protocol (MCP) para que clientes compatibles como Claude, ChatGPT, Gemini y Cursor puedan 
> L56: - Integrar datos abiertos de Ecuador en aplicaciones mediante el protocolo MCP estándar.

## 星数曲线

```mermaid
xychart-beta
    title "DweskZ/EcuDataMCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `70fc6aaa5821` · [字段定义](../../DATASET.md)*
