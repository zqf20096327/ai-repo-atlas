# MoJIeAIGC/Comfyui-MojieUI

⭐ — · [GitHub]() · 组织维护 · 中文 README

**以 ComfyUI 为后端的图像生成商用平台前后端源码**

Mojie-UI（已更名奇画AI-2.0 beta，原开源版不再维护）是以 ComfyUI 为图像处理后端的开源前后端系统：Vue3 前端提供对话式交互与常用功能，Django 后端用 Redis 缓存任务并分发至 ComfyUI，支持多任务多 GPU 负载均衡、快慢队列与充值算力积分逻辑；另含基于 BiRefNet 的抠图辅助服务。部署需 Linux、Redis、MySQL、ComfyUI，GPU 推荐 A10/L20/4090 以上，面向电商/广告/创意类商用场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Redis 任务队列将请求依次发送至 ComfyUI，支持多任务多 GPU 负载均衡
- Vue3+Vite 前端，对话式交互与拖拽操作
- 完整的充值算力积分逻辑与快/慢双队列
- BiRefNet 抠图辅助服务（自动输出 1024x1284 尺寸主体图）

## 适用场景

- 搭建面向电商/广告/创意用户的图像生成商用平台
- 以 ComfyUI 为算力后端做多任务队列化部署
- 做付费积分制的图像处理服务二次开发

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L3: ## 项目概述：以comfyui为后端的图像处理UI框架
> L24: - 使用redis作为任务缓存，将任务请求依次发送至comfyui
> L4: Mojie-UI已正式更名为奇画AI-2.0(beta)，奇画AI是摩诘智影旗下研发的AI商用系统，开箱即用，操作简单友好，效果更直观，可扩展性极佳，也适合电商/广告/创意类用户直接使用。平台已对接国内外主流大厂模型。支持模型微调定

## 星数曲线

```mermaid
xychart-beta
    title "MoJIeAIGC/Comfyui-MojieUI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-26 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1e3c3bf5ef86` · [字段定义](../../DATASET.md)*
