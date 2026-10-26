# lightonai/fast-plaid

⭐ 283 · Python · MIT · 推送 2026-09-10 · [GitHub](https://github.com/lightonai/fast-plaid) · [官网](https://github.com/lightonai/fast-plaid) · 组织维护

**面向 ColBERT/ColPali 的多向量检索引擎（Rust/GPU）**

FastPlaid 是用 Rust 编写、通过 PyO3 提供 Python 接口的多向量（per-token late interaction）检索引擎，兼容 PyTorch 生态并按 PyTorch 版本发布多个安装包。功能包括建索引、search/search_token_scores 查询、带缓冲的增量更新（自动质心扩展）、subset 子集过滤与元数据过滤，以及 index_gpu_memory/batch_size 等 GPU 显存分级调优（low/medium/high/auto），支持 CPU 设备（此时 GPU 参数无效）。采用乘积量化（默认 4 bit）与 IVF 探测等近似检索参数。基准在 H100 GPU 上与原版 PLAID 引擎对比（README 声称更快）。由 LightOn（lightonai）维护，需自行提供查询/文档 token 向量，不内置嵌入模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 实现并面向 GPU 优化的多向量（late interaction）检索引擎，PyO3 提供 Python API
- 按 PyTorch 版本（2.7.0–2.11.0）发布对应安装包
- 增量更新：缓冲累积 + 离群点 K-means 自动质心扩展
- GPU 显存分级（index_gpu_memory low/medium/high/auto）与 batch_size 自适应分块调优
- 提供 token 级相似度矩阵输出（含 ColPali 图像 patch）

## 适用场景

- 为 ColBERT/ColPali 模型输出建立多向量索引并做 top-k 检索
- RAG 管线中用 subset 参数做元数据过滤检索
- GPU 环境下按可用 VRAM 调节索引放置与打分分块

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L9:  FastPlaid - A High-Performance Engine for Multi-Vector Search
> L17: - **Multi-vector search**, used in models like ColBERT or ColPali, replaces a single document or image vector with 

## 星数曲线

```mermaid
xychart-beta
    title "lightonai/fast-plaid 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 281 --> 284
    line [282, 283, 283]
```

2026-10-18 282 → 2026-10-26 283（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e7791acbc503` · [字段定义](../../DATASET.md)*
