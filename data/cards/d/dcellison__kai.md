# dcellison/kai

⭐ 38 · Python · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/dcellison/kai) · 个人维护

**自托管常驻编码 agent 服务：人与 agent 在本机长期协作**

本地运行的 Python 服务，为编码 agent 提供常驻进程：shell、文件系统、git 与 web 访问，记忆跨会话持久化，支持定时任务、PR 审查、issue 分诊与 webhook 反应。通过浏览器端 Workshop 或 Telegram 与 agent 对话。核心是事件溯源的 SQLite 日志，五个可互换的 agent 后端（Claude Code、Codex CLI、Goose、OpenCode、Pi），经后端覆盖 OpenAI、DeepSeek、Ollama 等提供商。多用户隔离、本地向量记忆、whisper.cpp 语音转录；单 Python 进程，以 LaunchDaemon/systemd 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个可互换 agent 后端，提供商是配置项而非结构性依赖
- 事件溯源核心：SQLite 追加日志，状态可重建、消息持久确认
- 按人/项目隔离的本地向量记忆与多用户 OS 级隔离
- GitHub 自动化、定时任务与 webhook 反应在后台运行

## 适用场景

- 让编码 agent 常驻本机，跨会话记住我的偏好与项目上下文
- 推送 PR 后自动审查、issue 开启后自动分诊
- 通过 Telegram 或浏览器与 agent 协作并委派任务

## 场景标签

`编码 Agent` `Agent 记忆` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L10: Kai is a self-hosted service that gives coding agents a durable home: persistent processes with shell, filesystem, 
> L24: - **No vendor holds the keys.** Five interchangeable agent backends mean the provider is a configuration choice, no
> L42: Each Kai backend is a full coding harness with its own protocol, tools, and authentication. Kai normalizes lifecycl

## 星数曲线

```mermaid
xychart-beta
    title "dcellison/kai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `502b593e9cee` · [字段定义](../../DATASET.md)*
