# bqpro1/TheSystem

⭐ 6 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/bqpro1/TheSystem) · 个人维护

**单个 LLM 内用门控在选项决策与文本生成两模式间切换的模型**

TheSystem 基于 Qwen3.5-9B 冻结骨干，训练一个 <FAST> 门控按 prompt 在两种模式间路由：decision 模式从给定选项中选取答案（可用 256 单元隐藏层探针分类器或 LoRA 调整读取冻结内部状态），generation 模式走原始输出头。提供 Probe-256 与 LoRA 两个版本，经 Google Colab 笔记本运行，权重与数据集发布在 Hugging Face，测试时关闭 Qwen 原生 thinking 模式。代码与权重以 Apache 2.0 发布，作者为个人研究者，并附五个基准上的评估结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个 prompt 一次路由的 <FAST> 门控，可在 auto/decision/generation 间选择
- 两种决策架构：Probe-256 探针分类器与 LoRA 调整，骨干权重保持冻结
- 提供 Probe-256 与 LoRA 两个 Colab 笔记本及验证笔记本
- 在 VitaminC、PAWS、SQuAD2 等 5 个基准上报告决策准确率

## 适用场景

- 给定一组选项时让模型从中选择而非自由生成
- 研究单模型内决策与生成双目标的训练方式
- 在 Colab 上复现评估与路由/写作保持性验证

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L14: TheSystem runs on Qwen3.5-9B and uses a learned **`<FAST>`** gate to choose between these two modes.
> L63: I built **TheSystem**, whose learned internal gate, **`<FAST>`**, chooses once per prompt
> L64: between selecting a supplied answer and using the model’s original text-generation path.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `244edf39fe2e` · [字段定义](../../DATASET.md)*
