# IuCC123/CLIProxyAPI-Rust

⭐ 37 · Rust · Unlicense · 推送 2026-10-13 · [GitHub](https://github.com/IuCC123/CLIProxyAPI-Rust) · 个人维护

**把多家 AI 订阅账号聚合为一个兼容 API 的 Rust 单二进制网关**

单体 Rust 二进制代理，将 Claude、ChatGPT（Codex）、Gemini、Antigravity、Grok、Kimi、Meta、Devin、Vertex AI 等订阅账号与 API key 聚合为 OpenAI/Anthropic/Gemini 兼容端点，供 Claude Code、Codex、编辑器或任意 SDK 接入同一 URL。机制包括请求格式自动转换、多账号配额感知路由（5 小时/周配额、会话亲和、限流冷却、OAuth 自动刷新）、Codex WebSocket 中继、图像与视频生成端点，以及内置实时仪表盘。兼容 CLIProxyAPI 的凭据与 config.yaml，约 8 MB 单文件，无需 Node 或运行时。部分功能（如 banked resets）依赖非官方 provider 端点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制暴露 OpenAI/Anthropic/Gemini 兼容端点，格式自动转换、同格式直通
- 多账号配额感知路由：5 小时/周配额、会话亲和、冷却与自动 token 刷新
- 内置 WebSocket 实时仪表盘：账号配额、请求日志、登录流程、配置编辑
- 兼容 CLIProxyAPI 的凭据文件、config.yaml 两种布局与 Docker 路径，可随时切回

## 适用场景

- 让 Claude Code、Codex 等工具共用我已有的多个 AI 订阅账号
- 在 Claude Code 里用 GPT、在 Codex 里用 Claude 等跨厂商模型调用
- 多个订阅账号间自动分配配额，避免手动切换账号
- 用统一 OpenAI 兼容 base URL 接入现有 SDK 与工具链

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: A single Rust binary that exposes OpenAI, Anthropic and Gemini compatible endpoints, backed by the accounts you alre
> L24: - **Any model from any tool.** Use GPT inside Claude Code, Claude inside Codex, or Gemini behind the OpenAI SDK. Re

## 星数曲线

```mermaid
xychart-beta
    title "IuCC123/CLIProxyAPI-Rust 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 36 --> 39
    line [37, 38, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6609d875ab2e` · [字段定义](../../DATASET.md)*
