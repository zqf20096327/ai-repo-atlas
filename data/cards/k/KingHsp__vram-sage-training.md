# KingHsp/vram-sage-training

⭐ 56 · HTML · 推送 2026-10-30 · [GitHub](https://github.com/KingHsp/vram-sage-training) · 个人维护 · 中文 README

**在 12GB 显存上微调 SDXL 级扩散模型的训练套件**

名为 FluxForge Distillation Suite 的扩散模型微调环境，面向个人艺术家、研究者与小团队，宣称通过 Tensor Folding Engine、Hybrid Momentum Distillation 优化器与 Sleep-State Gradient Manager 等机制将 SDXL 级模型微调的显存基线降至 12GB（Titanic Mode 可至 8GB）。提供 Web 仪表盘 GUI、多语言 CLI、.safetensors 原生处理、checkpoint 状态回放与 Vision Tiler 数据集压缩。安装经由 forge-wizard 向导（需 Python 3.10+、CUDA 工具链），配置由 forge_config.toml 管理，核心引擎以 Python forge 模块暴露。注意：README 声明风险自担，水印注入器不强制使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 宣称 12GB VRAM 基线微调 SDXL 级模型，Titanic Mode 支持 8GB 显卡
- Web 仪表盘实时显示 VRAM、梯度范数与 loss 曲线
- checkpoint 保存 RNG 状态、调度器位置与数据加载顺序，可回放训练路径
- 提供七种语言的 CLI 与仪表盘本地化

## 适用场景

- 在单张 12GB 消费级显卡上微调 SDXL LoRA 或全量模型
- 研究者在小显存设备上做 ANIMA 模型的消融实验
- 通过手机远程 SSH 监控训练进度

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L12: **FluxForge Distillation Suite** shatters this paradigm. It is a precision-engineered environment that rethinks how
> L33: |**The Solo Artist**|Wants to train a custom LoRA on their personal art style, has a single RTX 3060.|Train SDXL fi
> L84: forge train \

## 星数曲线

```mermaid
xychart-beta
    title "KingHsp/vram-sage-training 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-31 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `1e86176bba83` · [字段定义](../../DATASET.md)*
