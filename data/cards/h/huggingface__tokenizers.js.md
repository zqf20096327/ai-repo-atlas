# huggingface/tokenizers.js

⭐ 58 · TypeScript · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/huggingface/tokenizers.js) · [官网](https://www.npmjs.com/package/@huggingface/tokenizers) · 组织维护

**纯 JS/TS 实现的分词器库，浏览器/Node 直接运行主流 tokenizer**

Hugging Face 官方维护的轻量分词器库，用纯 JavaScript/TypeScript 重新实现常用分词器（BPE、WordPiece、Unigram 等）及各类 normalizer、pre-tokenizer、post-processor 与 decoder，可在浏览器或 Node.js 中客户端侧运行，无需服务端或重依赖，兼容 Hub 上数千个模型的 tokenizer.json 配置。内置将 Rust tokenizers 的 Oniguruma 正则模式结构性转换为 JS RegExp u 模式的翻译层，并明确列出无法完全复现的构造与抛出 SyntaxError 的场景。

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

- 零依赖、约 8.3kB gzip，浏览器与 Node.js 均可运行
- 支持 BPE/WordPiece/Unigram/Legacy 模型及完整组件集
- Oniguruma 正则到 JS u 模式的结构化翻译，兼容 Rust tokenizers 配置
- 直接加载 Hugging Face Hub 的 tokenizer.json/tokenizer_config.json

## 适用场景

- 在浏览器中离线完成模型分词，无需服务端
- Node.js 应用中复用与 Hub 模型一致的分词结果
- 为 Transformers.js 类前端推理管线提供分词层

## 场景标签

 · 领域:LLM 基础设施/NLP 工具库

## 证据(README 行号)

> L7: Run today's most used tokenizers directly in your browser or Node.js application. No heavy dependencies, no server r
> L40: This library expects two files from Hugging Face models:
> L47: Tokenizer configs are authored for the Rust `tokenizers` crate, which compiles patterns with Oniguruma — a regex en

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/tokenizers.js 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 56 --> 59
    line [57, 58, 58]
```

2026-10-18 57 → 2026-10-26 58（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b168547aa8ff` · [字段定义](../../DATASET.md)*
