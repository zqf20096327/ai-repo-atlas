# CodeBoy2006/hybrid-image-tagger

⭐ 23 · Python · 推送 2026-07-17 · [GitHub](https://github.com/CodeBoy2006/hybrid-image-tagger) · 个人维护

**混合 WD Tagger 与 VLM 为图像数据集批量生成描述标签的工具**

面向 Stable Diffusion/LoRA 训练数据准备的图像打标工具：结合 WD Tagger（本地 ONNX）与 VLM（需 OpenAI 兼容 API key）双通道生成标签，支持并行/顺序/详细三种双通道策略，可仅用单一标签器。提供 Gradio 网页界面，含预检校验（图片与 LLM 凭证/端点/视觉支持）、大图自动压缩、批量并发处理、提示词编辑与丰富后处理（替换、触发词、去重排序等）。每张图输出同名 .txt 标签文件，结果打包下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WD Tagger + VLM 双通道打标，三种合并策略
- 批量并发处理与大图自动压缩以优化 API 用量
- 预检校验图片与 LLM 凭证/端点/模型/视觉支持
- 可编辑打标与合并提示词，含占位符约束

## 适用场景

- 为 Stable Diffusion / LoRA 训练准备图像标签数据集
- 批量给大量图片生成描述性标签并下载打包结果
- 通过网页界面调整标签后处理规则与触发词

## 场景标签

 · 领域:图像标注/数据集准备

## 证据(README 行号)

> L5: A powerful and user-friendly tool that uses a hybrid approach, combining the strengths of the WD Tagger and a Vision
> L9: - **Hybrid Tagging**: Utilizes both WD Tagger and a VLM for comprehensive and high-quality tag generation.

## 星数曲线

```mermaid
xychart-beta
    title "CodeBoy2006/hybrid-image-tagger 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ba181889a6b5` · [字段定义](../../DATASET.md)*
