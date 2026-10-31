# jorge-martinez-gil/embeddings

⭐ 16 · Python · MIT · 推送 2026-08-26 · [GitHub](https://github.com/jorge-martinez-gil/embeddings) · 个人维护

**嵌入向量压缩布局的可复现选型目录与预算约束顾问**

面向向量检索系统的嵌入压缩物理设计工具：在冻结文本嵌入模型、给定工作负载与相关性标注的前提下，统一评测 float16/int8/int4/二值/PQ/OPQ 及组合等布局，测量检索质量、每向量字节数与查询延迟，附带配对 bootstrap 置信区间、随机化 p 值与 TOST 等价判定，输出 Pareto 目录与可复现 manifest。CLI 顾问可回答：给定 RAM/延迟预算与质量 SLO，最小满足的布局是什么，或不可行时需放松哪一轴。Python 包名 embedopt，离线 smoke 路径无需 GPU 与外部数据下载，覆盖 BEIR 上 23 个 backbone-数据集对。

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

- 统一接口评测 float32/float16/截断/int8/int4/二值/PQ/OPQ 及组合布局
- 配对 bootstrap CI、随机化 p 值、TOST 等价判定与 codebook 种子方差统计标注
- Pareto 过滤目录 + 约束顾问（RAM/延迟/SLO，不可行时输出最小放松量）
- 每步可断点续跑，全部结果绑定 manifest（config 哈希、种子、版本、平台）

## 适用场景

- 向量检索系统按内存/延迟/质量预算选择嵌入存储布局
- 复现论文中 23 个 BEIR backbone-数据集对的压缩评测结果
- 评估 int4 或 PQ 等激进压缩对自家集合检索质量的影响

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: EmbedCatalog treats post-hoc embedding compression as a physical-design problem
> L31: 3. Measure quality, bytes per vector, and query latency under one protocol.

## 星数曲线

```mermaid
xychart-beta
    title "jorge-martinez-gil/embeddings 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9fce5f85f946` · [字段定义](../../DATASET.md)*
