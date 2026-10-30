# ThomasMBury/deep-early-warnings-pnas

⭐ 67 · Python · NOASSERTION · 推送 2025-11-28 · [GitHub](https://github.com/ThomasMBury/deep-early-warnings-pnas) · 个人维护

**复现 PNAS 2021 论文的深度学习临界预警信号代码**

PNAS 2021 论文《Deep learning for early warning signals of tipping points》的配套复现代码：用 AUTO-07P 生成分岔训练数据（共 70 万条时间序列，已存档 Zenodo），训练 20 个 TensorFlow 神经网络分类器识别 fold/Hopf/transcritical 分岔预警，并与 CSD 方差、滞后一阶自相关指标在数学模型与经验数据（地中海沉积、热声不稳定性、古气候）上做 ROC 对比。需要 Python 3.9+、TensorFlow 2.15.0 与 AUTO-07P；单网络 GPU 训练约 24 小时，训练数据生成需 CPU 集群并行。作者另维护 ewstools 包供应用层面使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AUTO-07P 生成分岔训练数据，含 fold/Hopf/transcritical/null 四类结果
- 训练 20 个神经网络分类器，预测取平均
- 在三个经验数据集上与 CSD 指标做 ROC 对比
- 完整训练数据集（5.87GB/5.38GB）存档于 Zenodo

## 适用场景

- 复现论文全部图表与结果
- 基于生成的时间序列训练自己的预警分类器
- 参考工作流将 DL 预警方法应用到其他时间序列数据

## 场景标签

 · 领域:计算科学/动力系统

## 证据(README 行号)

> L1: # Deep learning for early warning signals of tipping points
> L4: #### *Deep learning for early warning signals of tipping points*. Thomas M. Bury, R. I. Sujith, Induja Pavithran, )M

## 星数曲线

```mermaid
xychart-beta
    title "ThomasMBury/deep-early-warnings-pnas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-30 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `015ca32703ec` · [字段定义](../../DATASET.md)*
