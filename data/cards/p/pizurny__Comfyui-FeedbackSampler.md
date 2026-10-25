# pizurny/Comfyui-FeedbackSampler

⭐ 35 · Python · MIT · 推送 2026-02-08 · [GitHub](https://github.com/pizurny/Comfyui-FeedbackSampler) · 个人维护

**ComfyUI 自定义采样器：迭代反馈循环生成 Deforum 风格缩放动画**

一个 ComfyUI 自定义节点，通过迭代反馈循环采样生成 Deforum 风格的缩放/平移/旋转动画：每帧以前一帧输出为基础再采样，支持 ControlNet 序列逐帧条件、LAB 色彩一致性防色漂、防模糊锐化、噪声注入与批量帧输出。兼容 SD1.5/SDXL/Flux 及任何适配原生 Ksampler 的模型。安装方式为克隆到 custom_nodes 目录并可选安装依赖，README 标注 Work in Progress。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 迭代反馈循环采样，支持 zoom/pan/rotate 动画参数
- 自动检测批量 ControlNet 提示图并逐帧应用条件
- LAB 色彩一致性、防模糊锐化与噪声注入机制
- 批量输出全部帧用于视频合成

## 适用场景

- 在 ComfyUI 中生成无限缩放/平移风格的动画序列
- 结合 ControlNet 图像序列做逐帧引导的动画
- 配合 Turbo/Lightning 模型快速迭代出帧

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L4: A custom ComfyUI sampler for creating **Deforum-style zoom animations** through iterative feedback loop.
> L24: Works with:
> L33: 1. Clone into `custom_nodes` folder:

## 星数曲线

```mermaid
xychart-beta
    title "pizurny/Comfyui-FeedbackSampler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `03c40792afd9` · [字段定义](../../DATASET.md)*
