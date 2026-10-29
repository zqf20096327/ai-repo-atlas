# kyegomez/Finetuning-Suite

⭐ 59 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/Finetuning-Suite) · [官网](https://finetuning-suite.readthedocs.io/en/latest/) · 个人维护

**模型微调工具包：用 QLoRA/LoRA/PEFT 快速微调 HF 模型**

Python 微调工具包（ft-suite）：基于 QLoRA、BitsAndBytes、LoRA、PEFT 对 Hugging Face 模型做微调与量化，提供 FineTuner 类微调接口及 Inference、GPTQInference 推理类；README 列出与 LLAMA、Falcon 等模型配合使用，文档以示例代码为主，Roadmap 中多项功能（更多示例脚本、GUI、更多任务类型）尚未实现，安装方式为 pip 安装。面向需要快速微调开源大模型的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 QLoRA/LoRA/PEFT/BNB 的微调流程封装
- 提供微调与推理（含 GPTQ 量化推理）的 Python API
- pip install ft-suite 一行安装

## 适用场景

- 用 LoRA/QLoRA 快速微调 Hugging Face 上的开源模型
- 对微调后模型做常规或 GPTQ 量化推理

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: Finetune any model with unparalled performance, speed, and reliability using Qlora, BNB, Lora, Peft in less than 30 
> L20: ```python

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/Finetuning-Suite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-29 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b93fe9a6218f` · [字段定义](../../DATASET.md)*
