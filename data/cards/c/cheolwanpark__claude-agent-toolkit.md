# cheolwanpark/claude-agent-toolkit

⭐ 27 · Python · MIT · 推送 2026-01-25 · [GitHub](https://github.com/cheolwanpark/claude-agent-toolkit) · 个人维护

**基于 claude-code-sdk 的 Python Agent 构建框架**

对 claude-code-sdk 的封装库：用 @tool 装饰器与 BaseTool 类把 Python 函数定义为 Claude 工具，自动管理 MCP 服务器与工具发现。提供 Docker（默认）与子进程两种执行模式做运行时隔离，内置 FileSystemTool（基于模式的文件权限控制）与 DataTransferTool（Pydantic 结构化数据传输），支持经 stdio/HTTP 接入外部 MCP 服务器、parallel=True 并行执行与 CPU 密集进程池。需 Python 3.12+ 与 Claude Code OAuth Token。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- @tool 装饰器将 Python 函数转为 Claude 工具，自动管理 MCP 服务器
- Docker/子进程双执行模式实现运行时隔离
- FileSystemTool 基于模式控制文件访问权限
- 经 stdio/HTTP 接入外部 MCP 服务器

## 适用场景

- 快速构建带自定义工具的 Claude Code Agent
- 在生产环境以 Docker 隔离执行 Agent 工具
- 复用已有 MCP 服务器与 Node.js/Go 等语言工具

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: A Python framework that wraps claude-code-sdk to provide better developer experience through decorator-based tools, 
> L18: - **🎯 Decorator-Based Tools** - Simple `@tool` decorator converts any Python function into a Claude-compatible tool
> L19: - **🐳 Runtime Isolation** - Docker containers provide safe, controlled execution with only your specified tools

## 星数曲线

```mermaid
xychart-beta
    title "cheolwanpark/claude-agent-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `65af399a94f1` · [字段定义](../../DATASET.md)*
