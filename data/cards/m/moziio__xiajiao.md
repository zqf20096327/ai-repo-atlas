# moziio/xiajiao

⭐ 14 · JavaScript · MIT · 推送 2026-03-30 · [GitHub](https://github.com/moziio/xiajiao) · [官网](https://moziio.github.io/xiajiao/) · 个人维护 · 中文 README

**自托管 AI Agent 团队协作 IM：npm start 即用，无需 Docker/外部数据库**

以即时通讯形式运行多个 AI Agent 的自托管平台：支持群聊、@mention 路由、Agent 间任务交接与协作链（含可视化流程面板与人工干预）、7 个内置工具调用、三类持久记忆（语义/情景/程序性）、BM25+向量混合检索与 LLM 重排的 RAG 知识库。兼容 OpenAI 系 API（Qwen/Kimi/GLM/DeepSeek/Ollama 等）与 Anthropic messages 协议，数据存储用 SQLite（WAL+FTS5），共 6 个 npm 依赖。面向个人开发者、小团队与多 Agent 模式研究者；需 Node.js >= 22，也提供 Docker 构建方式。渠道连接（企业微信/飞书/钉钉/Telegram）处于开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 Agent 群聊与 @mention 路由，Agent 间可交接任务形成协作链
- 7 个内置工具（web_search/call_agent/manage_channel 等），支持 MCP 协议
- 三类持久记忆 + BM25 与向量混合检索（RRF + LLM 重排）的 RAG 知识库
- SQLite 单文件存储，共 6 个 npm 依赖，无 PostgreSQL/Redis 等外部服务

## 适用场景

- 在群聊中 @mention 不同 Agent 并让它们接力协作完成任务
- 小团队搭建零外部依赖的自托管 AI 工作区
- 研究者原型验证 Agent 间通信与记忆系统
- 接入飞书/钉钉等外部平台让 Agent 定时汇报或应答

## 场景标签

`多智能体` `聊天机器人` `RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6:  A lightweight, self-hosted, open-source platform to run AI agents as a team — group chat, @mention routing, tool ca
> L26:  @mention an agent → Get a real-time response → Hand off to another agent — all in one chat.
> L106: > **The core difference:** Dify and Coze are *AI app development platforms*. Xiajiao is an **AI Agent team collabo

## 星数曲线

```mermaid
xychart-beta
    title "moziio/xiajiao 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f56dd121d437` · [字段定义](../../DATASET.md)*
