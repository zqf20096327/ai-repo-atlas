# haileyok/victrola

⭐ 28 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/haileyok/victrola) · 个人维护

**单人操作的个人 AI agent 运行环境，支持自我修改与并行工具调用**

通用个人 AI agent harness（harness/运行时）：操作者通过本地 Web 界面或 Discord 与 agent 对话，agent 在沙箱化 Deno 进程中编写并运行 TypeScript 代码来完成任务，Python 侧承载实际网络/存储操作。具备基于条目与 RAG 的持久记忆（SQLite + FTS5 + 向量检索）、定时任务与条件触发器、经操作者审批的 agent 自写工具、AT Protocol/Bluesky 集成。支持 Anthropic、OpenAI 及 Ollama/llama-cpp 等 OpenAPI 兼容端点。README 声明无安全保证，依赖 Deno 沙箱而非强隔离（如 Firecracker）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 execute_code 原语：agent 写 TypeScript 链式调用工具，减少每调一次往返
- Deno 沙箱最小权限：作用域文件系统、无网络、256MB 堆、60s 超时
- 条目式记忆 + RAG 回忆，FTS5 与向量（本地 Ollama nomic-embed-text）混合检索
- 定时任务与条件触发器（TypeScript 条件脚本，需操作者批准）

## 适用场景

- 通过 Discord 或本地网页让 agent 代我写代码完成日常任务
- 让 agent 定时检查 Bluesky 提及并按条件唤醒处理
- 积累可复用技能与记忆的长期个人助手

## 场景标签

`AI 助手` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8: A general-purpose personal AI agent harness. You chat with it through a local web interface or through Discord. It w
> L10: Victrola is a single-operator agent runtime. You (the operator) drive it through chat. The agent has persistent mem
> L12: Victrola supports Anthropic, OpenAI, or any OpenAPI compatible endpoint like Ollama or llama-cpp.

## 星数曲线

```mermaid
xychart-beta
    title "haileyok/victrola 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c2830bf7c3c3` · [字段定义](../../DATASET.md)*
