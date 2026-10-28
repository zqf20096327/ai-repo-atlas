# tosinonye7-ui/SummaraMind-Transformer-Suite

⭐ 55 · HTML · 推送 2026-10-28 · [GitHub](https://github.com/tosinonye7-ui/SummaraMind-Transformer-Suite) · 个人维护

**混合式文本摘要工具：抽取+生成双层摘要，带可审计决策记录**

名为 EchoForge 的自动摘要系统，采用双路径架构：Path A 为基于依存与共指的话语图抽取式摘要（RhetRank/PageRank 变体），Path B 为自注意力编码-解码器生成式摘要，最终融合输出三层摘要（50/200/500 词）。支持 PDF/DOCX/EPUB/HTML 输入、多文档比较、查询聚焦模式，输出 JSON 决策记录与 0-100 信任分。分发方式为自包含 wheel（Releases 下载），不使用 pip/npm。README 自称研究级工具，声明摘要可能遗漏细节或产生幻觉。注：仓库名为 SummaraMind-Transformer-Suite，与 README 中 EchoForge 命名不一致。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 抽取+生成双路径融合，输出三层不同长度摘要
- 每次摘要附带 JSON 决策记录（抽取原因与评分明细）
- 自包含 wheel 分发，标准库外仅 Python 3.10+ 依赖
- 宣称 50M 参数模型可在 CPU 上运行（1k 词约 280ms）

## 适用场景

- 把企业文档、报告压缩为多层次的摘要
- 对多篇文档做跨文档比较式总结
- 需要可审计摘要依据的合规场景（README 提及法律/医疗/金融）

## 场景标签

 · 领域:自然语言处理/文本摘要

## 证据(README 行号)

> L8: Welcome to **EchoForge**, a novel architectural experiment that reimagines the entire paradigm of extractive and abs
> L14: - **Path A (Extractive Resonance):** A rule-based, dependency-aware extractor that scores sentences not by word fre
> L15: - **Path B (Abstractive Forging):** A lightweight, self-attentive encoder-decoder that *distills* the extracted res

## 星数曲线

```mermaid
xychart-beta
    title "tosinonye7-ui/SummaraMind-Transformer-Suite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `2ec44745e081` · [字段定义](../../DATASET.md)*
