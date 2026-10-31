# giddyyupp/ganilla

⭐ 482 · Python · NOASSERTION · 推送 2026-08-21 · [GitHub](https://github.com/giddyyupp/ganilla) · 个人维护

**GANILLA 官方 PyTorch 实现：照片到插画风格图像翻译**

GANILLA 论文的官方 PyTorch 实现，基于生成对抗网络（CycleGAN 结构、resnet_fpn 生成器）做图像到插画的风格翻译。支持 Linux/macOS/Windows，Python 2 或 3，CPU 或 NVIDIA GPU + CUDA CuDNN。提供训练与测试脚本、预训练模型下载与单侧生成（--model test）、Style & Content CNN 的训练/测试代码与权重，以及 visdom 训练可视化。安装方式为 git clone 源码加 pip 依赖，另提供 conda 依赖脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 CycleGAN 框架与 resnet_fpn 生成器的图像到插画翻译训练/测试代码
- 提供预训练模型下载与单侧生成（--model test、--dataset_mode single）
- 附带 Style & Content CNN 的训练代码与预训练权重
- 支持 Linux/macOS/Windows，CPU 或 NVIDIA GPU + CUDA

## 适用场景

- 在自己的图像对数据集上训练照片到插画的翻译模型
- 用预训练模型把照片批量转换为插画风格
- 复现论文实验或做风格迁移研究（如宫崎骏动画风格）

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: GANILLA: Generative Adversarial Networks for Image to Illustration Translation.
> L75: python train.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan --netG resnet_fpn

## 星数曲线

```mermaid
xychart-beta
    title "giddyyupp/ganilla 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 481 --> 483
    line [482, 482]
```

2026-10-18 482 → 2026-10-31 482（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `0deb75ebaa6b` · [字段定义](../../DATASET.md)*
