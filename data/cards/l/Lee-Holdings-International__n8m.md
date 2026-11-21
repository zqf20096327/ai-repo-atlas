# Lee-Holdings-International/n8m

⭐ 10 · TypeScript · MIT · 推送 2026-04-06 · [GitHub](https://github.com/Lee-Holdings-International/n8m) · 组织维护

**给 n8n 用户的 AI CLI：从命令行生成、修改、测试、部署工作流**

以 TypeScript/oclif 构建的 CLI，围绕用户的 n8n 实例封装 agentic 层：自然语言描述经 Architect/Engineer/QA 三阶段管道生成工作流 JSON，支持对本地或线上工作流做修改、生成含 Mermaid 图的文档、针对实例校验并自动修复失败。提供 fixture 离线回放测试、模式库提取（learn）、MCP server 暴露 8 个工具、HITL 暂停与 SQLite 会话持久化。凭据本地保存，需自备 AI key 与 n8n 实例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Architect→Engineer→QA 三阶段 agent 管道生成并校验工作流
- fixture 捕获真实执行数据，支持离线回放测试与 AI 修复循环
- n8m mcp 将生成/修改/测试/部署能力以 MCP 工具暴露给客户端
- 模式库（patterns）注入提示词以复用已验证的工程做法

## 适用场景

- 用自然语言生成 n8n 工作流并直接部署到实例
- 对现有工作流做 AI 辅助修改与失败自动修复
- 无 n8n 实例时用 fixture 离线回归测试工作流
- 通过 MCP 客户端（如 Claude Desktop）调用工作流操作工具

## 场景标签

`工作流自动化` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L16: **Stop clicking. Start shipping.** `n8m` is an open-source CLI that wraps your
> L71: Describe what you want and the agentic pipeline designs, builds, and validates
> L290: Expose `n8m`'s agentic capabilities as tools to any


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ad14e97215c1` · [字段定义](../../DATASET.md)*
