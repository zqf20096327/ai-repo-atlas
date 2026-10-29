# Jackohhhh/MedLLM-Finetuning

⭐ 20 · Python · MIT · 推送 2026-04-20 · [GitHub](https://github.com/Jackohhhh/MedLLM-Finetuning) · 个人维护 · 中文 README

**面向开发者的医疗文本二分类 LLM 微调框架**

基于 Hugging Face Transformers、PEFT 与 DeepSpeed 构建的微调框架，用于医疗文本二分类任务。支持 QLoRA（4bit）、LoRA（bf16 基座）与全量微调三种模式，通过 YAML/JSON 配置文件管理超参，代码与参数解耦。训练数据为 JSON 格式（input 文本 + 0/1 标签）。要求 Python≥3.10、Linux 与 NVIDIA GPU；集成 DeepSpeed ZeRO 支持多卡训练，7B/8B 模型 QLoRA 模式约 10GB 显存起。提供训练、评估脚本与检查点/预测结果输出结构。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QLoRA/LoRA/全量微调三种模式
- DeepSpeed ZeRO 多卡优化
- YAML 配置驱动的超参管理
- 兼容通用与医疗大模型（Hub ID 或本地权重）

## 适用场景

- 在消费级 GPU 上对 7B/8B 医疗模型做二分类微调
- 训练预测患者疾病风险等二分类任务
- 以配置文件复现和调整微调实验

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: 基于 **Hugging Face Transformers**、**PEFT** 与 **DeepSpeed** 的医疗文本二分类微调框架。
> L8: * **多模式支持：** 兼容 QLoRA（4bit + LoRA）、LoRA（bf16 全精度基座）与全量微调。
> L5: 本项目提供了一套开箱即用的微调流程，旨在降低医疗大语言模型（LLM）的训练门槛，提供高效、灵活的训练体验。

## 星数曲线

```mermaid
xychart-beta
    title "Jackohhhh/MedLLM-Finetuning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `507b7d92b6ba` · [字段定义](../../DATASET.md)*
