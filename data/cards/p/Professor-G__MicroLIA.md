# Professor-G/MicroLIA

⭐ 17 · Python · GPL-3.0 · 推送 2026-01-26 · [GitHub](https://github.com/Professor-G/MicroLIA) · 组织维护

**用机器学习检测广域巡天数据中微引力透镜事件的分类引擎**

开源 Python 程序，面向时域巡天数据检测微引力透镜事件。内置模块生成 PSPL 模拟光变曲线（也支持用户自带光变曲线，类别数不限），计算 148 个统计特征（含导数空间重算），提供特征选择、贝叶斯超参优化、数据插补与模型保存加载。支持 Python 3.9+，pip 安装。文档建议对候选事件用 pyLIMA 拟合作二次过滤，误报在数据质量差时较明显。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 148 个时序统计特征（含导数空间）并支持按误差加权
- 特征选择与贝叶斯超参数优化
- 训练集可用自带光变曲线目录生成，类别数不限
- 基于 RR-Lyrae 模板模拟短周期变星

## 适用场景

- 巡天光变曲线中筛选微引力透镜候选事件
- 模拟含微透镜与变星的光变曲线训练集
- 对候选事件结合 pyLIMA 拟合降低误报

## 场景标签

 · 领域:天文学/时域巡天

## 证据(README 行号)

> L7: MicroLIA is an open-source program for detecting microlensing events in wide-field surveys. You can use the built-in
> L25: * The machine learning engine hyperparameters can now be optimized using Bayesian analysis.

## 星数曲线

```mermaid
xychart-beta
    title "Professor-G/MicroLIA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `66d16c2af30b` · [字段定义](../../DATASET.md)*
