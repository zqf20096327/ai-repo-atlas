# carbon-design-system/Carbon-Monitor

⭐ 24 · JavaScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/carbon-design-system/Carbon-Monitor) · 组织维护

**面向 Carbon 设计系统的 AI PR 审查器与 IBM Cloud 定时 agent 运行框架**

Carbon Monitor 由两部分组成：一是 carbon-design-system/carbon 单仓的自动 PR 审查器，每个开放 PR 经 IBM Bob（默认）或 Claude 的 CLI agent 审查，Carbon 相关声明（组件 props、tokens、图标、无障碍模式）通过 Carbon MCP 服务器核验，结果以一条含内联评论与建议摘要的 GitHub review 形式发布；二是可复用的 agent 运行框架，部署在 IBM Cloud Code Engine，提供定时调度、并发运行、单次花费上限、Web 控制台、Elasticsearch 遥测与 Slack 摘要。附带 adapt-harness 技能可适配其他仓库、任务或 agent。运行审查需 IBM 网络访问（Bob）与 IBMid 认证的 Carbon MCP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- IBM Bob / Claude 双 agent 支持，一个环境变量切换，其他 CLI 需一个适配文件
- Carbon MCP 核验 Carbon API 相关声明（code_search、docs_search 等工具）
- IBM Cloud Code Engine 上的定时调度、花费上限、Elasticsearch 遥测与 Slack 摘要
- adapt-harness 技能引导最多十个问题生成适配 SPEC

## 适用场景

- 自动审查 Carbon Design System 仓库的开放 PR 并发布结构化评审
- 把 harness 指向自己的仓库或其他系统（Jira、ServiceNow、数据库）定时运行 agent 任务
- 团队通过 Slack 接收每日 PR 审查摘要，通过控制台查看花费与运行状态

## 场景标签

`代码审查` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Carbon Monitor is two things. It is a working reviewer for the
> L13: instead. It is also a harness for running any agent on a schedule in IBM Cloud, with cost
> L57: The agent is IBM Bob or Claude. Carbon Monitor is the harness around it:


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `923750947436` · [字段定义](../../DATASET.md)*
