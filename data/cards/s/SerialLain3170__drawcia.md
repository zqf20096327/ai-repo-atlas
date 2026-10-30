# SerialLain3170/drawcia

⭐ 16 · Go · 推送 2026-07-24 · [GitHub](https://github.com/SerialLain3170/drawcia) · 个人维护

**动漫图像/视频深度学习任务实现集与 GUI 应用**

汇总多种动漫图像与视频相关深度学习任务实现的仓库，覆盖超分辨率（SRGAN/ESRGAN）、图像风格迁移（CycleGAN/StarGAN 等）、插画生成（DCGAN/DRAGAN 等多种 GAN）、视频处理（Recycle-GAN、Add Blink）及角色应用（线稿提取、角色识别、发型迁移）。另提供 GUI 应用，仅支持处理 .png 文件，通过下载预训练模型文件、构建 Docker 镜像并以 docker-compose 启动，访问 0.0.0.0:5000 使用。仓库曾于 2023 年由 KawaiiGenerator 更名为 senju。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖超分辨率、风格迁移、插画生成、视频处理、角色应用五类任务实现
- 收录多种 GAN 变体实现（DCGAN/DRAGAN/CycleGAN/StarGAN 等）
- 提供基于 Docker 部署的 GUI 应用（仅支持 .png 输入）
- GUI 应用需下载预训练的 encoder/decoder 模型文件

## 适用场景

- 在 GUI 中试用动漫图像的线稿提取与发型迁移等应用
- 对照学习多种 GAN 架构在动漫插画生成上的实现
- 复现动漫图像超分辨率与风格迁移任务

## 场景标签

`图像视频处理` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L7: KawaiiGenerator enables users to try and compare deep learning tasks related to anime images and videos.
> L15: Implementations: SRGAN, ESRGAN, Residual Attention Module

## 星数曲线

```mermaid
xychart-beta
    title "SerialLain3170/drawcia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `87ea368d8e33` · [字段定义](../../DATASET.md)*
