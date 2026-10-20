# deepseek-ai/DeepSeek-Coder

⭐ 24,292 · Python · MIT · 推送 2025-11-11 · [GitHub](https://github.com/deepseek-ai/DeepSeek-Coder) · [官网](https://chat.deepseek.com/) · 组织维护 · 中文 README

**面向开发者的开源代码大模型系列（1B-33B）**

DeepSeek Coder 是一系列从零训练的代码语言模型，训练语料 2T tokens，其中 87% 为代码、13% 为中英文自然语言。模型提供 1B、5.7B、6.7B、33B 多个规模，采用 16K 窗口与 fill-in-the-blank 任务训练，支持项目级代码补全与填充。提供 Base 与指令微调的 Instruct 两类模型，附 Hugging Face transformers 推理示例、vLLM 高吞吐推理路径、微调脚本及 llama.cpp/GPTQ 量化问答。代码仓库为 MIT 许可，模型使用另有 Model License，声明支持商业使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`declining` — 距上次 push 341.1 天,年发版 0,15 位贡献者
- 涨星:近 1 天 **-1**(自 20261016 起算)
- 安装:pypi 包 `finetune` 月下载 181

## 能力要点

- 1B/5.7B/6.7B/33B 多规模模型，87% 代码 + 13% 中英文语料从零训练
- 16K 窗口与 fill-in-the-blank 任务支持项目级代码补全与填充
- 提供 finetune_deepseekcoder.py 微调脚本，支持 DeepSpeed 训练
- 支持 vLLM 高吞吐推理及 GGUM/GPTQ 量化路径

## 适用场景

- 在 IDE 或工作流中做项目级代码补全与插入
- 下载 Instruct 模型搭建代码问答助手
- 在下游任务上微调自己的代码模型
- 通过 vLLM 部署高吞吐推理服务

## 场景标签

`代码生成` `微调` · 领域:编码与开发

## 证据(README 行号)

> L11: DeepSeek Coder is composed of a series of code language models, each trained from scratch on 2T tokens, with a comp
> L17: - **Highly Flexible & Scalable**: Offered in model sizes of 1B, 5.7B, 6.7B and 33B, enabling users to choose the se
> L167: ### Inference with vLLM

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `7bdf7cc487f2` · [字段定义](../../DATASET.md)*
