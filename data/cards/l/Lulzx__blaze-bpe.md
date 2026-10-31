# Lulzx/blaze-bpe

⭐ 14 · Rust · MIT · 推送 2026-07-22 · [GitHub](https://github.com/Lulzx/blaze-bpe) · 个人维护

**Rust 实现的 tiktoken 兼容 BPE 分词器，输出字节级一致**

用 Rust 从零重写的 BPE 分词器库，支持 cl100k_base（GPT-3.5/4）与 o200k_base（GPT-4o 等）编码，经 tiktoken-rs 边缘用例、6000 条模糊测试与全语料验证输出与 OpenAI tiktoken 字节一致。机制：手写 SIMD 加速预分词扫描器 + 每线程 piece 缓存的 BPE 合并；超 256KB 输入自动在 piece 安全边界分块并行。README 以大量基准测试为主，含与 gigatoken、rs-bpe 等的对比，并声明大输入下 gigatoken 吞吐更高、blaze 吞吐对内容敏感等限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- cl100k_base 与 o200k_base 编码输出与 tiktoken 字节一致
- SIMD 加速预分词扫描器（aarch64）+ 每线程 piece 缓存
- 超 256KB 输入自动分块多核并行编码
- 提供 count（不物化 token 计数）与 encode_with_specials（Aho-Corasick 特殊 token 处理）

## 适用场景

- 在 LLM 推理/RAG 服务中做高吞吐分词
- 替换 Python tiktoken 以获得 Rust 原生分词性能
- 大文档训练语料的批量 token 计数

## 场景标签

 · 领域:NLP/LLM 基础设施

## 证据(README 行号)

> L3: A fast, tiktoken-compatible BPE tokenizer in Rust. Produces **byte-identical
> L213: BPE tokenization is a two-stage pipeline, and blaze-bpe reimplements both

## 星数曲线

```mermaid
xychart-beta
    title "Lulzx/blaze-bpe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5048619ab307` · [字段定义](../../DATASET.md)*
