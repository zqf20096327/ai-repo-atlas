# jterrazz/spwn

⭐ 14 · Go · MIT · 推送 2026-10-29 · [GitHub](https://github.com/jterrazz/spwn) · [官网](https://spwn.sh) · 个人维护

**以代码方式编排 AI agent 的工具：声明式环境构建与运行**

面向开发者的 agent 编排框架：将 agent、环境块（python/qmd/ffmpeg 等工具）、记忆与技能写成声明式文件，spwn build 生成 Docker 镜像或 runtime 原生目录（claude-code、codex 等），实现跨机器一致复现。支持多 agent 世界（worlds）、markdown 文件记忆、lockfile 与 spwn check 校验、cron/文件事件触发的自动化。运行依赖 Docker（可跳过改生成 runtime 树）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式环境块组合，同一项目内多 agent 各自独立沙箱
- spwn build 产出 Docker 镜像或 claude-code/codex 等 runtime 原生树
- 记忆为 markdown 文件夹，可读可 diff、跨重启保留
- cron 与文件事件触发的 agent 自动化（spwn automation daemon）

## 适用场景

- 把 agent 连同环境一起提交到 git，在 PR 中评审行为变更
- 为不同 agent 组装各自专属的沙箱化运行环境
- 定时或文件变更时自动唤醒 agent 执行任务

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  AI agents orchestration as code. One source, run anywhere.
> L21: With spwn, **you build that environment, block by block**. Stack `spwn:python` with `spwn:qmd`, add a local `tool/f
> L49: - **Reproducible.** One `spwn build` produces a Docker image, or a runtime-native tree (claude-code, codex and the 

## 星数曲线

```mermaid
xychart-beta
    title "jterrazz/spwn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `196afef4cdb2` · [字段定义](../../DATASET.md)*
