# supastishn/AutoMate

⭐ 21 · TypeScript · MIT · 推送 2026-03-06 · [GitHub](https://github.com/supastishn/AutoMate) · 个人维护

**自托管个人 AI agent：多渠道、可调用工具、插件扩展**

TypeScript 编写的自托管个人 AI 助手平台，运行于用户自有硬件（服务器到 Android 平板/Termux 均可）。接入任意 OpenAI 兼容 LLM（OpenAI、Anthropic 代理、Ollama、LM Studio 等），提供 Web UI、Discord、CLI 三种交互渠道。内置 30+ 工具（shell、文件、隐身浏览器自动化、网页搜索、图片分析/生成、cron 等），支持双层持久记忆与向量检索、并行子 agent、热重载插件与 SKILL.md 技能、定时自主巡检（heartbeat）。浏览器自动化依赖可选的 Python 3.10+ 与 Chrome/Chromium。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30+ 内置工具，按会话懒加载
- Python 隐身浏览器引擎（undetected-chromedriver，人类化输入与点击）
- 双层记忆（日志 + MEMORY.md）与向量+BM25 混合检索
- 热重载 JS 插件系统与 SKILL.md 技能、ClawHub 技能注册表

## 适用场景

- 在自己服务器上跑一个跨 Discord/Web/CLI 的个人 AI 助手
- 让 agent 定时执行任务、操作浏览器和处理文件
- 用低配置设备（如 Android + Termux）运行精简 agent

## 场景标签

`AI 助手` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: AutoMate is a personal AI assistant platform that runs on your own hardware. Connect any OpenAI-compatible LLM, giv
> L19: - **30+ built-in tools** — Shell, file ops, browser automation, web search, image analysis/generation, cron jobs, b
> L105: |Agent|`src/agent/agent.ts`|Core agent loop — LLM calls, tool execution, context management|

## 星数曲线

```mermaid
xychart-beta
    title "supastishn/AutoMate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `333f7500f91f` · [字段定义](../../DATASET.md)*
