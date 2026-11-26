# GyuyeongKim/KatoANN-public

⭐ 3 · C++ · Apache-2.0 · 推送 2026-11-16 · [GitHub](https://github.com/GyuyeongKim/KatoANN-public) · 个人维护

**基于服务器 CPU 矩阵引擎的近似最近邻检索系统**

以 C++ 实现、提供 Python 模块与命令行工具的 ANN 检索系统：索引为 IVF 分区结构，向量以 16-bit 编码存储（高低字节拆分），用四次 8-bit 矩阵乘还原精确距离，并通过 rank-then-refine 减少完整距离计算；在 Intel AMX 上运行，无 AMX 时回退 AVX-512 VNNI。内存中不保留 float32 副本。构建需在目标机器上进行（-march=native），要求 Linux x86-64、CMake≥3.20、GCC≥11 与 OpenBLAS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- IVF 分区索引，向量以 16-bit 编码存储，内存无 float32 副本
- 支持 Intel AMX 矩阵引擎，无 AMX 时回退 AVX-512 VNNI 且结果一致
- 提供 C++ API、Python 模块与命令行工具，含到达流压测（Poisson 到达、分位延迟报告）
- 附浏览器端 RAG 检索回放演示与结果复现脚本

## 适用场景

- 在服务器 CPU 上为 RAG 应用做高召回向量检索
- 对千万级向量索引做吞吐与召回压测
- 以 CLI 或 Python 模块构建与查询 ANN 索引

## 场景标签

`向量数据库` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L16: KatoANN is an approximate nearest neighbor (ANN) search system that reaches both high throughput and high recall on
> L17: the matrix engines of server CPUs, such as Intel AMX. It has a C++ API, a Python module, and a command-line tool. I
> L109: generation (RAG) demo with KatoANN as the retriever over 10 million PubMed abstracts (BGE-M3 embeddings). The page


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7e0496d090ce` · [字段定义](../../DATASET.md)*
