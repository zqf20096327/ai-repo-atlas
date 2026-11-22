# Neywa-Labs/mlx-vlm

⭐ 5,900 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/Neywa-Labs/mlx-vlm) · [官网](https://neywa-labs.github.io/mlx-vlm/) · 组织维护

**在 Apple Silicon Mac 上本地推理与微调多模态模型的工具包**

基于 Apple MLX 框架的 Python 包，用于在 Mac 上运行与微调多模态模型，输入覆盖文本、图像、视频、音频。提供 CLI 生成（mlx_vlm.generate）、本地服务器（含 chat、responses、messages、audio、image、cache、metrics 端点）、可选的 Gradio 聊天 UI，以及将 Hugging Face 模型转换为 MLX 并量化的工具（RTN/AWQ、混合配方）。内置投机解码，支持 dflash、eagle3、mtp 三类 drafter 家族。另随仓库附带可装入编码 agent 的 skills 技能包。pip 安装，Python 3.10+，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI 与本地服务器双入口推理，支持文本/图像/音频输入
- Hugging Face 模型到 MLX 的转换与量化（RTN/AWQ）
- 投机解码支持 dflash/eagle3/mtp 三类 drafter 家族
- 随仓库提供可装入 Claude Code/Codex/Gemini 的 agent skills 包

## 适用场景

- 在 Mac 上本地运行多模态模型做文本生成与 OCR 类任务
- 把 Hugging Face 模型转换并量化为 MLX 格式
- 起一个本地服务器为应用提供模型推理端点
- 为编码 agent 安装 mlx-vlm 工作流技能包

## 场景标签

`多模态` `OCR` `微调` `模型量化` · 领域:感知与多模态

## 证据(README 行号)

> L3: Any input. Any output. All local. Runs locally on your Mac. Install with pip install -U mlx-vlm or try it in Nativ.
> L5:  Run and fine-tune multimodal models on Apple Silicon. Text, images, video, and audio in — any out. Built on MLX.
> L99: This repo ships an agent-skills bundle under `skills/` for common MLX-VLM workflows — usage, conversion, developmen

## 星数曲线

```mermaid
xychart-beta
    title "Neywa-Labs/mlx-vlm 星数(近 13 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22"]
    y-axis "stars" 5815 --> 5907
    line [5822, 5832, 5836, 5840, 5845, 5846, 5848, 5853, 5859, 5861, 5862, 5865, 5900]
```

2026-11-08 5,822 → 2026-11-22 5,900（+78）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `4ec44c9ca5d4` · [字段定义](../../DATASET.md)*
