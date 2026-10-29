# gia-uh/autogoal

⭐ 215 · Python · MIT · 推送 2026-06-15 · [GitHub](https://github.com/gia-uh/autogoal) · [官网](https://autogoal.uhgia.org) · 组织维护

**AutoML/程序合成 Python 框架：自动搜索最优机器学习流水线**

面向开发者的 Python 框架，核心是程序合成：在用户定义的程序空间中搜索解决给定任务的最优方案，主要应用于 AutoML。内置数百种底层机器学习算法，可自动组装为流水线；提供 AutoML 类作为黑盒接口适配多种问题与数据格式，另有 CLI 可免代码训练与使用模型。安装支持 Docker 开发镜像或 pip（可选 contrib 依赖），版本处于 0.x 公测阶段，公开 API 可能变化，附带论文与在线 demo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于语法演化等方法的流水线自动优化搜索
- 预置数百种底层算法，AutoML 类以黑盒方式适配多种数据格式
- 提供 CLI 免代码训练模型、下载数据集
- 在线与本地 Docker demo 展示主要功能

## 适用场景

- 在标注数据集上自动搜索并训练分类/回归流水线
- 不为算法选型纠结时用 AutoML 黑盒接口快速获得可用模型
- 在自定义程序空间上做通用的程序合成与优化实验

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L8: AutoGOAL is a Python library for automatically finding the best way to solve a given task.
> L14: AutoGOAL provides a set of low-level components to define different spaces and efficiently search in them.
> L21: algorithms that can be automatically assembled into pipelines for different problems.

## 星数曲线

```mermaid
xychart-beta
    title "gia-uh/autogoal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 214 --> 216
    line [215, 215]
```

2026-10-18 215 → 2026-10-29 215（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a6125b1077eb` · [字段定义](../../DATASET.md)*
