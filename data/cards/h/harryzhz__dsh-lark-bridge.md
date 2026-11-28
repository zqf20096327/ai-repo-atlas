# harryzhz/dsh-lark-bridge

⭐ 5 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/harryzhz/dsh-lark-bridge) · 个人维护 · 中文 README

**把 Claude Code/Codex 等 Coding Agent 接入飞书群的 DSH 插件**

基于 DeepSeek Harness (DSH) 构建的飞书/Lark 桥接插件：通过官方 WebSocket 长连接接入，无需公网服务器；支持为不同群绑定代码仓库、运行时与并发配置；内置消息分流、逐成员主动监听、SQLite+FTS5 跨运行时长期记忆、夜间 Auto-Dream 复盘、A@B 委派跟进与驾驶舱可观测视图。依赖 DSH >= 0.2.2-rc.5 运行，以双插件（本插件 + dsh-external-agents）形式安装，支持一键脚本、界面或 CLI 三种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于飞书官方 WebSocket 长连接，零公网暴露
- 通过 dsh-external-agents 接入 Claude Code / Codex / Antigravity / TRAE CLI 等外部 Coding Agent
- SQLite + FTS5 混合检索的跨运行时长期记忆与 Auto-Dream 夜间复盘
- 告警主动监听、委派跟进与免重启热更新

## 适用场景

- 研发群里 @机器人 查代码、定位根因、改代码提 PR
- 告警群自动值守：P0/P1 告警秒开话题给止损与根因
- 同事间 A@B 指派任务自动跟进与到期催办
- 每日定时巡检并按需推送图文卡片

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L18: > 基于 DeepSeek Harness (DSH)（Desktop & Web）构建，受 dsh-superagent 与 botmux 启发。默认使用 DSH 原生预设与模型；一键安装脚本已配套 dsh-external-a
> L25:  默认直接使用 DSH 原生预设与模型；搭配 dsh-external-agents 开箱支持 **Claude Code / Codex / Antigravity / TRAE CLI**。研发群、告警群、发布群可各自绑定代码


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `17bbf81cd632` · [字段定义](../../DATASET.md)*
