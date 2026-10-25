# xberg-io/liter-llm

⭐ 263 · Rust · MIT · 推送 2026-10-25 · [GitHub](https://github.com/xberg-io/liter-llm) · [官网](https://docs.liter-llm.xberg.io) · 组织维护

**统一 LLM API 客户端：174 家供应商一套接口，14 种语言绑定**

以单一 Rust 核心构建的通用 LLM API 客户端：同一套 chat() 接口接入 174 家供应商（OpenAI、Anthropic、Google、AWS Bedrock 等），更换模型仅需改名称。同一核心编译出 Rust、Python、Node.js、Go、Java、C#、Ruby、PHP、Elixir、Dart、Swift、Zig、WASM 等 14 种原生绑定及 C/FFI 接口。CLI 单二进制（35MB）内置 OpenAI 兼容代理（22 个端点）、MCP 工具服务器，支持按成本/延迟/权重路由与自动回退、速率限制、缓存、成本追踪；本地模型经 OpenAI 兼容 API 接入 Ollama、vLLM、llama.cpp 等。另为 Claude Code、Cursor、Copilot 等编码助手提供插件与 Agent Skills。注意：已发布的 CLI 2.2.3 缺少部分修复，无额外鉴权配置启动需按指引源码构建。

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

## 能力要点

- 174 家供应商编译期内置，单一 API 换模型只改名称
- 14 种原生语言绑定共享同一 Rust 核心，行为一致
- 35MB 单二进制含 OpenAI 兼容代理与 MCP 服务器
- Tower 中间件：限流、缓存（40+ OpenDAL 后端）、成本追踪、预算与回退

## 适用场景

- 在 Python/TypeScript/Go 等项目中用统一接口调用多家 LLM 供应商
- 通过内置代理让现有 OpenAI SDK 直连其他供应商
- 为编码助手（Claude Code/Cursor 等）挂载跨供应商的 MCP 工具服务器
- 按成本或延迟在多供应商间路由并自动故障回退

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L71: liter-llm gives you a single, consistent way to call any large language model. Reach 174 providers — OpenAI, Anthro
> L76: - **One small binary** — the client, a drop-in OpenAI-compatible proxy, and an MCP server for AI agents ship in a s
> L96: |**Local LLM support**|Ollama, LM Studio, vLLM, llama.cpp, LocalAI, and llamafile via OpenAI-compatible APIs|

## 星数曲线

```mermaid
xychart-beta
    title "xberg-io/liter-llm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 260 --> 263
    line [261, 262, 262]
```

2026-10-18 261 → 2026-10-25 262（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `baefe2e6cb87` · [字段定义](../../DATASET.md)*
