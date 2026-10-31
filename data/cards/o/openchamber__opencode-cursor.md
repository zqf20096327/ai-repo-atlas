# openchamber/opencode-cursor

⭐ 14 · TypeScript · MIT · 推送 2026-08-21 · [GitHub](https://github.com/openchamber/opencode-cursor) · 组织维护

**OpenCode 插件：用 Cursor 订阅在 OpenCode 中运行 Cursor 模型**

面向 OpenCode 用户的 Cursor provider 插件：通过浏览器 PKCE OAuth 登录 Cursor 账号（无需 API key），自动发现订阅可用模型目录（Claude/GPT/Gemini/Grok/Composer/Cursor Auto，含 Thinking/Fast/effort 变体），经本地 OpenAI 兼容代理与 Node HTTP/2 桥接调用 Cursor API。支持流式输出、工具调用与卡顿恢复，无需 cursor-agent 二进制。要求 OpenCode、有效 Cursor 订阅、Bun 与 Node.js ≥ 18。npm 全局安装。

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

- 浏览器 PKCE OAuth 认证，令牌自动刷新，无需 API key
- 发现订阅实时模型目录并映射为 OpenCode 原生选项（含 Thinking/Fast/effort 变体）
- 本地 OpenAI 兼容代理 + HTTP/2 桥接 Cursor API，无 cursor-agent 依赖
- 流式输出、工具调用与约 90 秒卡顿恢复

## 适用场景

- 在 OpenCode 中使用 Cursor 订阅自带的模型
- 不安装 cursor-agent 直接在终端 agent 里调用 Cursor 模型
- 希望在 OpenChamber 中以 OAuth 方式接入 Cursor

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: **opencode-cursor is the OpenCode plugin for running Cursor models — Claude, GPT, Gemini, Grok, Composer, and Curso
> L33: No `cursor-agent` install and no SDK child process. OpenCode talks to a local OpenAI-compatible proxy, which talks 

## 星数曲线

```mermaid
xychart-beta
    title "openchamber/opencode-cursor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f4ba42344bb8` · [字段定义](../../DATASET.md)*
