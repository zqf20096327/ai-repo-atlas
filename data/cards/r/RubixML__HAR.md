# RubixML/HAR

⭐ 25 · PHP · MIT · 推送 2026-10-08 · [GitHub](https://github.com/RubixML/HAR) · [官网](https://rubixml.github.io/ML) · 组织维护

**基于手机传感器数据的六类人体活动识别示例项目**

Rubix ML 的官方示例工程：用 30 名志愿者手机 IMU 传感器（加速度计/陀螺仪）标注数据，训练 Softmax 分类器识别走路、上下楼、坐、站、躺六种活动。流水线含高斯随机投影降维（561 维降至 112 维）与 Z-score 标准化，支持分层验证切分、持久化保存/加载、交叉验证报告（准确率约 97%）。以教程形式给出 train.php 与 validate.php 完整源码，需 PHP 8.3+，通过 Composer 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Softmax 分类器 + Mini Batch 梯度下降（Momentum 优化器）训练
- 高斯随机投影将 561 维特征降至 112 维
- 模型与变换器持久化保存/加载，支持推理前 cleanup 释放状态
- 交叉验证报告含 Multiclass Breakdown 与 Confusion Matrix

## 适用场景

- 学习用 Rubix ML 构建完整分类流水线
- 复现人体活动识别（HAR）基线实验
- 参考降维与标准化在传感器数据上的用法

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: An example project that demonstrates the problem of human activity recognition (HAR) using mobile phone sensor data 
> L25: The experiments have been carried out with a group of 30 volunteers within an age bracket of 19-48 years. Each pers

## 星数曲线

```mermaid
xychart-beta
    title "RubixML/HAR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5c2ddd1e22b8` · [字段定义](../../DATASET.md)*
