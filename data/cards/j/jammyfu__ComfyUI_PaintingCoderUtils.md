# jammyfu/ComfyUI_PaintingCoderUtils

⭐ 17 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils) · [官网](https://jammyfu.github.io/ComfyUI_PaintingCoderUtils/) · 个人维护 · 中文 README

**ComfyUI 自定义节点集：为 AI 绘图工作流提供图像/文本处理工具**

由开发者个人维护的 ComfyUI 自定义节点集合，面向使用 Stable Diffusion（SDXL）与 Midjourney 分辨率规范的艺术家和开发者。提供图像分辨率调整（SDXL 最优比例预设）、尺寸与空 latent 创建、Web 图片加载、Base64 编解码、文本清理与合并、开关节点、动态图像输入、文本显示增强和蒙版预览等节点，用于在 ComfyUI 中组装图像生成工作流。以 git clone 到 custom_nodes 目录方式安装；v0.3.0 更改命名空间导致旧工作流失效，附带的修复工具可转换路径分隔符。

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

- SDXL 全部最优分辨率预设的图像调整与尺寸/latent 创建节点
- 文本清理（去空行/首尾空格）与支持正则分隔符的文本合并节点
- 条件开关、动态多图输入等工作流控制节点
- v0.3.0 命名空间变更附 HTML 工作流修复工具

## 适用场景

- 在 ComfyUI 中按 SDXL/Midjourney 规范生成图像尺寸和 latent
- 清理 prompt 文本或为 LoRA 训练准备文本数据
- 在图像生成工作流中做条件分支与蒙版预览

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L5: A practical collection of nodes designed for ComfyUI that streamlines image and text processing workflows. Features 
> L11: **Quick install / 快速安装:** `cd ComfyUI/custom_nodes && git clone https://github.com/jammyfu/ComfyUI_PaintingCoderUti

## 星数曲线

```mermaid
xychart-beta
    title "jammyfu/ComfyUI_PaintingCoderUtils 星数(近 3 点)"
    x-axis ["2026-10-24", "2026-10-26", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-24 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `63601e31f806` · [字段定义](../../DATASET.md)*
