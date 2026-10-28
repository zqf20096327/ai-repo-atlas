# makerlinck/Antool

⭐ 19 · Python · MIT · 推送 2026-03-26 · [GitHub](https://github.com/makerlinck/Antool) · 个人维护 · 中文 README

**基于深度学习标签模型的图片自动分类与标签服务**

基于 DeepDanbooru 图像识别模型（README 描述提及 LangChain）的媒体文件标签系统：Python 3.13 + LiteStar 后端提供标签生成服务，通过 WebSocket 长连接支持心跳、流式返回与任务取消；前端以 Eagle 媒体管理器 Node.js 插件形式提供标签管理与分类浏览界面；另提供 antool CLI 批量处理图片。README 中部署步骤标注'目前仅适用于开发调试'，主版本以源码方式运行；后继版本 Antool-Next 开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- DeepDanbooru 轻量级图像识别模型生成标签
- WebSocket API 支持心跳、流式返回、任务取消
- antool CLI 命令行批量处理图片
- Eagle 插件前端提供标签管理与分类浏览

## 适用场景

- 为图片媒体库批量生成分类标签
- 在 Eagle 中浏览和管理自动生成的标签
- 通过 WebSocket API 集成到自己的媒体处理流程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L14: 基于 ** Deepdanbooru ** 的智能媒体文件标签系统，帮助实现自动化图片媒体分类
> L18: - 后端：基于 Python 3.13 LiteStar 框架开发，集成轻量级图像识别模型，实现高性能标签生成服务。项目整体遵循整洁架构

## 星数曲线

```mermaid
xychart-beta
    title "makerlinck/Antool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4af1752eeda4` · [字段定义](../../DATASET.md)*
