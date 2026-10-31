# DegangWang97/IEEE_TGRS_DirectNet

⭐ 15 · Python · GPL-2.0 · 推送 2026-07-14 · [GitHub](https://github.com/DegangWang97/IEEE_TGRS_DirectNet) · [官网](https://ieeexplore.ieee.org/abstract/document/10400466) · 个人维护

**高光谱异常检测论文官方代码：双窗口重建网络 DirectNet**

IEEE TGRS 2024 论文（ESI 高被引）的 PyTorch 官方实现。面向无监督高光谱异常检测（HAD）：通过盲区网络结构中的滑动双窗口机制，擦除中心块信息，仅用外窗口感受野重建中心像素，使重建结果收敛于背景分布，从而放大异常目标的重建误差实现检测。网络深度自适应输入块尺寸。在四个数据集上实验。提供训练/测试命令，需自备 .mat 格式数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 滑动双窗口 + 盲区（blind-block）重建架构
- 网络深度自适应输入图像块尺寸，感受野与输入对齐
- 仅用外窗口信息重建中心像素，抑制异常对重建的影响
- 四个数据集上的实验，支持 Pavia 等数据集训练与预测命令

## 适用场景

- 复现论文的高光谱异常检测实验结果
- 在自己的 .mat 高光谱数据上训练与测试异常检测模型
- 作为 HAD 方法的对比基线代码

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L8: Hyperspectral anomaly detection (HAD) aims to identify anomalous objects that deviate from surrounding backgrounds i
> L30: python main.py --command train --dataset Pavia --batch_size 100 --epochs 1000 --learning_rate 1e-4 --win_out 19 --w

## 星数曲线

```mermaid
xychart-beta
    title "DegangWang97/IEEE_TGRS_DirectNet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0c452eb2610f` · [字段定义](../../DATASET.md)*
