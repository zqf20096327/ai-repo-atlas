# aniketmaurya/chitra

⭐ 234 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/aniketmaurya/chitra) · [官网](https://chitra.readthedocs.io/en/latest/) · 个人维护

**全栈深度学习多功能库：模型构建、训练与服务部署**

面向深度学习开发者的 Python 多功能库（名称源自印地语'图像'）：提供图像数据加载与 DataGenerator（组件可自定义、支持渐进式缩放、tf.data 转换）、继承 tf.keras.Model 的 Trainer（含循环学习率）、基于 GradCAM/GradCAM++ 的模型可解释性可视化、基于 imgaug 的边界框标注，以及框架无关的模型服务（create_api 生成 REST API、GradioApp 生成交互 UI）、模型自动 Docker 化。通过 pip 提供最小/训练/服务多种安装选项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图像 dataloader/datagenerator，组件可自定义，支持渐进式缩放与 tf.data 转换
- GradCAM/GradCAM++ 模型可解释性可视化
- 框架无关模型服务：create_api 生成 REST API，GradioApp 生成交互 UI
- 模型自动 Docker 化与 GPU 内存管理工具

## 适用场景

- 快速搭建图像分类数据加载与训练流程
- 为 ML/DL 模型生成 REST API 或交互式 UI 原型
- 用 GradCAM 可视化模型学习内容

## 场景标签

`图像视频处理` `MLOps` · 领域:感知与多模态

## 证据(README 行号)

> L10: **chitra** (**चित्र**) is a multi-functional library for full-stack Deep Learning. It simplifies Model Building, AP
> L267: Chitra can Create Rest API or Interactive UI app for Any Learning Model -

## 星数曲线

```mermaid
xychart-beta
    title "aniketmaurya/chitra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 233 --> 235
    line [234, 234]
```

2026-10-18 234 → 2026-10-28 234（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f3df030632ff` · [字段定义](../../DATASET.md)*
