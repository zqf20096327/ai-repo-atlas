# hankbesser/recursive-agents

⭐ 46 · Python · MIT · 推送 2025-12-10 · [GitHub](https://github.com/hankbesser/recursive-agents) · 个人维护

**面向开发者的自我改进 LLM Agent 元框架，含可追溯迭代记录**

以草稿-批判-修订三阶段迭代架构构建自我改进 LLM Agent 的 Python 元框架。每个 Companion 实例记录完整修订历史、停止条件与决策依据（run_log），模板以 .txt 文件存放并支持热重载；新领域只需继承 BaseCompanion 并指向模板即可生成完整 Agent。实例本身可作为可调用对象或 RunnableLambda 嵌入 LangGraph 等框架。提供 Streamlit 交互应用与多 Agent 编排示例。限制：安装说明仅展示 conda 创建环境步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Draft→Critique→Revision 三阶段链自动构建，无需手工接线
- 内置 run_log 追踪全部迭代与决策依据
- 模板为磁盘 .txt 文件，Git 可追踪变更且支持热重载
- 每个实例可作为 agent() 或 RunnableLambda 兼容 LangGraph 等框架

## 适用场景

- 构建会自我批判与修订输出的领域 Agent
- 审计 LLM 每轮回答的修订过程与决策理由
- 在 LangGraph 中编排多个递归 Agent 并保留透明性

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: Recursive Agents implements a **three-phase iterative refinement architecture** where LLM agents (instances of Class
> L28: |**Every Companion instance is itself an `agent()` or `RunnableLambda(agent)`**|Same object works standalone or in 
> L115: #### **LangGraph** (Parallel Execution + RA Transparency):

## 星数曲线

```mermaid
xychart-beta
    title "hankbesser/recursive-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3191c0b6423a` · [字段定义](../../DATASET.md)*
