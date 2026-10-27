# NorskRegnesentral/skchange

⭐ 44 · Python · BSD-3-Clause · 推送 2026-10-07 · [GitHub](https://github.com/NorskRegnesentral/skchange) · [官网](https://skchange.readthedocs.io) · 组织维护

**Python 变点检测库：时间序列分割与异常检测**

由挪威计算中心（Norsk Regnesrial）开发的 Python 库，在类 scikit-learn API 中提供变点检测/时间序列分割与多变量段异常检测算法，含移动窗口、种子二分分割、CAPA 等检测器，并支持基于 scipy 分布的自动惩罚校准。推荐配合 numba 安装以提升性能，也可纯 pip 安装。提供文档与测试，附 arXiv 论文引用信息；版本 0.17 之前升级需查阅迁移指南。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 类 scikit-learn API 的变点检测/时间序列分割
- 多变量段异常检测（CAPA 等）
- 基于 scipy 分布的自动惩罚校准
- 可选 numba 加速安装

## 适用场景

- 检测时间序列中的分布变点并做分割
- 多变量序列中的段异常检测
- 研究场景中复现与引用变点检测方法

## 场景标签

 · 领域:时间序列分析/统计机器学习

## 证据(README 行号)

> L12: Skchange provides fast and flexible changepoint detection algorithms within a scikit-learn-like API. See the docume
> L38: ### Changepoint detection / time series segmentation

## 星数曲线

```mermaid
xychart-beta
    title "NorskRegnesentral/skchange 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-27 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1d28b90875aa` · [字段定义](../../DATASET.md)*
