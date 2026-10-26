# snehitvaddi/Deep-Fake_First_Order_Model

⭐ 64 · Jupyter Notebook · NOASSERTION · 推送 2026-07-17 · [GitHub](https://github.com/snehitvaddi/Deep-Fake_First_Order_Model) · 个人维护

**First Order Motion Model 图像动画实现：用驱动视频让静态图动起来**

基于论文 First Order Motion Model for Image Animation 的源码整理仓库，转自 Two Minute Papers 视频介绍，原始代码来自 Aliaksandr Siarohin。功能是对一张源图像配一段驾驶视频，生成图像动画（deepfake 风格），输出 result.mp4。提供 Google Colab 运行方式、pip 依赖安装、预训练 checkpoint（Google Drive/Yandex Disk）下载，以及 crop-video.py 借助 face-alignment 库和 ffmpeg 生成裁剪命令的预处理脚本。

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

- First Order Motion Model 论文的图像动画实现
- 提供预训练 checkpoint 下载（Google Drive/Yandex Disk）
- demo.py 一条命令生成 result.mp4 动画结果
- crop-video.py 结合 face-alignment 与 ffmpeg 做半自动裁剪预处理

## 适用场景

- 用一张照片配驾驶视频生成动画
- 在 Colab 上快速运行图像动画 demo
- 本科/毕业设计学习 First Order Motion Model 的实现

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: This repository contains source code for the paper First Order Motion Model for Image Animation by Aliaksandr Siaroh
> L26: python demo.py  --config config/dataset_name.yaml --driving_video path/to/driving --source_image path/to/source --c

## 星数曲线

```mermaid
xychart-beta
    title "snehitvaddi/Deep-Fake_First_Order_Model 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-26 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c5633398820c` · [字段定义](../../DATASET.md)*
