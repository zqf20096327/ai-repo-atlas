# Arthur031221/Token-Beggar

⭐ 4 · Python · MIT · 推送 2026-11-09 · [GitHub](https://github.com/Arthur031221/Token-Beggar) · 个人维护 · 中文 README

**面向 Claude Code 用户的插件：按任务规模路由到更便宜的模型以降低开销**

Token Beggar 是 Claude Code 插件，由 Skill、7 个 hooks、一个 worker agent 和 CLI 组成。会话首轮提示时注入路由卡，由对话模型判断任务大小：小任务留在当前对话，大任务发给更便宜的 worker，并由对话模型检查 diff、运行测试，按模型与 effort 设定调用上限。基于 18 个开源 Python 项目的修 bug 基准测得 1.42x 花费节省，解决率持平。仅支持 Python 3.10+，仅标准库依赖，本地运行，数据不出本机（除每周模型价格页下载）。

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

- 按任务规模路由：小任务留在对话，大任务发给更便宜 worker 并回检 diff 与测试
- 基于 18 个真实 PR 的基准测量：1.42x 花费节省，解决率 69% 对 70%
- token-beggar doctor/mode/stats/ask 等 CLI 与环境变量配置
- 长会话上下文压缩守卫：压缩前保存笔记并恢复

## 适用场景

- 在 Claude Code 中降低大模型配额与费用开销
- 修 bug 等大型任务委托给更便宜模型并保证质量检查
- 长会话中管理上下文压缩时机

## 场景标签

`编码 Agent` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13: Token Beggar is a plugin for Claude Code. Before the big model does a job, it checks whether a cheaper model can do
> L96: 1. **Look up the mode.** The model and effort of your chat select one of three modes from `data/measured.json`. `fu
> L106: - **Skill**: the routing rules the chat reads. `skills/token-beggar/SKILL.md`, explained in docs/usage.md.

## 星数曲线

```mermaid
xychart-beta
    title "Arthur031221/Token-Beggar 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-08", "2026-11-25"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-26 3 → 2026-11-25 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `c8a46c468807` · [字段定义](../../DATASET.md)*
