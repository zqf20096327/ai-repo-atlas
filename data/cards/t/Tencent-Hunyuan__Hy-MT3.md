# Tencent-Hunyuan/Hy-MT3

⭐ 100 · Python · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/Tencent-Hunyuan/Hy-MT3) · 组织维护 · 中文 README

**开源多语言翻译模型系列：覆盖102种语言的文本翻译**

腾讯混元多语言翻译模型家族第三代，提供 1.8B、7B、30B-A3B（MoE）三个规模，语言覆盖从 38 种扩展至 102 种，权重以 FP8 与 GGUF 量化版本发布在 HuggingFace 和 ModelScope。README 给出 transformers、vLLM、SGLang、llama.cpp 四种推理部署路径及推荐采样参数，提供术语表、风格、个性化、结构化数据等任务的 prompt 模板，附完整训练管线（全参/LoRA 微调、DeepSpeed、LLaMA-Factory 集成），并开源基于 rubric 的翻译评测套件 TransRubric。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个规模（1.8B/7B/30B-A3B），支持 102 种语言，提供 FP8 与 GGUF 量化版本
- 提供术语、风格、个性化、分隔符保留、结构化数据等翻译任务的 prompt 模板
- 开源 TransRubric 翻译质量评测套件及 rubric 构建提示词
- 提供完整训练管线，支持全参微调与 LoRA 微调

## 适用场景

- 接入游戏本地化管线翻译游戏文本与术语
- 对 OCR 结果级联做图片文字翻译
- 用 TransRubric 对候选译文做细粒度质量评分
- 基于自有语料对翻译模型做 LoRA 微调

## 场景标签

`模型评测` `微调` `模型量化` · 领域:评测与运维

## 证据(README 行号)

> L13: Hy-MT3 is the third generation of the Tencent Hy multilingual translation model family. It includes three model siz
> L60: |**Default Translation**|将以下文本翻译为 `{target_lang}`，注意**只需要输出翻译后的结果，不要额外解释**： `{source_text}`|Translate the following
> L103: Build vLLM from source:

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/Hy-MT3 星数(近 3 点)"
    x-axis ["2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 71 --> 102
    line [73, 91, 100]
```

2026-11-26 73 → 2026-11-28 100（+27）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `ea73d53214f2` · [字段定义](../../DATASET.md)*
