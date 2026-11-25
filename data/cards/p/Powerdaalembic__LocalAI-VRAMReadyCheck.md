# Powerdaalembic/LocalAI-VRAMReadyCheck

⭐ 33 · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Powerdaalembic/LocalAI-VRAMReadyCheck) · 个人维护

**检测 Windows PC 能否本地运行 Ollama/LM Studio/ComfyUI 并推荐模型规格**

面向 Windows 10/11 x64 的便携式硬件诊断工具：读取 GPU 型号、专用显存、CUDA/Vulkan 支持级别、系统内存、CPU AVX2/AVX-512 与各盘剩余空间，输出适配显存容量的 GGUF 量化档位（如 Q4_K_M/Q8_0）与图像扩散精度（FP16/FP8/NF4）建议，并检查 Git/Python/Ollama 安装与模型缓存路径。以 GitHub Release 提供 LocalAICheck.zip，解压后运行 exe，无需安装、联网或管理员权限，只读运行，不下载模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检测 GPU 显存、CUDA/Vulkan 计算级别与 CPU 指令集
- 按显存档位给出 GGUF 量化与 FP8/FP16/NF4 精度推荐
- 检查 .ollama 与 HuggingFace 缓存路径及 C 盘剩余空间
- 便携离线运行，只读模式，无需 Python/CUDA toolkit

## 适用场景

- 购买/升级显卡前评估能跑多大参数量的本地 LLM
- 下载大模型前确认显存是否够用，避免 OOM 与带宽浪费
- 排查 ComfyUI 跑 Flux/SDXL 时的 CUDA 显存不足问题
- 检查 C 盘模型缓存占用并迁移缓存到其他 NVMe 盘

## 场景标签

 · 领域:本地 AI 硬件诊断工具

## 证据(README 行号)

> L12: LocalAI Ready Check inspects your GPU compute stack, dedicated VRAM, system RAM, and SSD free space on Windows: **r
> L32: - Detects GPU model, dedicated VRAM (`GB`), driver version, supported **CUDA** / **Vulkan** compute level, and CPU 
> L55: **Requirements:** Windows 10 or 11 (64-bit) with NVIDIA, AMD, or Intel Arc graphics (or CPU-only mode).


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `f55c3d2a8819` · [字段定义](../../DATASET.md)*
