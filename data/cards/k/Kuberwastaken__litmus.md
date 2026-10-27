# Kuberwastaken/litmus

⭐ 72 · HTML · MIT · 推送 2026-07-14 · [GitHub](https://github.com/Kuberwastaken/litmus) · [官网](http://litmus.kuber.studio/) · 个人维护

**OpenClaw 技能：在本地 GPU 机上运行并行自主 ML 研究组织**

一个部署在 OpenClaw 实例上的技能，把常驻 GPU 机器变成自主运行的 ML 研究实验室：2–8 个原生 subagent 工作者在各自 git 分支上过夜跑实验，Director 每 2 小时调度方向，Synthesizer 每天 04:00 把结果蒸馏为可复用技能库，03:00–06:00 进入休闲思考模式（读 arxiv、写猜想），08:00 向聊天推送研究简报。所有实验以 git 提交记录，支持跨 agent cherry-pick。基于 Karpathy 的 autoresearch 构建，通过对话式安装完成配置并注册 cron 任务。要求 Linux/macOS 与 NVIDIA CUDA GPU，不支持 Windows。

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

- 2–8 个并行 subagent 各自在独立 git 分支跑实验
- 六个 cron 作业分工：Director/Synthesizer/Dawn/Watchdog/Digest/Archive
- 共享技能库与结构化实验记录（attempts/skills/notes）
- 两阶段实验预算（90s 快检 + 300s 全跑）提前放弃死胡同

## 适用场景

- 让闲置的 GPU 机器过夜自主做 ML 架构/优化器实验
- 通过聊天查看研究进展并中途调整 agent 方向
- 积累可复用的实验技巧与跨 agent 共享发现

## 场景标签

`科研工具` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Litmus** is an OpenClaw skill that turns your always-on GPU machine into a self-directing ML research lab. Multip
> L13: Built on Karpathy's autoresearch. Everything is a native `sessions_spawn` subagent — no external CLI processes, no 
> L43: YOU ──▶ OpenClaw agent

## 星数曲线

```mermaid
xychart-beta
    title "Kuberwastaken/litmus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-27 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `066f18b0a83f` · [字段定义](../../DATASET.md)*
