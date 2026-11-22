# CHSZLab/AgenticAlgorithmEngineering

⭐ 37 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/CHSZLab/AgenticAlgorithmEngineering) · [官网](https://chszlab.github.io/AgenticAlgorithmEngineering/) · 组织维护

**让自主 agent 按算法工程循环优化代码性能的方法论插件**

Agentic Algorithm Engineering (AAE) 是一套方法论与 agent 技能/插件，把自主 agent 置入算法工程循环（设计、分析、实现、实验评估）：agent 先与用户确认基准、指标、正确性检查与预算，随后自主提出可证伪假设、实现修改、运行实验并裁决保留或丢弃。每次会话产出编号 Git 补丁与 PDF 报告（每个假设一页），并写入共享知识库。作为 Claude Code 插件或 Codex 技能安装；PDF 报告依赖 Python 3 与 LaTeX，缺 LaTeX 时仅跳过 PDF。README 记录了对 VieCut、KaHIP 等图算法代码的应用案例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个实验前生成带预测效果的可证伪假设，每次修改后运行正确性断言
- 输出编号 Git 补丁与逐假设的 PDF 报告，写入社区知识库
- 以 Claude Code 插件（/plugin install）或 Codex 技能安装脚本分发
- 支持多组件模式：共享基准中按组件独立裁决保留或丢弃

## 适用场景

- 让 agent 按可验证流程加速我现有的求解器或算法代码
- 需要每次修改都有正确性断言与可回溯补丁的自动化优化
- 在受控容器中无人值守运行长时优化实验循环

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: This repository contains the program definition for **Agentic Algorithm Engineering (AAE)**, a methodology that turn
> L41: /plugin install aae --marketplace CHSZLab/AgenticAlgorithmEngineering
> L51: Agentic Algorithm Engineering takes this methodology and hands the cycle to an autonomous AI agent. The agent formu


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `f93b1b1010bf` · [字段定义](../../DATASET.md)*
