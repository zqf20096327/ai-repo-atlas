# shootthesound/Fizgig

⭐ 802 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/shootthesound/Fizgig) · 个人维护

**面向消费级 GPU 的 LoRA 训练与微调工作台**

Fizgig 是一个 LoRA 与微调工作室：支持在消费级 GPU（最低 8 GB 显存）上对多款图像、视频与音乐基础模型进行 LoRA、LoKR 训练与全量微调，提供模型修复、epoch 目测挑选、热力图训练可视化、AI 打标（JoyCaption、WD EVA02）、Studio 渲染队列等功能。可在本地 Windows/Linux 安装，也支持一键部署到 RunPod 租赁硬件。支持 NVIDIA 与 AMD 显卡路径。

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

- 支持对十余款图像/视频/音乐模型训练 LoRA、LoKR 与全量微调
- 消费级 GPU 最低 8 GB 显存即可训练，含显存不足自动恢复
- 提供训练热力图、触发词注意力图与相似度评分（AdaFace）
- 支持 NVIDIA 与 AMD 显卡，可部署到 RunPod

## 适用场景

- 在自己的照片集上训练人物或风格 LoRA
- 修复训练失败或效果不佳的 LoRA 而不重训
- 本地显卡不足时在 RunPod 租赁 GPU 上训练
- 为动漫/插画模型生成 booru 标签数据集

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3:  Fine-tune base models on consumer GPUs — down to 8 GB. Fix broken LoRAs without retraining. Find the best epoch by 
> L4:  A train · fine-tune · repair · explore workbench built end-to-end for Flux 2 Klein 9B , Flux 3 Image Klein , Fibo 2

## 星数曲线

```mermaid
xychart-beta
    title "shootthesound/Fizgig 星数(近 28 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 564 --> 820
    line [585, 593, 599, 603, 610, 622, 629, 635, 642, 644, 651, 655, 603, 690, 714, 721, 730, 743, 748, 764, 771, 774, 776, 779, 785, 788, 799, 799]
```

2026-10-22 585 → 2026-11-24 799（+214）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `f70dd434015c` · [字段定义](../../DATASET.md)*
