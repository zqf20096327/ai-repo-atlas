# joshua-zyy/pi-omo-slim

⭐ 23 · JavaScript · MIT · 推送 2026-09-14 · [GitHub](https://github.com/joshua-zyy/pi-omo-slim) · 个人维护 · 中文 README

**为 Pi 编码智能体提供编排器与六个专家子智能体的配置包**

非 fork 的配置捆绑包：将 OMO-slim 的角色边界与编排方式适配到 Pi 的扩展和子智能体 API，安装一个 Orchestrator 与六个专家（Explorer/Librarian/Oracle/Designer/Fixer/Verifier），外加手动调用的多议员共识评审 /council。安装由 scripts/install.mjs 确定性完成：生成不可变 plan、备份、校验与失败回滚，支持模型继承或按角色配置。要求 Pi >= 0.84.0 及八个指定包。

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

- 六专家并行调度的 Orchestrator 模式（/orchestrator 命令）
- /council 多议员共识评审，产出共识度评级与缺席记录
- install.mjs 确定性安装：SHA-256 审批、备份与自动回滚
- 智能体模板不固定模型与思考级别，从父智能体继承

## 适用场景

- 给 Pi 编码智能体加上多角色分工的工作流编排
- 高风险架构决策时手动召集多议员共识评审
- 以可审计、可回滚的方式管理 Pi 配置安装

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: `pi-omo-slim` gives Pi a workflow-oriented Orchestrator and six focused specialist agents:
> L21: This project is a configuration bundle. It does not fork Pi, `pi-subagents`, or OMO-slim. It adapts OMO-slim's role

## 星数曲线

```mermaid
xychart-beta
    title "joshua-zyy/pi-omo-slim 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-30 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dc854d27b849` · [字段定义](../../DATASET.md)*
