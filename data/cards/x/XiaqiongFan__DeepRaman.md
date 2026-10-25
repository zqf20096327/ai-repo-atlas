# XiaqiongFan/DeepRaman

⭐ 36 · Python · MIT · 推送 2025-11-02 · [GitHub](https://github.com/XiaqiongFan/DeepRaman) · 个人维护

**基于伪孪生神经网络的拉曼光谱混合物成分识别工具**

提供名为 DeepRaman 的深度学习方法，用于拉曼光谱的成分鉴定：通过带空间金字塔池化的伪孪生神经网络（pSNN+SPP），将纯组分光谱与未知样品光谱进行比对，预测混合物中的成分。README 提到其在人工甜味剂 SERS 数据集与火药拉曼成像数据集上的结果。使用方式为运行 training.py 训练模型、运行 testing.py 预测，示例数据需从 releases 下载，依赖通过 requirements.txt 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 伪孪生神经网络 + 空间金字塔池化的光谱比对架构
- 输入纯组分光谱与未知光谱，预测混合物成分
- 提供训练（training.py）与预测（testing.py）脚本及示例数据

## 适用场景

- 科研人员对混合物拉曼光谱做成分鉴定
- 训练自己的拉曼光谱识别模型并用新样品光谱预测

## 场景标签

 · 领域:光谱分析/化学计量学

## 证据(README 行号)

> L3: Raman spectra contain abundant information from molecules but are difficult to analyze, especially for the mixtures.
> L19: Run the file 'testing.py'. Some data has been upload as examples.

## 星数曲线

```mermaid
xychart-beta
    title "XiaqiongFan/DeepRaman 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a74e73239f66` · [字段定义](../../DATASET.md)*
