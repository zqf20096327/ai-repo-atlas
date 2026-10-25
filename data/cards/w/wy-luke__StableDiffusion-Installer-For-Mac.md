# wy-luke/StableDiffusion-Installer-For-Mac

⭐ 48 · Shell · 推送 2026-09-25 · [GitHub](https://github.com/wy-luke/StableDiffusion-Installer-For-Mac) · 个人维护 · 中文 README

**一条命令在 Mac 上安装 Stable Diffusion WebUI 的脚本**

面向 macOS 用户的 Shell 安装脚本：通过 curl 执行单条命令完成 Stable Diffusion WebUI（AUTOMATIC1111 版）的安装，使用 Homebrew 安装依赖、micromamba 创建隔离 Python 虚拟环境，不改写系统 Python。README 说明安装后通过 http://127.0.0.1:7860 访问 Web UI，提供重新运行命令、AMD 显卡与 MPS 显存不足等故障排查方法，以及各版本 SD 模型文件与配置文件的放置说明。声明理论上兼容 Apple Silicon 与 Intel CPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单条 curl 命令完成安装
- 用 micromamba 建隔离虚拟环境，不污染系统 Python
- 提供 AMD 显卡与 MPS 内存不足的排查方案
- 说明 SD 1.x/2.x 模型与 yaml 配置文件的放置方法

## 适用场景

- 在不熟悉命令行的前提下在 Mac 上装好 Stable Diffusion
- 安装后需要重新启动 WebUI 生成图片
- 遇到显卡兼容或显存报错时按文档排查

## 场景标签

 · 领域:图像生成/开发环境工具

## 证据(README 行号)

> L7: Install Stable Diffusion web UI on your Mac **with one sigle command**:
> L13: Use mamba to create virtual environment, so it won't conflict with and won't pollute the Python environment in your
> L116: 1. Use Homebrew to install required dependencies. If you already have it installed, it will be used automatically.

## 星数曲线

```mermaid
xychart-beta
    title "wy-luke/StableDiffusion-Installer-For-Mac 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-25 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c7cc2d512f44` · [字段定义](../../DATASET.md)*
