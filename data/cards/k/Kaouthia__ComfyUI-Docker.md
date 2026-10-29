# Kaouthia/ComfyUI-Docker

⭐ 130 · Shell · 推送 2026-05-17 · [GitHub](https://github.com/Kaouthia/ComfyUI-Docker) · [官网](https://www.johnaldred.com/running-comfyui-in-docker-on-windows-or-linux/) · 个人维护

**用 Docker Compose 运行 ComfyUI 的自托管部署配置**

提供 ComfyUI 的 Dockerfile 与 Docker Compose 配置，在 Linux 或 Windows（WSL2）上以 NVIDIA GPU 支持运行 ComfyUI；容器重建时自动拉取最新版 ComfyUI 与在 entrypoint.sh 中定义的自定义节点，模型、输出、设置与工作流通过宿主机挂载卷持久化。附带 ComfyUI-Manager 等 6 个自定义节点，可通过其临时安装节点但重建后会重置；作者声明不维护预构建镜像、不合并自动化构建相关的 PR。

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

- Docker Compose 一键构建运行 ComfyUI，支持 NVIDIA GPU
- 模型/输出/设置/工作流通过挂载卷持久化，重建容器不丢失
- entrypoint.sh 自动安装 ComfyUI-Manager 等 6 个自定义节点
- 支持通过 Portainer-CE 运行

## 适用场景

- 在 Docker 中隔离运行 ComfyUI，尝试自定义节点而不破坏现有环境
- Windows/Linux 上以 GPU 加速自托管 ComfyUI
- 通过重建容器实现 ComfyUI 与自定义节点的干净更新

## 场景标签

 · 领域:AI 应用部署/容器化

## 证据(README 行号)

> L5: Run ComfyUI in Docker with Docker Compose — simple setup with persistent storage, NVIDIA GPU support, and custom nod
> L67: docker compose build --no-cache && docker compose up -d

## 星数曲线

```mermaid
xychart-beta
    title "Kaouthia/ComfyUI-Docker 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 128 --> 131
    line [129, 130, 130]
```

2026-10-18 129 → 2026-10-29 130（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ea991edae510` · [字段定义](../../DATASET.md)*
