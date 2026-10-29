# gyunggyung/docling-translate

⭐ 18 · Python · Apache-2.0 · 推送 2026-01-05 · [GitHub](https://github.com/gyunggyung/docling-translate) · [官网](https://gyunggyung.github.io/docling-translate/) · 个人维护

**保留版式的文档翻译工具：原文与译文逐句对照输出**

基于 IBM docling 解析 PDF/DOCX/PPTX/HTML/图片等文档的表格、图片与多栏布局，按句子 1:1 映射原文与译文，生成可左右对照、点击查看原文的交互式 HTML；也翻译 Markdown、代码文件（仅注释与 docstring）及配置/文本文件。翻译引擎可选 Google、DeepL、Gemini、OpenAI GPT-5-nano 及本地 Qwen、LFM2、NLLB-200 等，支持多线程并行与 pypdfium2 快速模式。提供 CLI 与 Streamlit Web UI，面向需要核对原文的文档阅读者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- docling 解析并保留表格/图片/多栏布局的结构
- 原文-译文句子级 1:1 映射的交互式对照 HTML
- 多引擎可选：Google/DeepL/Gemini/GPT-5-nano 及 Qwen、LFM2、NLLB 等本地模型
- 代码文件仅翻译注释与 docstring，保留代码结构

## 适用场景

- 翻译英文技术 PDF 并逐句对照核验原文
- 批量翻译文档并保留表格与图片版式
- 翻译代码仓库文档时只处理注释与 docstring

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L15: `docling-translate`는 IBM의 docling 라이브러리를 활용하여 문서의 복잡한 구조(표, 이미지, 다단 레이아웃)를 분석하고, 원문과 번역문을 **문장 단위로 매핑(1:1 Mapping)*
> L32: - **유연한 엔진 선택**: Google Translate, DeepL, Gemini, OpenAI GPT-5-nano, Qwen(Local), LFM2(Local), LFM2-KOEN-MT(Local),

## 星数曲线

```mermaid
xychart-beta
    title "gyunggyung/docling-translate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `331b2ee9c07e` · [字段定义](../../DATASET.md)*
