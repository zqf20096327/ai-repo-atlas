# przeprogramowani/agent-forum

⭐ 20 · TypeScript · 推送 2026-09-13 · [GitHub](https://github.com/przeprogramowani/agent-forum) · [官网](https://10xdevs.pl) · 组织维护

**让两个 AI Agent 进行多轮结构化对话并汇总的 TypeScript 库**

TypeScript 库，编排两个互补角色（如领域专家与知识提取者）的 Agent 进行指定轮次的多轮对话，每条消息连同时间戳、token 用量与上下文存为 markdown 文件形成审计记录；对话结束后可由可选的第三个 summarizer Agent 将原始对话转化为 PRD、分析等结构化交付物。模型通过 Vercel AI SDK 接入，支持依赖注入 mock LLM 服务与自定义对话策略以便测试。尚未发布到 npm，需从源码 clone 运行，API key 通过 .env 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 两 Agent 多轮角色对话编排，每轮基于完整上下文
- 消息落盘为 markdown（含时间戳、token 用量等元数据）形成审计记录
- 可选 summarizer Agent 将对话蒸馏为结构化输出
- 依赖注入 mock LLM 服务与自定义会话策略，无需真实 API 调用即可测试

## 适用场景

- 让两个不同角色的 Agent 深入探讨一个主题并留存完整对话记录
- 把 Agent 对话自动整理为 PRD、行动项等结构化文档
- 在 CI 中用 mock LLM 服务测试多 Agent 对话逻辑

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: A TypeScript library for enabling AI Agents to communicate with each other in structured conversations.
> L50: - [X] Core functionality works within the repository
> L51: - [ ] Published as standalone package on npm

## 星数曲线

```mermaid
xychart-beta
    title "przeprogramowani/agent-forum 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8d44e36cf7a2` · [字段定义](../../DATASET.md)*
