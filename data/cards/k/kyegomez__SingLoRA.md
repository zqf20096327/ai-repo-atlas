# kyegomez/SingLoRA

⭐ 47 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/kyegomez/SingLoRA) · [官网](https://discord.gg/jM3Z6M9uMq) · 个人维护

**SingLoRA 论文的单文件最小实现：单矩阵低秩微调**

提供 SingLoRA（Single Matrix Low-Rank Adaptation，Bensaïd 等人论文方法）的最小化单文件实现：用单个可训练矩阵替代 LoRA 的两个矩阵，实现参数高效微调。基于 PyTorch 与 Hugging Face Transformers，通过 apply_singlora_to_model 将模型中的注意力投影层替换为 SingLoRA 层，可配置 rank、alpha、ramp_up_steps 与目标模块，附带 DistilBERT 完整示例与 LLaMA 应用说明，并演示与全量微调的参数量对比。以 pip 包与源码形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 Python 文件的自包含实现，单可训练矩阵替代 LoRA 双矩阵
- 兼容 Hugging Face Transformers 模型，可替换注意力投影层
- 提供 DistilBERT 完整示例与 LLaMA（q_proj/k_proj/v_proj）应用说明
- 输出与全量微调的可训练参数量对比

## 适用场景

- 在自有 transformer 模型上做参数高效微调
- 复现或验证 SingLoRA 论文中的单矩阵低秩适配方法
- 对 LLaMA 类大模型进行低资源占用微调实验

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository provides a minimal, single-file implementation of SingLoRA (Single Matrix Low-Rank Adaptation) as de
> L7: SingLoRA is a parameter-efficient fine-tuning method that simplifies the LoRA architecture by using a single trainab

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/SingLoRA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-26 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a46d01397bef` · [字段定义](../../DATASET.md)*
