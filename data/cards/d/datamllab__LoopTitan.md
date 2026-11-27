# datamllab/LoopTitan

⭐ 35 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/datamllab/LoopTitan) · [官网](https://datamllab.github.io/LoopTitan/) · 组织维护

**looped MoE 语言模型的 PyTorch 开源研究基础设施与论文模型库**

为 looped mixture-of-experts 语言模型研究提供统一 PyTorch 实现：九类机制均为同一模型的配置字段，38 种配置以 recipe 形式声明谱系；训练前可在 CPU 上一条命令估算参数量、FLOPs 与 KV cache 并按 5% 容差匹配预算；与 Transformers Qwen3-MoE 做 30 项数值核对，支持两个已发布 looped 检查点转换。训练基于 TorchTitan（AdamW/Muon），导出为独立 Hugging Face 模型，并附带四赛道基准、研究记录协议与 17 个模型。训练需 CUDA，推理与对比可在 CPU 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 九类 looped MoE 机制收敛为单一可读 PyTorch 模型的配置字段，配置间以 lineage 声明父子关系
- 训练前 CPU 估算 unique 参数、训练 FLOPs 与 KV cache，三者在 5% 内视为预算匹配
- 与 Transformers Qwen3-MoE 在 logits、梯度、optimizer steps 与 cache 上做 30 项核对，两个已发布检查点可转换
- 研究以 issue 声明设计、外部队结果经 bench workflow 检查后并入公开记录

## 适用场景

- 在同一预算下对比不同 looped MoE 设计
- 复现或扩展论文中的 Phase 1 逐变更实验
- 将已发布的 looped 检查点导出为 Hugging Face 模型
- 通过四赛道基准提交并记录自己的研究结果

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L10:  Open PyTorch infrastructure for looped mixture-of-experts (MoE) language models.
> L118: Training runs on TorchTitan with AdamW or Muon. Initial weights, data order and validation samples do not depend o
> L148: Test bits per byte (BPB) after 5.0B tokens of DCLM (4,769 updates of 1,048,576 tokens, seed 42); lower is better. 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `e4497ed985ff` · [字段定义](../../DATASET.md)*
