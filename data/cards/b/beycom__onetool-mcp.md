# beycom/onetool-mcp

⭐ 24 · Python · GPL-3.0 · 推送 2026-09-01 · [GitHub](https://github.com/beycom/onetool-mcp) · [官网](https://onetool.beycom.online) · 组织维护

**单一 MCP 服务器：以 Python 代码调用 250+ 工具并代理现有 MCP 服务**

面向开发者的 MCP server，把 28 个工具包（共 253 个工具，涵盖搜索、文档、文件、数据库、Excel、图表、白板、记忆、RAG 知识库等）暴露为 Python API，agent 通过写代码调用而非逐个读取工具定义，以降低上下文 token 占用。内置 MCP 服务器代理，可包装既有 MCP server 并在运行时启停。通过安装脚本或 uv 安装，支持 Claude Code、Cursor、Codex 等 MCP 客户端；提供 age 加密秘钥管理、CLI 直连运行进程、Python 文件即插即用的扩展机制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 28 个工具包、253 个工具，agent 以 Python 代码形式调用
- 代理既有 MCP 服务器，可运行时启用/禁用/重启，无需重启客户端
- age 加密秘钥存入 OS keychain，秘钥文件可提交
- 放入 Python 文件即生成新工具包，另有 ot-ref agent 技能

## 适用场景

- 减少多个 MCP server 的工具定义 token 开销
- 在一个 MCP server 内统一使用搜索、文件、数据库、白板等工具
- 给 agent 挂载持久记忆与 RAG 知识库
- 将已有 MCP 服务器包装为代理并在对话中管理

## 场景标签

 · 领域:开发工具/MCP 服务器

## 证据(README 行号)

> L5:  🧿 One MCP for developers - no tool tax, no context rot. 250+ tools your agent calls as Python code: search, docs, f
> L24: OneTool is **one MCP server** that exposes tools as a Python API. Instead of reading tool definitions, your agent w
> L107: |**Runtime**|MCP server proxy with runtime enable/disable/restart, direct CLI/API into the running process, `ot-re

## 星数曲线

```mermaid
xychart-beta
    title "beycom/onetool-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `c0593fff9cb3` · [字段定义](../../DATASET.md)*
