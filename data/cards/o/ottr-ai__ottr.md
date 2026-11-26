# ottr-ai/ottr

⭐ 3 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/ottr-ai/ottr) · 组织维护

**为开发者的编码 agent 提供本地看板式任务分发与合并管理**

本地看板应用：用户以自然语言下达任务，Ottr 为任务分配 git worktree、在其中运行 omp 编码 agent、通过第二模型检查、审查透镜与变异测试验证结果，再经每项目队列合并。看板绑定 127.0.0.1，全部在本机运行；质量由项目自身的 AGENTS.md 约束。支持 Docker Compose、源码构建、Podman 与裸机（Bun）多种运行方式，并提供规则访谈、审查与发布工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言任务自动获得独立 git worktree 并运行 omp agent
- 合并前经第二模型检查、变异测试、安全审计与 UI/UX 检查
- 任务看板含 Todo/In progress/Merging/Done 全流程与规则访谈
- 每项目合并队列与总运行数上限（OMP_TRACKER_MAX_TOTAL）

## 适用场景

- 同时给多个编码 agent 派任务并在本地看板上跟踪进度
- 让 agent 改动自动经过变异测试与安全审计后再合并
- 为缺少 AGENTS.md 的项目通过访谈卡片生成规则文件

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5:  A local kanban board that runs omp coding agents on your git projects.
> L15: You type a task in plain language. Ottr gives it a git worktree, runs the agent in it, checks the result, and merge
> L90: |Work turn|Ottr creates `.worktrees/<id>` on branch `ott/<id>-<slug>` and runs `omp -p` in it. The agent finishes w

## 星数曲线

```mermaid
xychart-beta
    title "ottr-ai/ottr 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-16 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e0426004e328` · [字段定义](../../DATASET.md)*
