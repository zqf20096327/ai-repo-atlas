# xyangzhou/WorldLeague

⭐ 19 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/xyangzhou/WorldLeague) · [官网](https://xyangzhou.github.io/WorldLeague/) · 组织维护

**具身 AI 基准：60 个模拟机器人任务上量化物理目标达成进度**

由新加坡国立大学 xML Lab 发布的具身智能评测基准与配套评估代码，对 VLM、VLA、WAM 三类系统在 60 个交互式家庭任务上运行统一评测。评测器从机器人轨迹计算两项指标：衡量向物理目标推进程度的 Interactive Score，以及要求全部目标项与约束成立的物理成功率，合成 Physical Agency Profile。VLM 经 WorldHarness 接口发出命令，VLA/WAM 通过 WebSocket 等原生接口接入。运行需 OmniGibson/Isaac Sim 模拟环境与 BEHAVIOR-1K 资产。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 60 个家庭任务按 WorldSeek/WorldShape/WorldShift 三轨道、六能力维度组织
- Interactive Score 与物理成功率分离计分
- WorldHarness 为 VLM 提供观察-命令-反馈循环并支持回看历史相机画面
- 支持 Chat Completions 端点预设与自定义 VLA/WAM 策略插件接入

## 适用场景

- 在统一任务集上评测自家 VLA/WAM 模型的物理执行能力
- 通过 Chat Completions 端点评测 VLM 的机器人操作水平
- 对比不同系统的 Physical Agency Profile 与终止原因分析

## 场景标签

`模型评测` `多模态` · 领域:评测与运维

## 证据(README 行号)

> L20:  WorldLeague evaluates what an embodied agent can accomplish in 60 interactive household tasks.
> L49: Which physical goals can today’s AI systems achieve on their own? WorldLeague compares VLMs, VLAs and WAMs on 60 si
> L91: 1. Set up OmniGibson 3.7.1 with Isaac Sim 4.5.0, NVIDIA rendering support and the licensed BEHAVIOR-1K assets. Run 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `681b14b3e4e1` · [字段定义](../../DATASET.md)*
