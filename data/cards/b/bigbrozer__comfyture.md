# bigbrozer/comfyture

⭐ 18 · Shell · MIT · 推送 2026-10-27 · [GitHub](https://github.com/bigbrozer/comfyture) · [官网](https://hub.docker.com/r/bigbrozer/comfyture) · 个人维护

**自托管 ComfyUI 的 Docker 镜像与 compose 栈**

提供开箱即用的 Docker 镜像与 Docker Compose 编排，用于运行带 NVIDIA GPU 加速的 ComfyUI 实例，预装 20+ 个扩展（自定义节点），默认启用 Manager，支持 Flash Attention v2/v3 与 Triton，可配置 UID/GID 以非 root 运行，不提供模型需自行下载至 ./data/models。使用方式为下载 compose.yaml、创建 data 目录后 docker compose 启动，浏览器访问 localhost:8188 使用；数据通过本地 ./data 目录持久化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Docker Compose 一键启动带 NVIDIA CUDA 加速的 ComfyUI
- 预装 20+ 个自定义节点扩展并默认启用 Manager
- 支持 Flash Attention v2/v3 与 Triton
- 非 root 运行，UID/GID 可配置，./data 目录持久化全部数据

## 适用场景

- 用 Docker 快速部署自托管的 ComfyUI 图像生成环境
- 获得预装常用节点的 ComfyUI 实例，减少手动配置
- 在本地持久化模型、节点与输出图片

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Comfyture is a ready to use Docker image and compose stack designed to simplify running ComfyUI with NVIDIA GPU acce
> L16: * Easy to run ComfyUI from Docker.

## 星数曲线

```mermaid
xychart-beta
    title "bigbrozer/comfyture 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `62f804c70d40` · [字段定义](../../DATASET.md)*
