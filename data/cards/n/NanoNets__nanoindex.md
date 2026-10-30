# NanoNets/nanoindex

⭐ 70 · Python · Apache-2.0 · 推送 2026-04-15 · [GitHub](https://github.com/NanoNets/nanoindex) · [官网](https://nanoindex.nanonets.com) · 组织维护

**长文档 Agentic RAG 框架：树与实体图导航，答案精确到像素级引用**

面向长结构化文档（10-K、合同、医疗记录等）的开源 RAG 框架。用 Nanonets OCR-3 提取目录、章节层级与标题结构，构建文档树；可选抽取实体与关系构建实体图。查询时 LLM agent 多轮导航树结构、直接读取页面图像并验证计算，引用标注精确到页与像素坐标。支持把多份文档编译为 Karpathy 式 LLM wiki（markdown + [[backlinks]]，可用 Obsidian 浏览）。以 pip 包与 CLI 提供使用，需 Nanonets API key 与 LLM API key。不适用于短文档或需要亚秒级延迟的场景。

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

- 保留文档结构构建树，可选实体图（实体+关系抽取）
- LLM agent 多轮导航树并读取页面图像，引用精确到页与像素坐标
- 多文档编译为可持久化 wiki（markdown + backlinks，Obsidian 可浏览）
- 三种查询模式：agentic_vision / agentic_graph_vision / fast_vision

## 适用场景

- 对 10-K 财报、合同等长结构化文档做多跳问答
- 审计合规场景需要可核验的精确引用出处
- 跨多年多份文档做汇总问答（如营收变化、组合内 ROA 比较）

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: **Open-source agentic harness for long documents.**
> L37: NanoIndex preserves document structure instead of destroying it. Nanonets OCR-3 extracts the table of contents, sec

## 星数曲线

```mermaid
xychart-beta
    title "NanoNets/nanoindex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-30 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3473ca847494` · [字段定义](../../DATASET.md)*
