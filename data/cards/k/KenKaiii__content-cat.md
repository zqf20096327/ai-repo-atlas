# KenKaiii/content-cat

⭐ 18 · TypeScript · AGPL-3.0 · 推送 2025-12-23 · [GitHub](https://github.com/KenKaiii/content-cat) · 个人维护

**带可视化工作流编辑器的 AI 图像与视频生成平台**

基于 Next.js/React/TypeScript 的自托管生成平台：通过 fal.ai API 调用 Nano Banana Pro 生成 1K-4K 多比例图像，用 Kling 2.6/2.5 Turbo/Wan 2.6 生成视频，支持图生视频、参考图风格引导、由自拍创建 AI 角色以保持人脸一致性、产品摄影变体。核心机制为基于节点（XYFlow+Dagre）的可视化工作流编辑器，可拖拽组合图像生成、视频生成、剪辑、拼接、字幕等节点并导入导出工作流。依赖 PostgreSQL、Redis、Docker，一键脚本安装，AGPL-3.0 许可，需自备 fal.ai API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Nano Banana Pro 图像生成（1K-4K、多比例）与 Kling/Wan 视频生成
- XYFlow+Dagre 节点式可视化工作流编辑器，支持导入导出
- 由自拍创建 AI 角色实现人脸一致性生成
- 产品摄影变体（背景/光照/角度）与提示词画廊

## 适用场景

- 搭建自己的 AI 图像与视频生成工作台
- 用节点编排批量生成与后期（剪辑/拼接/字幕）管线
- 生成保持角色面部一致性的系列图像
- 批量生成不同背景光照的产品图

## 场景标签

`图像生成` `视频生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L3: AI-powered image and video generation platform with a visual workflow builder by Ken Kai.
> L8: - Image generation with Nano Banana Pro (1K-4K, multiple aspect ratios)
> L9: - Video generation with Kling 2.6, Kling 2.5 Turbo, and Wan 2.6

## 星数曲线

```mermaid
xychart-beta
    title "KenKaiii/content-cat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `5be446cb517b` · [字段定义](../../DATASET.md)*
