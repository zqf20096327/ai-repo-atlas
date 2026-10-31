# starbaser/ccproxy

⭐ 356 · Python · NOASSERTION · 推送 2026-08-10 · [GitHub](https://github.com/starbaser/ccproxy) · 个人维护

**面向 Claude Code 等 LLM 客户端的网络层代理与模型路由工具**

基于 mitmproxy 与 WireGuard 的透明网络拦截器：将进程置于无根 WireGuard 命名空间中，在网络层拦截 LLM 客户端流量，经 DAG 驱动的钩子管线做跨厂商请求/响应转换与重路由（Anthropic、Gemini、OpenAI/Codex、DeepSeek、Perplexity Pro）。内置 lightllm 转换层处理流式格式转换，支持 OAuth 凭据共享与刷新、shape 回放、MCP 特性桥接。Linux/WSL2 支持完整功能，macOS 仅支持反向代理模式，原生 Windows 不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WireGuard 命名空间内的透明流量捕获（Linux/WSL2）
- 跨厂商请求转换与重路由，含 DeepSeek 的 /anthropic/v1/messages 端点
- OAuth 凭据进程内刷新，可与 Claude Code CLI 共享凭据文件
- DAG 拓扑排序的钩子管线，支持按请求头覆盖

## 适用场景

- 为 Claude Code / Aider / Cursor 等客户端替换或路由底层模型
- 在厂商间转换请求/响应格式（Anthropic ↔ Gemini ↔ OpenAI 等）
- 拦截并检查 LLM 客户端的实际网络流量

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: ccproxy is a transparent network interceptor for LLM tooling and AI harnesses,
> L21: The hook pipeline is your extension point for building mods and taking control
> L23: - **Cross-provider routing**: redirect or transform requests between Anthropic,

## 星数曲线

```mermaid
xychart-beta
    title "starbaser/ccproxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 354 --> 357
    line [355, 356, 356]
```

2026-10-18 355 → 2026-10-31 356（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1c4391466df7` · [字段定义](../../DATASET.md)*
