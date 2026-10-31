# weiserlab/TinyLLM

⭐ 72 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/weiserlab/TinyLLM) · [官网](http://tinyllm.org) · 组织维护

**在资源受限设备上训练/微调/部署小规模 LLM 的框架**

面向边缘设备与 IoT 平台的小规模 LLM 训练、微调与部署框架。流程为：用 encode.py 分词自定义 CSV 或 HuggingFace/Fineweb/SHL 数据集，基于 llm.c（GPU）预训练 GPT-2 类模型，导出 HuggingFace 兼容格式后微调（支持 gpt2/llama/phi），再转换为 GGUF 交给 llama.cpp 在嵌入式设备推理，可选量化。演示场景包括手势检测、机器人定位与呼吸检测等嵌入式感知任务。安装需自行配置 llm.c 与 llama.cpp，并安装 PyTorch 与 requirements.txt 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- llm.c 预训练 + Python 微调 + GGUF 导出的完整流程
- 支持自定义 CSV 数据集与 HuggingFace/Fineweb/SHL 数据集
- 面向嵌入式设备，可转换为 GGUF 并量化后由 llama.cpp 推理
- 提供手势检测、定位、呼吸检测三个内置处理数据集

## 适用场景

- 在边缘/IoT 设备上训练并部署小规模 LLM
- 为嵌入式感知任务（手势、定位、呼吸）微调模型
- 将自有 CSV 数据集训练为可在嵌入式设备运行的模型

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L2: *A Framework for Training, Fine-Tuning, and Deploying Smaller LLMs on Custom Datasets*
> L8: TinyLLM is a lightweight and customizable framework for efficiently training, fine-tuning, and deploying small-scale
> L10: TinyLLM demonstrates adaptability across various datasets, particularly in embedded sensing tasks like hand gesture


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `51720ce16fae` · [字段定义](../../DATASET.md)*
