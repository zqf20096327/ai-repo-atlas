# madderscientist/WebAI2API

⭐ 36 · TypeScript · 推送 2026-09-19 · [GitHub](https://github.com/madderscientist/WebAI2API) · 个人维护 · 中文 README

**封装 DeepSeek 网页端为 OpenAI 兼容 API 的自用工具**

对 DeepSeek 网页接口（非官方 API Key 接口）的逆向封装，提供 OpenAI 兼容的 completions 与 responses 两套 HTTP API，利用网页自带的记忆管理复用对话，并通过提示词工程实现 tool-calling，可接入 CodeX、Copilot、QQbot 等。支持 API 请求与浏览器操作两种调用方式，含流式（仅 API 方式）。作者声明为个人练手自用，未为大规模使用设计，且明确提示逆向与反代的风险及账号封禁免责。仅支持 Windows，需 Node.js 20+、pnpm 与本机 Chrome/Edge。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 兼容的 completions 与 responses 双 API，responses 复用网页会话免维护上下文
- 通过提示词工程实现 tool-calling
- 提供凭证抓取（auth）与 HTTP 服务（server）两条命令链
- 给出 CodeX 与 VSCode Copilot 的接入配置

## 适用场景

- 把免费的 DeepSeek 网页端包装成 OpenAI 兼容接口供本地工具调用
- 让 CodeX / Copilot 通过本地端点使用 DeepSeek
- QQbot 等跨语言服务经 HTTP 调用 DeepSeek

## 场景标签

 · 领域:LLM 基础设施/API 封装

## 证据(README 行号)

> L4: 目标：实现个人免费的AI调用(如接入CodeX、Copilot、QQbot)，兼容OpenAI接口，具备工具执行的能力。个人练手（代码手写）
> L13: > 本项目调用的是 DeepSeek Web 接口，不是官方 `api.deepseek.com` API Key 接口。
> L100: 由于QQbot使用了nonebot，跨语言调用需要走网络请求。传统封装仅仅是 `completions` API，但由于网页AI自带记忆管理，因此 `Responses` API 更为合适。本项目两个都实现了，并用提示词工程实现

## 星数曲线

```mermaid
xychart-beta
    title "madderscientist/WebAI2API 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26", "2026-10-28"]
    y-axis "stars" 32 --> 37
    line [33, 34, 36, 36]
```

2026-10-18 33 → 2026-10-28 36（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d15b52768123` · [字段定义](../../DATASET.md)*
