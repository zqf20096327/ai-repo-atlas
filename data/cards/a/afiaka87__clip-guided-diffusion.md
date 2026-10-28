# afiaka87/clip-guided-diffusion

⭐ 459 · Python · MIT · 推送 2025-12-31 · [GitHub](https://github.com/afiaka87/clip-guided-diffusion) · 个人维护

**用 CLIP 引导 diffusion 从文本生成图像的 CLI 工具/Python 库**

基于 OpenAI CLIP 与 guided diffusion 的文生图工具，以 CLI 命令 cgd 和 Python 模块两种形式提供。支持多提示词加权（正/负权重）、图生图混合（init_image + skip_timesteps）、64-512 像素方形及实验性非方形尺寸、ddim 采样与时间步重排，输出中间帧、GIF 或 MP4。提供三项加速开关（降低 CLIP 引导频率、渐进 cutout、缓存 cutout 坐标）。CPU 可运行但耗时明显，GPU 自动选择设备；部分测试需要 GPU。作者声明重心已转向 pyglide，本仓库 bug 响应可能较慢。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本到图像生成，多提示词支持正负权重
- 图生图：init_image 混合与 VGG 感知损失
- 三项性能优化开关（reduce-clip / progressive-cutout / cached-cutouts）
- 输出中间帧、GIF、MP4，可接入 wandb 日志

## 适用场景

- 输入文字描述生成图像作品
- 以现有图像为起点做扩散再创作
- 生成过程录制为 GIF 或 MP4

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L22: `uv run cgd -txt "Alien friend by Odilon Redo"`
> L190: from cgd import clip_guided_diffusion

## 星数曲线

```mermaid
xychart-beta
    title "afiaka87/clip-guided-diffusion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 458 --> 460
    line [459, 459]
```

2026-10-18 459 → 2026-10-28 459（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `952fb1bb576d` · [字段定义](../../DATASET.md)*
