# Jeomon/Web-Use

⭐ 302 · Python · MIT · 推送 2026-08-06 · [GitHub](https://github.com/Jeomon/Web-Use) · 个人维护

**基于 CDP 与 LLM 的自主浏览器代理框架**

Python 编写的浏览器自动化代理框架：通过 Chrome DevTools Protocol 读取真实 DOM 构建带角色与文本的语义树，由 LLM（支持 Claude、Gemini、OpenAI、Groq、Ollama、Cerebras、Mistral 等）驱动导航、表单填写、文件上传下载等操作。内置 OAuth 2.0 + PKCE 认证流程与令牌持久化，支持 WebMCP 协议自动发现并调用网站暴露的工具，可选截图视觉理解。面向开发者以源码方式克隆安装，需 Python 3.11+ 与 uv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CDP 捕获真实 DOM 构建语义树（角色/id/类/文本）
- 多 LLM 接入：Claude、Gemini、OpenAI、Groq、Ollama、Cerebras、Mistral 等
- OAuth 2.0 + PKCE 内置认证流与令牌持久化存储
- WebMCP 协议自动发现并注册网站自定义工具

## 适用场景

- 用自然语言指令让代理完成网页查询、发帖、播放视频等任务
- 自动化需要登录的 OAuth 保护网站上的操作流程
- 调用支持 WebMCP 的网站工具完成文档检索等任务

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L16: **Web-Use** is an intelligent autonomous browsing agent, built to seamlessly navigate websites, interact with dynam
> L21: - **🛠️ Multi-LLM Support** — Works with Anthropic Claude, Google Gemini, OpenAI, Groq, Ollama, Cerebras, Mistral, a

## 星数曲线

```mermaid
xychart-beta
    title "Jeomon/Web-Use 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 300 --> 303
    line [301, 302, 302]
```

2026-10-18 301 → 2026-10-29 302（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3d49440d61dc` · [字段定义](../../DATASET.md)*
