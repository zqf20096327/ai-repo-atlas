# duguying/100M

⭐ 52 · Python · 推送 2026-05-08 · [GitHub](https://github.com/duguying/100M) · [官网](https://tinyllm.duguying.net) · 个人维护 · 中文 README

**在 Mac 上从零训练 0.1B 中文大模型的 Web 工作台**

面向 Apple Silicon（M 系列）MacBook 的端到端大模型训练工作台：通过 FastAPI + React Web UI 完成数据源采集、32k byte-level BPE tokenizer 构建、数据集准备、预训练、SFT、DPO 及推理流式 chat CLI 全流程。模型为类 LLaMA 架构（RoPE + RMSNorm + SwiGLU + GQA，约 96M 参数），依赖 PyTorch ≥ 2.5 MPS 后端，支持 --resume 断点续训；附带 ngrok 隧道将 Web UI 暴露到公网（无内置鉴权，README 明确提示安全风险）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Web UI 一站式覆盖数据采集→Tokenizer→数据集→训练
- 类 LLaMA 架构实现（约 96M 参数，GQA/RoPE/SwiGLU）
- 支持 pretrain、SFT、DPO 三种训练阶段与中断续训
- 基于 ngrok SDK 的公网隧道访问（附二维码与安全提醒）

## 适用场景

- 在自己的 MacBook 上从零跑通一个小型中文大模型的完整训练流程
- 学习 LLaMA 类架构、BPE tokenizer 与 SFT/DPO 的工程实现
- 通过公网隧道与他人共享训练工作台进行协作演示

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: 在 Apple Silicon（M 系列）MacBook 上从零训练一个 ~0.1B 参数、类 LLaMA 架构（RoPE + RMSNorm + SwiGLU + GQA）的中文大模型，全程在一个 Web UI 里完成：
> L5: - **Tiny LLM Studio**（FastAPI + React Web UI）：数据源 → 采集任务 → Tokenizer → 数据集 → 训练，一站式

## 星数曲线

```mermaid
xychart-beta
    title "duguying/100M 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 50 --> 53
    line [51, 52, 52]
```

2026-10-18 51 → 2026-10-28 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7c21d03b19b5` · [字段定义](../../DATASET.md)*
