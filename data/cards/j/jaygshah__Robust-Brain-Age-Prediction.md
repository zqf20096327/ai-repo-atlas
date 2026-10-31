# jaygshah/Robust-Brain-Age-Prediction

⭐ 19 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/jaygshah/Robust-Brain-Age-Prediction) · [官网](https://doi.org/10.1109/wacv57701.2024.00770) · 组织维护

**从 MRI 预测脑年龄的 PyTorch 官方实现（WACV 2024）**

论文 Ordinal Classification with Distance Regularization for Robust Brain Age Prediction 的官方 PyTorch 实现：将脑年龄预测从回归改写为有序分类，提出 ORDER 损失（按年龄差加权特征距离）与交叉熵联合训练，以缓解回归到均值导致的系统性偏差。面向医学影像研究人员，基于 MONAI/PyTorch，提供 age_binning 数据分箱、train.py 训练（含 mse/ce/order 等多种损失）与 evaluate.py 推理评估脚本，输出 MAE、ordinality、SB-L/SB-R 指标。需自备 MRI 数据与 GPU 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将脑年龄任务从回归改写为有序分类
- ORDER 损失保留年龄标签的有序信息
- 提供数据分箱、训练与评估完整脚本
- 报告 MAE/ordinality/系统性偏差（SB-L/SB-R）指标

## 适用场景

- 用我的 MRI 数据训练脑年龄预测模型
- 比较不同损失函数对预测偏差的影响
- 在外部队列上评估脑年龄预测并提取 BrainAGE

## 场景标签

 · 领域:医学影像分析/神经科学

## 证据(README 行号)

> L3: Official PyTorch implementation of **Ordinal Classification with Distance Regularization for Robust Brain Age Predic
> L16: Age is one of the major known risk factors for Alzheimer's Disease (AD). Detecting AD early is crucial for effectiv

## 星数曲线

```mermaid
xychart-beta
    title "jaygshah/Robust-Brain-Age-Prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bb52bfdfe8b0` · [字段定义](../../DATASET.md)*
