# sbaier1/pyttv

⭐ 44 · Python · MIT · 推送 2026-01-27 · [GitHub](https://github.com/sbaier1/pyttv) · 个人维护

**基于 Stable Diffusion 生成（音乐）视频的 CLI 工具**

基于 PyTTI 和 deforum 的文本生成视频工具：通过 YAML 配置驱动帧序列生成，主要机制是调用 AUTOMATIC1111 stable-diffusion-webui 的 REST API（需以 --api 启动 webui）生成帧，支持音频响应式动画与多种可扩展生成机制。仅负责生成帧，最终视频编码依赖 ffmpeg 等外部工具，另涉及 RIFE 插帧、RealESRGAN 放大等后处理。以 Python 源码方式安装（venv + requirements + init.sh），面向使用 Stable Diffusion 的创作者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI + YAML 配置驱动的文本生成视频流程
- 通过 stable-diffusion-webui REST API 生成帧
- 音频响应式动画与可扩展生成机制
- 文档给出 ffmpeg 编码、插帧与放大等后处理流程

## 适用场景

- 用文本提示生成动画视频帧序列
- 制作随音频变化的音乐视频
- 低分辨率生成后配合放大与插帧产出成片

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L1: # text2video utility
> L3: a tool for leveraging text2image tools such as StableDiffusion for generating videos.
> L24: - use https://github.com/AUTOMATIC1111/stable-diffusion-webui

## 星数曲线

```mermaid
xychart-beta
    title "sbaier1/pyttv 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `7b6347fdff36` · [字段定义](../../DATASET.md)*
