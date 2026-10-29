# dineshsoudagar/local-document-intelligence

⭐ 20 · Python · Apache-2.0 · 推送 2026-04-15 · [GitHub](https://github.com/dineshsoudagar/local-document-intelligence) · 个人维护

**完全本地运行的 PDF 文档知识库与 RAG 问答桌面应用**

面向终端用户的本地文档智能系统：上传 PDF 后解析分块并存入本地 Qdrant 向量库，通过稠密检索、BM25 稀疏检索、结果融合与 Qwen 重排器生成带引用的接地回答，无法支持时拒绝作答而非猜测。提供 Auto/Chat/Corpus/单文档四种查询模式。生成、嵌入、重排全部使用本地加载的 Qwen 模型，按显存提供 0.6B–4B 多档选择，并支持 bitsandbytes 4/8-bit 低内存加载。Windows 打包 EXE 交付，技术栈为 FastAPI + React + pywebview。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 稠密+BM25 混合检索、融合后经 Qwen3-Reranker 重排
- 回答附引用与来源，不支持时拒绝作答
- 按显存提供 Qwen 0.6B/1.7B/4B 多档模型选择
- bitsandbytes 4/8-bit 低内存加载选项

## 适用场景

- 在离线环境对私有 PDF 文档建立持久知识库并问答
- 检索限定在单篇文档内提问
- 显存受限设备上运行本地 RAG 问答

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: A fully local document intelligence system for building a private document workspace with persistent indexing, hybri
> L13: - 🧠 Generate grounded answers from local models
> L91: 8. Generate a supported answer or decline unsupported claims instead of guessing

## 星数曲线

```mermaid
xychart-beta
    title "dineshsoudagar/local-document-intelligence 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b3145f62c1ad` · [字段定义](../../DATASET.md)*
