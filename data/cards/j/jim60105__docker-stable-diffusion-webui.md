# jim60105/docker-stable-diffusion-webui

⭐ 38 · Dockerfile · AGPL-3.0 · 推送 2026-07-14 · [GitHub](https://github.com/jim60105/docker-stable-diffusion-webui) · 个人维护 · 中文 README

**Stable Diffusion WebUI 的 Docker 镜像封装：小型化并遵循最佳实践**

为 AUTOMATIC1111/Stable Diffusion WebUI 提供 Dockerfile 与 CI 自动构建，目标为保持镜像小型化（约 10GB）并遵循最佳实践（非 root 用户、OpenShift 任意 uid 支持）。提供 A1111 各版本、Forge、Forge-Neo 多种镜像标签，每周随上游 dev 分支重建，可从 ghcr 拉取或本地构建；另有首启时安装依赖、体积 1.3GB 的 runtime-deps 变体。面向需在 Docker 中以 GPU 运行 Stable Diffusion WebUI 的用户，需自备 NVIDIA 驱动与 NVIDIA Container Toolkit。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 镜像体积控制在约 10GB，较现有方案节省约 1/3
- 支持 A1111 / Forge / Forge-Neo 三系版本，dev 镜像每周重建
- runtime-deps 变体镜像缩至 1.3GB，依赖在首次启动时安装
- 非 root 用户运行，支持 OpenShift 任意 uid

## 适用场景

- 在 Docker 中快速以 GPU 运行 Stable Diffusion WebUI
- 通过镜像标签切换 A1111、Forge、Forge-Neo 版本
- 从现有 SD WebUI 配置迁移模型与设置到容器

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L14: Yet another docker image for AUTOMATIC1111/Stable Diffusion web UI: A web interface for Stable Diffusion, implement
> L16: The main goal of designing this image is to keep it ***small and follow best practices***. Successfully controlled 

## 星数曲线

```mermaid
xychart-beta
    title "jim60105/docker-stable-diffusion-webui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `bb4df3199e32` · [字段定义](../../DATASET.md)*
