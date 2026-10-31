# snad-space/coniferest

⭐ 17 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/snad-space/coniferest) · [官网](https://coniferest.snad.space) · 组织维护

**天文学数据主动异常检测 Python 包**

SNAD 合作组开发的主动异常检测（active anomaly detection）Python 包，面向天文学时序/星表数据筛查。包含三个模型：IsolationForest（Rust 实现的隔离森林重写版）、AADForest（Das 主动异常检测算法的隔离森林实现）、PineForest（基于树过滤的主动学习模型）。通过 pip 安装，Linux/macOS/Windows 提供预编译二进制 wheel，无需编译依赖；有论文（Astronomy and Computing 2025）与 ASCL 收录记录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 实现的 IsolationForest 与 AADForest 主动异常检测模型
- 自研 PineForest 主动学习模型（树过滤）
- 三平台预编译 wheel，安装无需编译

## 适用场景

- 对天文巡天数据做异常天体筛查
- 在人工标注反馈下迭代提升异常检测精度
- 时序/星表数据的主动学习标注流程

## 场景标签

 · 领域:天文学/机器学习

## 证据(README 行号)

> L8: Package for active anomaly detection with isolation forests, made by SNAD collaboration.
> L68: 	title = {Coniferest: A complete active anomaly detection framework},
> L76:        author = {{Korolev}, Vladimir and {Kornolov}, Matwey and {Malanchev}, Konstantin and {SNAD Team}},

## 星数曲线

```mermaid
xychart-beta
    title "snad-space/coniferest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `ac19a3028768` · [字段定义](../../DATASET.md)*
