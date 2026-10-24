# WaveSpeedAI/wavespeed-comfyui

⭐ 65 · JavaScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/WaveSpeedAI/wavespeed-comfyui) · [官网](https://wavespeed.ai) · 组织维护

**ComfyUI 插件：在节点工作流中调用 WaveSpeed 托管的 600+ 图像/视频模型**

WaveSpeed AI 官方的 ComfyUI 自定义节点插件：通过单一 Predictor 节点以 API Key 访问托管的 600+ 生成模型，覆盖文生图、图生图、文/图生视频、文生音频、图生 3D 等 20+ 类别；节点按模型 schema 动态生成参数，输入输出兼容 ComfyUI IMAGE/VIDEO/AUDIO 张量，张量自动上传 CDN，输出为 URL 并可经 Preview 节点转回张量。需先安装 ComfyUI 并注册 WaveSpeed API Key（含免费档），通过 git clone 到 custom_nodes 并安装依赖使用；另支持在 Krita AI Diffusion 插件中复用节点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 Predictor 节点访问 600+ 托管模型，参数按模型 schema 动态生成
- 覆盖文生图/视频、图生视频、文生音频、图生 3D 等 20+ 类生成任务
- 兼容 ComfyUI IMAGE/VIDEO/AUDIO 张量，输入张量自动上传 CDN、输出可转回张量
- 可通过 Krita AI Diffusion 插件无修改复用节点

## 适用场景

- 在 ComfyUI 工作流中调用 Seedream、Kling、Wan、Flux 等托管模型
- 串联多阶段流水线：文生图→图像增强→图生视频
- 不部署本地模型、依靠 API 免费额度做图像视频生成

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L10: Support for **20+ AI generation categories** including:
> L20: - **Single Predictor Node** - Access 600+ AI models through one node
> L35: - WaveSpeed AI API Key (free tier available)

## 星数曲线

```mermaid
xychart-beta
    title "WaveSpeedAI/wavespeed-comfyui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-24 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `d7a4f3578938` · [字段定义](../../DATASET.md)*
