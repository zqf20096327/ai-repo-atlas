# InternLM/InstantFusion

⭐ 22 · Python · 推送 2026-10-12 · [GitHub](https://github.com/InternLM/InstantFusion) · [官网](https://internlm.github.io/InstantFusion/) · 组织维护

**将异构扩散模型潜空间对齐共享以实现跨模型协作的方法实现**

论文 InstantFusion 的官方实现：通过 Sigma 条件化的潜空间对齐编解码器（LAE），把 Qwen-Image、SD3 等扩散模型的潜变量映射到共享潜空间，使去噪轨迹可在模型间交接。仓库提供 LAE 训练、跨模型 OPD 蒸馏训练（以 Qwen-Image 为冻结教师训练 SD3 LoRA）与 LAE 接手推理脚本，依赖 DiffSynth-Studio 环境，训练数据（VisPrompt5M）与模型权重均不随仓库分发。面向 diffusion 研究与实验复现场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LAE 训练：重建/交叉重建/潜对齐/去噪速度对齐四类损失
- 去噪中途跨模型交接：加速、多偏好组合、跨模型 OPD 蒸馏
- 提供 LAE 训练、OPD 训练与推理三套 shell 入口脚本
- 训练好的 checkpoint 发布于 Hugging Face

## 适用场景

- 复现论文中的潜空间对齐与跨模型交接实验
- 把一个扩散模型的去噪轨迹交接到另一个模型继续生成
- 用 Qwen-Image 作冻结教师对 SD3 做策略蒸馏训练

## 场景标签

`图像生成` `微调` · 领域:内容生成

## 证据(README 行号)

> L15: InstantFusion maps the latents of different diffusion models into a shared latent space, so their denoising traject
> L25: This repository includes LAE training, OPD training, and LAE-based model handoff inference.

## 星数曲线

```mermaid
xychart-beta
    title "InternLM/InstantFusion 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-31 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `6da68ab4cd00` · [字段定义](../../DATASET.md)*
