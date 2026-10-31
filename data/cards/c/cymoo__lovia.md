# cymoo/lovia

⭐ 18 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/cymoo/lovia) · [官网](https://cymoo.github.io/lovia) · 个人维护 · 中文 README

**轻量 Python AI Agent 框架：覆盖工具、会话、上下文压缩与服务**

面向开发者的 Python agent 框架，核心依赖仅 httpx/pydantic/pyyaml。提供 Agent（不可变配置）、Runner 执行、@tool 工具封装、结构化输出、多 agent（Handoff/Agent-as-tool/Subagents）、会话持久化、checkpoint 幂等重放、上下文压缩（只改模型视图以保持 prompt 前缀稳定）、guardrails、预算与审批、Workspace 文件/Shell 沙箱、Skills/MCP/Todo/Memory 插件、FastAPI Web UI 与行为评测套件。内置 OpenAI 与 Anthropic 兼容端点，自定义 provider 实现一个 Protocol 即可。

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

- 核心依赖仅 httpx/pydantic/pyyaml，按需安装 extras
- 上下文压缩只改下一轮模型视图，保持 prompt 前缀稳定以利缓存
- checkpoint 幂等重放：重发已完成 run_id 不再调用模型
- Skills/MCP/Todo/Memory 统一走同一插件扩展轴

## 适用场景

- 用普通 Python 组合原语构建自有 agent 循环
- 一行命令起带记忆与技能的 chat Web 服务
- 给敏感工具加审批、预算与 guardrail 后接入自有应用
- 用 ScriptedProvider 离线测试真实 agent 循环

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: lovia is an elegant, restrained Python framework for developers who want to
> L55: - **Lightweight model integration.** OpenAI, Anthropic, and compatible

## 星数曲线

```mermaid
xychart-beta
    title "cymoo/lovia 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-26 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `68c7b82e70c4` · [字段定义](../../DATASET.md)*
