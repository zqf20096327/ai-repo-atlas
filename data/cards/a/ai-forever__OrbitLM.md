# ai-forever/OrbitLM

⭐ 34 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/ai-forever/OrbitLM) · [官网](https://huggingface.co/ai-forever/OrbitLM-1.8B-Thinking) · 组织维护

**1.8B 循环语言模型的完整训练与推理流水线**

OrbitLM-1.8B 是基于 Ouro-1.4B 架构与 Qwen3 分词器的循环语言模型：单个 24 层 Transformer 栈对每个 token 运行四次，由退出门决定停止时机，共 1.86B 参数。仓库提供从预训练（4 阶段）、SFT 到 RL（基于 verl 0.9.1）的完整训练流水线，以及带 budget forcing、FP8 KV 缓存、投机解码的推理脚本；含数据准备、导出、评估与测试脚本。主要面向俄语文本与数学/代码任务，需 Python 3.12+ 与 CUDA GPU 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 循环架构：24 层栈每 token 运行 4 次，退出门输出停止概率
- 完整七阶段流水线：4 级预训练 + SFT + RL（verl）+ 推理
- 推理支持 budget forcing、FP8 KV 缓存与 self-speculative decoding
- 权重发布于 Hugging Face，加载需 trust_remote_code=True

## 适用场景

- 从零复现循环语言模型的预训练到 RL 全流程
- 对俄语提示运行带思考预算控制的推理
- 基于 verl 对数学与代码任务做 RL 训练或从 Qwen3-8B 做蒸馏

## 场景标签

`模型训练` `强化学习` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L11: # OrbitLM-1.8B
> L21: В репозитории лежит полный пайплайн обучения модели с нуля и скрипты инференса с budget forcing,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `1302336e3055` · [字段定义](../../DATASET.md)*
