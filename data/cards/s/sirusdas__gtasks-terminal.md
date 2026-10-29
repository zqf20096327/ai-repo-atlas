# sirusdas/gtasks-terminal

⭐ 37 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/sirusdas/gtasks-terminal) · 个人维护

**终端中管理 Google Tasks 的 CLI：过滤、去重、同步、报表与多账号**

基于 Python 的 Google Tasks 命令行工具，面向偏好终端操作的用户：提供任务的增删改查、按状态/优先级/标签/日期的过滤、多账号管理与隔离存储、任务去重、双向同步（含冲突解决与标签提取）、任务恢复备份、外部编辑器集成与分析报告生成，并带键盘驱动的交互模式。通过 OAuth 2.0 认证接入 Google Tasks API，配置与数据存于 ~/.gtasks 目录。AI 为可选功能：可配置 OpenAI/Anthropic/Gemini 以自然语言管理任务，并可启动 MCP server 供外部 AI agent 调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任务去重、双向同步与冲突解决、增量同步
- 多账号管理与每账号独立凭据存储
- 自然语言 AI 助手（OpenAI/Anthropic/Gemini 可选）与 MCP server 模式
- 分析报告生成：完成趋势、逾期分析、状态/优先级/标签分布

## 适用场景

- 在终端里高效管理我的 Google Tasks
- 在个人与工作等多个 Google 账号间切换处理任务
- 让 Claude Desktop 等 AI agent 通过 MCP 直接操作我的任务列表
- 生成任务完成情况的定期分析报告

## 场景标签

 · 领域:效率工具/任务管理

## 证据(README 行号)

> L15: 1. **Basic Task Management**: Add, list, update, and delete tasks
> L277: ### AI Assistant
> L288: Expose `gtasks` as a tool for external AI agents (like Claude Desktop):

## 星数曲线

```mermaid
xychart-beta
    title "sirusdas/gtasks-terminal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-29 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1e1bb5fe4fbd` · [字段定义](../../DATASET.md)*
