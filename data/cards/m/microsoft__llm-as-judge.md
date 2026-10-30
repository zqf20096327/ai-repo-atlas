# microsoft/llm-as-judge

⭐ 41 · Python · MIT · 推送 2026-02-11 · [GitHub](https://github.com/microsoft/llm-as-judge) · 组织维护

**用 LLM 评审 LLM 输出的结构化评测框架（FastAPI+Azure）**

微软开源的 LLM-as-Judge 框架：将多个配置了评审标准的 LLM 实例作为 judges，可组合为 assembly 协同评测，或采用集中式 Super Judge 模式。提供 FastAPI REST API 管理与执行评测（/evaluate 等端点），评测配置与结果存于 Azure Cosmos DB，附带统计分析和数据处理插件。部署面向 Azure（Terraform 基础设施即代码、Container Apps），需 Azure 账号与订阅，本地运行需 Python 3.12+ 与 Poetry。配置脚本多为 PowerShell。

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

- 多 judge 编排与 assembly 分组协同评测
- FastAPI REST 端点管理 judges/assemblies 并执行评测
- Terraform 一键部署到 Azure（Cosmos DB、Container Apps）
- 统计分析与数据处理插件系统

## 适用场景

- 为 LLM 应用搭建自动化输出质量评测服务
- 按自定义标准组合多评审者做综合评测
- 在 Azure 上快速部署一套评测 API 基础设施

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: LLM as Judge is a framework for implementing a pattern where Large Language Models (LLMs) act as judges to evaluate 
> L18: 1. **Judges**: Individual LLM instances configured with specific evaluation criteria
> L152: - `POST /evaluate` - Execute a judging evaluation

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/llm-as-judge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-30 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `94dbe21abb7e` · [字段定义](../../DATASET.md)*
