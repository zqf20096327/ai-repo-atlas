# Striveworks/valor

⭐ 40 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Striveworks/valor) · [官网](https://striveworks.github.io/valor/) · 组织维护

**轻量 numpy 机器学习模型评测库，覆盖分类/检测/分割**

valor-lite 是基于 numpy 的轻量评测库，为数据科学家和工程师提供机器学习流水线的性能评估，支持分类、目标检测、语义分割等任务的指标计算（如精度、IoU 等）。定位于需要快速响应评测的场景，可作为大型服务的组件或嵌入面向用户的工具中。由 Striveworks（位于德州奥斯汀的 MLOps 公司）维护，通过 PyPI 安装，也可从源码经 make install 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 numpy 的轻量实现，无需重量级依赖
- 支持分类、目标检测、语义分割评测
- 语义分割区分背景与前景标签的计算口径（背景计入 accuracy 不计入 mean IoU）
- 由公司团队（Striveworks）维护

## 适用场景

- 在建模流水线中快速计算模型评测指标
- 将评测能力嵌入面向用户的产品或服务
- 对比不同模型版本的分类/检测/分割表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: **valor-lite** is a lightweight, numpy-based library designed for fast and seamless evaluation of machine learning m
> L29: ### Classification

## 星数曲线

```mermaid
xychart-beta
    title "Striveworks/valor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-30 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0f1c7d7dd9df` · [字段定义](../../DATASET.md)*
