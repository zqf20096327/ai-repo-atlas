# bojackduy/opencode-web-bridges

⭐ — · [GitHub]() · 个人维护

**将已有 ChatGPT/Gemini 等网页登录会话接入 OpenCode 的插件**

面向 OpenCode 用户的插件：通过浏览器会话（CDP）或 HTTP+SSE 把 ChatGPT、Gemini、DeepSeek、Meta AI 的网页版接入为 OpenCode 可选模型，复用已有订阅登录、无需 API key 与按 token 计费。提供一行式 npx 安装、fail-closed 恢复（中断回合不重复提交）与校验和验证的二进制；AGPL-3.0 开源。依赖 Node.js 20+、OpenCode v1/v2、Bun 1.1+ 与 Chrome/Chromium。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 复用已登录浏览器会话，无需 API key
- 四个引擎：ChatGPT/Gemini/Meta AI 走浏览器 CDP，DeepSeek 走 HTTP+SSE 支持工具调用
- 一行式 npx 安装，二进制经校验和验证
- fail-closed 恢复，中断回合不重复提交

## 适用场景

- 用已有 ChatGPT 订阅在 OpenCode 里写代码，避免 API 费用
- 在同一编辑环境中并排使用多个网页版大模型
- 用 DeepSeek 网页通道获得工具调用能力

## 场景标签

`模型网关` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: ## Use ChatGPT, Gemini, DeepSeek & Meta AI inside OpenCode — no API key
> L14: - **One-line install** — `npx @bojackduy/opencode-web-bridges install`

## 星数曲线

```mermaid
xychart-beta
    title "bojackduy/opencode-web-bridges 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-22 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `ebd226f6b99a` · [字段定义](../../DATASET.md)*
