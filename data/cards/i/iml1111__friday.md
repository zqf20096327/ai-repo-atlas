# iml1111/friday

⭐ 15 · Python · 推送 2026-10-04 · [GitHub](https://github.com/iml1111/friday) · 个人维护

**构建服务端 AI agent 的领域无关 agent 循环 SDK**

Python SDK，提供由调用方驱动的 turn 循环：调用 FridayAgent.step()，内部走 LLM 调用并按 stop_reason 分支——end_turn 结束、tool_use 则运行工具后继续循环；上下文溢出时由调用方裁剪状态并调用 engine.compact() 压缩。LLM 后端通过实现 LLMProvider 接口切换（内置 Anthropic/OpenAI 适配器，API key 一律外部注入），工具与内存存储同样以接口注入方式扩展。内置 TODO 跟踪工具与可选的持久化记忆，面向在服务器端构建非编程领域的 AI agent 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用方驱动 step() 的 turn 循环，含 stop_reason 分支与上下文压缩 compact()
- LLM/工具/内存三个注入接口，可不改核心循环替换后端
- API key 仅外部注入，库内不读环境变量
- 内置 TodoWrite 工具与可选持久化记忆（memory_save/read/delete）

## 适用场景

- 在服务器端搭建自定义 AI agent 的基础循环
- 为不同领域需求注入工具与领域压缩要求
- 在 Anthropic/OpenAI 等后端间切换而复用循环逻辑

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Built by analyzing how several agent loops (agentic loops) work, this is a **domain-agnostic + LLM-agnostic** SDK
> L4: for **running agent loops on the cloud/server side**.
> L5: The goal is to serve as a foundation for building AI agents for a wide range of purposes beyond programming.

## 星数曲线

```mermaid
xychart-beta
    title "iml1111/friday 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4a470692b3c7` · [字段定义](../../DATASET.md)*
