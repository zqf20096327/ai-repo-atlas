# Hamna-Munir/08-AI-Business-Agent

⭐ 5 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/Hamna-Munir/08-AI-Business-Agent) · [官网](https://08-ai-business-agent.streamlit.app/) · 个人维护

**基于真实 SQLite 数据库与 MCP 服务器生成证据型业务分析报告的 AI Agent**

90 天 AI 工程 roadmap 第 8 周的教学型项目：接收自然语言业务问题，先分类问题并规划所需数据，通过 MCP 服务器（官方 mcp SDK）查询 SQLite 业务数据库，用纯 Python 计算涨幅并区分价格驱动/需求驱动的收入变化，可选调用 Tavily 做外部检索，最终产出结构化报告；规划步骤无 LLM 调用，报告 LLM 仅基于被显式交给的证据写作，证据不足时输出明确回退文案。以 Streamlit 为 UI，文件访问限定于白名单目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器暴露 7 个业务数据工具，可被 Claude Desktop 等任意 MCP 客户端连接
- 确定性规划步骤提取月份/地区/商品，无需 LLM 调用
- 报告 LLM 只基于显式证据写作，包含经测试的证据不足回退
- 沙箱化文件访问，结构化阻断路径穿越

## 适用场景

- 用自然语言提问并由 Agent 从数据库中核实业务指标变化原因
- 学习 MCP 协议下工具服务器与客户端的接入方式
- 参考证据约束式报告生成的实现范式

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L14:  An AI agent that investigates a real business question against a real SQLite database — through a real MCP server 
> L26: needs, queries a real SQLite database (optionally through a real MCP
> L37: - 🔌 **Real MCP Server** — `mcp_server.py` exposes 7 business-data tools over the actual Model Context Protocol (off

## 星数曲线

```mermaid
xychart-beta
    title "Hamna-Munir/08-AI-Business-Agent 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-10-19 5 → 2026-11-21 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `656b32b9411a` · [字段定义](../../DATASET.md)*
