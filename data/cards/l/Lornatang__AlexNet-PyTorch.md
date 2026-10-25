# Lornatang/AlexNet-PyTorch

⭐ 95 · Python · Apache-2.0 · 推送 2026-07-23 · [GitHub](https://github.com/Lornatang/AlexNet-PyTorch) · 个人维护 · 中文 README

**AlexNet 的 PyTorch 复现：供开发者训练与图像分类推理**

对论文 ImageNet Classification with Deep Convolutional Neural Networks（AlexNet, NIPS 2012）的 PyTorch 逐操作复现仓库。提供 ImageNet_1K 预训练权重下载（Google/Baidu 网盘），通过修改 config.py 切换训练/测试/断点续训模式，运行 train.py、test.py 或 inference.py 完成图像分类，测试输出 Top-1/Top-5 错误率对比与逐类别置信度。支持 MNIST、CIFAR10/100、TinyImageNet_200 等多种数据集制作说明。使用需自行下载权重与数据集，无 pip 安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AlexNet 论文的 PyTorch 逐操作复现实现
- 提供 ImageNet_1K 预训练权重（Google/Baidu 网盘下载）
- 通过 config.py 单文件配置训练/测试/断点续训
- inference.py 直接输出逐类别分类置信度

## 适用场景

- 学习经典 CNN 结构的 PyTorch 实现细节
- 在自有图像数据集上训练 AlexNet 分类模型
- 加载预训练权重做图像分类推理验证

## 场景标签

`模型训练` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L8: This repository contains an op-for-op PyTorch reimplementation of ImageNet Classification with Deep Convolutional Ne
> L75: python3 ./inference.py

## 星数曲线

```mermaid
xychart-beta
    title "Lornatang/AlexNet-PyTorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-25 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `dfc1d02f8404` · [字段定义](../../DATASET.md)*
