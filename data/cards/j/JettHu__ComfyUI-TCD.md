# JettHu/ComfyUI-TCD

⭐ 140 · Python · Apache-2.0 · 推送 2026-01-06 · [GitHub](https://github.com/JettHu/ComfyUI-TCD) · 个人维护 · 中文 README

**ComfyUI 的 TCD 采样器自定义节点，实现少步数图像生成**

将 TCD 论文中的 TCD Sampler 实现为 ComfyUI 自定义节点：TCD 是一种受 Consistency Models 启发的蒸馏技术，把预训练扩散模型的知识蒸馏到少步采样器中，并允许通过参数调节采样随机性以控制细节丰富度。提供 TCD Model Sampling Discrete 节点，参数与 KSampler 对齐（steps/scheduler/denoise/eta 等），scheduler 仅保留 simple 与 sgm_uniform 两种；README 附带示例工作流、与 LCM 的对比图，并列出可用的 TCD 与 Hyper-SD LoRA 文件。通过 git clone 或 ComfyUI-Manager 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TCD Sampler 的 ComfyUI 自定义节点实现（对应 TCD 论文）
- eta 参数控制采样随机性（论文中的 gamma），调节细节丰富度
- 提供示例工作流与 TCD/LCM 对比结果
- 列出 TCD-SD15/SDXL 及 Hyper-SD 等 LoRA 文件

## 适用场景

- 在 ComfyUI 中用少步数采样生成图像
- 配合 TCD/Hyper-SD LoRA 加速 SD1.5/SDXL 出图
- 调节 eta 在确定性与随机采样之间控制细节

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L7: This repository is the ComfyUI custom node implementation of TCD Sampler mentioned in the TCD paper.
> L9: TCD, inspired by Consistency Models, is a novel distillation technology that enables the distillation of knowledge f

## 星数曲线

```mermaid
xychart-beta
    title "JettHu/ComfyUI-TCD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 139 --> 141
    line [140, 140]
```

2026-10-18 140 → 2026-10-23 140（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8a79f8ae96cb` · [字段定义](../../DATASET.md)*
