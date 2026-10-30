# johndaskovsky/nightshift

⭐ 20 · TypeScript · 推送 2026-05-18 · [GitHub](https://github.com/johndaskovsky/nightshift) · [官网](https://www.npmjs.com/package/@johndaskovsky/nightshift) · 个人维护

**Claude Code 内的 AI agent 批处理框架：长时无人值守跑任务**

以 Claude Code 插件形式分发的 agent 批处理框架。用户定义 CSV 条目表与任务说明，Manager 子代理按序调度 Dev 子代理（独立的顶级 claude -p 子进程）逐项执行，内置每项最多 3 次重试、按 Validation 标准自我验证、把成功执行产生的步骤改进写回任务文件（可关闭），失败单项不阻塞整体，支持并行模式（自适应批大小）与中断续跑。Dev 子进程继承用户级 MCP 配置。需 Claude Code v2.1.83+ 及 qsv、flock、jq 三个系统依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Manager+Dev 双代理结构，Dev 以独立 claude -p 子进程执行并继承全部用户级 MCP 配置
- 每项最多 3 次尝试，按任务 Validation 标准自我验证
- 自我改进：成功执行的建议写回任务文件，可用 disable-self-improvement 关闭
- 并行模式带自适应批大小（成功翻倍、失败减半），中断后可续跑

## 适用场景

- 批量处理 CSV 条目列表的重复任务（如批量建页面、批量处理 URL）
- 无人值守长时间运行 agent 批次，失败项自动跳过并记录状态
- 在任务正式跑批前用 dry-run 调试单个任务定义

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: A batch processing framework for AI agents. Define a table of items, write task instructions, and let a manager-plu
> L14: Nightshift runs inside Claude Code as a `manager` subagent that dispatches dev work as fresh top-level `claude -p` 

## 星数曲线

```mermaid
xychart-beta
    title "johndaskovsky/nightshift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `79bbbe0f895f` · [字段定义](../../DATASET.md)*
