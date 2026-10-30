# ForgeOpus/ModelForge

⭐ 16 · Python · BSD-3-Clause · 推送 2026-05-01 · [GitHub](https://github.com/ForgeOpus/ModelForge) · 组织维护

**本地 GPU 上无代码微调 LLM 的工具包**

面向无深度 ML 背景用户的本地 LLM 微调工具：上传 JSONL 数据集，在 React 网页界面或 CLI 向导中选择任务（文本生成/摘要/问答）即可完成训练与评测。支持 HuggingFace 与 Unsloth 两种训练后端，训练策略含 SFT、QLoRA、RLHF、DPO；自动检测 CUDA 或 Apple MPS 硬件并推荐设置。要求 Python 3.11 与 4GB+ 显存 GPU，Apple Silicon 支持为实验性（仅 HuggingFace 后端、不支持量化）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- React 网页 UI 与 headless/SSH 场景的 CLI 向导两种交互方式
- SFT/QLoRA/RLHF/DPO 四种训练策略与内置任务评测指标
- 自动检测 GPU（CUDA/MPS）并推荐最优设置
- 支持 NVIDIA 4GB+ 显存与 Apple Silicon（实验性）

## 适用场景

- 在笔记本 GPU 上无代码微调 LLM 原型
- 黑客松或快速原型阶段的模型定制
- 通过 CLI 向导在无显示器的 SSH 服务器上训练

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L10: **Fine-tune LLMs on your laptop's GPU—no code, no PhD, no hassle.**
> L30: - **One-Click Workflow**: Upload data → Configure → Train → Test
> L34: - **Advanced Strategies**: SFT, QLoRA, RLHF, DPO support

## 星数曲线

```mermaid
xychart-beta
    title "ForgeOpus/ModelForge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ee9332b284eb` · [字段定义](../../DATASET.md)*
