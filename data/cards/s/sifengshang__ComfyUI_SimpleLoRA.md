# sifengshang/ComfyUI_SimpleLoRA

⭐ 10 · Python · 推送 2026-03-09 · [GitHub](https://github.com/sifengshang/ComfyUI_SimpleLoRA) · 个人维护

**ComfyUI 自定义节点：单节点配置完成 LoRA 微调**

该仓库是 ComfyUI 的自定义节点，通过名为 LoRATrainer 的单个节点对 stable diffusion 模型执行 text-to-image LoRA 微调。训练脚本 lora_core.py 基于 diffusers 示例修改，LoRA 默认 rank 为 4，可配置学习率、batch size、seed 等参数。支持 HuggingFace 数据集或用户自建数据集，训练产出的 LoRA 权重以 safetensors 存入 ComfyUI 的 loras 目录，可由 LoadLoRA 节点加载。当前版本不支持从 checkpoint 恢复训练；作者称主要在 SD1.5 架构上测试过。该项目为香港浸会大学课程 COMP3076 的 LoRA 教学展示开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单节点 LoRATrainer 配置即可启动 LoRA 微调工作流
- 支持 HuggingFace 数据集与自建 ImageFolder 数据集
- 训练权重自动存为 safetensors 并可直接被 LoadLoRA 节点加载
- 脚本修改处以 'SimpleLoRA Added' 注释标注

## 适用场景

- 在 ComfyUI 工作流内对 text-to-image 基础模型做 LoRA 微调
- 用自己的图片和标注文件训练个性化 LoRA
- 课程教学中展示 LoRA 训练流程

## 场景标签

`微调` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: **<u>'ComfyUI_SimpleLoRA'</u>** is a custom node of ComfyUI that enables you to LoRA fine-tune stable diffusion mode
> L5: To be more specific, the node starts a text-to-image LoRA fine-tuning script (`lora_core.py`) modified from the exam

## 星数曲线

```mermaid
xychart-beta
    title "sifengshang/ComfyUI_SimpleLoRA 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `6b5e8fd9f896` · [字段定义](../../DATASET.md)*
