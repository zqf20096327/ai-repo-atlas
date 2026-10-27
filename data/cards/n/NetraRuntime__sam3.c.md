# NetraRuntime/sam3.c

⭐ 24 · C · MIT · 推送 2026-05-10 · [GitHub](https://github.com/NetraRuntime/sam3.c) · 个人维护

**纯 C 实现的 SAM3 图像分割与视频跟踪推理引擎**

面向开发者的 C11 实现：从零手写 SAM3 全流水线（图像编码器、提示编码器、掩码解码器、文本编码器与分词器），约 5.7 万行可移植 C，无 Python 依赖。支持 Apple Metal GPU 与多线程 SIMD CPU（x86/ARM）后端，提供 Hiera/EfficientViT/TinyViT 三种骨干、FP16/BF16 精度、视频逐帧目标跟踪、编码特征缓存与磁盘溢出。自定义 .sam3 权重格式（mmap 加载），统一 CLI（segment/convert/info/track），并附 Python（CFFI）与 Rust 绑定。构建需 CMake 编译源码并静态编译 FFmpeg（首次约 10-15 分钟）。限制：SAM 3.1 仅接入图像检测路径，视频跟踪仍由 SAM3 承担。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 C11 手写 SAM3 全流水线，无 PyTorch/ONNX 依赖
- Apple Metal GPU 后端与多线程 SIMD CPU 后端（FP16/BF16）
- 视频目标跟踪（点/框/掩码提示，MPEG 视频与帧目录）
- 图像/文本编码特征缓存（LRU 内存预算 + 磁盘溢出，重复提示微秒级返回）

## 适用场景

- 在 Apple Silicon 或 x86 机器上本地运行交互式图像分割
- 用点/框/文本提示对图片中的对象生成掩码
- 跨视频帧跟踪指定对象并输出逐帧二值掩码
- 通过 Python 或 Rust 绑定将 SAM3 嵌入自有应用

## 场景标签

`推理引擎` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: A lightweight, dependency-free C11 implementation of Segment Anything Model 3 (SAM3) built from scratch for efficien
> L29: - **Full SAM3 pipeline** — image encoder (Hiera, EfficientViT, TinyViT), prompt encoder (points, boxes, masks), mas

## 星数曲线

```mermaid
xychart-beta
    title "NetraRuntime/sam3.c 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-27 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `852e8e0e9359` · [字段定义](../../DATASET.md)*
