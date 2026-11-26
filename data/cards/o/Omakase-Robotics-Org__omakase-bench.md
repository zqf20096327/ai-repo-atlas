# Omakase-Robotics-Org/omakase-bench

⭐ 5 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/Omakase-Robotics-Org/omakase-bench) · 组织维护 · 中文 README

**机器人大模型仿真基准测试框架：跑任务出评分报告**

omakase-bench 是一个机器人任务基准与执行框架：指定模型后在 MuJoCo 仿真中运行冻结的任务套件（如 core@1，20 个随机种子），模型通过统一的机器人 API 驱动机器人，评分取自仿真器真值而非模型自述，输出 results.json、report.html 与每回合视频。支持 URDF+robot.yaml 自定义机器人、任务包扩展，接口涵盖 tools/code/ee/chunks（VLA 策略），后端支持 MuJoCo（默认 CPU）、Isaac Sim 与真实机器人。需 Python 3.11+，用 uv 安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 冻结哈希的版本化套件保证结果可比（core@1 等 5 个套件）
- 评分基于仿真器 ground truth，并提供每回合 trace.jsonl 与视频
- tools/code/ee/chunks 多种接口，含 VLA 策略的动作块接口
- URDF+robot.yaml 即可添加机器人，任务包可扩展

## 适用场景

- 对比不同 LLM 在同一机器人任务套件上的得分
- 把自己的 URDF 机器人接入基准测试
- 评测 VLA 策略在仿真任务中的表现
- 复现并查看双机器人下棋等记录结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: Name a model, run robot tasks in simulation, get a scored report.
> L15: It is a framework as much as a benchmark: bring a URDF and you have a robot; add a package and you have a
> L49: |**Backend**|What executes the commands: MuJoCo (default, CPU), Isaac Sim, or a real robot. Simulators add reset an


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7bcfa6479ee0` · [字段定义](../../DATASET.md)*
