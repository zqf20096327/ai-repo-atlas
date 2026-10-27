# Janrupf/stable-diffusion-webui-nix

⭐ 29 · Nix · MIT · 推送 2026-06-20 · [GitHub](https://github.com/Janrupf/stable-diffusion-webui-nix) · 个人维护

**在 NixOS 上打包 Stable Diffusion Web UI 的可复现 flake**

提供 Nix flake，将 AUTOMATIC1111 的 Forge 分支与 ComfyUI 两个 Stable Diffusion Web UI 以完全可复现方式打包进 NixOS。用户通过 flake inputs 与系统模块引入，获得 stable-diffusion-webui 或 comfy-ui 命令；另提供 systemd 服务模块 sd-webui-forge 与含 Python/CUDA 的 FHS 环境（允许手动装扩展，默认 Nix 包依赖固定、不支持界面内安装扩展）。CUDA 相关包不在默认 NixOS 缓存中，建议添加 nix-community Cachix 替代源以减少编译时间。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 打包 Forge（AUTOMATIC1111 分支）与 ComfyUI，支持 CUDA 变体
- 提供 sd-webui-forge systemd 服务模块
- FHS 环境允许手动安装 WebUI 软件与扩展
- 数据目录路径可通过参数覆盖（Forge 默认 ~/.local/share/stable-diffusion-webui）

## 适用场景

- 在 NixOS 上以可复现方式运行 Stable Diffusion Web UI
- 把 Forge WebUI 作为 systemd 服务常驻运行
- 需要界面内安装扩展时改用 FHS 环境

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: # Stable diffusion Web UI's for Nix
> L3: ###### Fully reproducible flake packaging stable diffusion python UI's
> L29:   pkgs.stable-diffusion-webui.forge.cuda # For lllyasviel's fork of AUTOMATIC1111 WebUI

## 星数曲线

```mermaid
xychart-beta
    title "Janrupf/stable-diffusion-webui-nix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7f0e0d9809a8` · [字段定义](../../DATASET.md)*
