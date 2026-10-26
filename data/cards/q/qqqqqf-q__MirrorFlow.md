# qqqqqf-q/MirrorFlow

⭐ 73 · Python · Apache-2.0 · 推送 2026-03-19 · [GitHub](https://github.com/qqqqqf-q/MirrorFlow) · [官网](https://qqqqqf-q.github.io/MirrorFlow/) · 个人维护 · 中文 README

**对话数据到模型训练的闭环工具链：数字分身+蒸馏**

端到端工具链，覆盖对话数据提取（QQ/TG）、清洗转换、生成可训练样本、经 LlamaFactory 微调/蒸馏，到模型使用与评测。两条主要路线：用个人聊天记录微调的数字分身（还原表达习惯），以及对齐输出结构、拒答习惯、工具调用行为的数据蒸馏。README 展示了基于 Qwen2.5 1.5B + LoRA 的训练结果，部分代码参考 Weclone。教程文档主体放在外部链接中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QQ/TG 聊天数据提取与清洗转换
- LlamaFactory 微调流程与模型测试使用
- 数字分身与数据蒸馏两条训练路线

## 适用场景

- 用自己的聊天记录训练数字分身模型
- 通过蒸馏对齐模型的输出结构与拒答习惯

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L24: MirrorFlow 提供一套端到端工具链：
> L26: **对话数据 -> 清洗/提取 -> 可训练样本 -> 微调/蒸馏 -> 使用与评测**。
> L30: - **数字分身**：用你的聊天记录微调，尽量还原你的表达习惯（请看 Readme 的下端）

## 星数曲线

```mermaid
xychart-beta
    title "qqqqqf-q/MirrorFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 72 --> 74
    line [73, 73]
```

2026-10-18 73 → 2026-10-26 73（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `dee28c98926c` · [字段定义](../../DATASET.md)*
