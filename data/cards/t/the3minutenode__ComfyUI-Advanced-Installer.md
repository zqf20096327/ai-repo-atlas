# the3minutenode/ComfyUI-Advanced-Installer

⭐ 30 · Batchfile · MIT · 推送 2026-10-27 · [GitHub](https://github.com/the3minutenode/ComfyUI-Advanced-Installer) · 个人维护

**Windows 一键便携版 ComfyUI 安装器（Python 3.13 + CUDA 13）**

面向 Windows 用户的 ComfyUI 一键安装脚本：下载 bat 脚本运行后自动构建便携式嵌入式环境，预配置 Python 3.13.14、CUDA 13.0、SageAttention 与 Triton，并自动安装 ComfyUI-Manager、IPAdapter Plus、Impact Pack、GGUF 支持等节点。附带 ipadapter-downloader.bat 自动下载并归类 SD1.5/SDXL 的 IPAdapter 模型文件（约 15GB）。全程不改动系统 Python，通过 run.bat/update.bat 启动与更新。要求 Windows 10/11、NVIDIA RTX 20 系及以上显卡、约 15GB 空间。

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

- 一键 bat 脚本构建便携嵌入式 ComfyUI 环境（下载约 5GB）
- 预配置 Python 3.13.14 + CUDA 13.0 + SageAttention + Triton
- 自动安装 Manager、IPAdapter Plus、Impact Pack、GGUF 支持等节点
- IPAdapter 模型自动下载并归入对应 models 子目录

## 适用场景

- Windows 用户免手动配置快速搭建 ComfyUI 出图环境
- RTX 30/40/50 系显卡用户获得预配置的加速环境
- 使用 IPAdapter 做换脸和风格迁移时自动获取配套模型

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Get a pro-grade, portable ComfyUI environment in one click. Optimized for **Python 3.13**, **CUDA 13**, and **SageAt
> L29: 3. **Run Installer:** Double-click `comfy-adv-install.bat`. *Note: It will download ~5GB of data. Grab a coffee.*


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8ecf51b99e69` · [字段定义](../../DATASET.md)*
