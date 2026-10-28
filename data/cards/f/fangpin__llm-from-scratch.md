# fangpin/llm-from-scratch

⭐ 135 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/fangpin/llm-from-scratch) · [官网](https://fangpin.github.io/llm-from-scratch/) · 个人维护 · 中文 README

**从零实现 LLM 的教育性 PyTorch 项目：含训练/微调全流程**

面向教学用途，用 PyTorch 从零实现 decoder-only Transformer 的全部组件：多头注意力、RoPE、RMSNorm、SwiGLU、自实现 AdamW 与 BPE 分词器，另含 Triton 版 Flash Attention 2、DDP 与分片优化器的并行训练、数据清洗管线（去重/PII 掩码/质量过滤）以及 Qwen2.5-Math-1.5B 上的 SFT 与 RLFT 完整示例（gsm8k 零样本准确率 1.56%→62.9%）。通过 uv run 命令运行训练与生成脚本，配套 Sphinx 文档可构建 PDF/EPUB 书籍。

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

- Transformer 各组件（注意力/RoPE/RMSNorm/SwiGLU/优化器）从零实现
- Triton 版 Flash Attention 2 与基准测试套件
- DDP 与参数分片优化器支持多 GPU 训练
- Qwen2.5-Math-1.5B 上 gsm8k 的完整 SFT/RLFT 示例

## 适用场景

- 逐组件学习现代 LLM 的实现原理
- 在自己语料上训练 BPE 分词器与小型语言模型
- 实践分布式训练与 SFT/RLFT 微调流程

## 场景标签

`教程课程` `微调` · 领域:学习与行业

## 证据(README 行号)

> L5: This repository contains a from-scratch implementation of a modern decoder-only Transformer model in PyTorch, built 
> L35: * **From-Scratch Implementation:** Every component of the Transformer model is implemented from scratch using PyTor

## 星数曲线

```mermaid
xychart-beta
    title "fangpin/llm-from-scratch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 132 --> 136
    line [133, 135, 135]
```

2026-10-18 133 → 2026-10-28 135（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4f2ca6e9efaa` · [字段定义](../../DATASET.md)*
