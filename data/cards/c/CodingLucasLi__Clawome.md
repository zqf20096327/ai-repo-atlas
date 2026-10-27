# CodingLucasLi/Clawome

⭐ 96 · Python · Apache-2.0 · 推送 2026-03-14 · [GitHub](https://github.com/CodingLucasLi/Clawome) · [官网](https://clawome.com/) · 个人维护 · 中文 README

**开源 AI 浏览器代理：用自然语言指派任务，自动浏览网页并返回结果**

面向终端用户与开发者的 AI 浏览器代理工具：用户以自然语言下达任务，内置聊天助手 Beanie 理解上下文并处理追问，复杂多步任务交给基于 LangGraph 状态机的 Runner 规划、浏览并提取信息。采用 Playwright 驱动 Chromium，提供 100:1 的 DOM 压缩以降低 token 消耗，支持 12 家以上 LLM 提供商及自定义 OpenAI 兼容端点。通过 pip 安装，附带 Web 仪表盘、Chat/Browser REST API 与会话持久化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双层代理架构：Beanie 聊天代理 + LangGraph Runner 任务引擎
- DOM 压缩：典型页面约 100:1，保留可见文本与可交互元素
- Guard 节点自动处理 CAPTCHA、Cookie 弹窗与被拦截页面
- 12+ LLM 提供商支持，含任意 OpenAI 兼容自定义端点

## 适用场景

- 让 AI 代替我浏览网页查找、对比并汇总信息
- 通过网页仪表盘与 AI 助手多轮对话委派浏览任务
- 在自己的 agent 中独立调用其 DOM 压缩与浏览器 API

## 场景标签

`浏览器自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L7:  Open-source AI browser agent. Tell it what you want — it browses the web and brings back results.
> L105: You ──→ Beanie (Chat Agent) ──→ Runner (Task Engine) ──→ Browser

## 星数曲线

```mermaid
xychart-beta
    title "CodingLucasLi/Clawome 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 94 --> 97
    line [95, 96, 96]
```

2026-10-18 95 → 2026-10-27 96（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `92b4594d4d0f` · [字段定义](../../DATASET.md)*
