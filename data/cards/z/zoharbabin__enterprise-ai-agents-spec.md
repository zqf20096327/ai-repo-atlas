# zoharbabin/enterprise-ai-agents-spec

⭐ 53 · Shell · MIT · 推送 2026-07-03 · [GitHub](https://github.com/zoharbabin/enterprise-ai-agents-spec) · [官网](https://zoharbabin.github.io/enterprise-ai-agents-spec/) · 个人维护

**企业级 AI Agent 群产品开发规范与蓝图（3, 16字以内）**

提供用专业化 AI Agent 群覆盖软件开发生命周期（构思→规格→编码→测试→安全→部署→监控）的实施蓝图与规范文档，面向独立创始人与小团队。包含一份 Agent 编排架构规范，以及一条命令的 Roo Code 工作区初始化脚本（含 Orchestrator/Spec Writer/Coder/Tester 等角色占位配置、双重测试与文件访问规则概念、依赖跟踪/重试/升级的编排逻辑构想）。README 明确该脚本是模板起点，非开箱即用的完整 Agent 系统；同时讨论编排复杂性、合规治理（ISO/SOC/HIPAA/GDPR）与可审计性等挑战。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖全 SDLC 的 AI Agent 群编排规范蓝图
- 一键 shell 脚本初始化 Roo Code 实验工作区
- 内置双重测试（累积/递归）与严格文件访问规则的概念设计
- 强调 ISO/SOC/HIPAA/GDPR 合规与可审计的决策机制

## 适用场景

- 小团队搭建 AI Agent 驱动的产品开发流程参考架构
- 实验 Roo Code 多角色 Agent 协作工作区
- 了解 Agent 群开发的治理、合规与透明性设计考量

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L21: * **AI Agents Spec**
> L22:  A comprehensive blueprint detailing how to orchestrate a swarm of specialized AI agents across the full Software D
> L25:  A one-command shell script (`setup_roo_project.sh`) to bootstrap a basic workspace for experimenting with agentic 

## 星数曲线

```mermaid
xychart-beta
    title "zoharbabin/enterprise-ai-agents-spec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-26 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `88c1c867b0fc` · [字段定义](../../DATASET.md)*
