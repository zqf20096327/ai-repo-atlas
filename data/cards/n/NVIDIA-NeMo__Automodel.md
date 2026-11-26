# NVIDIA-NeMo/Automodel

⭐ 1,102 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/NVIDIA-NeMo/Automodel) · [官网](https://docs.nvidia.com/nemo/automodel/nightly) · 组织维护

**面向 LLM/VLM 的 PyTorch 分布式微调训练库**

NVIDIA 维护的 PyTorch 原生分布式训练库，为大型语言与视觉语言模型提供 SFT、LoRA、RL 与投机解码训练器（drafter）训练支持，开箱支持 Hugging Face 格式模型。通过 FSDP2、专家/流水线/上下文并行等并行策略在多 GPU/多节点上运行，以 recipe 形式给出各模型的训练配置，并提供文档、示例与模型覆盖页。需要 NVIDIA GPU 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 SFT、LoRA 与 RL（REINFORCE-Zero 等路线）训练能力
- 支持 FSDP2 与专家/流水线/上下文并行
- 开箱支持 Hugging Face 格式模型并提供各模型 recipe
- 支持 EAGLE、DFlash 等投机解码 drafter 的端到端训练

## 适用场景

- 在多 GPU 集群上对 LLM/VLM 做全参数或 LoRA 微调
- 按现成 recipe 复现特定模型的训练配置
- 训练投机解码 drafter 并导出到推理布局

## 场景标签

`微调` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L1: # 🚀 NeMo AutoModel
> L9: 📖 Documentation • 🔥 Ready-to-Use Recipes • 💡 Examples • Model Coverage • Performance • 🤝 Contributing
> L64: - [04/25/2026]**DeepSeek V4 Flash** We now support finetuning `deepseek-ai/DeepSeek-V4-Flash`, thanks to @Khazic. C

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA-NeMo/Automodel 星数(近 24 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 1041 --> 1107
    line [1046, 1047, 1048, 1055, 1058, 1060, 1061, 1063, 1064, 1047, 1079, 1080, 1082, 1081, 1082, 1083, 1084, 1087, 1092, 1096, 1097, 1099, 1100, 1102]
```

2026-10-24 1,046 → 2026-11-26 1,102（+56）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `57745f074a41` · [字段定义](../../DATASET.md)*
