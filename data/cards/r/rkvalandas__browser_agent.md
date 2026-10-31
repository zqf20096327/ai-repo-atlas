# rkvalandas/browser_agent

⭐ 37 · Python · MIT · 推送 2025-11-22 · [GitHub](https://github.com/rkvalandas/browser_agent) · 个人维护

**用自然语言控制浏览器的 AI 自动化代理（Python/Playwright）**

Python 应用，基于 Playwright 与 LLM（支持 OpenAI、Azure OpenAI、Groq、Anthropic）实现自然语言驱动的浏览器控制：自动检测与映射页面可交互元素、上下文感知导航、填表与提交、处理动态内容与错误恢复，任务执行中可向用户询问信息。可连接已有 Chrome 或启动新实例。需 Python 3.11+、Chrome 浏览器，推荐用 uv 安装运行。README 声明限制：无法处理 CAPTCHA 与复杂认证，不适用于银行等高安全操作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言指令驱动浏览器操作（导航、点击、填表）
- 自动检测与映射页面可交互元素，含历史与状态感知
- 支持 OpenAI、Azure OpenAI、Groq、Anthropic 多家 LLM 提供商
- 处理 AJAX、无限滚动、弹窗等动态内容并提供错误恢复

## 适用场景

- 用自然语言自动完成重复性网页任务
- 以自然语言对 Web 应用做站点测试
- 从网页中收集和提取信息
- 陪伴用户完成复杂流程的交互式浏览

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L19: Browser Agent is a sophisticated Python application that enables users to control web browsers through natural lang
> L41: - **🔧 Multiple LLM Providers**: Support for OpenAI, Azure OpenAI, Groq, and Anthropic (Claude Sonnet 4.5)

## 星数曲线

```mermaid
xychart-beta
    title "rkvalandas/browser_agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-31 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c0ce0e160dfa` · [字段定义](../../DATASET.md)*
