# X-GenGroup/Flow-Factory

⭐ 754 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/X-GenGroup/Flow-Factory) · 组织维护 · 中文 README

**扩散与流匹配模型的统一微调/在线 RL 训练框架**

提供统一配置界面对扩散与流匹配模型做离线微调与在线强化学习训练：19 个模型适配器覆盖文生图、图像编辑、文/图生视频及音视频联合生成，注册 16 种训练算法（SFT、DPO、GRPO、蒸馏等），支持全量权重或 LoRA、DDP/DeepSpeed ZeRO-2/FSDP2 后端及 TP/SP/CP 并行布局。通过 ff-train 命令启动训练，ff-prompt-enhance 可用模型的提示改写器预处理数据集。要求 Python 3.11+ 与 PyTorch 2.10+，训练依赖 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 19 个模型适配器与 16 种训练算法在统一接口下解耦
- 支持 FSDP2 与 TP/SP/CP 组合并行布局，提供 4/8-GPU 快速配置
- 异步奖励/优化重叠、EMA 状态与固定拓扑断点续训
- 支持 wandb/swanlab/tensorboard 在线记录训练样本与指标曲线

## 适用场景

- 用 GRPO + LoRA 微调 FLUX、Qwen-Image 等文生图模型
- 以 SFT/离线 DPO 在演示与偏好数据上微调视频生成模型
- 配置多卡 FSDP2/TP/CP 布局进行大模型并行训练

## 场景标签

`微调` `强化学习` `图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L5:  Unified Online RL and Offline Fine-Tuning for Diffusion and Flow-Matching Models
> L9: Train image, editing, video and joint audio-video models through one configuration interface.
> L16: |Algorithm|16 registered trainers, including SFT, DPO, GRPO/Guard, DPPO, NFT and multi-role distillation|Algorithm 

## 星数曲线

```mermaid
xychart-beta
    title "X-GenGroup/Flow-Factory 星数(近 18 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-26", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-24"]
    y-axis "stars" 731 --> 756
    line [733, 734, 735, 737, 739, 740, 742, 734, 747, 749, 750, 751, 752, 753, 752, 753, 754, 754]
```

2026-10-22 733 → 2026-11-24 754（+21）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `7e10aa2275e8` · [字段定义](../../DATASET.md)*
