# antonis19/autobrowse

⭐ 113 · Python · 推送 2026-08-29 · [GitHub](https://github.com/antonis19/autobrowse) · 个人维护

**自主 AI agent：接收任务后自动操作浏览器完成网页操作**

AutoBrowse 是一个自主网页浏览 agent：用户给出自然语言任务（如订酒店、注册账号、搜索商品），它通过三个 autogen agent 协作完成——HTML 助手用 RAG+OpenAI embeddings 分块回答页面 HTML 问题，代码生成器用 gpt-4 生成 puppeteer.js 代码，规划器协调两者。浏览器通过 websocket 连接到沙箱环境执行代码并返回渲染 HTML。需 Python 3.9 环境、OpenAI API key，并另行运行 browser-console 浏览器环境；模型与系统提示可在 agent_config.py 中修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三 agent 架构：HTML 助手、puppeteer.js 代码生成器、规划器
- HTML 经简化与 15,000 token 分块后用 RAG 检索相关片段
- 代码生成器可依据执行错误结果修正代码
- 通过 websocket 连接沙箱浏览器环境执行 puppeteer.js

## 适用场景

- 让 agent 自动完成订酒店、注册网站等网页任务
- 在网页上自动执行搜索并点击结果等操作
- 研究多 agent 协作完成浏览器自动化的实现方式

## 场景标签

`浏览器自动化` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L2: AutoBrowse is an autonomous AI agent that can browse the web.
> L61: AutoBrowse uses autogen agents and a browser console to plan and execute the task.

## 星数曲线

```mermaid
xychart-beta
    title "antonis19/autobrowse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-24 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `af2eac619159` · [字段定义](../../DATASET.md)*
