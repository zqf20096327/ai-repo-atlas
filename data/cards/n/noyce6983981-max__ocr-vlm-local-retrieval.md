# noyce6983981-max/ocr-vlm-local-retrieval

⭐ 41 · Python · MIT · 推送 2026-08-13 · [GitHub](https://github.com/noyce6983981-max/ocr-vlm-local-retrieval) · 个人维护 · 中文 README

**本地多模态个人资料库检索原型：OCR+视觉语言向量检索图片与文档**

面向个人图片与文档的本地多模态检索原型：将图片、ZIP、PDF、DOCX、PPTX统一转换为页面，用 PP-OCRv5 做 OCR，结合 BGE-M3 Dense、BM25 与 Qwen3-VL-Embedding-2B 视觉向量三路召回，再用 Qwen3-VL-Reranker-2B 重排，支持分库隔离、来源溯源、质量门控与拒答。以 Streamlit 界面提供，不依赖商业大模型 API，模型权重与原始资料不随公开仓库分发，自述为科研原型而非商业 SaaS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三路召回（Dense/BM25/视觉向量）+ Qwen3-VL 重排的检索链路
- 支持图片、ZIP、PDF、DOCX、PPTX 批量导入与页面级来源溯源
- 多资料库严格隔离与开放集拒答（证据不足时明确拒答）
- 提供 40 页合成数据 CPU 复现脚本与 GHCR 无网络验证镜像

## 适用场景

- 在本地对个人图片与办公文档做自然语言检索
- 建立分库隔离的私有资料库并保留每条结果的来源证据
- 运行可复现的检索评测链路验证工程实现

## 场景标签

`RAG` `OCR` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: 面向通用个人图片与文档的本地多模态检索原型：将图片、ZIP、PDF、DOCX和PPTX统一转换为页面，结合OCR文本、视觉语言向量、OCR质量门控与视觉语言重排，完成自然语言到资料页面的检索。项目强调本地隐私、分库隔离、证据溯源和人
> L76: - [x] Qwen3-VL-Embedding-2B视觉大模型语义分支
> L82: - [x] Qwen3-VL-Reranker-2B候选重排

## 星数曲线

```mermaid
xychart-beta
    title "noyce6983981-max/ocr-vlm-local-retrieval 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4c81284e9726` · [字段定义](../../DATASET.md)*
