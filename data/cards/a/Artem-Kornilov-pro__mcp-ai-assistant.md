# Artem-Kornilov-pro/mcp-ai-assistant

⭐ 20 · Python · MIT · 推送 2026-09-05 · [GitHub](https://github.com/Artem-Kornilov-pro/mcp-ai-assistant) · 个人维护

**Docker 化 MCP 服务器集合：134 个工具供任意 MCP 客户端调用**

将 24 个主题 MCP 工具服务器（文件系统、GitHub、Google Sheets、天气、QR 码、数学、货币等，共 134 个工具）打包为单个 Docker 镜像，通过 HTTP 或 stdio 暴露为单一 MCP 端点，可由 Claude Desktop、Claude Code、Cursor 等 MCP 客户端接入，无需本地安装 Python。环境变量 MCP_SERVERS 可选择启用的工具域，MCP_API_KEY 可开启鉴权。另附终端聊天示例客户端（依赖 Yandex Cloud API key）。部分工具域需 GitHub/Google OAuth 令牌，条码识别依赖系统库 libzbar。

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

- 24 个主题服务器、134 个工具打包为单个 Docker 镜像，经 HTTP/stdio 单端点暴露
- MCP_SERVERS 环境变量按需启用工具域
- 文件系统域有 Sandbox 限制在 WORKSPACE_DIR 内
- 终端聊天示例客户端通过自然语言调用这些工具

## 适用场景

- 为 Claude Desktop / Cursor 等 MCP 客户端一站式提供文件、GitHub、表格等工具
- 在对话中通过自然语言操作文件与 GitHub 仓库
- 按需只启用部分工具域降低暴露面

## 场景标签

 · 领域:LLM 基础设施/MCP 工具

## 证据(README 行号)

> L9: **Dockerized MCP-сервер со 134 инструментами (файлы, GitHub, Google Sheets, погода, изображения, QR/штрихкоды, матем
> L15: Проект построен на **Model Context Protocol (MCP)** — открытом стандарте для подключения AI-моделей к внешним инстр
> L20: MCP-клиент → HTTP / stdio → MCP-гейтвей (src/gateway.py) → выбранные servers/*.py → внешний сервис

## 星数曲线

```mermaid
xychart-beta
    title "Artem-Kornilov-pro/mcp-ai-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9de143b8efdb` · [字段定义](../../DATASET.md)*
