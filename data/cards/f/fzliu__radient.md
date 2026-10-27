# fzliu/radient

⭐ 281 · Python · BSD-2-Clause · 推送 2026-03-02 · [GitHub](https://github.com/fzliu/radient) · 个人维护

**多模态向量化与向量 ETL 工作流库：文本/音频/图像/图/分子转向量**

轻量级 Python 向量库，提供文本、音频、图、图像、分子的向量化接口，默认调用 bge-small-en-v1.5（sentence-transformers），支持 Imagebind、RDKit、TorchAudio、scikit-learn 等多种底层引擎。提供 accelerate 函数（基于 ONNX）在运行时优化部分向量化器以提升吞吐。另提供 Workflow 对象，将 source、transform、vectorizer、sink 组合成有向图，构建向量中心的不结构化数据 ETL（如 Google Drive → Voyage AI 向量化 → MongoDB）。明确不提供 LLM 连接器，RAG 上下文构建建议用 Haystack / LlamaIndex。以 pip 安装的库形式供开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本/音频/图像/图/分子多模态向量化统一接口
- Workflow 将 source/transform/vectorizer/sink 组成 ETL 有向图
- 基于 ONNX 的 accelerate 运行时加速（示例 32ms→17ms）
- 缺失依赖时提示自动安装

## 适用场景

- 为相似度搜索与 RAG 数据管道批量生成多模态向量
- 把 Google Drive 等数据源的文件持续向量化并存入向量库
- 为欺诈检测、分子搜索、推荐系统准备向量数据

## 场景标签

`语义搜索` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Radient is a developer-friendly, lightweight library for generating and working with embeddings. Radient supports si
> L69: Radient provides a `Workflow` object specifically for building vector-centric ETL applications. With Workflows, you
> L80: ### Supported vectorizer engines

## 星数曲线

```mermaid
xychart-beta
    title "fzliu/radient 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 280 --> 282
    line [281, 281]
```

2026-10-18 281 → 2026-10-27 281（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a80ab60da009` · [字段定义](../../DATASET.md)*
