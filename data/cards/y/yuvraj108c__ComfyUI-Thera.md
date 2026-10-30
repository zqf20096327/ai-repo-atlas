# yuvraj108c/ComfyUI-Thera

⭐ 37 · Python · 推送 2026-07-30 · [GitHub](https://github.com/yuvraj108c/ComfyUI-Thera) · 个人维护

**ComfyUI 的 Thera 任意尺度超分辨率节点（非官方实现）**

将论文 Thera（Aliasing-Free Arbitrary-Scale Super-Resolution with Neural Heat Fields）以自定义节点形式接入 ComfyUI，提供任意尺度图像超分辨率推理能力；模型文件自动下载到 /ComfyUI/models/Thera，通过示例工作流使用。README 记录了最近一次测试环境（ComfyUI v0.7.0、Torch 2.9.1、RTX4090、CUDA 13.0、Debian 12）。安装方式为在 custom_nodes 目录 git clone 后 pip 安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Thera 神经热场任意尺度超分辨率的 ComfyUI 节点封装
- 模型自动下载到 /ComfyUI/models/Thera
- 附带示例工作流

## 适用场景

- 在 ComfyUI 工作流中对图像做任意倍率超分
- 复用 Thera 论文方法进行图像增强实验

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L6: This project is an unofficial ComfyUI implementation of Thera (Aliasing-Free Arbitrary-Scale Super-Resolution with N
> L43:   title={Thera: Aliasing-Free Arbitrary-Scale Super-Resolution with Neural Heat Fields},

## 星数曲线

```mermaid
xychart-beta
    title "yuvraj108c/ComfyUI-Thera 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f24c7a4b4db4` · [字段定义](../../DATASET.md)*
