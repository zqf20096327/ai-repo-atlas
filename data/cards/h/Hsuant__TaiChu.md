# Hsuant/TaiChu

⭐ 15 · Python · NOASSERTION · 推送 2026-06-13 · [GitHub](https://github.com/Hsuant/TaiChu) · [官网](https://blog.devnest.top) · 个人维护 · 中文 README

**从零训练 Decoder-Only Transformer 与 BPE 分词器的全流程工程**

面向学习与构建场景的 LLM 训练工程：不依赖预训练模型，从零实现 BPE 分词器训练、Decoder-Only Transformer（MHA/GQA、RoPE、SwiGLU、RMSNorm、可选 MoE）、预训练与分布式训练（DDP、混合精度、梯度累积），模型规模 50M~1B+ 通过 YAML 配置切换。基于 HuggingFace tokenizers/datasets，提供单元测试与 SwanLab 训练监控（可选）。Agent 扩展（Tool Use/ReAct）处于规划阶段，SFT 进行中。许可证 CC BY-NC 4.0 禁止商用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 从零实现 BPE 分词器训练与词汇表构建
- Decoder-Only 架构：MHA/GQA、RoPE、SwiGLU、RMSNorm、可选 MoE
- 预训练支持 DDP 分布式、混合精度、梯度累积、Checkpoint 管理
- 50M~1B+ 模型规模经 YAML 配置切换

## 适用场景

- 我想亲手从零训练自己的小规模 LLM 并理解每个组件
- 学习 BPE 分词器训练与 Decoder-Only Transformer 实现
- 在多卡环境跑通预训练全流程并可视化训练过程

## 场景标签

`模型训练` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: > **从零实现 Decoder-Only Transformer，构建专属于自己的 LLM**
> L21: - **模型怎么训？** —— 从数据加载到分布式训练全链路打通
> L87: python -m trainer.train_pretrain --model_config configs/TaiChu_LLM.yaml --pretrain_config configs/train_pretrain_co

## 星数曲线

```mermaid
xychart-beta
    title "Hsuant/TaiChu 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `1fd7314c484b` · [字段定义](../../DATASET.md)*
