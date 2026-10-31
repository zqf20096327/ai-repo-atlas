# Saganaki22/ComfyUI-dotWaveform

⭐ 33 · JavaScript · MIT · 推送 2026-04-09 · [GitHub](https://github.com/Saganaki22/ComfyUI-dotWaveform) · 个人维护

**ComfyUI 节点：从音频生成 7 种动画点阵波形可视化**

面向 ComfyUI 用户的自定义节点，读取音频输入并生成带动画的点阵波形图像序列：提供滚动、呼吸、径向、条形、波浪、FFT 频谱、圆形共 7 种动画风格，支持最高 1920x1920 输出、多色渐变编辑器、8 套预设调色板、0.5x-5.0x 振幅增益与 4 档透明度模式；音频可直接传递给 VideoHelperSuite 视频合成节点，通过 ComfyUI Manager 或手动 git clone 安装，功能基于 FFT 与信号处理而非模型推理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 种动画风格（scrolling/breathing/radial/bars/wave/spectrum/circular）
- FFT 频谱分析实现低音到高音的可视化
- 最多 10 个渐变停点的可视化渐变编辑器与 6 套预设
- 与 VideoHelperSuite Video Combine 音频直通兼容（自动 mono→stereo）

## 适用场景

- 在 ComfyUI 工作流中为音频/音乐视频生成波形动画
- 制作频谱均衡器风格的视觉素材
- 通过预览模式快速调试波形样式与配色

## 场景标签

 · 领域:创意工具/音频可视化

## 证据(README 行号)

> L7: A ComfyUI node that generates animated dotted waveform visualizations from audio input with multiple animation style
> L93: 1. Clone to `ComfyUI/custom_nodes/ComfyUI-dotWaveform/`
> L20: - **Audio Passthrough**: Compatible with VideoHelperSuite Video Combine

## 星数曲线

```mermaid
xychart-beta
    title "Saganaki22/ComfyUI-dotWaveform 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `84250b2d0982` · [字段定义](../../DATASET.md)*
