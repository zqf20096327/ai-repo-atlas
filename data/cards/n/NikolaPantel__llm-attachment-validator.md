# NikolaPantel/llm-attachment-validator

⭐ 19 · Python · 推送 2026-02-28 · [GitHub](https://github.com/NikolaPantel/llm-attachment-validator) · 个人维护

**用 LLM 依据邮件正文对附件做相关性分类并评测的流水线**

基于 Python 的文档智能流水线：读取 .eml 文件，提取 HTML 正文与附件文件名（刻意忽略附件内容、MIME 类型与邮件头），将两者经提示工程发送到 Anthropic Claude API，输出每个附件 relevant/irrelevant 的 JSON 结果；另带评测模块，用 Accuracy/Precision/Recall/F1 对照 ground truth 数据打分。要求 Python 3.9+ 与 Anthropic API Key，通过 git clone 源码安装，设计上支持替换提示词、模型与分类逻辑的实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仅凭邮件 HTML 正文推断附件相关性，不读附件内容与元数据
- 调用 Anthropic Claude API 做上下文推理，输出结构化 JSON
- 内置 Accuracy/Precision/Recall/F1 评测模块对照 ground truth
- 模块化设计，可实验不同提示词、模型与分类逻辑

## 适用场景

- 批量处理 .eml 邮件并区分正文相关与装饰性附件
- 在标注数据上评测 LLM 附件分类的准确率
- 作为 LLM 流水线设计与提示工程的参考工程

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A document intelligence pipeline that classifies email attachments from `.eml` files as **relevant** or **irrelevant
> L7: The system leverages the **Anthropic Claude API** for contextual reasoning and includes an evaluation module for ben
> L53:  The HTML body and attachment list are sent to the Claude model with a carefully engineered prompt.

## 星数曲线

```mermaid
xychart-beta
    title "NikolaPantel/llm-attachment-validator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `f07973d816a4` · [字段定义](../../DATASET.md)*
