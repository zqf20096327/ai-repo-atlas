# Monadical-SAS/Morpheus

⭐ 29 · TypeScript · GPL-3.0 · 推送 2026-03-12 · [GitHub](https://github.com/Monadical-SAS/Morpheus) · 组织维护

**基于 Stable Diffusion 的协作式图像生成 Web 应用**

开源 Web 应用，通过图像编辑与 Stable Diffusion 模型生成艺术作品，支持 Image-to-Image、ControlNet、Pix2pix 等用法，可加载多个模型，并通过 Firebase 提供认证与协作绘画系统。面向希望自建服务器掌控数据的用户，支持本地（Linux、macOS M1-M2）或云端部署，提供 Docker Compose 快速启动与 Kubernetes/Terraform 生产部署模板，基础设施代码已开源。默认内置部分 Stable Diffusion 模型，可通过管理面板或 CLI 增删。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Image-to-Image、ControlNet、Pix2pix 等多种图像生成用法
- 多模型加载与管理（管理面板/CLI 两种方式）
- Firebase 驱动的认证与协作绘画系统
- Docker Compose 本地启动与 Kubernetes/Terraform 生产部署模板

## 适用场景

- 自建图像生成服务器，掌控自己的数据
- 团队协作创作基于 Stable Diffusion 的艺术作品
- 本地或云端部署图像编辑与生成平台

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: Morpheus A WebApp to generate artwork with stable diffusion models.
> L14: **Morpheus is an open-source project that offers a creative and innovative platform for generating stunning artwork
> L23: - **Versatility**: We offer Image-to-Image support, Controlnet, and Pix2pix among other use cases.

## 星数曲线

```mermaid
xychart-beta
    title "Monadical-SAS/Morpheus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f9ec492f2df6` · [字段定义](../../DATASET.md)*
