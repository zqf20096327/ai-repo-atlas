# ivanfioravanti/wine_variety_classification

⭐ 129 · Python · MIT · 推送 2026-04-21 · [GitHub](https://github.com/ivanfioravanti/wine_variety_classification) · 个人维护

**多 LLM 提供商对比示例：用酒评预测葡萄品种并评测各模型**

示例/实验项目：基于 Hugging Face 葡萄酒评论数据集，用多种 LLM 提供商（Ollama、OpenAI、Gemini、LM Studio、OpenRouter、DeepSeek、Anthropic、MLX 等）根据酒评、产区等特征预测葡萄品种，通过 Structured Output 获取一致响应并对比各模型在意大利/法国葡萄酒上的表现。重点考察本地模型（Ollama+llama.cpp、LM Studio+MLX），另包含 MLX LoRA 微调（Qwen3、Gemma 等）与自主超参搜索流程。以 Jupyter Notebook 与 Python 脚本形式提供，需各云厂商 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 9 类 LLM 提供商（Ollama/OpenAI/Gemini/LM Studio/OpenRouter/DeepSeek/Anthropic/MLX 等）的品种预测实现
- Structured Output 实现与跨模型性能对比图表
- MLX LoRA 微调（Qwen3 0.6B、Gemma 等）与批量推理
- AI agent 自主超参搜索：迭代修改 LoRA 训练配置并记录实验日志

## 适用场景

- 对比不同 LLM 提供商在文本分类任务上的表现
- 学习各提供商 Structured Output 的调用方式
- 在 Apple 芯片上用 MLX 微调并评测本地模型
- 搭建 AI agent 自动调参的 LoRA 训练循环

## 场景标签

`模型评测` `微调` · 领域:评测与运维

## 证据(README 行号)

> L5: This project demonstrates how to use various Large Language Models (LLMs) to predict wine varieties based on wine re
> L27: The project uses a dataset of Italian wines to test different LLMs' ability to predict grape varieties based on win

## 星数曲线

```mermaid
xychart-beta
    title "ivanfioravanti/wine_variety_classification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 128 --> 130
    line [129, 129]
```

2026-10-18 129 → 2026-10-31 129（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5c30ae0c989f` · [字段定义](../../DATASET.md)*
