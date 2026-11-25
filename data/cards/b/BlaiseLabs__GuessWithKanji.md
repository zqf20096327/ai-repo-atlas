# BlaiseLabs/GuessWithKanji

⭐ 4 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/BlaiseLabs/GuessWithKanji) · [官网](https://github.com/BlaiseLabs/GuessWithKanji) · 个人维护

**按已学汉字排序 Anki 日语生词卡的插件**

Anki 插件，重排日语牌组的新卡顺序，使每个生词在其汉字与读音刚被学过后出现，从而首次见词即可推测含义。核心机制为读取任意含词字段牌组、按 JmdictFurigana 拆分汉字-读音模式（99.0% 匹配）、以启发式加 EmbeddingGemma 嵌入相似度判断可推测性，贪心规划写入 Anki 新卡队列并在每次复习后重排。无额外软件即可运行；Ollama 为可选升级，提供更精细的含义判断与模型标注（每日 100 词上限）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按已学汉字读音排序新卡，使生词首次出现即可推测
- 启发式加 EmbeddingGemma 嵌入的加权可推测性判断（AUC 0.83）
- 任意 OpenAI 风格 API 模型批量标注（默认每日 100 词，可续跑）
- 内置仪表盘展示免费卡、可推测词与模式

## 适用场景

- 用 Anki 学日语时减少死记硬背的生词量
- 组织 JLPT 或 Core 6k 等大型词表牌组的学习顺序
- 在牌组内分享或众包人工标注的推测性标签

## 场景标签

 · 领域:语言学习/教育工具

## 证据(README 行号)

> L18: **No extra software needed.** Install the add-on and it works on its own. Ollama is an optional
> L94:  - **Model labels.** Any model behind an OpenAI-style API (Gemma 4 through Ollama by default) labels words in

## 星数曲线

```mermaid
xychart-beta
    title "BlaiseLabs/GuessWithKanji 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-10-30", "2026-11-25"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-29 3 → 2026-11-25 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `03a547810bdf` · [字段定义](../../DATASET.md)*
