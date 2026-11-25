# billy-enrizky/openbrowser-ai

⭐ 279 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/billy-enrizky/openbrowser-ai) · [官网](https://docs.openbrowser.me/) · 个人维护

**面向开发者的 LLM 驱动浏览器自动化框架，用 CDP 执行网页操作**

OpenBrowser 是一个 Python 编写的智能浏览器自动化框架，通过 Chrome DevTools Protocol 直接通信，采用 CodeAgent 架构：LLM 生成 Python 代码并在持久化命名空间中执行，自主完成网页导航、交互与信息提取。支持截图视觉理解、会话录制回放（导出 Jupyter/爬虫代码）、MCP Server 接入多种 AI 助手、CLI 守护进程与插件系统。要求 Python 3.12+，自动检测本地 Chromium 系浏览器，提供托管云版（cookie 保存与定时任务）的等待名单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CodeAgent 架构：LLM 在持久化 Jupyter 式命名空间中编写并执行浏览器自动化代码
- 直接使用 Chrome DevTools Protocol 通信
- 支持 15 家 LLM 提供商（含本地 Ollama）
- MCP Server 与 Claude Code 插件（8 个引导技能）

## 适用场景

- 自动抓取电商商品信息
- 自动完成机票预订等网页操作流程
- 自动填写网页表单
- 作为 Claude Code/Claude Desktop 的浏览器操作技能

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L32: OpenBrowser is a framework for intelligent browser automation. It combines direct CDP communication with a CodeAgen
> L42: - **CodeAgent Architecture** - LLM writes Python code in a persistent Jupyter-like namespace for browser automation
> L45: - **15 LLM Providers** - OpenAI, Anthropic, Google, Groq, AWS Bedrock, Azure, Ollama, DeepSeek, Cerebras, OpenRoute

## 星数曲线

```mermaid
xychart-beta
    title "billy-enrizky/openbrowser-ai 星数(近 6 点)"
    x-axis ["2026-10-23", "2026-11-02", "2026-11-06", "2026-11-11", "2026-11-14", "2026-11-25"]
    y-axis "stars" 278 --> 281
    line [279, 280, 279, 280, 279, 279]
```

2026-10-23 279 → 2026-11-25 279（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 low · 依据 README sha `2a2afbe9bac2` · [字段定义](../../DATASET.md)*
