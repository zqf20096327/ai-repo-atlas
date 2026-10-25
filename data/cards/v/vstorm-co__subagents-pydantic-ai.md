# vstorm-co/subagents-pydantic-ai

⭐ 62 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/vstorm-co/subagents-pydantic-ai) · [官网](https://vstorm-co.github.io/subagents-pydantic-ai/) · 组织维护

**给开发者的 Pydantic AI 多智能体委派框架**

基于 Pydantic AI 的 Python 库，为任意 agent 增加多智能体委派能力：可生成可嵌套的专家子 agent，支持 sync/async/auto 三种执行模式、运行时动态创建 agent、后台任务 token 跟踪与协作式/强制取消。提供 Capabilities API 与 Toolset API 两种接入方式，支持 YAML/JSON 声明式配置子 agent，以及后台子 agent 的追问、转向与取消。属于 Pydantic Deep Agents 生态组件之一，可独立使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- sync/async/auto 三种执行模式与任务取消
- 运行时动态创建 agent（DynamicAgentRegistry）
- YAML/JSON 声明式配置（SubAgentSpec）
- 后台子 agent 可被父 agent 追问、转向与取消

## 适用场景

- 让研究助手把任务委派给专家子 agent 并汇总
- 代码评审系统中安全/风格/性能 agent 并行工作
- 按数据量动态生成处理 worker 的数据流水线

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L33: **Subagents for Pydantic AI** adds multi-agent delegation to any Pydantic AI agent. Spawn specialist subagents that
> L245: This library is one piece of a broader open-source toolkit for production AI agents — all built on **Pydantic AI**

## 星数曲线

```mermaid
xychart-beta
    title "vstorm-co/subagents-pydantic-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-25 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `605022f4ae5e` · [字段定义](../../DATASET.md)*
