# Sega757/Fast-AtomRAG-Core

⭐ 84 · Python · 推送 2026-08-21 · [GitHub](https://github.com/Sega757/Fast-AtomRAG-Core) · 个人维护

**向量-图混合检索微服务：亚秒级 RAG 原子知识搜索**

基于 FastAPI 的微服务，对知识原子图（Atom-Entity Graph）执行向量与图混合检索：ONNX INT8 嵌入、USearch HNSW 向量搜索与 NetworkX 个性化 PageRank 结合，含正则/ONNX 查询分解步骤。面向需要在硬性 SLA（README 称完整 RAG 循环小于 2.0 秒）内运行的检索服务使用者；提供 Prometheus 指标、健康检查与多阶段 Docker 构建。README 仅 21 行，为俄文，细节有限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HNSW 向量搜索与个性化 PageRank 的混合打分
- ONNX INT8 嵌入，不依赖 PyTorch/Transformers
- FastAPI + Prometheus 指标 + Liveness/Readiness 健康检查
- Docker Compose 多阶段构建部署

## 适用场景

- 为 RAG 系统提供低延迟的原子知识检索服务
- 在限定 SLA 场景下做向量+图混合召回
- 以 Docker 容器方式部署可监控的检索后端

## 场景标签

`RAG` `语义搜索` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L3: Микросервис для сверхбыстрого векторно-графового поиска атомов знаний (Atom-Entity Graph). Оптимизирован для работы 
> L7: * **Гибридный резонансный поиск (S = α·Cos + (1-α)·PPR):** Совмещение HNSW-векторного поиска (USearch) и топологичес

## 星数曲线

```mermaid
xychart-beta
    title "Sega757/Fast-AtomRAG-Core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-30 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e9c8fe314a05` · [字段定义](../../DATASET.md)*
