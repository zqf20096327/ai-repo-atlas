# pccr10001/comfyui-gfx1151-fa

⭐ 20 · Dockerfile · 推送 2026-01-12 · [GitHub](https://github.com/pccr10001/comfyui-gfx1151-fa) · 个人维护

**面向 AMD Ryzen AI MAX+ 395 的 ComfyUI Flash Attention 方案**

针对 AMD Ryzen AI MAX+ 395（gfx1151）适配的 ComfyUI 构建，包含 Flash Attention 支持，通过 Docker Compose 启动：需准备 ComfyUI 目录与 venv 目录，运行时传入 video/render 组 GID 与用户 UID/GID 以访问 GPU 设备。README 仅给出 Docker 部署步骤，面向在 ROCm 环境下运行该 APU 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 针对 gfx1151（Ryzen AI MAX+ 395）的 ComfyUI 构建
- 集成 Flash Attention
- 提供 docker compose 启动方式

## 适用场景

- 在 AMD Ryzen AI MAX+ 395 上运行 ComfyUI 生成图像
- 在 ROCm 环境中以 Docker 部署 Stable Diffusion 工作流

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: ComfyUI for AMD Ryzen AI MAX+ 395 with Flash Attention
> L3: ### Docker

## 星数曲线

```mermaid
xychart-beta
    title "pccr10001/comfyui-gfx1151-fa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `434dd610434d` · [字段定义](../../DATASET.md)*
