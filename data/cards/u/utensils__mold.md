# utensils/mold

⭐ 54 · Rust · MIT · 推送 2026-10-25 · [GitHub](https://github.com/utensils/mold) · [官网](https://utensils.io/mold/) · 组织维护

**本地 AI 图像/视频生成引擎：CLI、桌面、移动端与 API 一体**

在用户自有 GPU 上运行的本地 AI 生成工具：支持 NVIDIA CUDA 与 Apple Silicon Metal，提供 CLI、原生桌面应用、Web Studio、iPhone/Android 伴侣端、Discord 机器人及 REST/SSE API 和 MCP 接口，均构建于同一 Rust 引擎。模型覆盖 FLUX、Stable Diffusion、Qwen-Image、LTX Video、Wan、MiniMax H3、Hunyuan3D 等，支持文生图/图编辑/文生视频/图生 3D。可连接多台机器（LAN/Tailscale/RunPod）统一调度与浏览。限制：crates.io 版本停止更新；GH200/GB200/GB300 不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一引擎提供 CLI、桌面、Web、移动端、REST/SSE 与 MCP 多种使用方式
- 支持 FLUX、SD、Qwen-Image、Wan、LTX Video、Hunyuan3D 等模型家族
- CUDA 与 Apple Metal 双后端，可连接远程 GPU 主机统一调度
- 图像编辑/ControlNet/LoRA、文生视频、图生 3D（glTF/OBJ/STL 导出）等能力

## 适用场景

- 在本地 GPU 上生成与编辑图像、视频和 3D 模型，不依赖云端服务
- 通过 CLI 或 REST/SSE/MCP 接口把生成能力接入脚本和 AI agent
- 把多台机器（含 RunPod 远程主机）接入同一 Library 统一管理作品

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L11: Local AI image and video generation on your own GPU. Mold supports NVIDIA CUDA
> L12: and Apple Silicon Metal, with a CLI, native desktop app, web studio, mobile

## 星数曲线

```mermaid
xychart-beta
    title "utensils/mold 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-28 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2dcbc553e63f` · [字段定义](../../DATASET.md)*
