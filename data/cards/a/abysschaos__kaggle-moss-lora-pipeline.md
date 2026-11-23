# abysschaos/kaggle-moss-lora-pipeline

⭐ 5 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/abysschaos/kaggle-moss-lora-pipeline) · [官网](https://github.com/abysschaos/kaggle-moss-lora-pipeline/releases/latest) · 个人维护 · 中文 README

**消费级显卡与 Kaggle 双轨训练 MOSS-Image LoRA 的管线**

面向 OpenMOSS MOSS-Image (5B DiT) 的 LoRA/DoRA/LoHa/LoKr 训练管线，基于 KohakuMossTrainer 构建，提供本地 Windows 与 Kaggle/Colab 云端两条路径。本地侧通过 C# 编译的原生 GUI 启动器提供 5-Tab 工作区、8 套预设模板、显存档位（6g~16g）与实时 Loss/EMA 看板；云端侧通过 kaggle.json 凭据与四种图集投递通道（临时外链/HF 私有仓/R2/Kaggle Dataset）推送 Notebook 训练并回传权重。支持断点续炼、暂停存盘与多子集配比。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 GUI 与 Kaggle/Colab 云端双轨训练路径
- 支持 LoRA/DoRA/LoHa/LoKr 与多子集配比 JSON
- 零拷贝复用本地 ComfyUI 模型库与 Python 环境
- 三阶解耦调度配合 6g~16g 显存档位配置

## 适用场景

- 在 6G~16G 显存的消费级显卡上微调 MOSS-Image
- 用 Kaggle 免费 T4 跑图集训练并自动回传权重
- 管理多人物/多画风数据集的配比训练
- 将训练产物直接同步到 ComfyUI 使用

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L9: > 一套面向 **OpenMOSS MOSS-Image (5B Single-Stream DiT)** 的双轨 LoRA / DoRA / LoHa / LoKr 自动化训练与工程调度方案，基于 KohakuBlueleaf/K
> L17: 在消费级显卡（如 8GB VRAM 的 RTX 4060 / 4070 Laptop）或免费云端容器（Tesla T4 16GB）上微调 50 亿参数的 MOSS-Image 单流 DiT 与 9B Qwen3.5 文本编码器，容
> L45: |**标准入口**|notebooks/kaggle_moss_lora_training.ipynb 或桌面 GUI【☁️ 云端遥控】/ `.\scripts\push_to_kaggle.ps1`|`MOSS_LoRA_Tra


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `3f15ebe4c322` · [字段定义](../../DATASET.md)*
