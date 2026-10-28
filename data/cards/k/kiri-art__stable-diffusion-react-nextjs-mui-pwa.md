# kiri-art/stable-diffusion-react-nextjs-mui-pwa

⭐ 134 · TypeScript · MIT · 推送 2026-08-11 · [GitHub](https://github.com/kiri-art/stable-diffusion-react-nextjs-mui-pwa) · [官网](https://kiri.art/) · 个人维护

**面向 Web 开发者的 Stable Diffusion PWA 前端（React/NextJS/MUI）**

基于 React/NextJS 与 Material UI 的 Progressive Web App 前端，用于向 Stable Diffusion 后端发起图像生成请求。后端目标支持多种：本地 docker 镜像（kiri-art/docker-diffusers-api）、本地已有 Stable Diffusion 安装（node spawn 调用 Python 脚本）、以及 Banana.dev 无服务器 GPU 容器（需 BANANA_API_KEY/BANANA_MODEL_KEY）。提供注册/登录/积分流程开关（REQUIRE_REGISTRATION）、Lingui 国际化命令行工具。项目自 2022 年 8 月起活跃开发，作者声明以有限业余时间维护，PR 优先响应。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持三类 Stable Diffusion 后端：本地 docker、本地安装、Banana.dev serverless GPU
- PWA 形态，可在本地免费运行或部署
- Lingui + NextJS i18n 路由的国际化支持
- 可配置的注册/登录/积分流程（仅生产默认开启）

## 适用场景

- 有 Web 开发背景的人通过熟悉的 React 技术栈体验 AI 图像生成
- 在没有本地 GPU 的环境下经 Banana.dev 跑 Stable Diffusion
- 部署一个可分享的图像生成 Web 界面

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: _PWA Web App front end for Stable Diffusion, on React/NextJS with Material UI_
> L13: - Web interface to run Stable Diffusion queries on:

## 星数曲线

```mermaid
xychart-beta
    title "kiri-art/stable-diffusion-react-nextjs-mui-pwa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 133 --> 135
    line [134, 134]
```

2026-10-18 134 → 2026-10-28 134（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `53902dbaea43` · [字段定义](../../DATASET.md)*
