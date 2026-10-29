# prime-radiant-inc/llm-proxy

⭐ 31 · Go · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/prime-radiant-inc/llm-proxy) · 组织维护

**LLM API 流量的透明日志代理：记录每个请求与响应**

位于 LLM 客户端（Claude Code、Codex、API 脚本）与提供商 API 之间的透明代理：将全部请求/响应以 JSONL 记录到 ~/.llm-provider-logs/，按提供商与日期组织，含时间与元数据。安装后自动配置 shell（通过 ANTHROPIC_BASE_URL / OPENAI_BASE_URL 重定向流量），以后台服务运行。支持 Anthropic、OpenAI 及任意 OpenAI 兼容 API，可作 AWS Bedrock 的 SigV4 签名代理。可选将日志实时推送 Grafana Loki，并提供 Web UI 浏览与全文检索日志。macOS 用 Homebrew、Linux 用安装脚本安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 记录所有 LLM 请求/响应对到本地 JSONL 日志，含时间与会话元数据
- 安装后自动配置 shell 环境变量，客户端无需改动
- AWS Bedrock 签名代理模式：代理处理 SigV4 签名，客户端无需直接管理 AWS 凭据
- 可选 Loki 实时导出与内置 Web 日志浏览器（会话列表、全文检索）

## 适用场景

- 调试和审计我的 LLM 客户端与 API 之间的全部交互
- 聚合多台机器或容器环境的 LLM 日志到中心化观测系统
- 让 Claude Code 通过代理接入 Bedrock 而不直接管理 AWS 凭据

## 场景标签

`LLM 可观测性` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A transparent logging proxy for LLM API traffic. Install once, and every request to Claude, ChatGPT, or other LLM pr
> L28: LLM Proxy sits between your LLM clients (Claude Code, Codex, API scripts) and the provider APIs. It:
> L125: - **Anthropic** (Claude, Claude Code)

## 星数曲线

```mermaid
xychart-beta
    title "prime-radiant-inc/llm-proxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-29 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bfada72c5070` · [字段定义](../../DATASET.md)*
