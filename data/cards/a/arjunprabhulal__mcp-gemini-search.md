# arjunprabhulal/mcp-gemini-search

⭐ 56 · Python · 推送 2026-08-12 · [GitHub](https://github.com/arjunprabhulal/mcp-gemini-search) · [官网](https://github.com/arjunprabhulal/mcp-gemini-search) · 个人维护

**用 Gemini 函数调用驱动 MCP 航班搜索工具的示例客户端**

演示项目：Python 客户端通过 stdio 连接本地 MCP 服务器（mcp-flight-search），将用户自然语言查询发给 Gemini 2.5 Pro，由其自动提取函数参数，再调用 MCP 工具经 SerpAPI 查询 Google Flights 数据并以 JSON 格式展示。需要 Python 3.7+、Google AI Studio API key 与 SerpAPI key，安装 mcp-flight-search 包后运行 client.py。面向学习 MCP 与函数调用集成方式的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言航班搜索，Gemini 自动提取函数参数
- 通过 stdio 连接 mcp-flight-search MCP 服务器
- 经 SerpAPI 查询 Google Flights 并格式化 JSON 输出
- 多层级错误处理（输入校验、API 通信、工具执行等）

## 适用场景

- 学习 MCP 客户端与 Gemini 函数调用的集成方式
- 自然语言查询航班信息并获取结构化结果
- 了解 MCP 工具注册与调用的数据流

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: This project demonstrates how to use Google's Gemini 2.5 Pro with function calling capabilities to interact with the
> L9: 1. Connect to a local MCP server process (`mcp-flight-search`) using stdio communication
> L10: 2. Use natural language prompts with Gemini 2.5 Pro to search for flights (e.g., "Find flights from Atlanta to Las 

## 星数曲线

```mermaid
xychart-beta
    title "arjunprabhulal/mcp-gemini-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-24 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1b3ad00c395e` · [字段定义](../../DATASET.md)*
