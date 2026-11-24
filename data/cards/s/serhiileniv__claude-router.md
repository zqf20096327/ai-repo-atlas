# serhiileniv/claude-router

⭐ 10 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/serhiileniv/claude-router) · [官网](https://serhii-leniv.github.io/claude-router/) · 个人维护

**给 Anthropic API 用户省钱：自动按复杂度路由请求到便宜模型**

自托管的 Anthropic 兼容代理，通过 ANTHROPIC_BASE_URL 接入 Claude Code、Cursor、Cline 或自有 SDK 代码，零代码改动地把每个请求按任务复杂度路由到 Haiku/Sonnet/Opus 等层级。路由采用合取门控启发式（默认），可切换 AI 分类或混合模式；含参数归一化、截断自动升级、限流自动回退、Sonnet 下限保护。每次响应报告相对基线的节省金额，支持 stats 统计与 dashboard。通过 npm 全局安装，提供 install 一键配置与 status/stop/doctor 等管理命令。

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

- 按请求复杂度自动路由 Haiku/Sonnet/Opus，零代码改动
- heuristic/ai/hybrid 三种分类模式，决策带可审计 reason
- 截断自动升档重试、429 自动回退、参数归一化防 400
- Claude Code 编排模式：五个角色 agent 按层级分流

## 适用场景

- 混合难易流量的 Anthropic API 计费场景降低模型成本
- Claude Code 主会话钉住 Opus、子 agent 路由到便宜层级
- 自托管代理查看每次调用实际节省的金额

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13: **Cut your Anthropic API bill by routing every request to the cheapest Claude model that can handle it — Haiku, Son
> L32: |🔌 **Zero code changes**|Point any Anthropic app at the proxy via `ANTHROPIC_BASE_URL`, or `import` it as a library


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `e7232f4d3df7` · [字段定义](../../DATASET.md)*
