# Firmamento-Technologies/TurboQuant

⭐ 20 · Python · Apache-2.0 · 推送 2026-03-28 · [GitHub](https://github.com/Firmamento-Technologies/TurboQuant) · 组织维护

**面向向量检索的 TurboQuant 量化库：纯 Python 压缩嵌入向量**

实现 Google ICLR 2026 论文（arXiv:2504.19874）的 TurboQuant 算法，用于 FAISS 兼容的向量量化：随机旋转后按坐标做 Lloyd-Max 量化，无需训练数据与预处理即可压缩嵌入向量（按位宽 4.0-16.0 倍），提供暴力检索 TurboQuantIndex 与基于 IVF 的次线性 ANN 检索两种索引，另有低层量化器 API（MSE 版、内积版 TurboQuantProd、LloydMaxQuantizer）。面向需要降低向量内存/存储的开发者。限制：暴力索引为 O(N)，默认在内存中保存重建的 float32 矩阵；纯 Python/NumPy 实现在大规模下查询速度低于 C++ 库；召回基准基于随机单位向量，真实嵌入可能不同。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 随机旋转 + Lloyd-Max 逐坐标量化，无训练数据与预处理
- 提供暴力索引与 IVF 次线性 ANN 索引两种检索接口
- 6-bit 下实测 Recall@10 95.3%、压缩 5.3x（all-MiniLM-L6-v2，d=384）
- 3,823 个参数化测试用例覆盖论文六项核心声明的验证

## 适用场景

- RAG 或检索系统压缩嵌入向量以降低内存占用
- 在无 GPU、不引入 C++/CUDA 依赖的环境做向量量化检索
- 移动/IoT 场景下以高位宽压缩换取更小存储

## 场景标签

`向量数据库` `模型量化` · 领域:知识与检索

## 证据(README 行号)

> L15: A pure Python implementation of the **TurboQuant** algorithm (Zandieh et al., ICLR 2026) for **FAISS-compatible vec
> L99: TurboQuant implements a mathematically elegant compression scheme from Google Research (arXiv:2504.19874):

## 星数曲线

```mermaid
xychart-beta
    title "Firmamento-Technologies/TurboQuant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d9083783c7e3` · [字段定义](../../DATASET.md)*
