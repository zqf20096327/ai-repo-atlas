# jina-ai/embedding-inversion-demo

⭐ 61 · Python · Apache-2.0 · 推送 2026-03-07 · [GitHub](https://github.com/jina-ai/embedding-inversion-demo) · [官网](https://embedding-inversion-demo.jina.ai) · 组织维护

**从嵌入向量反推原文的条件掩码扩散模型（研究+训练+Demo）**

Jina AI 的嵌入反演研究项目：给定一条文本嵌入向量，用条件掩码扩散（MDLM + AdaLN-Zero 条件机制）从全掩码序列并行去噪重建原文，无需通过目标编码器反复重嵌入。架构对编码器无关，通过配置文件支持 Qwen3-Embedding-0.6B、jina-embeddings-v3、EmbeddingGemma-300m 等编码器，报告最高 81.3% token 准确率（Qwen3，72.5K 步，A100-40GB 训练）。提供两阶段数据准备脚本、训练与推理代码、FastAPI 交互 Demo 及在线演示，面向嵌入隐私与攻击研究人群。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 并行去噪的嵌入反演，无需自回归重嵌入迭代
- AdaLN-Zero 条件机制使架构对编码器无关
- 两阶段数据管线覆盖 10 语种 C4/mC4 语料
- 提供训练、推理（invert.py）与 FastAPI Demo 全链路

## 适用场景

- 评估文本嵌入的可逆性以做隐私风险研究
- 针对特定嵌入模型训练并复现反演实验
- 通过在线 Demo 直观查看嵌入反演效果

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: Text embeddings are widely assumed to be safe, irreversible representations. This project demonstrates otherwise: gi
> L13: We take a different approach: **embedding inversion as conditional masked diffusion**. Starting from a fully masked
> L82: Opens on port 8080. Live demo: https://embedding-inversion-demo.jina.ai

## 星数曲线

```mermaid
xychart-beta
    title "jina-ai/embedding-inversion-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-26 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `41e33d171d32` · [字段定义](../../DATASET.md)*
