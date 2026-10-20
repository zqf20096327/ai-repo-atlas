# lidge-jun/opencodex

⭐ 17,563 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/lidge-jun/opencodex) · [官网](https://opencodex.me/) · 个人维护 · 中文 README

**本地代理：让 Codex/Claude Code 等工具运行任意 LLM**

opencodex 是一个本地代理服务，将 Codex 的 Responses API 翻译为各提供商的协议（流式、工具调用、推理 token、图像双向转换），使 Claude Code、Codex、Claude Desktop、Grok Build 可调用 40+ 内置提供商或任意 OpenAI 兼容端点。通过 `provider/model` 语法路由模型，支持 Combo 故障转移/加权轮询、子代理任意模型、ChatGPT 账号池配额路由、xAI/Anthropic/Kimi OAuth 登录。CLI 经 npm 安装（Node 18+，Bun 运行时自动捆绑），另提供 beta 桌面应用（.dmg/.msi/.AppImage/.deb），仪表盘运行在 localhost:10100。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.8 天,年发版 100,224 位贡献者
- 涨星:近 1 天 **+59**(自 20261016 起算)
- 安装:npm 包 `@bitkyc08/opencodex` 月下载 97,261
- 平台:WINDOWS / MACOS / LINUX · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- 将 Codex Responses API 翻译为各提供商协议，40+ 内置提供商
- ChatGPT 账号池：配额刷新、最低用量路由、线程亲和
- Combo 虚拟模型：跨提供商 failover 或加权轮询
- 内存有界管理：14 个保留存储按 256 MiB 预算驱逐

## 适用场景

- 让 Codex CLI 改用 Claude、Gemini、Ollama 等非 OpenAI 模型干活
- 管理多个 ChatGPT 账号自动分摊 Codex 配额
- 在仪表盘集中查看各提供商状态与实时请求日志
- 为子代理挑选不同厂商模型并配置回退链

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L48: opencodex is a lightweight local proxy that translates Codex's Responses API into whatever your
> L120: - **Use any LLM with Codex, Claude Code, Claude Desktop, and Grok Build** — 40+ providers out of
> L114: The CLI install requires Node 18+; the desktop app needs neither Node nor Bun. The Bun runtime is bundled on `npm 

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `eab8d2382778` · [字段定义](../../DATASET.md)*
