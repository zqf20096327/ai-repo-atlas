# cenkcorapci/fashion-parser

⭐ 24 · Python · MIT · 推送 2026-05-11 · [GitHub](https://github.com/cenkcorapci/fashion-parser) · 个人维护

**基于 Mask R-CNN 的服装图像分割模型训练与部署项目**

在 imaterialist-fashion-2019-FGVC6 数据集上训练 Mask R-CNN（ResNet-50 FPN）进行服装品类分割的 PyTorch 项目。提供 uv 管理依赖的训练脚本、TorchScript 导出脚本，以及通过 Docker 运行 NVIDIA Triton Inference Server 的生产部署流程与客户端推理脚本；配置用 python-dotenv 管理，可视化用 Matplotlib/OpenCV。面向希望训练并将时尚分割模型服务化的深度学习开发者。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Mask R-CNN（ResNet-50 FPN）服装分割训练脚本
- 导出 TorchScript 并以 Docker 运行 Triton Inference Server 部署
- uv 包管理与 .env 配置
- 提供 Triton 客户端推理脚本

## 适用场景

- 在 imaterialist-fashion-2019 数据集上训练服装分割模型
- 将训练好的模型通过 Triton 以 Docker 方式部署
- 对图像执行服装品类分割推理

## 场景标签

`目标检测` `推理引擎` · 领域:感知与多模态

## 证据(README 行号)

> L8: Fashion segmentation based on **Mask R-CNN** (ResNet-50 FPN) using the imaterialist-fashion-2019-FGVC6 dataset.
> L14: |**Framework**|PyTorch 2.1+, Torchvision|

## 星数曲线

```mermaid
xychart-beta
    title "cenkcorapci/fashion-parser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8f4ce780050b` · [字段定义](../../DATASET.md)*
