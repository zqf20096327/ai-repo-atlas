# ffxvs/sd-webui-complete-setup

⭐ 51 · Jupyter Notebook · MIT · 推送 2026-04-18 · [GitHub](https://github.com/ffxvs/sd-webui-complete-setup) · [官网](https://ffxvs.github.io/sd-webui-complete-setup/) · 个人维护

**云 GPU 上安装 Stable Diffusion WebUI 的 Jupyter notebook 部署工具**

面向 Paperspace 与 Runpod 用户的部署方案：通过预构建 Docker 容器（auto1111 与 Forge 两种镜像，容器体积低于 6GB）启动 Jupyterlab，再用 ipynb notebook 安装 SD WebUI、下载 SD v1.5/SDXL/FLUX 模型及扩展、loRA、embedding、upscaler、VAE 等资源，资源存放于共享/持久存储。内置按 4 类风格整理的热门模型清单与扩展清单，支持从 URL 安装资源，容器随版本更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 auto1111 与 Forge 两种预构建 Docker 容器镜像（低于 6GB）
- notebook 覆盖 WebUI 安装与 SD v1.5/SDXL/FLUX 模型下载
- 支持 Paperspace 与 Runpod 云 GPU 平台
- 模型、loRA、输出等资源存储于共享/持久存储，支持从 URL 安装扩展与资源

## 适用场景

- 在 Paperspace/Runpod 云 GPU 上一键部署 SD WebUI 或 Forge
- 按风格分类清单挑选并下载 SD/SDXL/FLUX 模型与 loRA 等资源
- 希望用小体积容器快速搭建可更新的绘图环境

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L2: Jupyter notebook for Stable Diffusion WebUI and Stable Diffusion WebUI Forge.
> L19: * Notebook for installing WebUI, downloading SD v1.5, SDXL and FLUX models.

## 星数曲线

```mermaid
xychart-beta
    title "ffxvs/sd-webui-complete-setup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-26 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `13a246ac7453` · [字段定义](../../DATASET.md)*
