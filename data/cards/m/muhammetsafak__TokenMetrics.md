# muhammetsafak/TokenMetrics

⭐ 3 · Go · GPL-3.0 · 推送 2026-11-17 · [GitHub](https://github.com/muhammetsafak/TokenMetrics) · 个人维护

**桌面应用：统计本地 AI 工具的 token 用量与成本估算**

基于 Wails（Go + Web 前端）构建的桌面应用，读取 Claude Code、Codex CLI、Gemini CLI 的本地日志文件及 Anthropic/OpenAI Admin API，将 token 用量与估算成本存入本地 SQLite 数据库，按服务、模型、项目、会话和时间维度统计，提供 5 小时/周订阅窗口的限额追踪、预算阈值系统通知、JSON/CSV 导入导出。数据全部留在本机，不读取提示词内容；界面语言为土耳其语；当前为 Beta（0.y.z），成本与限额均为近似估算值。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从本地日志增量扫描 token 用量，删除原日志后已存数据保留
- 按服务/模型/项目/会话/时间多维统计与对比表
- 预算阈值触发 OS 通知与托盘图标提醒，支持系统托盘常驻
- 内置 verify-claude/verify-codex 独立解析器交叉核验统计结果

## 适用场景

- 追踪多个 AI CLI 工具的 token 消耗与费用
- 监控订阅限额的 5 小时与每周使用窗口
- 离线导出 JSON/CSV 归档或迁移用量数据

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: A desktop app that tracks AI token usage and estimated cost from local logs and admin APIs.
> L13: local database and breaks it down by service, model, project, session and time.

## 星数曲线

```mermaid
xychart-beta
    title "muhammetsafak/TokenMetrics 星数(近 2 点)"
    x-axis ["2026-11-14", "2026-11-21"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-14 3 → 2026-11-21 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `220daac1af53` · [字段定义](../../DATASET.md)*
