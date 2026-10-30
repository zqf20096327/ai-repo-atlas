# AgarwalYash14/ORLA

⭐ 17 · TypeScript · MIT · 推送 2026-09-26 · [GitHub](https://github.com/AgarwalYash14/ORLA) · 个人维护

**文本/图片生成 3D 模型的 Web 应用**

基于 React + TypeScript 前端与 FastAPI + Celery + Redis 后端的 Web 应用：用户输入文本提示，经 Stability AI 的 Stable Diffusion 3.5 Large Turbo API 生成适配 3D 转换的 2D 图像，再由腾讯 Hunyuan3D-2 模型转换为 3D 模型，浏览器内用 Three.js 实时交互查看。支持文本到 3D 与图片到 3D 两种输入。需 Node.js 18+、Python 3.9+、Docker 及 Hugging Face API token，通过 Docker Compose 启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本提示经增强后生成 2D 图像再转 3D 的多步流水线
- 文本到 3D 与图片到 3D 两种生成方式
- Three.js 实时交互式 3D 查看器（旋转/缩放/平移）
- Celery + Redis 异步任务处理，Docker Compose 部署

## 适用场景

- 输入文字描述快速获得 3D 模型资产
- 把已有 2D 图片转换为 3D 模型
- 在浏览器中交互查看与检查生成的 3D 模型

## 场景标签

 · 领域:生成式 3D/创意工具

## 证据(README 行号)

> L30: - **Text-to-3D Generation**: Create 3D models from textual descriptions
> L48: - **Stable Diffusion 3.5** AI model for image generation
> L49: - **Hunyuan3D-2** AI model for 3D model creation

## 星数曲线

```mermaid
xychart-beta
    title "AgarwalYash14/ORLA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `06b61a734c3c` · [字段定义](../../DATASET.md)*
