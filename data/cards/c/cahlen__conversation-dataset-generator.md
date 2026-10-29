# cahlen/conversation-dataset-generator

⭐ 18 · Python · MIT · 推送 2026-05-01 · [GitHub](https://github.com/cahlen/conversation-dataset-generator) · [官网](https://cahlen.github.io/conversation-dataset-generator/) · 个人维护

**为 LLM 微调生成多角色对话数据集的 Python 工具**

通过 LLM 生成 ShareGPT 格式的合成对话数据集，供微调使用。支持手动指定话题/人设/风格、创意简报自动生成参数、固定人设话题变化、角色池随机配对、3 人以上多人对话，并可续写已有对话。可用 web 搜索丰富人设背景，支持余弦相似度去重、角色到 human/gpt 的可配置映射，以及 HuggingFace Hub 上传。默认后端为本地 transformers（需 NVIDIA GPU 与 CUDA），也可切换到任意 OpenAI 兼容服务器（LM Studio、Ollama、vLLM 等）。提供 CLI、批量 YAML 配置、Gradio 网页界面与 Docker 支持，另含数据集质量评估脚本（Distinct-N、Vendi Score 等指标）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种生成模式：手动、创意简报、固定人设变化、角色池随机配对
- 多说话人（3+）对话与可配置 human/gpt 角色映射
- 支持本地 transformers 与 OpenAI 兼容服务器双后端
- 内置数据集评估指标（Distinct-N、话题多样性、Vendi Score 等）

## 适用场景

- 为角色扮演或对话模型制备微调数据集
- 批量生成多样化合成对话并控制去重阈值
- 无本地 GPU 时通过 Ollama/LM Studio 等服务器生成数据

## 场景标签

 · 领域:LLM 训练数据/合成数据

## 证据(README 行号)

> L3: Generate synthetic conversational datasets in ShareGPT format for LLM fine-tuning. Define personas, topics, and styl
> L234: |`--backend {hf,openai}`|`hf`|Inference backend: local transformers (`hf`) or OpenAI-compatible HTTP server (`open

## 星数曲线

```mermaid
xychart-beta
    title "cahlen/conversation-dataset-generator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8c01c0000057` · [字段定义](../../DATASET.md)*
