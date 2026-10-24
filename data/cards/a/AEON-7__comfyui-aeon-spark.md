# AEON-7/comfyui-aeon-spark

⭐ 87 · Shell · 推送 2026-10-06 · [GitHub](https://github.com/AEON-7/comfyui-aeon-spark) · [官网](https://ghcr.io/aeon-7/comfyui-aeon-spark) · 个人维护

**专为 NVIDIA DGX Spark 打造的 ComfyUI 发行版：预置图/视频/音乐模型运行环境**

面向 NVIDIA DGX Spark（GB10/Blackwell/sm_121a）的 ComfyUI Docker 发行版：内置 CUDA 13.0.2 + PyTorch cu130 + 为 sm_121a 从源码编译的 SageAttention v3 与 CUTLASS NVFP4 GEMM，预装 14 个自定义节点包与默认工作流，配套 Flux 2 Dev、LTX 2.3 22B、ACE-Step v1.5 XL Turbo 的 BF16 权重下载（首次启动约 285 GB，经用户 HF_TOKEN 下载，镜像本身不含权重）。提供交互式 setup.sh 安装器与 sync.sh 增量更新；Flux 2 dev 为非商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CUDA 13.0.2 + PyTorch 2.9.1+cu130 ARM64，首个可生成 sm_121 代码的工具链
- SageAttention v3 为 sm_121a 从源码编译，CUTLASS NVFP4 硬件加速 GEMM
- 预置 Flux 2 Dev / LTX 2.3 22B / ACE-Step v1.5 与 14 个自定义节点包
- setup.sh 交互式安装与 sync.sh 增量更新（幂等，仅拉取增量）

## 适用场景

- 在 DGX Spark 上一键部署 ComfyUI 生成图像、视频与音乐
- 需要 sm_121a 原生编译的注意力与 NVFP4 加速路径
- 自行挑选模型的 :slim 模式部署（无自动下载）

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L4: > Bleeding-edge ComfyUI distribution **purpose-built for the NVIDIA DGX
> L8: > paths. CUDA 13.0.2 + PyTorch cu130 + SageAttention v3 compiled for
> L12: docker pull ghcr.io/aeon-7/comfyui-aeon-spark:latest          # auto-downloads weights using your HF_TOKEN

## 星数曲线

```mermaid
xychart-beta
    title "AEON-7/comfyui-aeon-spark 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 85 --> 88
    line [86, 87, 87]
```

2026-10-18 86 → 2026-10-24 87（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fe1af23b0d67` · [字段定义](../../DATASET.md)*
