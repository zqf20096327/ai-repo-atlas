# pohl-michel/time-series-forecasting-uoro-rtrl

⭐ 17 · MATLAB · BSD-3-Clause · 推送 2026-07-04 · [GitHub](https://github.com/pohl-michel/time-series-forecasting-uoro-rtrl) · [官网](https://doi.org/10.48550/arXiv.2106.01100) · 个人维护

**MATLAB RNN 呼吸运动时间序列预测代码（UORO/RTRL）**

MATLAB 实现的多变量时间序列预测研究代码：用 UORO 或 RTRL 在线训练 vanilla RNN，附带 LMS 与普通最小二乘线性自回归基线；应用于胸部/腹部外部标记物的呼吸运动预测，用于肺癌放疗场景。包含数据转换脚本、网格搜索超参数优化脚本（需 Parallel Computing Toolbox）、可配置 GPU 计算与梯度裁剪。作者声明本仓库为 2022 年论文原始代码，更新的合并实现位于 2D-MR-image-prediction 仓库。BSD-3-Clause 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- UORO 与 RTRL 在线训练的 vanilla RNN 实现
- 附 LMS 与普通最小二乘线性自回归基线
- 网格搜索超参数优化脚本（验证集选参、测试集评估）
- 支持 GPU 计算（MATLAB Parallel Computing Toolbox）

## 适用场景

- 复现呼吸运动预测论文结果
- 研究在线学习算法（UORO/RTRL）在时间序列预测中的应用
- 在自有多变量时序数据上运行 RNN 预测（指标假设为 3D 标记物坐标）

## 场景标签

 · 领域:医疗/机器学习（呼吸运动预测）

## 证据(README 行号)

> L7: This repository contains MATLAB code for forecasting multivariate time-series data. Specifically, it implements vani
> L67:  - Michel Pohl, Mitsuru Uesaka, Hiroyuki Takahashi, Kazuyuki Demachi, Ritu Bhusal Chhatkuli, "Prediction of the Pos

## 星数曲线

```mermaid
xychart-beta
    title "pohl-michel/time-series-forecasting-uoro-rtrl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1f54bd873021` · [字段定义](../../DATASET.md)*
