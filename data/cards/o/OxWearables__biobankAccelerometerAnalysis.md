# OxWearables/biobankAccelerometerAnalysis

⭐ 253 · Python · NOASSERTION · 推送 2025-11-10 · [GitHub](https://github.com/OxWearables/biobankAccelerometerAnalysis) · [官网](https://biobankaccanalysis.readthedocs.io/en/latest/index.html) · 组织维护

**从大型加速度计数据集提取健康信息的处理工具**

读取 Axivity(.cwa)、Actigraph、GENEActiv 及自定义 CSV 格式的可穿戴加速度计原始数据，经校准、重采样与已发表的方法汇总，生成睡眠、久坐、身体活动等时间序列与汇总指标（JSON/CSV 输出），并提供活动曲线绘图与批量处理（递归扫描、压缩格式、容错）。适用于生物银行等大型加速度计数据集的健康研究分析，需 Python 3.7-3.10 与 Java 8 环境。

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

- 支持 Axivity/Actigraph/GENEActiv 及自定义 CSV 多种加速度计数据格式
- 批量处理支持递归扫描、压缩格式(.gz/.zip/.bz2/.xz)与容错继续
- 输出时间序列与汇总指标（睡眠/久坐/身体活动）及活动曲线图
- 采用已发表方法进行校准、重采样与汇总

## 适用场景

- 处理 UK Biobank 等大型加速度计数据集并提取健康行为指标
- 批量转换多个传感器品牌原始数据为汇总统计
- 生成个体活动时间曲线用于研究分析

## 场景标签

`数据分析` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L7: A tool to extract meaningful health information from large accelerometer datasets. The software generates time-serie
> L56: Actigraph and GENEActiv files are also supported, as well as custom CSV files. See Usage for more details.

## 星数曲线

```mermaid
xychart-beta
    title "OxWearables/biobankAccelerometerAnalysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 251 --> 254
    line [252, 253]
```

2026-10-18 252 → 2026-10-22 253（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9956475dfa1a` · [字段定义](../../DATASET.md)*
