# mhiqrambg/systemone-decision-mcp

⭐ 3 · TypeScript · MIT · 推送 2026-11-03 · [GitHub](https://github.com/mhiqrambg/systemone-decision-mcp) · 个人维护

**MCP 服务器：为 OpenCode Agent 在调用前决定需要哪些工具与技能**

面向 OpenCode Agent 的 MCP 路由服务器：在 Agent 发起调用前判定任务实际需要哪些 MCP 工具与技能，输出 required/recommended/optional/not_recommended 分级建议及优先级。决策来自经 OpenAI 风格 API 访问的远程决策模型，不可达时回退到确定性规则引擎，响应标注来源引擎。提供 8 个 systemone_* 工具覆盖任务决策、单工具判定、执行审计与结果评估；不执行任何被推荐的工具或技能，仅提供建议。要求 Node 20+、npm 9+、OpenCode v2。

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

- 调用前工具/技能路由，输出分级建议与优先级阈值
- 模型引擎与规则引擎双路径，响应标注 decision_source
- 任务后执行审计与利用率评估（systemone_audit_execution 等）
- 索引 OpenCode 目录下的 SKILL.md frontmatter 做技能推荐

## 适用场景

- 复杂任务前判断哪些 MCP 工具值得调用以节省时间与上下文
- 为写作、审阅、研究类任务匹配已有技能
- 任务结束后对比计划与实际调用，核查遗漏的必需工具

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: An MCP server that tells an OpenCode agent which MCP tools and skills a task actually
> L6: Decisions come from a remote decision model reached over an OpenAI-style API. When that
> L24: It cannot invoke, filter, or observe other MCP servers. MCP has no primitive for that, and

## 星数曲线

```mermaid
xychart-beta
    title "mhiqrambg/systemone-decision-mcp 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-16 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f2e4cebdf985` · [字段定义](../../DATASET.md)*
