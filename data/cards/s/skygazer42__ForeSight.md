# skygazer42/ForeSight

⭐ 119 · Python · GPL-3.0 · 推送 2026-05-03 · [GitHub](https://github.com/skygazer42/ForeSight) · 个人维护

**Python 时间序列预测工具包：统一接口调用 250+ 统计/ML/深度学习模型**

面向 Python 开发者的时间序列预测工具包，以统一注册表与接口组织 250+ 模型，覆盖统计（ARIMA/ETS/theta 等）、机器学习（sklearn/XGBoost/LightGBM/CatBoost）与 PyTorch 深度学习（Transformer/RNN/CNN/SSM 等）7 种后端。工作流以 walk-forward 回测为先，提供 20+ 点预测与概率化指标、预测区间、网格调参、排行榜与 CLI。数据采用 unique_id/ds/y 长格式，核心安装仅依赖 numpy+pandas，重后端经可选 extras 安装。beta 适配器（sktime/Darts/GluonTS）与实验性模型族不在稳定兼容承诺范围内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 250+ 注册模型经统一接口调用，涵盖统计/ML/深度学习 7 种后端
- walk-forward 回测、交叉验证表、多数据集 sweep 与网格调参
- conformal/bootstrap 区间与 Pinball/CRPS/Winkler 等概率化指标
- 核心安装仅依赖 numpy+pandas，重运行时按 extras 可选加载

## 适用场景

- 用统一 API 对比统计与深度学习模型在历史数据上的预测表现
- 做 walk-forward 回测并生成模型排行榜
- 训练跨多条序列的全局/面板模型并输出分位数区间预测
- 通过 CLI 完成从数据加载到预测与导出的完整流程

## 场景标签

 · 领域:时间序列预测/机器学习

## 证据(README 行号)

> L19: - One interface across statistical, ML, and deep learning forecasters.
> L208: |MLP / Linear|`torch-mlp-direct`, `torch-nlinear-direct`, `torch-dlinear-direct`, `torch-tide-direct`, `torch-kan-
> L276: - Walk-forward backtesting with expanding or rolling windows.

## 星数曲线

```mermaid
xychart-beta
    title "skygazer42/ForeSight 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 118 --> 120
    line [119, 119]
```

2026-10-18 119 → 2026-10-28 119（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a85c4655284e` · [字段定义](../../DATASET.md)*
