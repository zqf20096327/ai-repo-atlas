# insung8150/AgentWebSearch-MCP

⭐ 20 · Python · MIT · 推送 2026-02-19 · [GitHub](https://github.com/insung8150/AgentWebSearch-MCP) · 个人维护 · 中文 README

**无需 API key 的本地网页搜索 MCP 服务器，供本地 LLM 调用**

通过 Chrome DevTools Protocol 启动并控制 3 个真实 Chrome 实例，并行搜索 Naver/Google/Brave，无需 API key，支持登录会话持久化与反爬场景。以 MCP Server 形式提供给 Claude Code、Cursor、LM Studio、OpenClaw 等客户端，提供 web_search、smart_search 等工具；agentcpm 工具可选接入 SGLang 上运行的 AgentCPM-Explore 4B 模型做搜索规划与回答生成（需 CUDA）。也可通过 CLI 直接运行。要求 Python 3.10+ 与 Chrome/Chromium。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CDP 控制真实 Chrome 并行搜索 Naver/Google/Brave，无需 API key
- 提供 stdio 与 SSE 两种 MCP 模式，6 个 MCP 工具
- smart_search 支持 simple/medium/deep 深度控制与部分结果返回
- 可选 AgentCPM-Explore 4B 模型（SGLang）生成搜索规划与回答

## 适用场景

- 给本地 LLM（Ollama、LM Studio）或 Claude Code 提供联网搜索工具
- 需要登录态或韩国 Naver 搜索的场景
- 不想购买搜索 API 的免费联网检索方案

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Local WebSearch without API keys + MCP Server**
> L88: Use web search as an MCP tool in Claude Code, Cursor, LM Studio, or OpenClaw/Moltbot.

## 星数曲线

```mermaid
xychart-beta
    title "insung8150/AgentWebSearch-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d0a99ffd5b74` · [字段定义](../../DATASET.md)*
