# 0xShug0/audio.cpp

⭐ 4,460 · C++ · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/0xShug0/audio.cpp) · 个人维护

**纯 C++ 本地音频模型推理引擎：运行 TTS/ASR 等任务**

基于 ggml 的 C++ 音频推理框架，通过统一 CLI 与 server API 本地运行 154 个音频模型家族（250+ 变体），覆盖 TTS、ASR、语音克隆/转换、分离、对齐、音乐生成、VAD 等任务。支持 CUDA、HIP/ROCm、Vulkan、Metal、WebGPU、SYCL 与 CPU 后端，运行于 Windows/Linux/macOS，无 Python 依赖，提供内置 WebUI（Studio/Arena/TTS 应用）、GGUF 打包、LoRA 适配器、流式推理与 C ABI 库。模型权重许可与本项目许可分离，另有 Audio Model Architecture Atlas 收录 100+ 模型架构。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 154 个音频模型家族、250+ 变体，统一 CLI 与 server API 调用
- 支持 CPU/CUDA/HIP/Vulkan/Metal/WebGPU/SYCL 后端，含 ARM NEON 与 Rockchip NPU 优化
- 内置 WebUI：语音克隆 Studio、模型对比 Arena、TTS 叙事编辑
- GGUF 打包、LoRA 适配器、流式会话与 C ABI 集成库

## 适用场景

- 本地运行 TTS 与语音克隆生成语音
- 本地批量转录语音为文字（ASR/说话人分轨）
- 在无 Python 环境的机器上部署音频模型推理
- 浏览器 WebGPU 环境下运行音频推理

## 场景标签

`语音合成` `语音识别` `推理引擎` · 领域:内容生成

## 证据(README 行号)

> L5: `audio.cpp` is a high-performance C++ audio inference framework built on top of `ggml`, designed to make modern loca
> L32: ⭐ **154 audio model families and 250+ variants.** Run TTS, ASR, music generation, voice cloning, conversion, separa
> L38: ⭐ **Portability.** A native `ggml` runtime supporting CUDA, HIP/ROCm, Vulkan, Metal, WebGPU, SYCL, and CPU through 

## 星数曲线

```mermaid
xychart-beta
    title "0xShug0/audio.cpp 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 3642 --> 4534
    line [3716, 3741, 3748, 3777, 3802, 3833, 3850, 3877, 3896, 3919, 3741, 4120, 4153, 4174, 4197, 4218, 4233, 4253, 4307, 4324, 4343, 4358, 4376, 4390, 4410, 4426, 4460]
```

2026-10-24 3,716 → 2026-11-26 4,460（+744）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `853323a1ee53` · [字段定义](../../DATASET.md)*
