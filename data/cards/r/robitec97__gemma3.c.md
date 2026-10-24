# robitec97/gemma3.c

⭐ 117 · C · 推送 2026-10-07 · [GitHub](https://github.com/robitec97/gemma3.c) · 个人维护

**纯 C11 实现的 Gemma 3 4B 推理引擎，CPU/Apple Metal 运行**

从零用纯 C11 编写的 Gemma 3 4B IT 推理引擎，无 Python、无 ML 框架、零依赖。直接内存映射 Hugging Face 官方 BF16 safetensors 权重，无需转换；实现 grouped-query attention、QK-norm、SentencePiece BPE 分词器（与 HF tokenizers 逐 token 验证一致），logits 与 NumPy 参考实现差异在 1e-4 内。支持 CPU（NEON/AVX2 SIMD、多线程）与 Apple Silicon Metal GPU 后端，多轮对话复用 KV cache。提供 CLI 与 C 库 API（流式回调）。构建需 C 编译器与 make，下载模型需 Python3 与约 9 GB 磁盘、建议 16 GB 内存。

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

- 纯 C11 零依赖，直接 mmap 官方 BF16 safetensors 权重，无需转换
- CPU（NEON/AVX2+FMA、线程池）与 Apple Silicon Metal GPU 双后端
- logits 与独立 NumPy 参考实现差异在 1e-4 内，分词器与 HF tokenizers 逐 token 验证
- 多轮对话复用 KV cache，提供 CLI 与 C 库 API（流式回调、TTFT 统计）

## 适用场景

- 在本地 CPU 或 Apple Silicon 上运行 Gemma 3 4B 进行对话与单次推理
- 将 Gemma 3 推理以 C 库形式嵌入自己的程序
- 研究 Gemma 3 架构（GQA、滑动窗口、RoPE 缩放）的参考实现

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: A **from-scratch inference engine for Google's Gemma 3 4B IT**, written in pure C11.
> L6: No Python, no ML framework, no dependencies. It runs on the CPU (NEON / AVX2,

## 星数曲线

```mermaid
xychart-beta
    title "robitec97/gemma3.c 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 116 --> 118
    line [117, 117]
```

2026-10-18 117 → 2026-10-24 117（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `a884338c1088` · [字段定义](../../DATASET.md)*
