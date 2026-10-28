# gaosh/ToMoE

⭐ 42 · Python · Apache-2.0 · 推送 2026-08-27 · [GitHub](https://github.com/gaosh/ToMoE) · 个人维护

**科研代码：通过动态结构剪枝把稠密 LLaMA 转为 MoE 模型**

TMLR 论文 ToMoE 的官方实现，提供两条流水线：Pipeline A 训练超网络学习动态结构剪枝，将稠密 LLaMA 检查点转换为剪枝后的 MoE 检查点；Pipeline B 增加门控注意力 upcycling、导出显式 Hugging Face MoE 模型、token 打包数据准备与八卡 FSDP 持续预训练，并支持可选的 Tulu 3 监督微调与 grouped-GEMM 专家执行。环境面向 Linux、CUDA 12.8、Python 3.11、PyTorch 2.7.1，使用 gated Llama 3 需接受许可并通过 Hugging Face 认证。供需要复现论文或做稠密模型转 MoE 研究的科研人员使用。

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

- 超网络训练+动态结构剪枝，将稠密 LLaMA 转换为 MoE 检查点
- Pipeline B 支持门控注意力 upcycling 与显式 Hugging Face MoE 导出（Llama 3 8B → 约 3.5B 激活/20B 总参数）
- 八 GPU FSDP、BF16、8-bit Adam 的持续预训练与 token 打包数据管线
- 可选 Tulu 3 SFT 与 grouped-GEMM 专家执行

## 适用场景

- 复现论文中稠密 LLM 到 MoE 的转换流程
- 对自有 LLaMA 检查点做结构剪枝与 MoE 化实验
- 导出 MoE 模型后做持续预训练与监督微调

## 场景标签

`模型训练` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L11: 1. **Pipeline A: Original ToMoE conversion** — train a hypernetwork that learns dynamic structural pruning, then co
> L12: 2. **Pipeline B: Upcycling and continual pretraining** — train ToMoE with gated attention, export an explicit Huggi
> L22: - Gated-attention ToMoE upcycling, validated on Llama 3 8B, resulting in an MoE model with approximately 3.5B activ

## 星数曲线

```mermaid
xychart-beta
    title "gaosh/ToMoE 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-28 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `5f8ffb12a9e2` · [字段定义](../../DATASET.md)*
