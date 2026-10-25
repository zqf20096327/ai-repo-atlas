# Arkya-AI/claude-additional-models-mcp

⭐ 45 · JavaScript · MIT · 推送 2026-02-15 · [GitHub](https://github.com/Arkya-AI/claude-additional-models-mcp) · [官网](https://arkya.ai/) · 组织维护

**让 Claude Desktop 通过 MCP 调用 Gemini/GLM-5 的委托服务器**

一个 MCP 服务器，以 Claude Desktop 子进程方式运行，把重计算任务（代码生成、分析、文档处理、网络检索）委托给外部模型 Google Gemini 3.x 或 Z.ai GLM-5（744B），Claude 保留编排与文件 I/O 角色。Gemini 走 OpenAI 兼容与原生 Google API 双路径，提供 ask_gemini、web_search、web_reader、parse_document 等 5 个工具；通过 CLAUDE.md 强制子代理也执行委托规则。安装方式为 git clone 后 npm install，再写入 claude_desktop_config.json。README 以降低 Claude 订阅额度消耗为动机，节省数据为自述。

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

- Gemini 与 GLM-5 双后端，均暴露 5 工具接口（ask/web_search/web_reader/parse_document）
- Gemini 双路径：OpenAI 兼容接口 + 原生 API（搜索接地、URL 上下文）
- CLAUDE.md 委托规则：超 50 行代码或 300 词内容须委托外部模型
- 支持并行子代理委托执行

## 适用场景

- Claude Pro 用户降低额度消耗，把重活交给 Gemini/GLM-5
- 长文分析、多文档对比、网络调研等任务的委托执行
- 希望 Claude 只做编排、外部模型做生成的工作流

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L32: `claude-additional-models-mcp` is a production-ready Model Context Protocol (MCP) server that integrates external A
> L63: The Model Context Protocol allows Claude Desktop to discover and execute tools provided by a local server. This MCP

## 星数曲线

```mermaid
xychart-beta
    title "Arkya-AI/claude-additional-models-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ecc5b43f9490` · [字段定义](../../DATASET.md)*
