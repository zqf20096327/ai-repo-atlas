# Mirantis/prism

⭐ 21 · Rust · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/Mirantis/prism) · [官网](https://docs.lenshq.io/prism-agent/) · 组织维护

**自托管企业 AI Agent：对话结束后仍持续记忆与执行任务**

由 Mirantis 构建并在内部使用的自托管 AI Agent：具备长期记忆、定时任务（自然语言或 cron）、心跳巡检、Webhook 事件接收，可直接编辑文件、运行 Shell 命令、调用 Claude Code/Codex 处理编码任务，并支持 Computer use 操作桌面与浏览器。Agent 身份由 Soul/User/Memory 等 7 份 Markdown 文档定义，含工具风险门控与锁定模式。接入方式覆盖 WebUI、TUI、编辑器（ACP）、Slack 与 Teams。安装支持一键脚本与 Docker；默认模型为 Claude 系列且可配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话结束后的持续执行：目标追踪、定时任务与心跳巡检
- 7 份 Markdown 文档定义 Agent 身份，可在对话内自管理
- 通过 Agent Skills 开放格式加载技能，插件遵循 Agent Plugins 标准
- WebUI/TUI/Slack/Teams/编辑器多接口接入，含工具风险门控

## 适用场景

- 让团队在 Slack/Teams 里直接分派并跟踪后台任务
- 设置定时巡检，仅在发现新情况时通知
- 把编码任务交给 Claude Code/Codex 并跟进到完成
- 用 Webhook 让外部系统事件触发 Agent 处理

## 场景标签

`AI 助手` `编码 Agent` `GUI 自动化` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Prism Agent is an enterprise-ready AI agent that keeps working after the
> L79: - **Goals** — set a background goal with `/goal` and the
> L92: - **Memory** — search, write, delete entries in its long-term memory store.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `85a2d6003c32` · [字段定义](../../DATASET.md)*
