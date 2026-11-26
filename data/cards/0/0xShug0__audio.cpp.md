# 0xShug0/audio.cpp

⭐ 4,460 · C++ · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/0xShug0/audio.cpp) · 个人维护

**纯 C++ 本地音频模型推理引擎：无需 Python 跑 TTS/ASR 等**

基于 ggml 的音频推理框架，通过共享 CLI 与 server API 在本地运行 TTS、ASR、语音克隆、变声、音乐生成、分离、对齐、VAD 等任务，README 列出 154 个模型家族、250+ 变体。支持 CPU、CUDA、HIP/ROCm、Vulkan、Metal、WebGPU、SYCL 后端，跨 Windows/Linux/macOS，含 ARM NEON 与 Rockchip RKNN 优化。内置 WebUI（Studio 语音生成、Arena 模型对比、TTS 应用）。无 Python 依赖，提供 C ABI 库、便携构建包与源码编译路径。模型权重许可证与本体许可证分离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 154 个音频模型家族、250+ 变体，经共享 CLI 与 server API 本地运行
- 7 类后端：CPU/CUDA/HIP/ROCm/Vulkan/Metal/WebGPU/SYCL，含 ARM NEON 与 RKNN 优化
- 内置 WebUI：Studio 语音生成/克隆、Arena 模型对比、TTS 叙事编辑
- 提供 C ABI 库、GGUF 打包、LoRA 适配器加载与流式推理

## 适用场景

- 在没有 Python 环境的机器上本地跑 TTS 与语音识别
- 批量生成或克隆配音，组装旁白与跨语言配音
- 在 Apple Silicon、AMD 或仅 CPU 设备上做音频推理
- 通过 server API 把语音能力集成到自己的应用

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
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `aa08952d088c` · [字段定义](../../DATASET.md)*
