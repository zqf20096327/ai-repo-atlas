# Haardt/dctx0ctl

⭐ — · [GitHub]() · 个人维护

**给 AI 原生开发的可执行规格语言：先定契约再并行实现**

DCTX0 是一种可执行规格语言与配套 CLI：用户用自然语言描述产品，由编码代理协助把需求写成类型化、机器可读的契约（数据契约、示例、不变量、生命周期），契约驱动依赖感知的任务 DAG 与并行实现波次，并在实现后用同一规格核对应用实际行为。提供 dctx0 CLI 做 prepare/verify/tasks plan/claim 等命令，含原子任务认领、守卫式任务交付与复现脚本。README 声明项目为实验性、未针对 token 效率优化，混合验收与发布验证仍处于进行中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 规格编译校验 + 用同一契约核对应用实际行为的双重验证
- 从已验证规格派生任务 DAG 并按依赖波次组织并行实现
- 原子任务认领与守卫式任务交付（adoption 需证据）
- 提供可复现的本地验收/基准脚本（Python3）

## 适用场景

- 在编码代理写代码前先固定产品行为契约，避免实现与测试同时误解需求
- 让多个代理按依赖波次并行实现任务而不互相冲突
- 对已有应用按规格做验收验证与基准诊断

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: An executable specification language for AI-native software development.
> L94: People and coding agents develop the specification together. People own the product decisions; agents can write and
> L142: This makes the specification useful for organizing implementation as well as checking it: it exposes parallel work


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `ab33daa79ce5` · [字段定义](../../DATASET.md)*
