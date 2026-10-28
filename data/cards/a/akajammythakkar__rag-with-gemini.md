# akajammythakkar/rag-with-gemini

⭐ 27 · Jupyter Notebook · 推送 2026-09-03 · [GitHub](https://github.com/akajammythakkar/rag-with-gemini) · 个人维护

**单笔记本 RAG 教学：用 Gemini 对 PDF 做有据问答**

一个可在 Google Colab 直接运行的单笔记本项目，演示完整 RAG 流程：pypdf 逐页抽取 PDF 文本，两轮分块（1000 字符递归切分 + 256 token 句子级切分），Chroma 默认 sentence-transformers 生成向量存入内存集合，top-k 检索后构造提示词让 Gemini 仅依据所给片段回答。仓库附带 Alphabet 年报（100+ 页）作示例文档，换自己的 PDF 只需改一行路径。作者明确说明这是教学笔记本而非服务，并列出生产化前需做的修改（持久化索引、降低温度、重排、引用、评测）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端到端 RAG 管线：抽取→两轮分块→嵌入索引→top-k 检索→受限生成
- 两阶段分块（字符级 + token 级）避免超出嵌入模型 token 上限
- 附带 100+ 页示例 PDF，Colab 中开箱即跑
- README 列出生产化前的五项改进建议（持久化/温度/重排/引用/评测）

## 适用场景

- 在 Colab 上快速理解 RAG 各环节及分块策略的影响
- 用自己的 PDF 做有依据的问答实验
- 学习如何评测检索与生成两个环节的质量

## 场景标签

`RAG` `文档问答` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L3: Retrieval-Augmented Generation over a PDF, end to end, in a single Colab notebook. Point it at a 100-page annual rep
> L53: **5. Generate.** Those chunks are pasted into a prompt that instructs Gemini to answer using only the supplied info

## 星数曲线

```mermaid
xychart-beta
    title "akajammythakkar/rag-with-gemini 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `6867d33985db` · [字段定义](../../DATASET.md)*
