# randombet/bodhi_realtime_agent

⭐ 16 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/randombet/bodhi_realtime_agent) · [官网](https://randombet.github.io/bodhi_realtime_agent/) · 个人维护

**基于 Gemini Live API 构建实时语音 agent 应用的 TypeScript 框架**

面向开发者的 TypeScript 框架，基于 Google Gemini Live API 构建实时双向语音 agent 应用。核心机制：多 agent 人格与运行中转移（transfer_to_agent）、Zod 校验的 inline/background 两种工具模式——后台长任务交给 Vercel AI SDK 子代理执行，Gemini 对话不中断；音频走低延迟快路径直连客户端与 Gemini。还提供用户事实自动提取与 JSON 持久化的记忆系统、基于 resumption handle 的会话恢复、类型安全 EventBus 与生命周期钩子。要求 Node.js >= 22 与 Google API key，pnpm 安装；License 为 UNLICENSED。

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

- 双向音频流式传输与服务端轮次检测
- 后台子代理执行长任务时对话不中断
- 多 agent 定义与运行中 agent 转移
- 用户事实自动提取、跨会话 JSON 持久化

## 适用场景

- 构建带多角色的实时语音对话 agent 应用
- 在语音对话中执行长时间后台任务且不打断交流
- 需要会话恢复与事件观测的语音 agent 后端

## 场景标签

`语音 Agent` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: TypeScript framework for building real-time voice agent applications using the Google Gemini Live API.
> L10: - **Background subagents**: Long-running tool calls hand off to Vercel AI SDK subagents while Gemini keeps talking

## 星数曲线

```mermaid
xychart-beta
    title "randombet/bodhi_realtime_agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bc9eacb0e014` · [字段定义](../../DATASET.md)*
