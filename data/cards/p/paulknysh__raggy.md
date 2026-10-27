# paulknysh/raggy

⭐ 33 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/paulknysh/raggy) · 个人维护

**本地优先的 CLI RAG 工具：对本地文档问答并给出引用**

基于 LangChain、Chroma 和 Ollama 构建的轻量命令行 RAG 工具，面向在本地文档集合上做问答的用户。嵌入与混合检索（向量 + BM25 词法索引）完全本地运行，生成可用本地 LLM 或 API（OpenAI/Anthropic/Google）远程执行；支持 pdf/docx/图片 OCR 等常见格式。检索经倒数排名融合与本地 onnxruntime 交叉编码器重排，按相关性阈值过滤后生成回答并附引用与相关性分数；DB 按 SHA-256 manifest 做增量重建。需 Python 3.10+ 与 Ollama，以克隆仓库 + uv/pipx 可编辑安装方式提供，也支持 Python API 调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 向量+BM25 混合检索，倒数排名融合合并结果
- 本地 onnxruntime 交叉编码器重排与相关性阈值过滤
- 嵌入与索引完全本地运行，生成可切换本地 LLM 或远程 API
- 按 manifest 哈希做增量更新，未改动文件不重复嵌入

## 适用场景

- 对本地文件夹里的 PDF、Office、Markdown 文档做带引用的问答
- 在无网络或注重隐私的环境下用本地模型检索文档
- 扫描件/图片文档经 OCR 后纳入检索问答

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: A lightweight CLI tool for Retrieval-Augmented Generation (RAG) over local documents built with LangChain, Chroma, a
> L18: Ollama is required for running the local embedding model (which feeds the on-disk vector DB), and also a local LLM 

## 星数曲线

```mermaid
xychart-beta
    title "paulknysh/raggy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-27 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b80ddc86200e` · [字段定义](../../DATASET.md)*
