# SmallDoges/small-doge

⭐ 200 · Python · Apache-2.0 · 推送 2026-01-06 · [GitHub](https://github.com/SmallDoges/small-doge) · [官网](https://huggingface.co/SmallDoge) · 组织维护 · 中文 README

**超快小型语言模型家族：20M-320M，支持训练到部署全流程**

提供 20M/60M/160M/320M 四档参数规模的 decoder 语言模型及 Instruct 变体，采用 Dynamic Mask Attention 与 Cross Domain MoE 架构，WSD 调度器支持断点续训。覆盖三阶段训练流水线（预训练→指令微调→推理微调），附数据处理器、评测工具包、内置聊天 Web 界面与 OpenAI 兼容 API。模型可通过 transformers AutoModelForCausalLM 加载，CPU 即可推理（i7-11 上 20M 达 142 tok/s）。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20M-320M 四档模型，提供 Instruct/checkpoint 变体
- Dynamic Mask Attention + Cross Domain MoE 架构
- 三阶段训练流水线与 WSD 断点续训
- 内置聊天 Web 界面与 OpenAI 兼容 API

## 适用场景

- 在资源受限设备或 CPU 上运行语言模型
- 快速实验与原型验证小模型训练流程
- 学习 AI/ML 时用可管理规模的模型上手

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L13: SmallDoge is a family of dynamic, ultra-fast small language models designed for **efficiency** and **accessibility*
> L39: from transformers import AutoTokenizer, AutoModelForCausalLM

## 星数曲线

```mermaid
xychart-beta
    title "SmallDoges/small-doge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 199 --> 202
    line [201, 200, 200]
```

2026-10-18 201 → 2026-10-31 200（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `8e7b09cf3b88` · [字段定义](../../DATASET.md)*
