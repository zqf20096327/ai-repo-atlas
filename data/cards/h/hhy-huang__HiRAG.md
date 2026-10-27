# hhy-huang/HiRAG

⭐ 555 · Python · MIT · 推送 2026-06-16 · [GitHub](https://github.com/hhy-huang/HiRAG) · [官网](https://arxiv.org/pdf/2503.10150) · 组织维护

**基于分层知识的 Graph RAG 系统，EMNLP 2025 Findings 论文**

HiRAG 是论文《Retrieval-Augmented Generation with Hierarchical Knowledge》（EMNLP 2025 Findings）的官方实现，一个基于分层知识组织的 Graph RAG 系统。用户通过 Python API 执行查询，LLM 与检索 API 可在 config.yaml 中配置，README 提供 DeepSeek、ChatGLM、OpenAI 的接入示例脚本；同时附完整评测流程：抽取上下文、插入图数据库、生成回答并用 LLM 批量评估，与 Naive RAG、GraphRAG、LightRAG、FastGraphRAG、KAG 在四个数据集上给出胜率对比表。安装方式为 clone 后 pip install -e .。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层知识组织的 Graph RAG 检索生成
- 支持 DeepSeek / ChatGLM / OpenAI 等第三方 API 配置
- 内置数据集抽取、图数据库插入与 LLM 批量评测流程
- 提供与 Naive RAG、GraphRAG、LightRAG、FastGraphRAG、KAG 的四数据集对比结果

## 适用场景

- 搭建基于分层知识的 Graph RAG 问答系统
- 在 Mix/CS/Legal/Agriculture 等数据集上评测 RAG 方法
- 复现或对比 Graph RAG 类方法的实验结果

## 场景标签

`RAG` `知识图谱` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: - This is the repo for the paper HiRAG: Retrieval-Augmented Generation with Hierarchical Knowledge.
> L24: graph_func = HiRAG(

## 星数曲线

```mermaid
xychart-beta
    title "hhy-huang/HiRAG 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 554 --> 557
    line [556, 555, 555]
```

2026-10-18 556 → 2026-10-27 555（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `972ae4b28a86` · [字段定义](../../DATASET.md)*
