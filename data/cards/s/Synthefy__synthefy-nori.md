# Synthefy/synthefy-nori

⭐ 76 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/Synthefy/synthefy-nori) · [官网](https://docs.synthefy.com/nori/) · 组织维护

**表格数据基础模型：免训练上下文学习回归并给出预测分布**

Synthefy 维护的开源表格基础模型，通过上下文学习做回归：fit 仅存储标注行作为上下文，predict 单次前向即出结果，无需任务专属训练或微调。提供 nori-6m/1-5/30m/100m 四个规模（nori-1-5 约 21M 参数），权重托管在 Hugging Face Hub 公开可下载。模型完全在合成数据上训练，内置 999 分位 pinball 头输出预测区间。以 scikit-learn 风格估计器 NoriRegressor 提供，另支持 remote/SageMaker 客户端模式与时间序列预测包。设备自动优先 CUDA、Apple MPS、CPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上下文学习回归：无训练循环、无梯度更新，单次前向预测
- 999 分位 pinball 头，原生输出分位数/完整预测分布与预测区间
- 四个模型规模，权重公开托管于 Hugging Face Hub，首次调用自动下载
- 支持 pandas 数值/类别/文本混合列，缺失值经学习 mask 嵌入原生处理

## 适用场景

- 拿少量标注行直接做表格回归预测，跳过训练调参流程
- 为回归结果生成预测区间和不确定性量化
- 在类别/有序目标（评分、计数）上做离散化预测

## 场景标签

 · 领域:机器学习/表格数据基础模型

## 证据(README 行号)

> L11: Nori is a tabular foundation model for **regression**
> L12: via in-context learning (ICL). Given a few labeled rows as context, it predicts on
> L13: new query rows in a single forward pass, with no task-specific training or fine-tuning.

## 星数曲线

```mermaid
xychart-beta
    title "Synthefy/synthefy-nori 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-26 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `047c92195e17` · [字段定义](../../DATASET.md)*
