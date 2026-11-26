# Zar-Manah/HELIOS-Space-Weather

⭐ 3 · HTML · MIT · 推送 2026-11-21 · [GitHub](https://github.com/Zar-Manah/HELIOS-Space-Weather) · 个人维护

**CME 到达时间预报的信息上限实证研究与五级预测管线**

针对太阳周期 23–25 的 CME 到达时间预报做经验性信息上限测量：冻结的五个阶段管线（影响概率、传播到达时间、风暴严重度、磁障碍检测、Dst 临近预报）作为测试载体，将模型效应、队列效应与发射时可用信息分离，并以四格表、配对 bootstrap 与两个 conformal 区间门限报告结果。附带单文件 HTML 驾驶舱，默认物理模式读取 NOAA SWPC 遥测，可选经 localhost 桥加载 14 个冻结 .joblib 伪影运行完整 ML 管线。所有阶段在单 CPU 核上运行，原始观测数据不随包分发。

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

- 五级全本地预测管线：LightGBM/XGBoost 集成、CQR 与自适应 conformal 区间
- 零安装单文件 HTML 驾驶舱，浏览器直接运行并读取九路 SWPC 遥测
- 14 个冻结 .joblib 伪影随包分发，可复现四格表与基准数字
- 21 项测试编码两个信息不可行门限，防止阈值松动

## 适用场景

- 复现或检验 CME 到达时间预报的信息上限测量
- 读取 SWPC 实时遥测查看物理模式的到达时间与 Dst 预测
- 以驾驶舱 or CLI 跑通冻结伪影得到四格基准表

## 场景标签

`科研工具` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: > **An empirical information-ceiling study of CME arrival-time forecasting across Solar Cycles 23–25, with a fully a
> L162: |1. Impact|probability that the CME reaches Earth|launch|five-member ensemble (LightGBM, XGBoost, logistic regress
> L19: |**Standalone** (default)|exact v3.4 physics backbone + live NOAA SWPC telemetry|physics-only: exact DBM transit (7

## 星数曲线

```mermaid
xychart-beta
    title "Zar-Manah/HELIOS-Space-Weather 星数(近 2 点)"
    x-axis ["2026-11-13", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-13 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `f7d36496acd4` · [字段定义](../../DATASET.md)*
