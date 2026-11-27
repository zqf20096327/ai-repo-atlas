# selimfirat/pysad

⭐ 322 · Python · BSD-3-Clause · 推送 2026-11-26 · [GitHub](https://github.com/selimfirat/pysad) · [官网](https://pysad.readthedocs.io/en/stable/) · 个人维护 · 中文 README

**Python 流式异常检测库：逐点评分 50+ 在线检测器**

面向数据流场景的 Python 异常检测库，提供 LODA、RRCF、Half-Space Trees、xStream、DAMP、SAND 等 50+ 多元/单变量在线检测器，每个数据点到达时即时学习与评分。核心机制包括共形校准将任意分数归一化到 [0,1] 并触发告警、10 种漂移监测器、prequential 评测（先评分后学习），以及用 |、& 组合预处理/检测/校准的流水线。提供 MCP server、实时终端仪表盘和可选 Rust 加速内核。限制：非本产品需要的系统级依赖为无 JVM，但可选 CapyMOA 集成需 Java（该库本身不依赖）。

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

- 50+ 在线多元/单变量检测器（LODA/RRCF/xStream/DAMP/SAND 等）
- 共形/极值/高斯尾校准器将原始分数归一化并触发二值告警
- prequential 评测与 17 个 ODDS、58 个 NAB 序列的基准复现
- 通过 MCP 协议暴露检测器、漂移计与解释功能

## 适用场景

- 对传感器或指标数据流逐点做异常评分并输出校准告警
- 检测网络流量、日志中的入侵或异常事件
- 处理带概念漂移的数据流并自动重置检测器
- 在欺诈检测中回放信用卡交易流并计算流式 AUROC

## 场景标签

 · 领域:机器学习/流式异常检测

## 证据(README 行号)

> L7:  Streaming anomaly detection in Python for multivariate and univariate data streams.
> L8:  PySAD scores and learns from each point as it arrives, with calibrated alerts, drift handling, and prequential eval
> L104: - `pysad.mcp` exposes detectors, drift meters, and explanations through the Model Context Protocol (MCP). Install 

## 星数曲线

```mermaid
xychart-beta
    title "selimfirat/pysad 星数(近 11 点)"
    x-axis ["2026-10-25", "2026-10-28", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-25", "2026-11-27"]
    y-axis "stars" 313 --> 323
    line [314, 315, 314, 318, 319, 320, 321, 322, 321, 322, 322]
```

2026-10-25 314 → 2026-11-27 322（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `77f5231ca6c2` · [字段定义](../../DATASET.md)*
