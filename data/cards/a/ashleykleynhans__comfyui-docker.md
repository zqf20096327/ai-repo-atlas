# ashleykleynhans/comfyui-docker

⭐ 61 · Shell · GPL-3.0 · 推送 2026-10-19 · [GitHub](https://github.com/ashleykleynhans/comfyui-docker) · 个人维护

**ComfyUI 的 Docker 镜像，面向 RunPod 与本地 GPU 部署**

为 ComfyUI v0.42.1 打包的 Docker 镜像：基于 Ubuntu 22.04，提供 CUDA 12.4 与 12.8 两档、Python 3.11/3.12 各两种变体，内置 Jupyter Lab、code-server、runpodctl、croc、rclone、CivitAI Downloader 等工具。面向在 RunPod 上部署 Stable Diffusion 工作流的用户，也支持本地 docker run 运行；构建镜像缓存模型需至少 32GB 系统内存，否则需移除相关 Dockerfile 代码。通过环境变量与端口映射（ComfyUI/Code Server/Jupyter 等）配置服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CUDA 12.4/12.8 × Python 3.11/3.12 四种镜像变体
- 内置 Jupyter Lab、code-server、runpodctl、CivitAI Downloader 等工具
- 提供 RunPod 一键模板，也支持本地 docker run 运行
- 通过 EXTRA_ARGS 等环境变量传递 ComfyUI 命令行参数

## 适用场景

- 在 RunPod GPU 实例上快速部署 ComfyUI 工作流
- 本地用 Docker 运行带 Jupyter/code-server 的 ComfyUI 环境
- 为 ComfyUI 自定义节点选择 Python 3.11 镜像以保持兼容

## 场景标签

 · 领域:生成式图像/容器化部署

## 证据(README 行号)

> L26: * ComfyUI v0.42.1
> L39: This image is designed to work on RunPod.

## 星数曲线

```mermaid
xychart-beta
    title "ashleykleynhans/comfyui-docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-27 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `aa0b77bedcd8` · [字段定义](../../DATASET.md)*
