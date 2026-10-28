# guillaume-be/rust-tokenizers

⭐ 345 · Rust · Apache-2.0 · 推送 2026-01-22 · [GitHub](https://github.com/guillaume-be/rust-tokenizers) · 个人维护

**Rust 实现的 Transformer 分词器库，供 rust-bert 使用**

以 Rust 编写的分词器库，提供 WordPiece、Byte-Pair Encoding（BPE）与 Unigram（SentencePiece）三类模型，覆盖 BERT、RoBERTa、GPT2、DeBERTa、MBart50 等架构；WordPiece 支持单线程与多线程处理，BPE 分词器使用共享缓存且仅单线程。词表与合并文件需从 Transformers 库手动下载，SentencePiece 加载与 C++ 库相同的 .model proto 文件。被 rust-bert crate 使用，另有 Python 绑定，构建 Python API 需 Rust nightly 工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WordPiece/BPE/Unigram(SentencePiece) 三类分词算法
- 覆盖 BERT、RoBERTa、GPT2、DeBERTa 等多种 Transformer 架构
- 提供 Python 绑定（需 Rust nightly 从源码编译）
- Rust 层面有完整单元测试与集成/基准测试

## 适用场景

- 在 Rust 项目中为 Transformer 模型做分词预处理
- 配合 rust-bert 构建模型推理管线
- 通过 Python 绑定在 Python 侧使用该分词器

## 场景标签

 · 领域:NLP/深度学习基础库

## 证据(README 行号)

> L5: License
> L8: These tokenizers are used in the rust-bert crate.

## 星数曲线

```mermaid
xychart-beta
    title "guillaume-be/rust-tokenizers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 344 --> 346
    line [345, 345]
```

2026-10-18 345 → 2026-10-28 345（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2d566b894b23` · [字段定义](../../DATASET.md)*
