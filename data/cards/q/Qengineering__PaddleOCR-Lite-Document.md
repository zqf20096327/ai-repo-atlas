# Qengineering/PaddleOCR-Lite-Document

⭐ 31 · C++ · BSD-3-Clause · 推送 2026-03-15 · [GitHub](https://github.com/Qengineering/PaddleOCR-Lite-Document) · [官网](https://qengineering.eu/install-paddle-lite-on-raspberry-pi-4.html) · 个人维护

**树莓派上本地运行的 PaddleOCR 文档扫描 C++ 应用**

基于 ncnn 移植 PaddleOCR v5 的 C++ 应用，在 Raspberry Pi 4/5 上本地执行文本检测、方向判定与字符识别（中文或拉丁），无需安装 PaddlePaddle 或 Paddle-Lite，不依赖云服务。提供 det/rec/system 三种运行模式，支持 arm8 硬件与 FP32 精度参数配置，可检测模型阈值等参数通过 config.txt 调整。需从源码编译（CMake 或 Code::Blocks），系统依赖 OpenCV 64 位与 ncnn。给出 RPi 4/5 上的推理耗时实测数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ncnn 版 PaddleOCR v5，无需 PaddlePaddle/Paddle-Lite
- 支持文本检测、方向判定与中/拉丁字符识别三种模式
- 完全本地运行于 Raspberry Pi 4/5，无云服务
- README 提供 RPi 4/5 实测推理耗时数据

## 适用场景

- 在树莓派上离线扫描并识别文档文字
- 嵌入式设备上部署中英文 OCR 识别
- 按需调整检测阈值与识别参数处理不同文档

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L6: PaddleOCR is a text engine. It can detect text in a scene, determine the orientation, and recognise the characters (
> L9: For this reason, we use the ncnn port of the latest PaddleOCR version (**v5**).

## 星数曲线

```mermaid
xychart-beta
    title "Qengineering/PaddleOCR-Lite-Document 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `156ac1a4b07c` · [字段定义](../../DATASET.md)*
