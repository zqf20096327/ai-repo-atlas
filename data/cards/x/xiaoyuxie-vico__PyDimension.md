# xiaoyuxie-vico/PyDimension

⭐ 51 · Python · MIT · 推送 2026-04-10 · [GitHub](https://github.com/xiaoyuxie-vico/PyDimension) · [官网](https://xiaoyuxie.top/PyDimension-Book/intro.html) · 个人维护

**从数据中发现隐藏对称性与无量纲定律的 Python 科学 ML 包**

模块化 Python 包，实现 Nature Communications 论文中的 dimensionless learning 方法，并正向更广的对称性发现框架 OpenSymmetry 演进。流水线含数据生成、预处理+量纲分析、内禀坐标（PCA/SIR/自编码器）与对称性发现四阶段；无量纲学习模块可将多参数约化为少数无量纲群并学习标度律。提供 CLI、Python API 与 Streamlit 网页界面，支持 conda/mamba/pip/Docker 安装，v1.0 论文代码保留在分支中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四阶段流水线：数据生成→预处理+量纲分析→内禀坐标（PCA/SIR）→对称性发现
- 无量纲学习模块：多参数约化为无量纲群并学习标度律
- CLI、Python API、Streamlit 网页与 Docker 镜像多种使用方式
- v2 基准流水线保留用于一致性验证，run_pipeline.py 按 --pipeline-version 分发

## 适用场景

- 实验与工程数据中发现隐藏不变结构与低维表征
- 从带单位测量表中恢复无量纲数与标度律
- 生成已知对称性的合成数据并做流水线验证

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: A modular Python package for **symmetry discovery from data** in physical systems using **data and machine learning*
> L193: PyDimension is moving toward a modular pipeline for **symmetry discovery from data**:

## 星数曲线

```mermaid
xychart-beta
    title "xiaoyuxie-vico/PyDimension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-24 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e130e60a87dc` · [字段定义](../../DATASET.md)*
