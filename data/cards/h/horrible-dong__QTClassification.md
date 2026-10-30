# horrible-dong/QTClassification

⭐ 20 · Python · Apache-2.0 · 推送 2026-05-27 · [GitHub](https://github.com/horrible-dong/QTClassification) · 个人维护 · 中文 README

**轻量可扩展的 PyTorch 图像分类工具箱（QTCLS）**

基于 PyTorch 的图像分类训练与评估工具箱（QTCLS），作者为浙江大学 QIU Tian。提供命令行与 config 文件两种方式运行训练/评估，内置 mnist、cifar10/100、imagenet1k 等数据集自动下载，默认模型库扩展自 torchvision 与 timm，涵盖 ResNet、ViT、Swin 等 30 余个模型家族，也支持原始 timm 全部模型。数据集、模型、损失、优化器、调度器、评估器均可注册扩展。开发环境为 python 3.8 & pytorch 1.13.1+cu117，支持单卡/多卡与 AMP 混合精度训练。Apache 2.0 许可。

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

- 命令行与 .py config 文件两种训练/评估方式，参数可覆盖合并
- 默认模型库扩展自 torchvision 与 timm，覆盖 30 余个模型家族，另支持原始 timm 全部模型
- 数据集/模型/损失/优化器/调度器/评估器均可注册扩展
- 10 个数据集自动下载，支持 folder 格式与假数据调试（--dummy）

## 适用场景

- 快速上手图像分类模型的训练与评估
- 通过注册接口扩展自定义数据集、模型或训练组件
- 在不同模型家族间用统一配置进行对比实验（--comp_dirs 日志对比）

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: **A lightweight and extensible toolbox for image classification and MORE**
> L122: |`--model_lib`|Model library where models come from. The toolbox's basic (default) model library is extended from 
> L180: The toolbox's basic (default) model library is extended from `torchvision` and `timm`,

## 星数曲线

```mermaid
xychart-beta
    title "horrible-dong/QTClassification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5dc739995844` · [字段定义](../../DATASET.md)*
