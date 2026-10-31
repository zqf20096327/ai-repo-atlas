# TensorHarmony/lorakit

⭐ 19 · Python · Apache-2.0 · 推送 2026-08-02 · [GitHub](https://github.com/TensorHarmony/lorakit) · 组织维护

**单 YAML 配置驱动的 SDXL DreamBooth/LoRA 微调工具包**

面向 SDXL 微调的配置驱动训练工具：准备 10–30 张图像、编辑一个 YAML、运行一条命令即可产出 diffusers 格式的 LoRA 权重。训练代码基于 Hugging Face AutoTrain Advanced 的 DreamBooth 分支，配置风格取自 ai-toolkit。提供 4-bit/8-bit QLoRA 与 bf16 两种路径（16 GB 起，24 GB 推荐），支持潜空间缓存、torch.compile、可恢复检查点、训练中实时预览，以及基于 19 类人脸解析的掩码以将学习集中于主体。需 NVIDIA GPU，用 uv 管理依赖、源码安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 YAML 配置 + 单命令完成 SDXL LoRA 训练，无需写代码
- QLoRA 4-bit 使 16 GB 显存可训练，bf16 + torch.compile 达到基准 5.9x 步速（RTX 4090 实测）
- 潜空间缓存、可恢复检查点与训练中实时预览
- 19 类人脸解析掩码将 LoRA 学习集中于主体、排除衣物与背景

## 适用场景

- 用一组人物照片训练专属 SDXL LoRA 角色模型
- 在 16 GB 显存的 T4 上以 4-bit QLoRA 低成本微调 SDXL
- 训练过程中通过预览图检查效果并可中断续训

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: **Fine-tune Stable Diffusion XL (SDXL) with LoRA from a single YAML file.**
> L5: lorakit is a small, fast, config-driven toolkit for SDXL DreamBooth / LoRA training. Point it at a folder of images,

## 星数曲线

```mermaid
xychart-beta
    title "TensorHarmony/lorakit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5253bb58154c` · [字段定义](../../DATASET.md)*
