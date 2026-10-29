# amber132/Master-Orchestrator

⭐ 25 · Python · MIT · 推送 2026-05-19 · [GitHub](https://github.com/amber132/Master-Orchestrator) · [官网](https://amber132.github.io/Master-Orchestrator/) · 个人维护 · 中文 README

**把自然语言目标拆成 DAG、并发调度 Claude/Codex 的任务编排 CLI**

面向使用 Claude Code 与 Codex CLI 的开发者：将自然语言目标分解为有向无环图子任务，按阶段路由不同 provider（Claude 规划/审查、Codex 执行），无依赖任务并行执行，另一 Agent 做交叉审查；错误按类型分类重试（限流退避、上下文压缩、provider 切换），收敛阶段做停滞/劣化/回归检测。Simple 模式面向批量任务（默认 16 并发 worker），检测越权改动并自动 git 回滚。需本机 PATH 中有 claude 或 codex，Python 3.11+，源码方式安装。

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

- 目标→DAG 任务分解，按阶段路由 provider 并发执行
- Simple 模式 16 并发 worker，含自动重试与越权改动回滚
- 错误分类恢复：限流退避、上下文压缩重试、provider 自动切换
- 交叉审查与收敛检测（停滞升级、劣化回滚、回归暂停）

## 适用场景

- 让多个 AI Agent 并发完成跨多文件的重构或功能开发
- 批量修复上百个 lint/格式化问题并自动重试
- 按阶段混合使用不同模型：规划用 Claude、执行用 Codex

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: **一条命令把"重构这 15 个文件"分解成 DAG，让多个 Claude / Codex 并发跑，按阶段路由不同模型，Simple 模式自动检测越权改动并回滚。**
> L34: 2. **阶段路由**：按任务类型选择 provider，例如 Claude 负责推理，Codex 负责执行
> L94: 流水线的每个阶段都可以使用不同 AI Agent：

## 星数曲线

```mermaid
xychart-beta
    title "amber132/Master-Orchestrator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `fa986f079ba3` · [字段定义](../../DATASET.md)*
