# abbey2017/wind-energy-analytics

⭐ 28 · Python · BSD-3-Clause · 推送 2026-01-07 · [GitHub](https://github.com/abbey2017/wind-energy-analytics) · 个人维护

**风机 SCADA 数据分析库：功率曲线滤波与期望功率估计**

面向风电行业工程师与分析师的 Python 库（pip 包名 scada-data-analysis），帮助领域专家使用科研中的分析方法。对运行风机采集的时序数据提供模块化分析：功率曲线迭代滤波（区分正常/异常数据点）与基于运行数据的期望功率估计，可作为更大项目的构件使用。安装方式为克隆 GitHub 仓库（附带示例 notebook 与公开数据）并 pip 安装。当前 README 仅列出两个模块。

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

- 功率曲线迭代滤波，返回正常与异常数据点
- 基于运行数据的期望功率估计器
- 提供示例 notebook 与公开数据（随仓库克隆）

## 适用场景

- 风电工程师对风机 SCADA 时序数据做常规与非常规分析
- 清洗功率曲线数据、剔除异常数据点
- 在更大项目中复用基础分析模块估计期望功率

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: Modules are implemented for different routine and non-routine analysis of time series
> L6: data collected from operating wind turbines. Practicing wind engineers and analysts

## 星数曲线

```mermaid
xychart-beta
    title "abbey2017/wind-energy-analytics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `dffb069c3ddc` · [字段定义](../../DATASET.md)*
