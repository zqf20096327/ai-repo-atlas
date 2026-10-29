# jaehyunnn/DeepAerialMatching_pytorch

⭐ 92 · Python · 推送 2026-01-13 · [GitHub](https://github.com/jaehyunnn/DeepAerialMatching_pytorch) · 个人维护

**航拍图像匹配的 PyTorch 官方实现：两流对称网络**

论文《A Two-Stream Symmetric Network with Bidirectional Ensemble for Aerial Image Matching》(Remote Sensing 2020) 的官方 PyTorch 实现，提供 CNN（ResNet101/ResNeXt101/SE-ResNeXt101/DenseNet169）与 ViT-L/16（DINOv3 sat493m 预训练）骨干、特征相关与回归模块，输出图像匹配结果；v2.0 加入 dual softmax 相关、GroupNorm 与 Muon 优化器。模型与数据集托管于 Hugging Face Hub，提供 install.sh 安装脚本、demo 脚本与变换标签生成器。需 Python>=3.9、PyTorch>=2.5、timm>=1.0；ViT 模型含私有数据训练成分。

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

- 支持 5 种骨干（含 DINOv3 预训练的 ViT-L/16），PCK@0.05 达 99.0%
- 模型与训练/评测数据集（18K 对训练、500 对评测）托管于 Hugging Face Hub
- 标签生成器支持 affine/homography 随机变换标注
- v2.0 加入 dual softmax 相关、GroupNorm、Muon 优化器

## 适用场景

- 做航拍/遥感图像匹配与配准研究
- 复现论文实验或评测预训练模型
- 生成随机变换标签用于训练数据构造

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: Official PyTorch implementation of:
> L5: > **A Two-Stream Symmetric Network with Bidirectional Ensemble for Aerial Image Matching**
> L128: ### Model Architecture

## 星数曲线

```mermaid
xychart-beta
    title "jaehyunnn/DeepAerialMatching_pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-29 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `58d8b177486d` · [字段定义](../../DATASET.md)*
