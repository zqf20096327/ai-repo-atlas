# andrewdalpino/MewZoom

⭐ 15 · Python · Apache-2.0 · 推送 2026-04-29 · [GitHub](https://github.com/andrewdalpino/MewZoom) · [官网](https://andrewdalpino.github.io/MewZoom/app) · 个人维护

**图像超分辨率模型家族：2X/3X/4X/8X 放大并去模糊去噪**

开源图像超分辨率模型家族，提供 TrunkNet 与 UNet 两种架构的预训练权重（参数量 1.8M–128M），支持 2X/3X/4X/8X 放大，训练目标包含去除模糊、噪声与压缩伪影，在全 RGB 色域上工作。推理通过 Python mewzoom 库（基于 PyTorch）加载 HuggingFace Hub 权重，也可下载 ONNX 图在兼容引擎中运行。另提供浏览器端 Web UI，推理在本地设备完成，受 Web Assembly 限制仅支持 CPU 与最大 4GB 内存。面向需要图像放大与修复的开发者与使用者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TrunkNet 与 UNet 双架构，参数量 1.8M–128M 多档可选
- 辅助训练目标去除模糊、噪声与压缩伪影
- 支持 PyTorch 库推理与 ONNX 格式部署
- 浏览器端 Web UI，数据不离开本地设备

## 适用场景

- 把低分辨率照片放大 2X–8X 并去除噪声伪影
- 在 Python 项目中集成图像超分推理
- 在浏览器本地完成图像放大而不上传数据

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L5: A family of open-source super-resolution models with purrfect pixels. Pre-trained on a diverse set of images and fin
> L31: |Name|Upscale|Architecture|Channels|Layers|Parameters|Library Version|

## 星数曲线

```mermaid
xychart-beta
    title "andrewdalpino/MewZoom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fd48bec327fa` · [字段定义](../../DATASET.md)*
