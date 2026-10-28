# dog-last/E-mem

⭐ 31 · Python · Apache-2.0 · 推送 2026-05-03 · [GitHub](https://github.com/dog-last/E-mem) · 组织维护

**面向 LLM Agent 的情景记忆重建框架（ICML 2026）**

E-mem 是为 LLM Agent 提供记忆管理的框架，针对 RAG 与长上下文系统中的'破坏性去语境化'问题，采用 Master-Assistant 异构层级架构：Master Agent 负责全局规划与推理综合，Assistant Agents 维护未压缩记忆块并在激活片段内做局部推理提取证据。路由机制结合全局对齐、语义关联与符号触发三种信号，支持 KV Cache 与纯文本两种存储模式。提供 LoCoMo 与 HotpotQA 基准复现脚本，基于 uv 管理依赖，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Master-Assistant 多智能体架构：全局规划与局部记忆推理解耦
- 三信号正交路由（摘要意图过滤/向量相似度/关键词实体匹配）
- KV Cache 缓存内部神经表示以减少重复编码开销
- 提供 LoCoMo 与 HotpotQA 基准自动化评测脚本

## 适用场景

- 为我的 LLM Agent 构建带情景重建的长程记忆系统
- 在长对话多跳推理任务上评测记忆框架效果
- 复现论文中 LoCoMo / HotpotQA 基准实验结果

## 场景标签

`Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L13: **E-mem** is a novel memory framework designed to address the "destructive de-contextualization" problem in traditi
> L15: Inspired by biological engrams, E-mem employs a **Heterogeneous Hierarchical Architecture**:
> L110: To reproduce the results presented in our paper, we provide automated scripts for both **LoCoMo** and **HotpotQA**

## 星数曲线

```mermaid
xychart-beta
    title "dog-last/E-mem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `25b4e093fef6` · [字段定义](../../DATASET.md)*
