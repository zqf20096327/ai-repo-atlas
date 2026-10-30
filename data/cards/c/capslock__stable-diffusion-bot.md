# capslock/stable-diffusion-bot

⭐ 15 · Rust · MIT · 推送 2025-11-26 · [GitHub](https://github.com/capslock/stable-diffusion-bot) · [官网](https://capslock.github.io/stable-diffusion-bot/) · 个人维护

**给 Telegram 用户的 Stable Diffusion 生图机器人客户端**

用 Rust 编写的 Telegram bot，作为客户端接入 Stable Diffusion Web UI 或 ComfyUI 的 API 实例，用户发送 prompt 即可文生图，发送图片加说明可实现图生图，回复带内联键盘可重跑、保存种子、改设置。通过 allowed_users 白名单控制访问，支持群组配置。安装途径包括 cargo install、源码编译、Nix Flakes、NixOS 模块与预构建 Docker 镜像；README 自述 Docker 支持目前较简略（TODO 扩充）。项目含四个 crate，其中三个 API 封装层可作为独立库引用。

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

- 接入 Stable Diffusion Web UI 与 ComfyUI 两种后端，通过 api_type 切换
- 支持 txt2img / img2img，回复带重跑、保存种子、修改设置的内联键盘
- allowed_users 用户白名单与群组 Chat ID 授权机制
- stable-diffusion-api / comfyui-api / sal-e-api 三个子 crate 可独立作为库使用

## 适用场景

- 在 Telegram 里通过对话生成或改图，无需打开 Web UI
- 限定白名单用户在私聊或群组中使用生图服务
- 作为库复用 ComfyUI/Stable Diffusion Web UI 的 Rust API 绑定

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: A Telegram bot written in Rust that can be connected to a
> L6: Stable Diffusion web UI or
> L7: ComfyUI backend to generate images.

## 星数曲线

```mermaid
xychart-beta
    title "capslock/stable-diffusion-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b7333534bdcf` · [字段定义](../../DATASET.md)*
