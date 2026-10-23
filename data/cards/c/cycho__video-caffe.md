# cycho/video-caffe

⭐ 176 · C++ · NOASSERTION · 推送 2026-09-06 · [GitHub](https://github.com/cycho/video-caffe) · 个人维护

**Caffe 的 3D 卷积扩展：视频读取与 C3D 网络训练**

将 Facebook C3D 概念与视频读取器移植到较新版 Caffe（rebase 于 2018 年 8 月）的分支仓库，提供 NdConvolution/NdPooling 层与视频输入层，支持以 (L x H x W) 3D 形状指定卷积/池化参数。面向使用 Caffe 做视频动作识别的研究者，附 UCF-101 上的 C3D 训练示例脚本与预训练模型（top-1 约 47%）。构建依赖 CUDA 与 cuDNN（已知兼容 v4/v5），refactor 分支尚未包含 Python 包装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在较新 Caffe 上实现 3D 卷积/池化（NdConvolution/NdPooling）
- 自带视频读取器，支持直接读视频或抽取帧
- UCF-101 的 C3D 训练脚本与预训练模型（top-1 约 47%）

## 适用场景

- 我在 Caffe 框架下训练 C3D 做视频动作识别
- 我需要视频读取与 3D 卷积集成的深度学习工具链
- 在 UCF-101 数据集上复现或微调 C3D 训练

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L1: # Video-Caffe: Caffe with C3D implementation and video reader
> L36: Look at `${video-caffe-root}/examples/c3d_ucf101/c3d_ucf101_train_test.prototxt` for how 3D convolution and pooling

## 星数曲线

```mermaid
xychart-beta
    title "cycho/video-caffe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 175 --> 177
    line [176, 176]
```

2026-10-18 176 → 2026-10-23 176（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `235830924518` · [字段定义](../../DATASET.md)*
