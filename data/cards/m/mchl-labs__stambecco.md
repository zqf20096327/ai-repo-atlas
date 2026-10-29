# mchl-labs/stambecco

⭐ 19 · Jupyter Notebook · NOASSERTION · 推送 2026-08-07 · [GitHub](https://github.com/mchl-labs/stambecco) · 个人维护

**意大利语指令遵循 LLaMA 模型家族（7B/13B LoRA 适配器）**

基于 Meta LLaMA 7B/13B 的意大利语指令微调模型家族，使用 PEFT/LoRA 方法，训练数据来自两套翻译为意大利语的指令数据集（源自 Alpaca-Data-Cleaned 与 Alpaca GPT-4，经 gpt-3.5-turbo 翻译）。因 LLaMA 基础权重受限，仅发布 LoRA 适配器权重与数据集（Hugging Face）。训练可在 Google Colab 单卡 A100 上数小时内完成，推理通过 Colab 笔记本与 Gradio 界面提供。许可为 CC BY-NC-SA 4.0，仅限学术研究，禁止商用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7B/13B 两个规模的 LoRA 适配器权重
- 配套发布两套意大利语指令微调数据集
- 可在 Google Colab 单卡（建议 A100 40GB）训练
- 提供 Gradio 聊天界面的 Colab 笔记本

## 适用场景

- 意大利语对话与指令遵循研究实验
- 获取意大利语指令微调数据集
- 在 Colab 上复现 LoRA 微调流程

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L9: **Stambecco** is an Italian instruction-following language model family based on Meta's LLaMA architecture. Fine-tun
> L13: Because original LLaMA foundation weights are restricted, we release the trained **PEFT/LoRA adapter weights** ("pa

## 星数曲线

```mermaid
xychart-beta
    title "mchl-labs/stambecco 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `613feacf5660` · [字段定义](../../DATASET.md)*
