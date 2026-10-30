# OxWearables/actinet

⭐ 16 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/OxWearables/actinet) · [官网](https://actinet.readthedocs.io/) · 组织维护

**腕部加速度计数据的人类活动分类工具**

基于自监督学习的活动分类模型工具，读取 AX3 等腕部加速度计数据文件（.cwa/.cwa.gz），生成时间序列与汇总指标（睡眠、久坐、体力活动时长等），并提供缺失数据填补后的调整估计、活动曲线绘图（-p）、多文件批量处理与输出汇总脚本（actinet-collate-outputs）。面向健康研究与可穿戴设备数据分析人员，以 Python 包（pip/conda 安装）与命令行方式使用，运行需 Java 8。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从加速度计数据生成活动分类时间序列与汇总指标
- 基于自监督学习的活动分类模型
- 缺失数据填补（同时间点均值插补）与调整估计
- 支持批量处理、活动曲线绘图与输出汇总脚本

## 适用场景

- 分析腕部加速度计采集的睡眠/久坐/体力活动数据
- 批量处理大规模加速度数据集并汇总为 CSV
- 为流行病学研究生成身体活动指标

## 场景标签

 · 领域:健康/可穿戴设备数据分析

## 证据(README 行号)

> L6: A tool to extract meaningful health information from large accelerometer datasets.
> L7: The software generates time-series and summary metrics useful for answering key questions such as how much time is s
> L11: *Minimum requirements*: Python>=3.9, Java 8 (1.8)

## 星数曲线

```mermaid
xychart-beta
    title "OxWearables/actinet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bdc76897d355` · [字段定义](../../DATASET.md)*
