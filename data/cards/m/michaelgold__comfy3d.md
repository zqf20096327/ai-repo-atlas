# michaelgold/comfy3d

⭐ 72 · Python · 推送 2026-09-18 · [GitHub](https://github.com/michaelgold/comfy3d) · 个人维护

**面向 ComfyUI 3D 工作流的 GPU 加速 Docker 容器环境**

为使用 ComfyUI 进行 3D 与扩散模型工作流开发提供的容器化环境：预装 CUDA 12.1/12.6 运行时、ComfyUI-Manager、Hunyuan3D Wrapper、ComfyUI-3D-Pack、ControlNet 扩展等自定义节点，并内置 Hunyuan3D-2、FLUX、Wan 2.2 等模型，覆盖图像生成、视频生成、带纹理网格重建与多视图渲染。支持 Runpod 一键部署、本地 docker compose 构建及 NVIDIA DGX Spark（ARM64）原生构建，输出 GLB 与图像到挂载目录。给需要在可复现环境中运行 ComfyUI 3D 工作流的开发者使用。

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

- 预构建 Docker 镜像，支持 CUDA 12.1 与 12.6
- 内置 Hunyuan3D-2、FLUX、Wan 2.2 等模型与多个自定义节点
- 提供角色生成、单视图/多视图网格重建示例工作流
- 支持 AMD64 与 DGX Spark ARM64（CUDA 13）原生构建

## 适用场景

- 在可复现的容器中运行 ComfyUI 3D 工作流
- 从单张图像生成带纹理的 GLB 3D 网格
- 在 Runpod 等 GPU 云上一键部署扩散模型 3D 环境

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: **Comfy3D** is a GPU-accelerated containerized environment for advanced 3D workflows using ComfyUI, enhanced with re
> L5: This setup provides out-of-the-box workflows for image generation, video generation, textured meshes, and multi-view
> L25: - 📦 **Prebuilt Docker Environment** with CUDA 12.1 and 12.6 support

## 星数曲线

```mermaid
xychart-beta
    title "michaelgold/comfy3d 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-25 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `99b2119d31a6` · [字段定义](../../DATASET.md)*
