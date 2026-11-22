# Manomenu/suwalski-agent-eval

⭐ 3 · C# · MIT · 推送 2026-11-21 · [GitHub](https://github.com/Manomenu/suwalski-agent-eval) · 个人维护

**给 AI agent 做回归测试与生产监控的评测框架**

Suwageval 用单元测试的方式测试 LLM agent：场景以 YAML 形式存放于 agent 仓库，框架多次向运行中的 agent 发送对话并判定检查结果；结合历史区分真回归与噪音，回归/新失败/agent 错误使 CI 失败。提供 7 种检查类型（工具调用、事件、引用、文本、模型评判）、多轮模拟用户、sweep 对比、以及上线后的生产会话监控与一键转场景。交付形态包括 Web 应用、CLI、CI 退出码与 Claude Code 插件，服务端基于 ASP.NET Core 与 PostgreSQL。

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

- 8 种检查状态区分回归、噪音与不稳定，仅真回归使 CI 失败
- 按 agent 契约哈希做版本 diff，追踪 prompt/模型/工具变化
- 生产会话监控并可一键把失败会话转为回归场景
- 提供 Web 应用、CLI、CI 与 Claude Code 插件四种入口

## 适用场景

- agent 发版前跑回归测试，改 prompt 后查看哪些检查变差
- 为不同模型或 prompt 配置做 sweep 对比
- 收集线上失败会话转化为回归场景
- 在 Claude Code 中用自然语言编写和修复测试场景

## 场景标签

`模型评测` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L1: Suwageval — regression tests for LLM agents before a release, and checks on their real conversations after it. Scena
> L3: **Suwageval** tests LLM agents the way unit tests test code. Scenarios — a conversation plus checks on the agent's n
> L10:  How it works. 1 Write (you): suwageval/scenarios/*.yaml, a conversation and checks on the answer. 2 Run (evaluatio


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `1aa11a14eff7` · [字段定义](../../DATASET.md)*
