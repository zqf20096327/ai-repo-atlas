# WildBearCub/glm-5.4-leader-coder

⭐ 3 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/WildBearCub/glm-5.4-leader-coder) · 个人维护 · 中文 README

**给 GLM-5.4 编码会话用的 Leader+Coder 双模型子智能体分工方案**

一套针对 z.ai GLM-5.4 编码场景的子智能体分工配置包：通过 Leader 技能与 Coder 子智能体定义，让 GLM-5.4 只做定方案、派单、审查，代码编辑交给 GLM-5.3-Flash。包含 AGENTS.md 防发散规则、安全规矩（coder.md）以及基于 ZCode 遥测记录的四天 token 对照数据与 Python 复算脚本。安装说明在包内 INSTALL.md；数据复算需要本机的 ZCode 日志与用量库。

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

- Leader 技能 + Coder 子智能体的双模型分工定义文件
- AGENTS-discuss-before-diverging.md 防发散规则
- 四天 13,052 次模型响应的遥测数据与可复算脚本 data/telemetry_stats.py
- coder.md 内含子智能体安全规矩一节

## 适用场景

- 用 GLM-5.4 做长程编码任务时降低额度消耗
- 让主会话模型只负责方案与审查、代码交给更便宜模型
- 复算自己的 ZCode 遥测数据验证 token 用量变化

## 场景标签

`编码 Agent` `提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Leader + Coder：给 z.ai GLM-5.4 用的双模型子智能体分工方案
> L5: **一句话**：不让 GLM-5.4 自己写代码，让它只做定方案、派单、审查三件事，代码交给 GLM-5.3-Flash 去写。
> L17: |Leader（主会话上的一个技能）|GLM-5.4|定方案、派单、审查|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `d1c658a3d427` · [字段定义](../../DATASET.md)*
