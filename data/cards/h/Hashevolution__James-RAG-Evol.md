# Hashevolution/James-RAG-Evol

⭐ 21 · Python · MIT · 推送 2026-09-29 · [GitHub](https://github.com/Hashevolution/James-RAG-Evol) · [官网](https://www.bestpractices.dev/projects/12806) · 个人维护

**本地优先的可审计知识平台：Graph-RAG + 审计日志 + 状态重放**

SEKOS（内部引擎代号 JAMES）是一个本地优先的知识平台：查询经 RBAC/ABAC 安全校验后进入 BM25+稠密混合检索、Graph-RAG 本体遍历与推理循环，产出回答。核心机制为 Replayable RAG——所有推理步骤写入 append-only 审计日志，reconstruct_graph_at(t) 可按字节重建任意历史知识状态；矛盾仲裁用 LLM-free 的确定性 4 规则决策树；自演化改动需人工审批。默认在本地 Ollama 上运行，需 Python 3.11+ 与至少 16GB 内存；明确声明不做 LangChain 的替代品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 审计日志可逐字节重放任意历史知识状态（reconstruct_graph_at(t)）
- LLM-free 的确定性矛盾仲裁与 T1/T7 时效版本链
- 默认 100% 本地 Ollama 运行，云为按查询可选
- 自演化改动经 propose→审批→部署→回归自动回滚的人工门控

## 适用场景

- 需要回答'系统在 T 时刻知道什么、为什么这么说'的审计场景
- 合规要求知识状态可重放、数据不出本地的企业部署
- 时点查询：取回某文档在过去某时间点有效的版本

## 场景标签

`RAG` `知识图谱` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: > A local-first, auditable knowledge platform with Graph-RAG retrieval,
> L42: |**Local-first execution**|Cloud-default (OpenAI / Anthropic API calls in every retrieval)|Runs on local Ollama (ge
> L111: **The flow in one sentence**: a user query passes through 3-stage security (RBAC + ABAC + instruction isolation), 

## 星数曲线

```mermaid
xychart-beta
    title "Hashevolution/James-RAG-Evol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `6e6bef963c56` · [字段定义](../../DATASET.md)*
