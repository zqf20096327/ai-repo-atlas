# mozihe/moxin

⭐ 14 · Python · MIT · 推送 2026-03-20 · [GitHub](https://github.com/mozihe/moxin) · 个人维护 · 中文 README

**从零实现的中文 LLM/VLM/VLA 模型项目，含完整训练流程**

基于 PyTorch 原生实现（不依赖第三方训练框架）的中文语言模型项目：从 BPE Tokenizer 训练、约 270M 参数的 Dense+MoE 混合架构预训练、两阶段 SFT、基于 forward hook 的 LoRA 微调，到冻结 CLIP ViT-B/16 的视觉语言模型（图文对话），再扩展为 π₀ 风格 Flow Matching 的 VLA 模型实现机器人操控。模型权重托管于 HuggingFace，提供 Flask+SSE 流式 WebUI 与多组评测脚本。限制：C-Eval 总体准确率 24.2%，LIBERO-Spatial 成功率 70%，VLA 训练使用 1× A100。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tokenizer/预训练/SFT/LoRA/VLM/VLA 全流程从零实现，仅依赖 PyTorch
- Dense+MoE 混合架构（2 Dense + 10 MoE Block，4 专家激活 2）
- VLA 采用 π₀ 风格 Flow Matching + Action Expert，LIBERO-Spatial 成功率 70%
- 提供 Flask+SSE 流式 WebUI，支持 LLM 对话与 VLM 看图

## 适用场景

- 学习从 Tokenizer 到 VLA 的完整模型训练实现细节
- 复现或修改 MoE 架构的中文小型 LLM 训练流程
- 作为 VLA 机器人操控任务的端到端训练与评测基线

## 场景标签

`模型训练` `微调` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L14: MoXin（墨心）是一个完全从零构建的中文语言模型项目，覆盖从 Tokenizer 训练、语言模型预训练、多阶段 SFT、LoRA 微调到多模态视觉语言扩展的完整流程，并进一步扩展至视觉语言动作（VLA）模型，实现端到端的机器人操
> L18: - **从零构建** — Tokenizer、模型架构、训练管线全部从头实现
> L21: - **视觉语言动作（VLA）** — π₀ 风格 Flow Matching + Action Expert，端到端机器人控制

## 星数曲线

```mermaid
xychart-beta
    title "mozihe/moxin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `fdbfeabeb409` · [字段定义](../../DATASET.md)*
