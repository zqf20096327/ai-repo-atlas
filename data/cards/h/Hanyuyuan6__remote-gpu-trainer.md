# Hanyuyuan6/remote-gpu-trainer

⭐ 42 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Hanyuyuan6/remote-gpu-trainer) · 个人维护 · 中文 README

**让编码 agent 在租用 GPU 上安全训练的 Agent Skill**

面向 Claude Code、Codex、Cursor、Gemini CLI、GitHub Copilot 等编码 agent 的技能包（SKILL.md + 参考文档 + 脚本模板），使 agent 能在 AutoDL、RunPod、vast.ai、Lambda、Paperspace 等租用 GPU 平台或任意 SSH 机器上启动、监控、恢复与停止训练。关键机制：租用前在本地 CPU 排练全流程、checkpoint 原子化保存、释放前读回并做 SHA-256 校验与指标复算、按平台选择真正停止计费的操作，并内置各平台的计费陷阱档案（如 AutoDL 15 天自动释放）。通过 git clone 安装到各宿主的 skills 目录，无需托管服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 AutoDL、RunPod、vast.ai、Lambda、Paperspace 等 9 个租用 GPU 平台及任意 SSH 机器
- 释放实例前将 checkpoint 读回独立位置并做文件清单、SHA-256、安全加载与指标复算校验
- 各平台计费行为档案（关机/释放区别、闲置计费、自动释放计时器）
- 租用前在本地 CPU 用小数据完整排练训练脚本

## 适用场景

- 在租来的 GPU 上跑训练并确保 checkpoint 不因释放实例丢失
- 让 agent 找出 NaN、OOM、假活等训练故障的原因
- 多实例并行跑消融实验并核对结果可复现性

## 场景标签

`模型训练` `MLOps` · 领域:训练与推理

## 证据(README 行号)

> L12: remote-gpu-trainer is an Agent Skill for Claude Code, Codex and other coding agents. It lets your agent launch, mon
> L66: remote-gpu-trainer is a skill, not a CLI or an SDK: a `SKILL.md` your agent loads, plus reference docs and script t

## 星数曲线

```mermaid
xychart-beta
    title "Hanyuyuan6/remote-gpu-trainer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `59412874df4d` · [字段定义](../../DATASET.md)*
