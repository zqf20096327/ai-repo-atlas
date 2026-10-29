# CogitatorTech/vq

⭐ 23 · Rust · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/CogitatorTech/vq) · [官网](https://cogitatortech.github.io/vq/) · 组织维护

**Rust 向量量化库：压缩高维嵌入向量以省存提速**

提供二值量化(BQ)、标量量化(SQ)、乘积量化(PQ)与树结构量化(TSVQ)四种算法的 Rust 库，带 Python 绑定（PyVq）。面向嵌入向量压缩场景（如向量数据库存储、RAG 应用检索提速），输入 f32 向量可压缩至少 50%（BQ/SQ 达 75%），支持欧氏/余弦/曼哈顿距离、批量量化与量化器保存加载，通过 SIMD（依赖 Hsdlib C 库）、多线程与零拷贝提升性能。需 Rust 1.85+；启用 simd 特性需支持 C11 的 C 编译器。项目自述处于早期开发阶段，可能有 bug 与破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- BQ/SQ/PQ/TSVQ 四种量化算法，统一 API
- 存储压缩至少 50%（BQ/SQ 达 75%），面向 128–1536 维嵌入向量
- SIMD 加速、多线程、零拷贝；支持三种距离度量
- 通过 PyVq 提供 Python 绑定，量化器可保存加载

## 适用场景

- 压缩向量数据库中的嵌入以降低内存占用
- 加速 RAG 应用的近邻搜索响应
- 在 Rust 项目中做高维数据压缩与相似度检索

## 场景标签

 · 领域:机器学习基础设施/向量搜索

## 证据(README 行号)

> L11: Vq (**v**[ector] **q**[uantizer]) is a vector quantization library for Rust.
> L17: For example, vector quantization can be used to reduce the size of data stored in a vector database or speed up the
> L67: > Vq is primarily designed for embedding vector compression (like the ones stored in a vector database),

## 星数曲线

```mermaid
xychart-beta
    title "CogitatorTech/vq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `607336090d74` · [字段定义](../../DATASET.md)*
