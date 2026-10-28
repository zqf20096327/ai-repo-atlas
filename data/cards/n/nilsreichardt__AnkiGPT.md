# nilsreichardt/AnkiGPT

⭐ 184 · Dart · AGPL-3.0 · 推送 2026-04-05 · [GitHub](https://github.com/nilsreichardt/AnkiGPT) · [官网](https://AnkiGPT.help) · 个人维护

**把讲义幻灯片转成 Anki 抽认卡并导出的 GPT 网页应用**

面向学生的抽认卡生成工具：上传 PDF 幻灯片或输入文本，应用先检测语言、分段并向 OpenAI GPT 模型（GPT-3.5/GPT-4）发起多次请求，一次最多生成 150 张卡片，可在浏览器中编辑、删除、生成记忆术并以 CSV 导入 Anki。仅客户端代码开源（Flutter），后端与提示词闭源；可通过网站或 ChatGPT 中的自定义 GPT（需 ChatGPT Plus）使用。限制：GPT 对数学公式处理较弱，PDF 输入仅处理文本、忽略图片。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上传 PDF 或输入文本，一键生成最多 150 张抽认卡
- 支持编辑、删除卡片并生成记忆术，CSV 导出至 Anki
- 自动检测输入语言，支持多数语言
- 另以 ChatGPT 自定义 GPT 形式提供，可从图片生成卡片

## 适用场景

- 把课件幻灯片快速转成 Anki 抽认卡备考
- 在复习前为卡片生成记忆术辅助记忆
- 已有 ChatGPT Plus 订阅的用户直接在 ChatGPT 内生成卡片

## 场景标签

 · 领域:教育/学习工具

## 证据(README 行号)

> L12: - 🧠 Generate flashcards up to 150 Anki flashcards with one click using GPT-3.5 or GPT-4 by OpenAI
> L26: AnkiGPT first detects the language of the input. Then it splits the text into multiple sections and sends multiple 

## 星数曲线

```mermaid
xychart-beta
    title "nilsreichardt/AnkiGPT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 183 --> 185
    line [184, 184]
```

2026-10-18 184 → 2026-10-28 184（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `11d652c34c04` · [字段定义](../../DATASET.md)*
