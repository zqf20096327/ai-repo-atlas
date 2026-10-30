# JonathanHarford/verne_durand

⭐ 15 · Python · 推送 2026-01-24 · [GitHub](https://github.com/JonathanHarford/verne_durand) · 个人维护

**自动化串行调用 Jules AI agent 执行任务清单的脚本工具**

基于 jules-agent-sdk 的自动化执行脚本：读取项目中的 PLAN.yaml 任务清单，串行调用 Jules AI agent 逐项执行，自动批准计划以维持自主运行，自动重试失败任务或恢复挂起会话。集成 Git 工作流，自动创建分支、推送远端、合并 Jules 的改动并清理临时分支。通过 uv 运行，内联依赖元数据实现零配置执行；用户可在 Jules Web UI 暂停会话以停止循环。项目自述为 ALPHA 状态，Jules API 功能较 Web UI 受限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按 PLAN.yaml 清单串行调度 Jules agent 会话
- 计划自动批准与失败任务自动重试/会话恢复
- 自动分支创建、推送、合并与临时分支清理
- uv 内联依赖元数据零配置运行

## 适用场景

- 用满每日 Jules 会话额度批量执行编码任务清单
- 让 Jules 自主完成带 Git 分支管理的开发任务
- 通过 Web UI 暂停会话随时中止自动化循环

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: This script automates the sequential execution of tasks using the Jules AI agent.
> L15: - **API-Based**: Uses the jules-agent-sdk to communicate with the Jules AI agent.

## 星数曲线

```mermaid
xychart-beta
    title "JonathanHarford/verne_durand 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `be565524212c` · [字段定义](../../DATASET.md)*
