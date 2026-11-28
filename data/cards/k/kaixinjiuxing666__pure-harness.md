# kaixinjiuxing666/pure-harness

⭐ 19 · Jupyter Notebook · MIT · 推送 2026-08-08 · [GitHub](https://github.com/kaixinjiuxing666/pure-harness) · 个人维护 · 中文 README

**教学库：28 个 Notebook 从零实现 LLM Agent 执行 Harness**

基于综述论文 Agent Harness Engineering: A Survey 提出的 ETCLOVG 七层架构（执行、工具、上下文、生命周期、可观测性、验证、治理）的教学与实验库，以单文件自包含的 Jupyter Notebook 组织，共 28 个已完成 Notebook 覆盖沙箱、工具调用、记忆、多 Agent、成本遥测、评估与治理等主题，另有进阶模块在 TODO 中。全部运行由 .env 配置的真实 LLM API 驱动，不使用静态 Mock 数据，仅 CPU 即可运行，MIT 协议开源。适合学习 Agent 执行基础设施原理的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 28 个自包含、真实 API 驱动的 Notebook，按 ETCLOVG 七层架构组织
- 无需 GPU，普通笔记本 CPU 即可运行
- 运行时可观测：输出上下文、工具调用决策、权限控制与 Trace 树
- TODO 列出基础与 opt 可选进阶模块及完成状态

## 适用场景

- 逐层学习 Agent 执行基础设施的机制与实现
- 为构建自有 Agent 平台做技术预研与实验
- 在本地笔记本上以真实 API 复现 Agent 运行链路

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L8: **pure-harness** 是一个基于 Python 的微型 Agent 执行基础设施教学与实验库。就现阶段实践与生产而言，“**决定 Agent 可靠性的往往不是模型本身，而是包在它外面的 Harness**”。本项目参考综
> L18: - 📖 **单文件自包含 / Notebook-first**


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `db7c812bcdfa` · [字段定义](../../DATASET.md)*
