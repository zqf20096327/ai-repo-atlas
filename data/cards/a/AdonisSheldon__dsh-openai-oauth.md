# AdonisSheldon/dsh-openai-oauth

⭐ 10 · TypeScript · MIT · 推送 2026-11-03 · [GitHub](https://github.com/AdonisSheldon/dsh-openai-oauth) · 个人维护

**DeepSeek Harness 插件：用 ChatGPT OAuth 调用 Codex 模型**

面向 DeepSeek Harness（DSH）的社区插件，通过 ChatGPT OAuth 登录使用账号目录中的 Codex 模型，无需 OpenAI API key 或 Codex CLI。提供浏览器 PKCE 与 Device Code 两种登录、自动 token 刷新、本地凭据存储，并经 DSH 既有 web provider 接口接入 Codex 原生 web_search。限制：仅支持 macOS/Linux 的 DSH 0.2.1-rc.5，Web 集成仅限绑定 127.0.0.1 的本地 Host，凭据以未加密方式存储。

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

- PKCE 浏览器登录与 Device Code 无头登录两种 OAuth 方式
- 自动 token 刷新，凭据存储在 Harness home 本地
- 经 DSH web provider 接口启用 Codex 原生 web_search，不修改 Harness 源码
- 模型与推理档位从登录账号的 Codex 目录发现

## 适用场景

- 在 DeepSeek Harness 中用 ChatGPT 账号调用 Codex 模型而无需 API key
- 为无头/远程环境提供 Device Code 登录接入 Codex
- 在 DSH 会话中通过 ChatGPT OAuth 使用 web 搜索工具

## 场景标签

`编码 Agent` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L1: dsh-openai-oauth — OpenAI OAuth community plugin for DeepSeek Harness
> L9: Sign in to ChatGPT from DeepSeek Harness and use available Codex models without an OpenAI API key or Codex CLI. The 
> L22: - DeepSeek Harness `0.2.1-rc.5`

## 星数曲线

```mermaid
xychart-beta
    title "AdonisSheldon/dsh-openai-oauth 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-08 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `d5bf4aaaaec8` · [字段定义](../../DATASET.md)*
