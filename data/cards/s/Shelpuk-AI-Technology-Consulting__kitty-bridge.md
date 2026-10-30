# Shelpuk-AI-Technology-Consulting/kitty-bridge

⭐ 16 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Shelpuk-AI-Technology-Consulting/kitty-bridge) · [官网](https://www.shelpuk.com) · 组织维护

**本地 LLM 代理桥：让 Claude Code/Codex 等编码 agent 接入任意模型商**

运行在本机的协议翻译代理：架在编码 agent（Claude Code、Codex CLI、Gemini CLI、Kilo Code）与上游 LLM 提供商之间，实时转换各 agent 原生协议。支持 API key 与订阅账号（ChatGPT/Claude 订阅经浏览器 OAuth 或设备码登录）两种认证，可创建多提供商均衡池，请求随机分发、故障自动重试。README 明确声明 Kitty 内部不使用 LLM，仅做代理与翻译，无文件系统或 shell 权限。pip 安装，需 Python 3.10+，支持 Linux/Windows/macOS。限制：Claude 订阅转发仅可用于 Claude Code。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令将编码 agent 指向任意提供商，实时协议翻译
- 支持 ChatGPT/Claude 订阅账号认证（OAuth 与无头机器设备码登录）
- 均衡池：多提供商随机分发、故障转移、成员可标记为备份
- 本机运行、无文件系统/shell 权限、内部不使用 LLM

## 适用场景

- 用 MiniMax/GLM 等较低价提供商驱动 Claude Code 或 Codex
- 复用已有 ChatGPT 或 Claude 订阅而非单独购买 API 额度
- 把贵模型与便宜模型混搭降低长会话成本
- 多提供商池化应对单一提供商限流或宕机

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L41: Agent (Claude Code / Codex / Gemini / Kilo) → Kitty Bridge → any LLM provider
> L44: Kitty sits between your coding agent and the upstream provider, translating each agent's native protocol in real ti
> L52: ✅ **Just a bridge** — Kitty only proxies and translates traffic between the coding agent and the backend model API.
> L55: ✅ **No AI inside Kitty** — Kitty does not use an LLM, embeddings, or any other AI system internally. It is a

## 星数曲线

```mermaid
xychart-beta
    title "Shelpuk-AI-Technology-Consulting/kitty-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bb46ac8a130a` · [字段定义](../../DATASET.md)*
