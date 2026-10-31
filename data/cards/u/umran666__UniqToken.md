# umran666/UniqToken

⭐ 18 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/umran666/UniqToken) · 个人维护

**面向研究实验的 Unigram/BPE 分词器工具包，含 Rust 加速**

Python 分词器研究工具包，捆绑 PyO3/Rust 原生扩展：支持 Unigram（EM 训练、Viterbi 分割、可选 FFBS 正则化）与 BPE（含 CEM/SuperBPE 后训练扩展）词表训练，可导入 tiktoken ranks、Hugging Face JSON、SentencePiece Unigram 模型；提供字节回退、字符级偏移追踪、Unicode 图界预分词、CLI、Hugging Face 集成与 GGUF 导出。面向做词表构建与多语言实验的开发者/科研用户；限制包括新词表需模型重新适配嵌入层、导入保真度受配置约束、确认性实验未执行。

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

- Unigram/BPE/CEM/SuperBPE 词表训练与扩展
- tiktoken/Hugging Face/SentencePiece 兼容导入器
- 全 256 字节回退与字符索引偏移（raw_span）追踪
- PyO3+Rayon 原生加速：前缀 trie、Viterbi、批处理

## 适用场景

- 实验不同的词表构建与后训练扩展策略
- 把已有 tiktoken/SentencePiece 词表导入统一框架做分析
- 做多语言文本的分词与 token 偏移对齐研究

## 场景标签

 · 领域:NLP/分词工具

## 证据(README 行号)

> L3: UniqToken is a Python tokenizer research toolkit with a bundled Rust extension. It supports training Unigram and BPE
> L19: - A CLI, Rust acceleration, Hugging Face integration/export, and GGUF export. Integration fidelity depends on the c

## 星数曲线

```mermaid
xychart-beta
    title "umran666/UniqToken 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3222ab847722` · [字段定义](../../DATASET.md)*
