# robtacconelli/Nacrith-GPU

⭐ 23 · Python · Apache-2.0 · 推送 2026-03-21 · [GitHub](https://github.com/robtacconelli/Nacrith-GPU) · [官网](https://www.nacrith.com/) · 个人维护

**基于 LLM 神经算术编码的无损文本压缩器**

将 SmolLM2-135M 语言模型与算术编码结合的无损压缩系统：LLM 逐 token 预测下一 token 概率分布，送入 2^24 精度 CDF 算术编码器，压缩与解压运行同一模型保证逐字节还原。集成 N-gram（1-4 阶）、上下文混合器、自适应头与置信度跳过的集成预测。v1.1 使用 llama.cpp 推理后端（PyTorch 自动回退）、支持多 GPU worker 并行压缩（最多 8 个，自动按 VRAM 检测），并支持 NC06 混合二进制/文本压缩。限制：压缩速度慢于传统压缩器。基准在 GTX 1050 Ti 上测得。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SmolLM2-135M 逐 token 预测 + 2^24 精度 CDF 算术编码，完全无损
- llama.cpp 推理后端，无 llama-cpp-python/GGUF 时自动回退 PyTorch
- 最多 8 个 GPU worker 并行压缩，按 nvidia-smi 查询 VRAM 自动确定实例数
- NC06 模式对 PDF/可执行文件等二进制数据做文本/二进制分块混合压缩

## 适用场景

- 对英文文本追求高压缩比且要求逐字节还原的场景
- 压缩含嵌入文本的二进制文件（PDF、可执行文件）
- 在有 CUDA GPU 的环境并行压缩大文件

## 场景标签

 · 领域:数据压缩/神经压缩

## 证据(README 行号)

> L9: At its core, Nacrith GPU pairs a small but capable LLM (SmolLM2-135M, 135M parameters) with an arithmetic encoder. T
> L164: **Together**: the LLM provides the probabilities, the arithmetic coder turns them into bits. The better the LLM pr

## 星数曲线

```mermaid
xychart-beta
    title "robtacconelli/Nacrith-GPU 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `711c6117771d` · [字段定义](../../DATASET.md)*
