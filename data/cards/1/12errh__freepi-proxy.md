# 12errh/freepi-proxy

⭐ 3 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/12errh/freepi-proxy) · 个人维护

**面向编码 Agent 的本地免费推理代理：OpenAI/Anthropic 兼容接口+仪表盘**

零依赖的本地代理，将 free-pi（广告资助的社区推理服务）包装为 OpenAI 兼容 Chat Completions、Anthropic 兼容 Messages 与 MCP（Streamable HTTP）服务器，使编码 Agent 能用免费额度而非付费 API key。提供单文件 HTML 仪表盘（额度/用量图表、请求日志、模型目录、内置流式 Chat）。凭据通过 GitHub device-flow 登录写入本地文件；服务仅绑定 127.0.0.1。限制：需保持 Overview 标签页打开以展示广告，否则上游会以 ads_required 暂停补全；项目声明为非官方，上游行为可随时变更。

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

- 提供 OpenAI 与 Anthropic 兼容端点及 MCP 工具服务器（generate_image/web_search/docs_lookup/check_usage）
- 零依赖，Node ≥ 22.19 或 Bun 直接运行 TypeScript 源码，无构建步骤
- 单文件 HTML 仪表盘：额度图表、请求日志、模型目录、内置流式 Chat
- freepi-proxy claude 命令以 JSON settings 配置接入 Claude Code 且不改动用户配置文件

## 适用场景

- 让编码 Agent 通过本地代理消耗 free-pi 每日免费额度
- 用内置 Chat 界面流式对话并追踪 token 与额度消耗
- 在 OpenCode/omp 等客户端中配置 MCP 图像生成与网页搜索工具

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A **zero-dependency** local proxy, dashboard, chat UI, and MCP server for
> L8: - **OpenAI-compatible** Chat Completions at `/v1/chat/completions` + model discovery at `/v1/models`
> L86: Nothing is exposed beyond loopback: the server binds `127.0.0.1` only and requires no API key of


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `e8e729d4d9df` · [字段定义](../../DATASET.md)*
