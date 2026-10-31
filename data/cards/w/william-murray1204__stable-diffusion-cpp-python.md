# william-murray1204/stable-diffusion-cpp-python

⭐ 126 · Python · MIT · 推送 2026-05-12 · [GitHub](https://github.com/william-murray1204/stable-diffusion-cpp-python) · 个人维护

**stable-diffusion.cpp 的 Python 绑定：本地生成图像/视频**

为 leejet 的 stable-diffusion.cpp 库提供 Python 绑定：低层 ctypes 接口访问 C API，高层 StableDiffusion 类接口支持 Stable Diffusion、FLUX（含 Kontext/Chroma/Klein）、Wan 的 txt2img/img2img/视频生成。pip 安装时从源码编译 stable-diffusion.cpp，可通过 CMAKE_ARGS 启用 CUDA/HIPBLAS/Metal/Vulkan/SYCL/OpenCL 等后端。支持 LoRA 加载（量化模型下不可用）与 flash attention。面向需要在 Python 中本地运行扩散模型的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ctypes 低层 C API 接口 + 高层 StableDiffusion 类接口
- 支持 Stable Diffusion / FLUX.1 / FLUX.2 / Kontext / Chroma / Klein / Wan
- 多硬件加速后端：CUDA、ROCm、Metal、Vulkan、SYCL、OpenBLAS、MUSA、OpenCL(Adreno/Android)
- 支持 LoRA 与 flash attention（部分模型/后端）

## 适用场景

- 在 Python 项目中本地运行 Stable Diffusion 或 FLUX 生成图像
- 用 gguf 量化权重在消费级 GPU 上跑 FLUX 模型
- 通过 LoRA 定制生成风格
- 在 Android/Apple Silicon 等非桌面平台上构建运行

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: Simple Python bindings for **@leejet's** `stable-diffusion.cpp` library.
> L11: - Low-level access to C API via `ctypes` interface.
> L12: - High-level Python API for Stable Diffusion, FLUX and Wan image/video generation.

## 星数曲线

```mermaid
xychart-beta
    title "william-murray1204/stable-diffusion-cpp-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 125 --> 127
    line [126, 126]
```

2026-10-18 126 → 2026-10-31 126（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7d5e2a6495f9` · [字段定义](../../DATASET.md)*
