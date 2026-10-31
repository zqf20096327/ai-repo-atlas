# mllam/weather-model-graphs

⭐ 35 · Python · 推送 2026-08-17 · [GitHub](https://github.com/mllam/weather-model-graphs) · [官网](https://kutt.to/mllam) · 组织维护

**构建、可视化与存储数据驱动天气模型图的 Python 工具库**

面向基于消息传递的图神经网络天气模型，提供图的创建、可视化与落盘存储的 Python 库。以 networkx.DiGraph 作为统一中间数据结构，使生成流程模块化、可逐步调试，并支持输出到多种文件格式；通过可选的 pytorch extra 可保存为 neural-lam 所用的 pytorch-geometric 数据结构（默认装 CPU 版 pytorch，GPU 变体需自行先装）。开发流程基于 pdm 与 pre-commit，文档用 Jupyter Book 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 networkx.DiGraph 为统一中间结构，生成流程模块化
- 支持保存为 neural-lam 使用的 pytorch-geometric 数据结构（可选 extra）
- 文档由可执行 Jupyter notebook 构成，含图架构设计原理
- 提供 Keisler 2021 flat graph 架构示例

## 适用场景

- 为图神经网络天气模型生成计算图
- 在建模各步骤中可视化检查图结构
- 将图导出为 pytorch-geometric 等格式供 neural-lam 使用

## 场景标签

 · 领域:地球科学/机器学习工具

## 证据(README 行号)

> L5: `weather-model-graphs` is a package for creating, visualising and storing graphs used in message-passing graph-based
> L18: If you want to be able to save to pytorch-geometric data-structure used in


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6749d342cb2f` · [字段定义](../../DATASET.md)*
