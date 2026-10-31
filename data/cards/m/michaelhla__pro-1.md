# michaelhla/pro-1

⭐ 103 · Python · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/michaelhla/pro-1) · [官网](https://michaelhla.com/blog/pro1.html) · 个人维护

**GRPO 训练的蛋白质稳定性改造推理模型**

Pro-1 是以 GRPO 强化学习方法、面向 Rosetta REF2015 物理能量奖励函数训练的推理模型（8b/70b 适配器权重）。输入蛋白质序列、文本描述及既往工程改造效果，模型推理后提出提升序列稳定性的修改建议。主要在酶序列上训练，作者称应适用于任意蛋白质序列。运行需要 NVIDIA GPU 实例（A100 80GB 最佳，可用更小 GPU）、60-200GB 存储，通过克隆仓库、setup.sh 与 hf_download.sh 安装运行；可选接入 OpenAI API 作为 LM 序列应用器。作者声明为预览版，输出突变需人工核对、引用可视为幻觉。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- GRPO 强化学习训练，奖励为 Rosetta REF2015 物理能量函数
- 输入序列+描述+既往改造效果，输出稳定性改进建议
- 提供 8b 与 70b 适配器权重下载（默认 8b creativity tuned）
- 可选 LM sequence applier 需设置 OPENAI_API_KEY

## 适用场景

- 对酶或蛋白质序列提出稳定性提升的改造建议
- 结合既往工程改造记录迭代优化蛋白质
- 复现与检验 GRPO 物理奖励训练的推理模型

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L8: Pro-1 is a reasoning model trained using GRPO towards a physics based reward function for protein stability.
> L10: It takes in a protein sequence + text description of the protein + effects of previous engineering attempts, reason

## 星数曲线

```mermaid
xychart-beta
    title "michaelhla/pro-1 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 102 --> 104
    line [103, 103]
```

2026-10-18 103 → 2026-10-31 103（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `150579d587ea` · [字段定义](../../DATASET.md)*
