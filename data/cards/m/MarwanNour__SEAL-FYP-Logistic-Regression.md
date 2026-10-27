# MarwanNour/SEAL-FYP-Logistic-Regression

⭐ 33 · C++ · GPL-3.0 · 推送 2026-04-04 · [GitHub](https://github.com/MarwanNour/SEAL-FYP-Logistic-Regression) · 个人维护

**基于 Microsoft SEAL 的同态加密逻辑回归毕业设计项目**

作者的个人毕业设计（FYP）代码库，使用 Microsoft SEAL 3.4.5 在全同态加密数据上实现逻辑回归：提供矩阵/向量同态运算（线性变换、矩阵乘法、转置）、多项式求值（Horner 法与树法）、sigmoid 的 3/5/7 次多项式逼近及 CKKS 加密逻辑回归训练与预测，并附带基准测试与 GNUPlot 图表生成。限制：依赖 SEAL 3.4.5（3.6 迁移待做），需先安装 Microsoft SEAL 并用 CMake/Make 编译，图表演示需另装 GNUPlot 与 Python 3。属研究/学习性质项目，尚无正式发布形态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CKKS 方案上的加密逻辑回归（含多项式逼近的 sigmoid）
- 同态矩阵/向量运算（线性变换、矩阵乘法、转置）
- Horner 法与树法两种多项式求值实现
- CKKS 基准测试（向量规模 10/100/1000）与 GNUPlot 图表生成

## 适用场景

- 学习如何在加密数据上训练逻辑回归模型
- 复现同态加密下的矩阵/向量运算与多项式逼近
- 作为隐私保护机器学习的实验参考代码

## 场景标签

 · 领域:密码学/隐私计算

## 证据(README 行号)

> L2: My final year project using Microsoft SEAL. The purpose of this project is to **Create Functionalities for Matrices 
> L89: This version of Logistic Regression works on encrypted data using the CKKS scheme. It has the same functions as the

## 星数曲线

```mermaid
xychart-beta
    title "MarwanNour/SEAL-FYP-Logistic-Regression 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `90c81faa821d` · [字段定义](../../DATASET.md)*
