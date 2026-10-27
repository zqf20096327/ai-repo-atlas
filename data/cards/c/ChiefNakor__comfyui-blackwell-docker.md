# ChiefNakor/comfyui-blackwell-docker

⭐ 36 · Dockerfile · MIT · 推送 2026-01-28 · [GitHub](https://github.com/ChiefNakor/comfyui-blackwell-docker) · 个人维护

**为 ComfyUI 提供 NVFP4 量化的 Docker 部署方案，面向 RTX 50 系列**

面向 NVIDIA Blackwell（RTX 50 系列）GPU 的 ComfyUI Docker 化部署方案：通过 Dockerfile 与 docker-compose 构建容器镜像，内置 Nunchaku 以支持 NVFP4 4-bit 量化模型，README 标注 FLUX.1-dev 在 RTX 5090 上约 12 秒生成、模型体积 6.77GB；也兼容 Ampere/Ada 架构（无 NVFP4 加速）及常规 BF16/FP16 模型。模型、输出与自定义节点持久化在宿主机；安装自定义节点后需重建镜像；通过 .env 配置路径、显存保留与 PyTorch/CUDA 版本。要求 Docker 20.10+ 与 NVIDIA Container Toolkit。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Dockerfile + docker-compose 构建沙箱化 ComfyUI 环境
- 通过 Nunchaku 支持 NVFP4 4-bit 量化模型（FLUX.1-dev 6.77GB）
- 模型/输出/自定义节点数据持久化在宿主机
- SageAttention v2/v3 可选安装与 .env 版本配置

## 适用场景

- 在 RTX 50 系列 GPU 上以低显存运行 FLUX 类图像生成模型
- 以容器方式部署 ComfyUI 保持系统环境隔离
- 需要持久化自定义节点与工作流的本地 ComfyUI 工作站

## 场景标签

`图像生成` `模型量化` `推理引擎` · 领域:内容生成

## 证据(README 行号)

> L3: A production-ready Docker setup for ComfyUI that unlocks the full potential of NVIDIA Blackwell GPUs (RTX 50 series)
> L90: ├── docker-compose.yml       # Container configuration

## 星数曲线

```mermaid
xychart-beta
    title "ChiefNakor/comfyui-blackwell-docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-27 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `11938ef9949f` · [字段定义](../../DATASET.md)*
