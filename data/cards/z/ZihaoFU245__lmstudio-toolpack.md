# ZihaoFU245/lmstudio-toolpack

⭐ 34 · Python · MIT · 推送 2026-04-06 · [GitHub](https://github.com/ZihaoFU245/lmstudio-toolpack) · 个人维护

**面向本地 LLM 的 MCP 工具集合：一个 venv 运行多个本地 MCP 服务器**

将多个本地 MCP 服务器集中在一个仓库与一个 uv 管理的 Python 虚拟环境中，包含三个服务器：基于 DuckDuckGo 的网页搜索与摘要、允许 agent 执行 Python（NumPy/SymPy）的沙盒（README 声明其 exec/eval 非安全沙盒）、轻量级长期记忆笔记存储。默认 stdio 传输，可切换 HTTP；附带向导脚本生成 LM Studio 兼容的 mcp.json 配置，python-sandbox 执行记录写入 JSONL 审计日志。面向使用 LM Studio 等本地 LLM 客户端的开发者。

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

- 单一 uv 环境承载多个本地 MCP 服务器
- 向导式生成 LM Studio/Cursor 风格 mcp.json 配置
- python-sandbox 执行记录追加写入 JSONL 审计日志
- stdio 与 HTTP 两种传输方式可切换

## 适用场景

- 为本地 LLM 客户端一次性配置搜索、代码执行与记忆三类工具
- 让 agent 执行 Python 数学计算并留存审计日志
- 快速生成 MCP JSON 配置接入 LM Studio

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: > A small collection of Model Context Protocol (MCP) tools, built for local LLMs. One venv, many options.
> L19: ## MCP Servers
> L52: ## Run the MCP Server

## 星数曲线

```mermaid
xychart-beta
    title "ZihaoFU245/lmstudio-toolpack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `71c79b61851d` · [字段定义](../../DATASET.md)*
