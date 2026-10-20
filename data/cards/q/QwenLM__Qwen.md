# QwenLM/Qwen

⭐ 21,927 · Python · Apache-2.0 · 推送 2026-03-05 · [GitHub](https://github.com/QwenLM/Qwen) · 组织维护 · 中文 README

**阿里云开源的通义千问大语言模型官方仓库**

Qwen（通义千问）系列的官方仓库，收录 1.8B/7B/14B/72B 四个规模的基础模型与 Chat 对话模型，提供权重下载链接（Hugging Face、ModelScope）。内容覆盖：Transformers/ModelScope 推理示例、GPTQ 与 KV cache 量化、全参数/LoRA/Q-LoRA 微调教程、vLLM 与 FastChat 部署、WebUI/CLI demo、DashScope API 与 OpenAI 风格 API 搭建、工具调用/Agent/代码解释器用法。注意仓库声明不再积极维护，后续跟进指向 QwenLM/Qwen2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`declining` — 距上次 push 226.8 天,年发版 0,31 位贡献者
- 涨星:近 1 天 **+5**(自 20261016 起算)
- 安装:pypi 包 `csrc` 月下载无数据
- 平台:— · 协议:OPENAI-API

## 能力要点

- 提供 1.8B 至 72B 四种规模的基础模型与 Chat 模型
- 量化模型（Int4/Int8、GPTQ、KV cache 量化）降低推理显存需求
- 微调教程覆盖全参数、LoRA、Q-LoRA
- 支持工具调用、Agent 与代码解释器用法

## 适用场景

- 下载并本地推理通义千问系列模型
- 对模型做 LoRA/Q-LoRA 微调
- 通过 vLLM/FastChat 部署为 API 服务
- 用 DashScope 云端 API 直接调用 Qwen

## 场景标签

`微调` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L19: We opensource our **Qwen** series, now including **Qwen**, the base language models, namely **Qwen-1.8B**, **Qwen-7
> L21: In brief, we have strong base language models, which have been stably pretrained for up to 3 trillion tokens of mul

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `a7a5ac9f8d66` · [字段定义](../../DATASET.md)*
