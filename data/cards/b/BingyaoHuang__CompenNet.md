# BingyaoHuang/CompenNet

⭐ 40 · Python · NOASSERTION · 推送 2025-12-15 · [GitHub](https://github.com/BingyaoHuang/CompenNet) · 个人维护

**CVPR'19 论文 CompenNet 的 PyTorch 实现：投影仪光度补偿**

CVPR'19 口头报告论文 End-to-end Projector Photometric Compensation 的 PyTorch 官方实现。CompenNet 是一个卷积神经网络，将投影表面光度补偿问题表述为端到端学习问题，学习补偿函数以生成投影仪输入图像，使相机拍摄结果接近目标图像。提供独立于系统设置的评测基准与数据集，支持多 GPU 训练、visdom 可视化，并给出在自己相机-投影仪设备上采集数据（含单应性变换对齐）的流程与自实现模型对比接口。限定 PyTorch 0.4.0、Python 3.7，许可证为非营利非商业使用。

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

- 卷积神经网络端到端学习投影补偿函数
- 提供独立于系统设置的定量评测基准与数据集
- 支持多 GPU 训练与 visdom 训练过程可视化
- 可接入自有相机-投影仪设备的数据采集与训练流程

## 适用场景

- 复现 CVPR'19 投影光度补偿论文结果
- 在自己的投影表面上训练补偿模型
- 在基准上与自实现补偿模型做定量对比

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L6: PyTorch implementation of [CompenNet][1]. Also see [CompenNet++][9] and [journal version][8].
> L9: * For the first time, we formulate the compensation problem as an end-to-end learning problem and propose a convolut

## 星数曲线

```mermaid
xychart-beta
    title "BingyaoHuang/CompenNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-28 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d9504fe4210c` · [字段定义](../../DATASET.md)*
