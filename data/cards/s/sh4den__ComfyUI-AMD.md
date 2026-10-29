# sh4den/ComfyUI-AMD

⭐ 28 · PowerShell · 推送 2026-07-06 · [GitHub](https://github.com/sh4den/ComfyUI-AMD) · [官网](https://comfyui-amd.github.io) · 个人维护

**AMD RDNA GPU 上安装运行 ComfyUI 的 PowerShell 一键脚本**

面向 Windows AMD 显卡（RDNA 3/3.5/4，如 RX 7900/9070 系列、Ryzen AI 核显）用户的一键安装脚本：自动安装 uv、克隆 ComfyUI 仓库、创建 Python 3.12 虚拟环境、按 GPU 型号安装对应的 ROCm PyTorch 构建与依赖，配置 HIP_VISIBLE_DEVICES 后启动 ComfyUI Web UI。首次运行交互选择 GPU 代际并保存配置，多卡系统可选择指定 GPU。限制：仅支持 Windows 10/11 64 位，需 Git 与 PowerShell 5.1+；模型文件不随脚本提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条 PowerShell 命令完成 ComfyUI + ROCm PyTorch 环境搭建
- 支持 RDNA 3 / 3.5 / 4 三代 AMD GPU（gfx1100/gfx1151/gfx1200）
- 使用 uv 管理依赖，GPU 配置在多次运行间保存
- 多 GPU 系统可配置 HIP_VISIBLE_DEVICES

## 适用场景

- AMD 显卡用户在 Windows 上快速搭建 ComfyUI
- 避免手动配置 ROCm PyTorch 与虚拟环境
- 多卡系统指定使用某块 AMD GPU 运行 ComfyUI

## 场景标签

 · 领域:AI 工具链/图像生成环境配置

## 证据(README 行号)

> L8: A PowerShell script that sets up ComfyUI with ROCm support for AMD RDNA GPUs on Windows. It uses uv for fast and rel
> L60: * Installs the correct ROCm PyTorch build for your GPU

## 星数曲线

```mermaid
xychart-beta
    title "sh4den/ComfyUI-AMD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-29 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0011d9fa1495` · [字段定义](../../DATASET.md)*
