# Dootmaan/MT-UNet

⭐ 198 · Python · MIT · 推送 2026-03-02 · [GitHub](https://github.com/Dootmaan/MT-UNet) · 个人维护

**ICASSP 2022 医学图像分割网络 MT-UNet 官方实现**

论文 *Mixed Transformer UNet for Medical Image Segmentation* 的官方 PyTorch 代码：提供在 Synapse 与 ACDC 两个数据集上的训练脚本（train_mtunet_Synapse.py / train_mtunet_ACDC.py），权重与预处理数据已迁移至 Zenodo 长期共享。ACDC 采用作者自建划分并自行复跑所有对比方法。使用方式为 git clone 后修改数据路径，以 CUDA_VISIBLE_DEVICES 指定 GPU 后台训练；早期私下索取的旧版代码已被声明弃用，应使用仓库最新版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Synapse 与 ACDC 数据集训练脚本与预训练权重（Zenodo 托管）
- ACDC 采用作者自建数据划分以保证对比公平
- 支持加载公开权重继续训练（argparser 参数）
- 默认输出 checkpoint 至 ./checkpoint、预测至 ./predictions

## 适用场景

- 复现论文中医学图像分割实验结果
- 在自有医学影像数据上训练 MT-UNet 模型
- 基于公开预训练权重做迁移或继续训练

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L74: This is the official implementation for our ICASSP2022 paper *MIXED TRANSFORMER UNET FOR MEDICAL IMAGE SEGMENTATION
> L41: CUDA_VISIBLE_DEVICES=0 nohup python3 -u train_mtunet_ACDC.py >train_mtunet_ACDC.log 2>&1 &

## 星数曲线

```mermaid
xychart-beta
    title "Dootmaan/MT-UNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 197 --> 199
    line [198, 198]
```

2026-10-18 198 → 2026-10-30 198（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `49d2e71a9bc4` · [字段定义](../../DATASET.md)*
