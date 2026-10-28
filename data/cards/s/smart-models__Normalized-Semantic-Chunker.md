# smart-models/Normalized-Semantic-Chunker

⭐ 23 · Python · GPL-3.0 · 推送 2026-03-13 · [GitHub](https://github.com/smart-models/Normalized-Semantic-Chunker) · 组织维护

**面向 RAG 的语义分块服务：语义连贯且满足 token 上限**

以 FastAPI REST 服务形式提供的文本语义分块工具：将上传文档按句切分、用 sentence-transformers（默认 all-MiniLM-L6-v2）生成向量、基于相邻句相似度分布并行搜索最优切分百分位，并以 95 分位统计估计保证分块 token 数不超过上限；过小块自动合并、超限块再切分。支持 GPU（CUDA/PyTorch）与 CPU 运行，提供 GHCR 预构建 Docker 镜像与 docker-compose 部署，兼容 .txt/.md/.json 输入，可选 Bearer Token 认证。限制：Python 3.13+ 不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语义相似度分块 + 95 分位统计保证 token 上限
- 并行多核百分位搜索优化
- 小块自动合并、超限块再切分的后处理
- FastAPI REST 服务，预构建 Docker 镜像（GPU/CPU）

## 适用场景

- RAG 入库前的文档切分，避免上下文窗口溢出
- 为 embedding 与语义检索准备大小均衡的文本块
- 以 REST API 形式接入任意语言的文档处理流水线

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L14: The Normalized Semantic Chunker overcomes these challenges by combining semantic cohesion with statistical guarante
> L41: 1. The application exposes a simple REST API endpoint where users can upload a text document and parameters for max
> L43: 3. Each sentence is transformed into a vector embedding using state-of-the-art transformer models (default: `senten

## 星数曲线

```mermaid
xychart-beta
    title "smart-models/Normalized-Semantic-Chunker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `3e3a7953e40d` · [字段定义](../../DATASET.md)*
