# Bicameral-AI/claude-code-mode-benchmark

⭐ 4 · Python · NOASSERTION · 推送 2026-11-17 · [GitHub](https://github.com/Bicameral-AI/claude-code-mode-benchmark) · 个人维护

**对 Claude Code Code Mode 开关影响的可复现基准实验**

围绕 Claude Code 实验性 Code Mode 功能的基准仓库：同一批六项任务在四个模型上各以 Code Mode 关/开两种方式运行，共 96 次运行；所有数字从 Claude Code 保存的 transcript 中读取，而非屏幕记录。仓库提供脚本、提示词与测试数据供任何人在自己机器上复现，单个模型耗时远低于一小时；另含预测先行的记录、失败运行报告、版本间对比与 Code Mode 行业概览。脚本仅在 macOS 上试运行，许可为 all rights reserved。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六项任务 × 四模型 × 开关两模式，共 96 次运行，数字全部读自 transcript
- 脚本、提示词与测试数据齐备，任何人可在本机复现
- 预测先于运行写下，错误预测保留在文中
- 失败运行（3 次，均为 Haiku 5.5）被如实报告

## 适用场景

- 复现并验证 Code Mode 对 token 消耗与正确性的影响
- 评估自己工作负载是否适合 Code Mode（工具聚合 vs 文件工作）
- 参考其方法设计 agent 功能的对照基准

## 场景标签

`模型评测` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3:  A repeatable experiment that measures what Code Mode changes in Claude Code:
> L44: **What the benchmark is.** Six small tests, each run in a new Claude Code session with Code Mode off and again with
> L52: - **To be repeatable by anyone.** The scripts, prompts and test data are all here, and one model takes well under a


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `40eca1483d8c` · [字段定义](../../DATASET.md)*
