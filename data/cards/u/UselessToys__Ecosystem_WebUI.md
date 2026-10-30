# UselessToys/Ecosystem_WebUI

⭐ 25 · Python · NOASSERTION · 推送 2026-08-27 · [GitHub](https://github.com/UselessToys/Ecosystem_WebUI) · 个人维护

**LoRA/大模型训练套件 WebUI：数据集、训练、生成一体化**

基于 Kohya SS 的 NextJS/React Web 界面，覆盖 Stable Diffusion 类模型训练全流程：数据集准备（拖拽上传、WD14/BLIP/GIT 自动打标、标签编辑器）、多架构训练（SDXL、SD1.5、Flux、SD3/3.5、Lumina、Anima、HunyuanImage，LoRA/LoCon/LoHa/LoKr/DoRA）、40+ 训练预设与实时监控（步数/损失/学习率/ETA），内置 ComfyUI 工作区直接生成测试。支持 Civitai/Arc En Ciel/HuggingFace 模型浏览下载、LoRA 合并烘焙与训后上传。需 NVIDIA CUDA 12.1+ GPU、Python 3.10-3.12 与 Node.js 20.19+，AMD/ROCm 为社区支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多架构 LoRA 训练（SDXL/Flux/SD3/Lumina/Anima/HunyuanImage，含 DoRA/LoHa/LoKr）
- WD14/BLIP/GIT 自动打标与标签批量编辑
- 内置 ComfyUI 工作区，训练后直接生成测试
- Civitai/Arc En Ciel/HuggingFace 模型浏览下载与 24+ 种 checkpoint 合并模式

## 适用场景

- 为 Stable Diffusion/Flux 等模型训练 LoRA 并现场验证效果
- 整理数据集：批量上传、自动打标、标签清洗
- 从 Civitai/HuggingFace 下载底模与 LoRA 并做合并烘焙

## 场景标签

`微调` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L7: **Train, tag, and generate — a full LoRA & checkpoint training suite with ComfyUI built in.**
> L9: A web interface built on Kohya SS. Prepare datasets, auto-tag, train across many model types (SDXL, Flux, SD3, Lumin

## 星数曲线

```mermaid
xychart-beta
    title "UselessToys/Ecosystem_WebUI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4262a586f6a0` · [字段定义](../../DATASET.md)*
