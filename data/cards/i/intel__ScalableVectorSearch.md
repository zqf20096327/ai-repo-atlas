# intel/ScalableVectorSearch

⭐ 239 · C++ · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/intel/ScalableVectorSearch) · [官网](https://intel.github.io/ScalableVectorSearch/) · 组织维护

**面向十亿级高维向量的相似度检索性能库**

Intel 维护的 C++ 向量相似度检索库，提供 Python API，支持欧氏距离、内积、余弦相似度，数据类型覆盖 float32/float16/uint8/int8，并含向量压缩（LVQ/LeanVec 的压缩技术以闭源共享库与 PyPI 包形式提供，仅限 Intel 硬件）。针对 Intel Xeon 2-6 代处理器与 AVX-512 指令优化，无 AVX-512 时性能下降并给出警告。本仓库仅含开源部分。面向应用与框架开发者，需引用 VLDB 2023 论文。

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

- 支持十亿级高维向量的相似度检索（欧氏/内积/余弦）
- LVQ 等向量压缩以闭源共享库/PyPI 包提供，仅限 Intel 硬件
- C++ 编写并提供兼容常见标准库的 Python API
- 针对 Xeon 2-6 代（Cascade Lake 至 Granite Rapids）与 AVX-512 优化

## 适用场景

- 在 Intel Xeon 服务器上构建大规模向量检索/RAG 索引
- 应用或框架中嵌入高性能 C++ 相似度检索
- 对比压缩索引下的检索吞吐与内存占用

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L7: **Scalable Vector Search (SVS)** is a performance library for vector similarity search.
> L15: This enables application and framework developers using similarity search to unleash its performance on Intel(R) Xe
> L17: SVS offers a fully-featured and yet simple Python API, compatible with most standard libraries.

## 星数曲线

```mermaid
xychart-beta
    title "intel/ScalableVectorSearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 238 --> 240
    line [239, 239]
```

2026-10-18 239 → 2026-10-26 239（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e36559ddfbb9` · [字段定义](../../DATASET.md)*
