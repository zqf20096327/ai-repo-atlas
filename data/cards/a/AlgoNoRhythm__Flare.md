# AlgoNoRhythm/Flare

⭐ 310 · TypeScript · MIT · 推送 2026-09-27 · [GitHub](https://github.com/AlgoNoRhythm/Flare) · 个人维护

**给开发者的图结构 agentic 编程 IDE，多 agent 协作看板与沟通频道**

Flare 是以代码依赖图为主界面的桌面/浏览器 IDE：每个文件为节点、import 为边，提供 Canvas、Wheel、Districts 三种视图与多种着色透镜，agent 修改文件时图实时更新并快照为可回退的本地历史。内建终端运行 claude/codex/opencode 等 CLI agent；控制面板含 Tasks 看板、Design decisions、Questions，全部经 MCP 查询与更新，支持多 agent 认领同一看板、Stop hook 续派任务；Channel 频道让多 agent 宣告占用、提问协调，冲突以竞争状态呈现而非强制锁定。安装提供 npm 与二进制包两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 代码库实时依赖图（文件为节点、import 为边），三种视图切换
- Tasks/Decisions/Questions 经 MCP 供 agent 自主循环，支持多 agent 认领
- Channel 频道：agent 间宣告文件占用、协调与争议可视化
- 变更快照为本地影子历史，可按文件或整树 diff 与回退

## 适用场景

- 在可视化依赖图上观察 agent 对代码库的实时修改与影响范围
- 多 agent 并行开发同一仓库时通过看板与频道协调分工
- 审查 agent 的设计决策与代码改动并按需回退

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A graph-first IDE for agentic coding — desktop app, or served to a browser
> L7: imports are edges — with a full terminal underneath where you run `claude`,
> L104:  All three are queryable over MCP, so an agent can run its own loop:

## 星数曲线

```mermaid
xychart-beta
    title "AlgoNoRhythm/Flare 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 309 --> 311
    line [310, 310]
```

2026-10-18 310 → 2026-10-30 310（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b43077163741` · [字段定义](../../DATASET.md)*
