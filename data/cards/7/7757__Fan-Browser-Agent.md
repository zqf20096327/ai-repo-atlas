# 7757/Fan-Browser-Agent

⭐ 40 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/7757/Fan-Browser-Agent) · [官网](https://fandcode.com) · 个人维护 · 中文 README

**开源桌面浏览器 AI agent，人机协同完成网页任务**

Electron 桌面应用 + 内嵌 Chromium + 本地 Python agent 运行时的桌面 AI agent：用户描述目标后，agent 观察实时页面、规划步骤、操作浏览器并整理结果；遇到登录、验证码、敏感字段或重要决策时暂停并交还控制权。面向需要在可见浏览器中完成表单填写、文献检索、包裹查询等真实网页任务的用户。面向模型的浏览器 API 精简为 snapshot/run/handoff 三个接口以控制 token 消耗。配置、会话、Skills 与任务历史默认存本地，支持自带模型（内置 provider 或 OpenAI 兼容端点）。当前为未签名的早期预览版本（0.4.3）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内嵌可见浏览器中执行任务的 agent，关键步骤暂停交还人工确认
- 面向模型的浏览器 API 精简为 browser_snapshot/browser_run/browser_handoff 三个接口
- 本地优先：配置、会话、Skills、任务历史默认存于本机，无需产品账号
- 支持 DeepSeek、DashScope、Ollama Cloud 等内置 provider 及 OpenAI 兼容自定义端点
- 支持本地定时任务、Skills、MCP 与插件扩展，可派发子 agent

## 适用场景

- 在可见浏览器中让 AI 代填签证申请等网页表单，敏感步骤由本人确认
- 跨多个标签页做文献检索并生成可核查的摘要
- 把常用网页工作流沉淀为 Skills、插件或定时任务复用

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5:  An open-source desktop AI agent that works with you in a real, visible browser.
> L19: Fan brings an Electron desktop app, an embedded Chromium browser, and a local Python agent runtime into one workspa
> L21: It is more than a chat window that tells you what to do, and it does not require a hand-written automation script f

## 星数曲线

```mermaid
xychart-beta
    title "7757/Fan-Browser-Agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-25 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cbe8aae3a80c` · [字段定义](../../DATASET.md)*
