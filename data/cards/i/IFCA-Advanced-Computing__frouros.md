# IFCA-Advanced-Computing/frouros

⭐ 260 · Python · BSD-3-Clause · 推送 2026-04-23 · [GitHub](https://github.com/IFCA-Advanced-Computing/frouros) · [官网](https://frouros.readthedocs.io) · 组织维护

**ML 系统漂移检测库：专注概念漂移与数据漂移检测**

BSD-3 许可的 Python 库，提供经典与较新的漂移检测算法：概念漂移（流式，如 DDM、ADWIN、KSWIN 等 13 种）与数据漂移（批次与流式，含距离度量与统计检验约 20 种），标注单变量/多变量、数值/类别适用性。明确声明只做漂移检测单一任务，不包含异常检测、对抗检测等其他功能。提供 pip 安装、readthedocs 文档与 SoftwareX 论文，正被 AI4EOSC、iMagine 项目用于 ML 流水线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 概念漂移检测器 13 种（DDM、ADWIN、KSWIN、EDDM 等）
- 数据漂移检测覆盖距离度量与统计检验（KS 检验、MMD、PSI 等）
- 明确限定单一用途：仅漂移检测
- 已被 AI4EOSC、iMagine 项目采用

## 适用场景

- 为流式或批量 ML 服务的性能衰减做概念漂移检测
- 上线前后的数据分布变化（数据漂移）检测
- 在 ML 流水线中集成漂移监控

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L39: Frouros is a Python library for drift detection in machine learning systems that provides a combination of classica
> L275: Frouros is actively being used by the following projects to implement drift

## 星数曲线

```mermaid
xychart-beta
    title "IFCA-Advanced-Computing/frouros 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 259 --> 261
    line [260, 260]
```

2026-10-18 260 → 2026-10-26 260（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3aa0a1e382f0` · [字段定义](../../DATASET.md)*
