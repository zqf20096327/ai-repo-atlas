# Djdefrag/FluidFrames

⭐ 280 · Python · MIT · 推送 2026-09-27 · [GitHub](https://github.com/Djdefrag/FluidFrames) · 个人维护

**Windows 视频补帧与慢动作 AI 应用（RIFE）**

基于 RIFE AI 模型的 Windows 桌面应用，读取用户视频并生成中间帧，实现 x2/x4/x8 补帧（如 30fps→240fps）与 x2/x4/x8 慢动作。Python 编写，使用 onnxruntime-directml 引擎，支持所有 DirectX12 兼容 GPU（AMD/Intel/Nvidia）与多 GPU，硬件加速编码（nvenc/amf/qsv），全程本地运行无需联网。除源码自行搭建外，通过 itch.io 与 Steam 分发安装包；源码运行需自备 FFMPEG.exe。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RIFE/RIFE_Lite 模型驱动的 x2/x4/x8 补帧与慢动作生成
- onnxruntime-directml 引擎支持所有 DirectX12 GPU（AMD/Intel/Nvidia）
- 补帧任务 STOP&RESUME 与多视频批处理
- 本地运行，无需联网

## 适用场景

- 把低帧率视频提升到 60/120/240fps
- 对视频做 x2/x4/x8 慢动作处理
- 在 AMD/Intel/Nvidia 显卡上本地批量补帧

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L17: FluidFrames.RIFE is a Windows app powered by RIFE AI to create frame-generated and slowmotion videos.
> L66: - [x] Video frames generation x2 / x4 / x8

## 星数曲线

```mermaid
xychart-beta
    title "Djdefrag/FluidFrames 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 280 --> 282
    line [281, 281]
```

2026-10-18 281 → 2026-10-25 281（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `dcf79c60a79f` · [字段定义](../../DATASET.md)*
