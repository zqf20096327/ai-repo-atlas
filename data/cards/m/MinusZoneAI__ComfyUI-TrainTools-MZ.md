# MinusZoneAI/ComfyUI-TrainTools-MZ

⭐ 66 · Python · 推送 2026-04-08 · [GitHub](https://github.com/MinusZoneAI/ComfyUI-TrainTools-MZ) · 个人维护 · 中文 README

**在 ComfyUI 中进行 LoRA 微调的自定义节点集**

ComfyUI 自定义节点集合，将 kohya-ss/sd-scripts 训练流程封装为节点：初始化训练工作区（可指定 sd-scripts 分支与下载源）、复制图片与数据集配置、基础与高级训练参数配置、训练主线程（支持加载已有 LoRA 继续训练、按 epoch 生成示例图片）。20240706 起支持混元 LoRA 训练（使用 sd-scripts 的 HunYuanDiT 分支）。安装方式为克隆到 custom_nodes 目录后重启 ComfyUI，训练依赖 sd-scripts 等外部工具。面向使用 ComfyUI 的 Stable Diffusion 用户与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 sd-scripts 的 LoRA 训练流程封装为 ComfyUI 节点
- 工作区初始化节点支持切换 sd-scripts 分支与加速下载源
- 训练主线程支持加载已有 LoRA 继续训练（network_weights）
- 每次保存模型时自动生成并展示示例图片

## 适用场景

- 我想直接在 ComfyUI 工作流里完成 LoRA 训练，不用切到命令行
- 训练过程中想看到每个 epoch 的示例图以判断效果
- 为混元 DiT 模型训练 LoRA

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: 在ComfyUI中进行lora微调的节点,依赖于kohya-ss/sd-scripts等训练工具(Nodes for fine-tuning lora in ComfyUI, dependent on training tools 
> L49: ### MZ_KohyaSSTrain

## 星数曲线

```mermaid
xychart-beta
    title "MinusZoneAI/ComfyUI-TrainTools-MZ 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-27 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c7f45c188168` · [字段定义](../../DATASET.md)*
