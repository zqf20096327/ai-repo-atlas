# hpcaitech/ColossalAI

⭐ 41,431 · Python · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/hpcaitech/ColossalAI) · [官网](https://www.colossalai.org) · 组织维护 · 中文 README

**面向开发者的大模型分布式训练与推理加速系统**

分布式深度学习训练与推理框架：提供数据并行、流水线并行、1D/2D/2.5D/3D 张量并行、序列并行、ZeRO、自动并行等并行策略，以及异构内存管理（PatrickStar）；支持通过配置文件声明并行方式，用少量代码启动分布式训练与推理。附带应用示例（Open-Sora 视频生成、Colossal-LLaMA-2、ColossalChat RLHF 流水线、Stable Diffusion 加速、AlphaFold 加速）和 LLaMA3/2/1、MoE、GPT、BERT 等训练 demo，并提供文档、示例与论坛。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 2.8 天,年发版 0,190 位贡献者
- 涨星:近 1 天 **+1**(自 20261016 起算)
- 安装:pypi 包 `colossalai` 月下载 12,511
- 平台:WINDOWS · 协议:—

## 能力要点

- 多种并行策略：数据/流水线/1D-2D-2.5D-3D 张量/序列并行/ZeRO/自动并行
- 异构内存管理（PatrickStar）与配置文件驱动的并行声明
- 附带 ColossalChat 完整 RLHF 流水线与 Open-Sora 视频生成应用
- 提供 LLaMA、GPT、BERT、MoE、AlphaFold 等训练示例

## 适用场景

- 在多卡/多机环境训练大语言模型并选择并行策略
- 微调 LLaMA 类模型或跑 RLHF 训练流程
- 加速 Stable Diffusion、AlphaFold 等模型的训练与推理
- 在消费级 GPU 上以低显存做小规模训练 demo

## 场景标签

`模型训练` `微调` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L93: Colossal-AI provides a collection of parallel components for you. We aim to support you to write your
> L95: distributed training and inference in a few lines.
> L97: - Parallelism strategies

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `f53e1d19ecde` · [字段定义](../../DATASET.md)*
