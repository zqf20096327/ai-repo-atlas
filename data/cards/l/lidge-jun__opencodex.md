# lidge-jun/opencodex

⭐ 18,728 · TypeScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/lidge-jun/opencodex) · [官网](https://opencodex.me/) · 个人维护

**本地 AI 网关：让编码工具接入任意 LLM 提供商**

opencodex 是运行在本地的轻量网关，位于 Codex、Claude Code、Claude Desktop、Grok Build 等编码工具与模型提供商之间：接收 Responses、Chat Completions、Anthropic Messages 三种 API 并翻译为各提供商的协议，承载流式输出、工具调用、推理与图像。内置 40+ 提供商，支持 provider/model 路由语法、组合模型（failover/加权轮询）、子代理路由、OAuth 登录及 web 搜索/视觉 sidecar。通过 npm 全局安装并运行 `ocx start`，提供 localhost:10100 网页仪表盘；另提供 macOS/Windows/Linux 桌面安装包，CLI 安装需 Node 18+。

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

- 接收三种 API 并翻译为各提供商协议，承载流式/工具调用/推理/图像
- 40+ 内置提供商及任意 OpenAI 兼容端点，provider/model 路由语法
- Combo 组合模型支持 failover 与加权轮询；子代理可路由任意模型
- 仪表盘展示提供商状态、OAuth、模型选择与实时请求日志

## 适用场景

- 在 Codex CLI 中使用 Claude、Gemini、DeepSeek 等非默认模型
- 让 Claude Code 通过本地代理运行 Ollama 本地模型
- 为多个模型配置故障切换的组合模型
- 在本地仪表盘集中管理各工具的提供商账户与请求日志

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L50: opencodex is a lightweight local gateway between your coding tools and your model providers. It
> L51: accepts the Responses, Chat Completions and Anthropic Messages APIs and translates each request into
> L127: - **Use any LLM with Codex, Claude Code, Claude Desktop, and Grok Build** — 40+ providers out of

## 星数曲线

```mermaid
xychart-beta
    title "lidge-jun/opencodex 星数(近 28 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 17627 --> 18807
    line [17725, 17781, 17821, 17843, 17890, 17930, 17970, 18008, 18034, 18068, 18107, 18138, 17843, 18298, 18359, 18399, 18441, 18487, 18532, 18575, 18599, 18613, 18637, 18666, 18685, 18697, 18709, 18709]
```

2026-10-22 17,725 → 2026-11-24 18,709（+984）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `b9b3d67507bf` · [字段定义](../../DATASET.md)*
