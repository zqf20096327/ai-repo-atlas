# jcartu/rasputin-memory

⭐ 33 · Python · MIT · 推送 2026-04-25 · [GitHub](https://github.com/jcartu/rasputin-memory) · 个人维护

**已归档的 LLM agent 对话记忆系统：事实分道检索研究代码**

面向 LLM agent 的长期对话记忆系统研究代码库，已归档停止维护，以 sprint-2-integration 最终状态发布。核心机制：将检索按四类事实分道（窗口/事实/实体/事件），用交叉编码器 Qwen3-Reranker 重排，后端为 Qdrant 与 FalkorDB，通过 HTTP API（端口 7777）与 MCP server 提供服务。LoCoMo 基准 72.40%，作者声明落后 SOTA（Hindsight 89.61%）约 17 个百分点，建议生产需求先评估 Hindsight。包含消融方法论文档与回归测试集，MIT 许可，欢迎 fork。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四事实分道检索 + Qwen3-Reranker 重排的架构
- 提供 HTTP API 与 MCP server 两种接入方式
- 33 题回归语料 + LoCoMo 评测 harness 与消融纪律文档
- FalkorDB 图基础设施已具备但未集成图遍历到检索路径

## 适用场景

- 研究 agent 记忆的分道检索架构与调参方法
- fork 后在其基础上继续改进记忆检索
- 参考其消融纪律文档设计检索评测流程

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L23: RASPUTIN is a long-term conversational memory system for LLM agents. It maintains a persistent store of memories ex
> L102: - HTTP API + MCP server

## 星数曲线

```mermaid
xychart-beta
    title "jcartu/rasputin-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c17cf76b5110` · [字段定义](../../DATASET.md)*
