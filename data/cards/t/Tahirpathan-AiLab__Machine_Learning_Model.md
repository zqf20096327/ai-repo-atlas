# Tahirpathan-AiLab/Machine_Learning_Model

⭐ 24 · Python · 推送 2026-10-18 · [GitHub](https://github.com/Tahirpathan-AiLab/Machine_Learning_Model) · [官网](https://www.linkedin.com/in/tahirpathan/) · 个人维护

**杠铃动作可穿戴传感器数据的特征工程流水线**

基于 MetaMotion 手环（加速度计+陀螺仪）数据的端到端特征工程流水线，处理五名参与者的六类杠铃动作（卧推/深蹲/推举/硬拉/划船/静止，分重/中重量）。流程包括：线性插值补全离群值剔除后产生的缺失值、Butterworth 低通滤波降噪、PCA 降维、矢量幅值计算、滚动窗口时序抽象、FFT 频域特征（主频/功率谱熵等）与 K-Means 聚类，最终输出 Pickle 格式特征数据集，供动作分类与自动次数统计等任务使用。以 Python 代码项目形式提供，需先具备已清洗的数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Butterworth 低通滤波 + PCA + FFT 频域特征 + K-Means 聚类的完整特征管线
- 输出含主成分、矢量幅值、滚动统计、频域与聚类标签的特征数据集（Pickle）
- 按 Chauvenet 准则剔除离群值后通过线性插值恢复信号连续性

## 适用场景

- 把可穿戴传感器原始信号转成可用于动作分类的特征数据集
- 为杠铃训练动作识别与自动次数统计准备训练数据
- 复用导出的 Pickle 特征集做人活动识别（HAR）模型训练

## 场景标签

 · 领域:机器学习/运动传感分析

## 证据(README 行号)

> L7: My contribution begins after the dataset has been cleaned through preprocessing and statistical outlier removal. In 
> L11: The repository demonstrates how wearable sensor recordings can be transformed into highly informative machine learn
> L56: The final output is a comprehensive machine learning dataset containing original sensor values, statistical feature

## 星数曲线

```mermaid
xychart-beta
    title "Tahirpathan-AiLab/Machine_Learning_Model 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ca4d1cc906b6` · [字段定义](../../DATASET.md)*
