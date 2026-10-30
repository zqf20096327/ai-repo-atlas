# Ivan-Ayub97/Warlock-Studio

⭐ 251 · Python · MIT · 推送 2026-03-17 · [GitHub](https://github.com/Ivan-Ayub97/Warlock-Studio) · 个人维护

**Windows 桌面套件：用多种模型做图像视频超分/修复/补帧**

面向 Windows 用户的图像与视频处理桌面应用，集成 Real-ESRGAN、BSRGAN、RealESRNet、RealESR_Animex4、IRCNN 做超分与去噪，GFPGAN 做人脸修复，RIFE 做 2×/4×/8× 补帧，支持批处理与多步骤流水线（Process Chaining，步骤间自动传递输出）。执行后端为 ONNX 模型，硬件加速按 CUDA→DirectML→CPU 顺序选择。提供 x64 安装包（PyInstaller/Inno Setup 构建），要求 Windows 10+ 64 位。

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

- 集成 6 类模型：超分（Real-ESRGAN/BSRGAN 等）、人脸修复（GFPGAN）、补帧（RIFE）
- Process Chaining 多步骤流水线，模型自动发现与逐步 VRAM 控制
- 硬件加速按 CUDA→DirectML→CPU 顺序选择
- 批处理与自定义输出格式/质量参数

## 适用场景

- 我把低分辨率照片或视频放大并恢复细节
- 给模糊的人脸照片/视频帧做人脸修复
- 用补帧生成慢动作或平滑视频画面
- 按顺序串联超分、修复、补帧批量处理多个文件

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L13: **Warlock Studio** is a unified platform for **upscaling, restoring, denoising, and interpolating frames in videos 
> L61: - **AI Upscaling & Restoration** – Utilize **Real-ESRGAN, BSRGAN, RealESRNet, RealESR_Animex4, and IRCNN** models f

## 星数曲线

```mermaid
xychart-beta
    title "Ivan-Ayub97/Warlock-Studio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 250 --> 253
    line [252, 251, 251]
```

2026-10-18 252 → 2026-10-30 251（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `35efb15bb66c` · [字段定义](../../DATASET.md)*
