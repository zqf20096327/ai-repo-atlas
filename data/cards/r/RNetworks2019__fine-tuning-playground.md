# RNetworks2019/fine-tuning-playground

⭐ 55 · HTML · 推送 2026-10-21 · [GitHub](https://github.com/RNetworks2019/fine-tuning-playground) · 个人维护

**Hugging Face Transformers 微调渐进式教程仓库（脚本+笔记本+笔记）**

以课程式结构组织的微调实践仓库：从 Trainer 高层 API、自定义训练循环、tokenizer 深入解析，到 LoRA/Prefix Tuning 参数高效微调、bitsandbytes 量化微调，再到 BLEU/ROUGE/F1 评测脚本与损失曲线可视化。每个笔记本配有解释决策过程的 markdown 与作者推理日记 THINKING.md；超参数外置到 YAML，提供非英语语料示例与 CPU 兼容示例。依赖在 environment.yml 中固定版本，脚本基于 transformers 4.44 测试。面向已有 PyTorch 基础的开发者与学习者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Trainer 到手写训练循环、tokenizer 细节、LoRA/Prefix Tuning、量化微调的渐进式目录
- 自定义评测脚本计算 BLEU/ROUGE/F1/困惑度并附消融实验
- 每目录含 THINKING.md 记录作者推理与失败实验
- YAML 外置超参数，BERT/RoBERTa/GPT-2 切换改两行

## 适用场景

- 系统学习 Hugging Face 微调从高层 API 到底层细节
- 在 6GB 显存消费级 GPU 上做 LoRA/量化微调练习
- 多语言语料微调时参考 tokenizer 适配与语言特定坑位

## 场景标签

`微调` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L18: This repository is structured as a progressive curriculum, mirroring the way an expert masters their craft:
> L25: - **`03_low_level/`**: A step-by-step reconstruction of a training loop *without* the `Trainer`. Here, you manually
> L29: - **`05_peft/`**: Practical implementations using **LoRA** (Low-Rank Adaptation) and **Prefix Tuning**. We dissect 

## 星数曲线

```mermaid
xychart-beta
    title "RNetworks2019/fine-tuning-playground 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `07a0e2934f8c` · [字段定义](../../DATASET.md)*
