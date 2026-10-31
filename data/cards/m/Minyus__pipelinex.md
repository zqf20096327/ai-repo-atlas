# Minyus/pipelinex

⭐ 228 · Python · NOASSERTION · 推送 2026-04-15 · [GitHub](https://github.com/Minyus/pipelinex) · [官网](https://pipelinex.readthedocs.io/) · 个人维护

**构建 ML 实验流水线的 Python 包：Kedro 插件集 + YAML 配置扩展**

面向 ML 工程师的实验流水线工具，围绕 Kedro 提供一组可独立或组合使用的组件：HatchDict 允许在 YAML/JSON 配置中写 Python 对象与表达式（支持 $ 引用、括号表达式）；Flex-Kedro 插件简化流水线配置；MLflow-on-Kedro 以 DataSet 与 Hook 方式集成 MLflow，无需在业务代码中写 MLflow 代码；Kedro-Extras 为 PyTorch、Ignite、Pandas、OpenCV 等包提供 DataSets 与包装器（可选依赖，未用的包无需安装）。通过 pip 安装，另提供 Docker 构建方式与 Kedro starter 模板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HatchDict：YAML/JSON 中免 import 使用 Python 对象，支持嵌套与 $ 引用
- MLflow-on-Kedro 通过 Hook 在后台处理 MLflow 记录，业务代码无需改动
- Kedro-Extras 提供 PyTorch/Ignite/OpenCV 等包的 Kedro DataSets
- 提供 MNIST 分类、Kaggle、OpenCV 图像处理等示例工程

## 适用场景

- 以配置文件方式快速搭建和切换 ML 实验流水线
- 在 Kedro 项目中接入 MLflow 做实验跟踪
- 在 YAML 中直接声明模型对象与超参，避免硬编码 import

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L12: PipelineX is a Python package to build ML pipelines for experimentation with Kedro, MLflow, and more
> L28: - MLflow-on-Kedro: Kedro plugin for MLflow users
> L34: - Kedro-Extras: Kedro plugin to use various Python packages

## 星数曲线

```mermaid
xychart-beta
    title "Minyus/pipelinex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 227 --> 229
    line [228, 228]
```

2026-10-18 228 → 2026-10-31 228（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f6aaeced4ccb` · [字段定义](../../DATASET.md)*
