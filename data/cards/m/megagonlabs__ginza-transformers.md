# megagonlabs/ginza-transformers

⭐ 16 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/megagonlabs/ginza-transformers) · 组织维护

**spaCy v3 扩展：在 spacy-transformers 中使用自定义分词器**

ginza-transformers 是 spacy-transformers 的扩展库，允许在 spaCy v3 的 transformer 流水线组件中使用定义于 huggingface/transformers 之外的自定义分词器（如 SudachiTra）。提供两级回退机制：分词器先走 AutoTokenizer 标准加载、失败后经 importlib 导入 config.cfg 指定的类；模型加载先查本地目录、再查本地缓存、最后自动从 Hugging Face Hub 下载。通过 pip 安装，配置 config.cfg 后用于 spacy 训练与分析两个阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 spacy-transformers 中加载 huggingface/transformers 之外的自定义分词器
- 分词器与模型加载各含多级回退机制
- 运行时自动从 Hugging Face Hub 下载指定模型

## 适用场景

- 日语 NLP 流水线中为 spaCy v3 接入 SudachiTra 自定义分词器
- 训练与分析阶段分别使用不同 transformer 模型配置
- 避免手动下载模型，运行时自动拉取 Hugging Face Hub 模型

## 场景标签

 · 领域:NLP/工具库

## 证据(README 行号)

> L3: The `ginza-transformers` is a simple extension of the spacy-transformers to use the custom tokenizers (defined outsi
> L29: With this config, `ginza-transformers` employs `SudachiTra` as a transformer tokenizer and use `megagonlabs/tansfor

## 星数曲线

```mermaid
xychart-beta
    title "megagonlabs/ginza-transformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fe9d4eaf72b3` · [字段定义](../../DATASET.md)*
