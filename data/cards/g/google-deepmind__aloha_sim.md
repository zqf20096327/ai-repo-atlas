# google-deepmind/aloha_sim

⭐ 319 · Python · NOASSERTION · 推送 2025-11-13 · [GitHub](https://github.com/google-deepmind/aloha_sim) · 组织维护

**Aloha 机器人的 MuJoCo 桌面任务仿真与评测环境库**

DeepMind 维护的 Python 库，为 Aloha 桌面机器人定义 MuJoCo 仿真环境，包含基础操作、指令跟随与灵巧操作三类任务集合，附带交互式查看器（暂停/恢复、物体交互、输入新指令）、批量评测脚本与基准成功率数据（每任务 100 回合×3 次）。支持通过 pip 或 uv 安装，可选装 inference 扩展以接入 Gemini Robotics 模型做仿真推理与评测（限 Trusted Tester）。README 声明非 Google 官方支持产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定义 Aloha 机器人在 MuJoCo 中的桌面任务仿真环境
- 提供可交互查看器（暂停/恢复、物体交互、输入新指令）
- 提供批量评测脚本 run_eval.py 与可复现的随机种子设定
- 可选 inference 扩展接入 Gemini Robotics 模型进行仿真推理（限 Trusted Tester）

## 适用场景

- 在仿真中评测机器人操作策略模型的表现
- 复现 Gemini Robotics 模型在桌面任务上的基准成绩
- 通过交互式查看器调试机器人任务场景

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: Aloha Sim is a python library that defines the sim environment for the Aloha
> L6: robot. It includes a collection of tasks for robot learning and evaluation.

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/aloha_sim 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 318 --> 321
    line [320, 319, 319]
```

2026-10-18 320 → 2026-10-31 319（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `56c4efa8f796` · [字段定义](../../DATASET.md)*
