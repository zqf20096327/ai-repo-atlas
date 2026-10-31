# ktbilyeu/Kudasai

⭐ 26 · Python · GPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/ktbilyeu/Kudasai) · 个人维护

**日英文本预处理与机器翻译工具，面向轻小说/小说译者**

Kudasai 是命令行/交互式日英翻译工具：先用 Kairyou 按替换 JSON 预处理文本（替换人名地名等不易翻译的词），再调用 EasyTL 通过 OpenAI、Gemini、DeepL、Google Translate 四种 API 完成翻译，均需 API key。提供批处理、并发控制、成本预估、日英对照校对日志等设置项，输出译文及调试/预处理/对照日志文件。仅在 Windows 10 与 Linux Mint 上测试，要求 Python 3.10+，需手动安装 spaCy 日语模型 ja_core_news_lg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于替换 JSON 的日文文本预处理（Kairyou）
- 四种翻译后端：OpenAI、Gemini、DeepL、Google Translate
- 提供 CLI 两种模式（preprocess / translate）与丰富的翻译设置（批次、并发、重试、性别上下文）
- 输出日英对照校对文本与预处理结果日志

## 适用场景

- 翻译日文小说/轻小说文本前先替换专有名词以保证一致性
- 用 LLM 或 DeepL 批量翻译日文 txt 文件并生成对照稿供校对
- 通过 CLI 脚本化批量预处理与翻译流程

## 场景标签

 · 领域:NLP/机器翻译

## 证据(README 行号)

> L58: After preprocessing is completed (if triggered), you will be prompted to choose a translation method.
> L168: Kudasai currently supports OpenAI, Gemini, DeepL, and Google Translate for translation. OpenAI is the recommended 


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `91a478eb45f0` · [字段定义](../../DATASET.md)*
