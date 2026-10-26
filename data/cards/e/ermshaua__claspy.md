# ermshaua/claspy

⭐ 146 · Jupyter Notebook · BSD-3-Clause · 推送 2026-03-19 · [GitHub](https://github.com/ermshaua/claspy) · 组织维护

**时间序列分割 Python 库：无参数变点检测与状态识别**

ClaSP 算法的官方 Python 实现，提供时间序列分割能力：BinaryClaSPSegmentation 支持单变量与多变量时序的变点检测，参数无需设置，输出 0-1 分数剖面并可视化；StreamingClaSPSegmentation 面向流式时序实时分割（每秒数千观测点），自动滑窗管理内存；另含 CLaP 状态检测，推断潜在系统状态及转移结构。面向科研与数据分析用户，通过 pip 安装，附 Jupyter 示例与引用文献。

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

- 单变量/多变量时间序列的无参数变点检测
- 流式实时分割实现（每秒数千观测点，自动滑窗）
- CLaP 状态检测：推断状态序列与转移结构
- 内置 TSSB/HAS 数据加载与分割可视化

## 适用场景

- 对传感器信号做语义分段或变点检测
- 流式 ECG 等实时监控中即时检测状态变化
- 从重复出现的分段中恢复系统状态与转移过程
- 作为分类或异常检测的预处理步骤

## 场景标签

`数据分析` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L4: Time series segmentation (TSS) tries to partition a time series (TS) into semantically meaningful segments. It's an 
> L19: As an example, we choose the Cricket data set that contains motions of different umpire signals captured as wrist a

## 星数曲线

```mermaid
xychart-beta
    title "ermshaua/claspy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 145 --> 147
    line [146, 146]
```

2026-10-18 146 → 2026-10-26 146（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9941335c257c` · [字段定义](../../DATASET.md)*
