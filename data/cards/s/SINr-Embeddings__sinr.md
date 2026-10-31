# SINr-Embeddings/sinr

⭐ 22 · Jupyter Notebook · NOASSERTION · 推送 2026-06-11 · [GitHub](https://github.com/SINr-Embeddings/sinr) · 组织维护

**为科研者提供可解释的词与图嵌入训练 Python 库**

基于图社区结构（Louvain 类检测）生成稀疏可解释向量的 Python 库，覆盖图嵌入与词嵌入：从大规模文本语料提取共现图（PMI 过滤），检测社区后按顶点与社区的关联构建嵌入，支持稀疏化、相似度评测（MEN/WS353/SCWS）与维度含义查看。依赖 Networkit（C++/OpenMP），需 Python 3.9 与 C++ 编译器，由 Le Mans 大学维护，附多篇论文与在线文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于图社区结构生成稀疏可解释嵌入，维度对应社区
- 从大规模文本语料提取共现图并做 PMI 过滤
- 内置相似度评测（MEN/WS353/SCWS）与维度可解释性查看接口
- 提供向量稀疏化与模型保存/加载

## 适用场景

- 训练并解释词向量/节点向量的每一维含义
- 从文本语料构建共现图并生成可解释词嵌入
- 科研中对嵌入做相似度下游评测

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L4: *SINr* is an open-source tool to efficiently compute graph and word
> L5: embeddings. Its aim is to provide sparse interpretable vectors from a
> L131: *SINr* is currently maintained at the *University of Le Mans*. If you

## 星数曲线

```mermaid
xychart-beta
    title "SINr-Embeddings/sinr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bf1b7564d440` · [字段定义](../../DATASET.md)*
