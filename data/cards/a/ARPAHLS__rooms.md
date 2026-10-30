# ARPAHLS/rooms

⭐ 20 · Python · NOASSERTION · 推送 2026-09-04 · [GitHub](https://github.com/ARPAHLS/rooms) · [官网](https://arpacorp.net) · 个人维护

**本地优先的多智能体编排框架：结构化会话空间中运行 AI 智能体**

Python 编写的多智能体编排框架，在结构化会话空间中测试、模拟并协调多个 AI 智能体。通过 LiteLLM 将请求路由到本地模型（如 Ollama）或商业 API，声明零数据外泄的本地优先设计。支持轮询/辩论/动态三种发言编排、按专业度对智能体评分的动态路由、@AgentName 指定发言、PASS 跳过机制、人机回环、全局协调者与时间戳会话记忆；也可绕开 LLM 接入自定义 Python 推理函数。默认会话数据仅存内存，退出时可导出 Markdown/CSV。以 git clone 源码方式安装，运行交互式 CLI 向导。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- round_robin/argumentative/dynamic 三种发言编排模式
- 动态模式下按专业度评分选择下一个发言的智能体
- 经 LiteLLM 路由到本地 Ollama 或商业 API，支持自定义 Python 推理函数
- 时间戳会话记忆，RAM-only 默认，退出时可导出 Markdown/CSV

## 适用场景

- 搭建多个 AI 智能体围绕议题讨论的模拟会话
- 在本地离线模型上测试多智能体协作流程
- 为不同智能体配置不同人格、温度与技能后观察群体行为

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: **Rooms** is a robust, highly-configurable framework designed for testing, simulating, and orchestrating multiple A
> L20: - **Dynamic Turn Orchestration**: Agents interact via `round_robin`, `argumentative`, or `dynamic` relevance-based 
> L21: - **Expertise-Weighted Selection**: In `dynamic` mode, agents are scored against the live topic context — the most 

## 星数曲线

```mermaid
xychart-beta
    title "ARPAHLS/rooms 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `33f1416656cf` · [字段定义](../../DATASET.md)*
