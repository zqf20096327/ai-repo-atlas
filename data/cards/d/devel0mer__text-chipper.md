# devel0mer/text-chipper

⭐ 4 · Rust · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/devel0mer/text-chipper) · 个人维护

**面向 RAG/LLM 管道的 Markdown 感知文本分块库（Rust+Python）**

以 Rust 实现并通过 PyO3 提供零依赖 Python 绑定的文本分块库：保证每块 token 数不超过预算、保持 Markdown 代码块/列表/GFM 表格完整、超长表格按行边界切分并在续块重复表头；支持内置 BPE 编码、Hugging Face tokenizer、自定义计数器及多 tokenizer 统一预算守护；提供流式大文件读取与精确源偏移。仅支持 Markdown 与纯文本，不支持 HTML/PDF/DOCX；源码构建需 Rust 工具链与 maturin。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 严格 token 预算：strict 模式下每块 token_count ≤ max_length
- Markdown/GFM 表格感知，超长表格按行切分并重复表头
- 支持 Hugging Face tokenizer、tokenizer.json 与自定义计数器
- 提供 from_file_stream 有界内存流式处理与精确字符/字节偏移

## 适用场景

- 为 RAG 管道生成不超嵌入模型 token 上限的文本块
- 分块含大量 GFM 表格的 Markdown 文档并保留列头上下文
- 流式分块超大 UTF-8 文本文件而避免全量载入内存
- 在多个 tokenizer/模型预算下统一控制文本块长度

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: **High-performance, Markdown- and table-aware, strictly budget-enforced text chunking for RAG and LLM pipelines.
> L15: - **Token-exact budget (`token_count <= max_length` guaranteed).** In the default strict mode, every chunk is re-to
> L25: Install from PyPI (pre-built `abi3` wheels for Python ≥ 3.9 include the Rust core and Hugging Face `tokenizers` sup


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `1cdb83861e77` · [字段定义](../../DATASET.md)*
