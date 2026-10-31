# nyomnisgarz/amd-diffusion-lab

⭐ 13 · Python · MIT · 推送 2026-07-06 · [GitHub](https://github.com/nyomnisgarz/amd-diffusion-lab) · 个人维护

**低显存 AMD GPU 上做 Stable Diffusion LoRA 训练与推理的实验仓库**

面向小显存（8-12GB VRAM）AMD GPU 的 Stable Diffusion 个人实验仓库：提供针对低显存优化的 SD 1.5 LoRA 训练配置、推理参数（batch size/steps/sampler）与提示词模板，通过 diffusion_lab.py 命令行执行生成与训练。README 明确声明不做 SDXL 训练、不做 ControlNet、不构建生成服务，定位为个人创作工作流（生成一致风格的美术素材）。硬件在 AMD RX 7800 XT 与 7900 XTX 上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面向 8-12GB 低显存的 LoRA 训练配置（sd15_lora_low_vram.yaml）
- 命令行执行推理与训练（generate/train 子命令）
- OOM 处理指引：减小 batch size 或启用梯度检查点
- 在 AMD RDNA3 显卡上测试

## 适用场景

- 我在小显存 AMD 显卡上训练 SD 1.5 风格 LoRA
- 调整采样步数与 batch size 平衡生成质量与速度
- 用提示词模板生成风格一致的项目美术素材

## 场景标签

`图像生成` `微调` · 领域:内容生成

## 证据(README 行号)

> L3: This repo is a small diffusion playground for low-VRAM workflows: LoRA configs, inference notes, and practical exper
> L33: python diffusion_lab.py generate --prompt 'a cat in space' --steps 25

## 星数曲线

```mermaid
xychart-beta
    title "nyomnisgarz/amd-diffusion-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `bc0b7869564e` · [字段定义](../../DATASET.md)*
