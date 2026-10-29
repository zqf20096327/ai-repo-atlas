# roeimichael/ContextAnalyzerTerminal

⭐ 18 · Python · MIT · 推送 2026-04-07 · [GitHub](https://github.com/roeimichael/ContextAnalyzerTerminal) · 个人维护

**监测 Claude Code 会话中每次工具调用 token 消耗的终端工具**

面向 Claude Code 用户的上下文分析器：通过挂钩 hook 事件与 statusline 快照两条数据流，按会话 ID 与时间戳关联计算每次工具调用的 token 成本；用 Welford 算法构建滚动基线，以 Z-score 检测异常，并可选用 Haiku 分类器生成自然语言解释。提供 Rich TUI 实时仪表盘、SQLite 持久化、Slack/Discord 通知与多会话独立追踪。安装需 Python 3.11+ 与 uv，从源码 git clone 后运行 uv sync。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按工具调用（Read/Bash/Grep 等）追踪 token 成本
- Welford 算法滚动基线与可配置 Z-score 异常检测
- 关联 hook 事件与 statusline 快照计算单次调用增量
- Rich TUI 仪表盘、Slack/Discord webhook 通知、多会话独立追踪

## 适用场景

- 排查 Claude Code 中哪个工具调用导致上下文暴涨
- 在上下文耗尽前收到告警与 /compact、/clear 建议
- 长期观察不同任务类型的 token 成本趋势

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L12: Claude Code shows you total token usage -- but not *which* tool call caused the spike. Was it that `Bash` command t
> L14: It hooks silently into your Claude Code sessions, tracks token cost **per tool call**, builds rolling baselines, an
> L81: Claude Code hooks don't include token counts. CAT correlates two data streams:

## 星数曲线

```mermaid
xychart-beta
    title "roeimichael/ContextAnalyzerTerminal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2e415956c047` · [字段定义](../../DATASET.md)*
