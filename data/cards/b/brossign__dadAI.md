# brossign/dadAI

⭐ 43 · Python · MIT · 推送 2026-02-15 · [GitHub](https://github.com/brossign/dadAI) · 个人维护

**面向新手爸爸的本地微调育儿 AI 助手（Qwen 14B + RAG）**

个人开发者构建的开源育儿助手：以 Qwen2.5-14B-Instruct（4-bit MLX）为基座，用 2,260 条真实 Reddit 父母问答对做 QLoRA 微调塑造语气，再用 ChromaDB + 交叉编码器重排器的两阶段 RAG 从 4 本育儿书中检索知识，通过 Gradio 聊天界面流式输出，支持 3 轮对话记忆。限定 macOS Apple Silicon（M1-M4，16GB 内存起步）本地运行，约 2.5 小时可在 M1 上完成训练；线上 HF Spaces 演示用的是标准 Mistral 模型加提示词，非微调版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Qwen2.5-14B QLoRA 微调（mlx-lm，Apple Silicon 本地训练约 2.5 小时）
- 两阶段 RAG：ChromaDB 向量检索 Top-5 + 交叉编码器重排器，覆盖 4 本书 1,637 段落
- Gradio 流式聊天界面，3 轮对话记忆，LoRA 融合权重快速推理
- 提供从数据采集到训练、融合、RAG 构建的完整复现流程

## 适用场景

- 新手爸爸在孕期和育儿早期获得情感支持与实用建议
- 在 Mac 上本地运行带书源知识的育儿问答助手
- 作为 QLoRA + RAG 组合的微调学习参考项目

## 场景标签

`AI 助手` `微调` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L3: **DadAI** is an open-source AI built to support new fathers during pregnancy and early parenthood.
> L76: |**Model**|Mistral 7B (4-bit)|**Qwen2.5-14B-Instruct (4-bit)**|
> L87: - **Model:** Qwen2.5-14B-Instruct (4-bit MLX) — ~8.3 GB on disk

## 星数曲线

```mermaid
xychart-beta
    title "brossign/dadAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-30 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f87e9402c238` · [字段定义](../../DATASET.md)*
