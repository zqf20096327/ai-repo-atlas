# mlcommons/ck

⭐ 649 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/mlcommons/ck) · [官网](https://cTuning.ai/project/cmeta) · 组织维护

**MLCommons 维护的 ML/MLOps 自动化框架，自动化运行与基准测试**

由 MLCommons 维护的 Collective Knowledge (CK) 与 Collective Mind (CM/CMX) 自动化框架：将软件项目转换为基于文件的可移植构件库（代码、数据、模型、脚本），通过统一 CLI 与 Python API 串联为自动化工作流，用于跨平台组合、运行、基准测试与优化 AI/ML 应用；包含 MLPerf 推理基准自动化脚本与 CK Playground 构件索引平台。需 Python 3.8+，支持 Ubuntu/MacOS/Windows 等系统。README 标明本仓库为 legacy，由原作者另行开发下一代 cMeta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将项目转为带元数据的可移植可复用构件，串联为自动化工作流
- CM 脚本自动化 MLPerf 推理基准的组成、运行与优化
- 统一 CLI 与 Python API，Python 3.8+ 最小依赖，跨多操作系统与容器运行
- CMX 向后兼容 CM，可作为 drop-in 替代

## 适用场景

- 跨硬件平台自动化运行与复现 MLPerf 基准
- 将研究项目整理为可复用、可复跑的构件与工作流
- 聚合、对比 MLPerf 基准结果并组织优化竞赛
- 会议 artifact evaluation 的自动化评审流程

## 场景标签

`MLOps` `模型评测` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L33: It helps users non-intrusively convert their software projects
> L67: We have developed a collection of portable, extensible and technology-agnostic automation recipes
> L85: Just install `pip install cmx4mlperf` and substitute the following commands and flags:

## 星数曲线

```mermaid
xychart-beta
    title "mlcommons/ck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 648 --> 650
    line [649, 649]
```

2026-10-18 649 → 2026-10-23 649（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0934321fc6f3` · [字段定义](../../DATASET.md)*
