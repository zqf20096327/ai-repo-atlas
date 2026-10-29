# datastone-spirit/spirit-lora-trainer

⭐ 88 · Python · NOASSERTION · 推送 2025-11-05 · [GitHub](https://github.com/datastone-spirit/spirit-lora-trainer) · [官网](https://serverless.datastone.cn) · 组织维护 · 中文 README

**训练 Flux 等模型 LoRA 的 Web 工具包（基于 kohya-ss 脚本）**

智灵训练器是训练 Flux1-LoRA 模型的工具包，基于 kohya-ss sd-scripts 脚本构建，采用前后端解耦架构，提供 Web 界面配置少量参数即可启动训练，支持实时监控 loss、训练步数与剩余时间，训练状态可持久化并在重新打开页面后恢复监控。支持训练 Flux、Flux Kontext、Hunyuan Video、Wan 2.1/2.2、Qwen Image (Edit) 等模型，并内置 Florence2 与 Joy-Caption-Two-Alpha 图像打标工作流。安装需自行搭建前端（Node.js/pnpm）、后端（Python 3.10+/torch 2.5.1+cu121/xformers）并克隆部署 kohya-ss、ai-toolkit、diffusion-pipe、musubi-tuner 等多个上游训练脚本仓库，还需手动下载各类模型与 tokenizer 文件。

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

- 前后端解耦架构，训练状态持久化，重开页面可恢复监控
- 支持 Flux / Flux Kontext / Hunyuan Video / Wan 2.1/2.2 / Qwen Image (Edit) 多模型 LoRA 训练
- 内置 Florence2 与 Joy-Caption-Two-Alpha 图像打标工作流
- 实时监控 loss、训练步数与预计剩余时间

## 适用场景

- 在 Web 界面配置少量参数训练自己的 Flux LoRA 模型
- 训练 Wan 2.1/2.2 视频或 Qwen Image 的 LoRA
- 为训练数据集自动生成图像描述（打标）

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L11: Spirit Lora Trainer is a robust toolkit for training Flux1-LoRA models with a focus on simplicity and reliability a

## 星数曲线

```mermaid
xychart-beta
    title "datastone-spirit/spirit-lora-trainer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 87 --> 89
    line [88, 88]
```

2026-10-18 88 → 2026-10-29 88（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `96e0f732799b` · [字段定义](../../DATASET.md)*
