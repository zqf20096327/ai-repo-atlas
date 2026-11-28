# larkxai/larkx

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/larkxai/larkx) · [官网](https://larkx.ai) · 组织维护

**移动端持久化 AI Agent 执行运行时 SDK**

面向移动设备的开源执行运行时，供开发者在手机上构建可离线运行、可崩溃恢复的 AI Agent。核心机制：用设备端 SQLite 保存执行记录，C++ 运行时决定下一步模型调用、工具调用或远程委派；已提交步骤崩溃后不重复执行，非幂等中断进入 BLOCKED 并经 reconcile 恢复。本地通过可选 Cactus 适配器接入模型（如 qwen3-0.6b），远程通过 HTTP 任务协议或 A2A 1.0 JSON-RPC 委派给 LangGraph/Google ADK/OpenAI Agents SDK 等部署的服务。目前公开 SDK 为 React Native（npm，0.2.0），Swift/Kotlin 尚在计划中；README 声明尚未在真机上完成下载与推理验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SQLite 持久化的持久执行与崩溃恢复（已提交步骤重放、幂等重试、reconcile）
- 可选 Cactus 本地推理引擎适配器，模型按实例排队
- HTTP 任务协议与 A2A 1.0 JSON-RPC 的远程 Agent 委派
- 默认无远程 Agent 时仅在本机运行，提示词与工具结果留在设备

## 适用场景

- 在手机上运行离线可用的本地 Agent
- 本地 Agent 把单个任务委派给 LangGraph 等远程服务并保持父运行在设备端
- 需要进程被杀后从上次提交点恢复的移动 Agent 应用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: LarkX is an open-source, mobile-first execution runtime for building durable, offline-first AI agents that can coll
> L22: LarkX keeps one execution record in SQLite on the device. The C++ runtime decides the next model call, tool call, o
> L118: Implemented today: the React Native SDK, the shared C++ runtime, SQLite, native tools, optional Cactus, the HTTP d


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `1af993ca2cf4` · [字段定义](../../DATASET.md)*
