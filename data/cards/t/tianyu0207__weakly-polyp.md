# tianyu0207/weakly-polyp

⭐ 46 · Python · NOASSERTION · 推送 2025-11-12 · [GitHub](https://github.com/tianyu0207/weakly-polyp) · 组织维护

**弱监督息肉视频帧检测的对比 Transformer MIL 代码与数据集**

MICCAI'22 论文官方仓库：提出基于对比 Transformer 与多示例学习（MIL）的方法，在仅有视频级标签的弱监督设定下检测结肠镜视频中的息肉帧。提供数据集下载入口（预处理 I3D 特征与原始结肠镜视频）、训练命令（python main_transformer.py）与推理命令（python inference.py），并附论文及数据集（LDPolypVideo、HyperKvasir）引用信息。面向医学影像研究者复现论文结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对比 Transformer + 多示例学习的弱监督息肉帧检测
- 提供预处理 I3D 特征数据集下载链接
- 提供训练与推理脚本（main_transformer.py / inference.py）

## 适用场景

- 复现 MICCAI'22 论文的弱监督息肉检测方法
- 在结肠镜视频数据上训练/评估息肉帧检测模型
- 作为弱监督 MIL 医学视频异常检测的参考实现

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: > [**MICCAI'22 Early Accept**] **Contrastive Transformer-based Multiple Instance Learning for Weakly Supervised Poly
> L17: After downloading the dataset and extracting the I3D features using this **repo**, simply run the following command

## 星数曲线

```mermaid
xychart-beta
    title "tianyu0207/weakly-polyp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-30 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `dc5746c83cd0` · [字段定义](../../DATASET.md)*
