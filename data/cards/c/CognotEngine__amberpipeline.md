# CognotEngine/amberpipeline

⭐ 14 · TypeScript · Apache-2.0 · 推送 2025-12-29 · [GitHub](https://github.com/CognotEngine/amberpipeline) · [官网](https://ap.popolili.com) · 组织维护

**把 AI 生成图像转换为游戏资产的中间件工具**

面向游戏设计师的中间件：将 AI 生成的图像加工为游戏可用资产。基于 SAM 图像分割模型实现 AI 驱动的抠图与背景移除（支持点提示引导），提供角色多级图层管理（堆叠与混合模式）、骨骼创建/蒙皮权重绘制与动画预览，另可生成法线贴图。技术栈为 Electron + React 前端与 Python FastAPI 后端，需分别安装并以开发模式启动；后端要求 Python 3.8+，推荐 8GB 以上 GPU 显存。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 SAM 的 AI 图像分割与背景移除，支持点提示引导
- 角色多级图层管理与混合模式
- 骨骼创建、权重绘制与动画预览
- 提供法线贴图生成 API（/generate-normal-map）

## 适用场景

- 把 AI 生成的角色原图处理成可用的游戏资产
- 对角色素材做分层编辑与骨骼绑定
- 批量处理图像抠图并导出法线贴图

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L10: **AmberPipeline** is a middleware tool focused on converting AI-generated images into game assets, providing design
> L48: - **SAM (Segment Anything Model)** - A powerful image segmentation model

## 星数曲线

```mermaid
xychart-beta
    title "CognotEngine/amberpipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c0af6d6a7dc6` · [字段定义](../../DATASET.md)*
