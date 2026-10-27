# ml-rust/splintr

⭐ 61 · Rust · MIT · 推送 2026-10-18 · [GitHub](https://github.com/ml-rust/splintr) · [官网](https://crates.io/crates/splintr) · 组织维护

**给开发者的 Rust/Python 高速分词器库，兼容主流词表格式**

纯 Rust 实现的分词器库，提供 Python 绑定（PyPI 包 splintr-rs）与 Rust crate（cargo）。支持四种词表加载途径：18 个内置词表、HuggingFace tokenizer.json、原始 .tiktoken 文件、GGUF 词表（仅 Rust），统一返回 AnyTokenizer 句柄；在 14 个模型家族上输出与 HuggingFace tokenizers 逐 id 一致。附带流式解码器、非受信文本的三种特殊 token 编码模式、splintr-train 训练二进制（BPE/WordPiece/Unigram），批量编码用 Rayon 多核并行。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种词表来源统一为 AnyTokenizer 句柄，14 个家族输出与参考实现逐 id 一致
- 18 个内置词表无需文件下载与网络，每个词表附加 54 个 agent token
- 流式解码器缓冲不完整 UTF-8 字节，逐 token 解码与整体 decode 结果一致
- splintr-train 支持 BPE/WordPiece/Unigram 词表训练，批量编码 Rayon 多核并行

## 适用场景

- 为 LLM 推理与训练流水线提供分词/解码组件
- 流式输出场景逐 token 解码生成文本
- 训练自有 BPE/WordPiece/Unigram 词表

## 场景标签

 · 领域:LLM 基础设施/分词

## 证据(README 行号)

> L7: Pure Rust by default, with 18 bundled vocabularies and four tokenizer backends behind one <code>AnyTokenizer</code> 
> L41: Splintr loads a tokenizer from a bundled vocabulary, a HuggingFace `tokenizer.json`, a raw `.tiktoken` file, or a G
> L43: Tokenization runs on every prompt, training corpus, and RAG chunk. Splintr runs at Rust speed behind one API.

## 星数曲线

```mermaid
xychart-beta
    title "ml-rust/splintr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-27 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `eb2200864edb` · [字段定义](../../DATASET.md)*
