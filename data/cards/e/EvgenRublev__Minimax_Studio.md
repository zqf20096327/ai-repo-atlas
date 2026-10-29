# EvgenRublev/Minimax_Studio

⭐ 27 · TypeScript · GPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/EvgenRublev/Minimax_Studio) · [官网](https://t.me/Evgeny_Rublev) · 个人维护

**本地离线的 MiniMax H3 电影感视频+音频生成桌面工作室**

面向 Windows + NVIDIA GPU 用户的完全本地视频生成应用：基于 ComfyUI 后端运行 MiniMax H3 模型，支持双通道（低清→latent upscale→高清）生成带声音的视频，可输入图片/视频/音频参考。内置 Qwen3.5 9B（.gguf）LLM 助手辅助写提示词并理解参考图，whisper CPU 语音输入，DLSS 5 超分、RIFE/FILM 补帧、Face Refine、ControlNet 运动控制等。通过 install.bat 一键安装约 9 GB 组件，start.bat 以 Electron 窗口启动；需 8+ GB VRAM、CUDA 12.x 驱动、约 25 GB 磁盘；模型（Diffusion ~22.9 GB 等）需在 UI 内另行下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MiniMax H3 两通道视频+音频生成，Draft 单通道快速模式
- LLM 助手默认 Qwen3.5 9B（Q4_K_M，含视觉），支持自定义 .gguf
- DLSS 5 超分、RIFE/FILM 补帧、Face Refine、ControlNet 运动控制
- 完全离线运行，install.bat/start.bat 单文件安装与启动

## 适用场景

- 本地生成带声音的电影感视频，不依赖云端
- 用图片/视频/音频参考控制生成结果
- 对生成视频做超分、补帧、人脸修复等后处理

## 场景标签

`视频生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L3: Локальный веб-интерфейс для генерации кинематографичных видео со звуком на базе модели **MiniMax H3**. Работает полн
> L91: - **Генерация видео + аудио** — двухпроходная (low-res → latent upscale → high-res)

## 星数曲线

```mermaid
xychart-beta
    title "EvgenRublev/Minimax_Studio 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-28 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `2dca3cf3ad0b` · [字段定义](../../DATASET.md)*
