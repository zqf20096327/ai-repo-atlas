# rokbenko/quackd

⭐ 268 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/rokbenko/quackd) · [官网](https://www.quackd.org) · 个人维护

**多机器人统一 CLI：为每台机器人接 LLM 大脑并发目标指令**

面向机器人拥有者的命令行工具：通过适配器声明每台机器人的身体与技能清单，注册后可用自然语言目标驱动，由 LLM 逐技能挑选执行，多机组成 flock 时各自带模型并分工。支持 Claude/OpenAI/Gemini/Grok 等云 API 及 Ollama/vLLM/llama.cpp/LM Studio 本地模型，可选 decision LLM（非文本生成）。收录 9 个机体，其中仅 SO-101 臂经 LeRobot 在真实硬件运行，其余 8 个处于模拟或 mock 阶段。无机器人时可用自带卡通/ MuJoCo 物理模拟器。Apache 2.0，Python 3.11+，PyPI 发布，MCP 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 按技能清单逐步选择执行机器人目标，契约限定技能/步数/人工确认
- 支持多家云 API 与 Ollama/vLLM/llama.cpp/LM Studio 本地模型（无 key）
- 可选 --decision-llm 打分式决策（不生成文本），支持 shadow 模式
- 9 个机体适配器；无实体机器人可用卡通或 MuJoCo 模拟器（种子测试 10/10 通过）

## 适用场景

- 把拥有的多台机器人注册到一个 CLI 统一下达目标指令
- 让带轮/带臂的机器人组队分工协作完成任务
- 无实体机器人时在模拟器中试用目标驱动机器人控制

## 场景标签

 · 领域:机器人/具身智能

## 证据(README 行号)

> L3:  One CLI for all your robots. Connect them, command them, and let them work together, each with an LLM for a brain.
> L41: **quackd** is a command line for the robots you own. Each one joins through an adapter that declares, as a manifest
> L45: **One of the nine bodies runs on real hardware, and the recording above is it.** On 2026-09-15 an SO-101 follower a

## 星数曲线

```mermaid
xychart-beta
    title "rokbenko/quackd 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 262 --> 269
    line [263, 266, 268]
```

2026-10-18 263 → 2026-10-22 268（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `775b8c0d8f6e` · [字段定义](../../DATASET.md)*
