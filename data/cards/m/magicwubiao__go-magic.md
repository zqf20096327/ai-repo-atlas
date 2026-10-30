# magicwubiao/go-magic

⭐ 33 · Go · MIT · 推送 2026-10-29 · [GitHub](https://github.com/magicwubiao/go-magic) · [官网](https://magictech.cc/) · 个人维护 · 中文 README

**Go 编写的 AI Agent 框架，含 TUI 与 Web 仪表盘**

用 Go 实现的 AI Agent 框架，灵感来自 Nous Research 的 hermes-agent。支持 22+ AI 提供商（含 Ollama、vLLM 及 OpenAI 兼容端点），每个提供商可配置多模型并热切换。提供 BubbleTea TUI、Vue 3 Web 仪表盘（会话管理、Token 用量看板、看板、群聊）、15+ 内置工具（文件/终端/浏览器/代码执行）、技能系统（L0/L1/L2 渐进加载）、MCP 协议接入、Bot 模式（跨实例互联）与 15 个消息网关平台（Telegram/飞书/钉钉等）。会话基于 SQLite 持久化并支持 FTS5 全文检索。安装途径含二进制发布、go install 与 Docker。限制：Docker 部署中各 webhook 端口为源码硬编码，无法用配置覆盖。

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

- 支持 22+ AI 提供商及任意 OpenAI 兼容端点，多模型热切换
- TUI（BubbleTea）+ Vue 3 Web 仪表盘双界面
- 15+ 内置工具、技能系统与 MCP 协议接入
- Bot 模式支持命名 Agent 档案与跨实例 HTTP 互联

## 适用场景

- 通过命令行或 Web 界面与多提供商 AI 模型对话
- 把 Agent 接入 Telegram/飞书/钉钉等消息平台
- 用多 Agent 群聊与 Bot 档案组织协作任务
- 统计各模型/会话的 Token 消耗

## 场景标签

`Agent 框架` `多智能体` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: go-magic is a full-featured AI Agent framework that combines a powerful Go backend with a modern Vue 3/TypeScript w
> L17: DeepSeek, OpenAI, Anthropic, Gemini, Ollama, vLLM, Groq, 硅基流动, 智谱GLM, 通义千问, 文心一言, MiniMax, MiMo, 腾讯混元, 豆包(火山引擎), Mo

## 星数曲线

```mermaid
xychart-beta
    title "magicwubiao/go-magic 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-30 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `856dcf051dfa` · [字段定义](../../DATASET.md)*
