# Haohao-end/Ctrip-Style-AI-Travel-Assistant

⭐ 57 · Python · 推送 2026-01-10 · [GitHub](https://github.com/Haohao-end/Ctrip-Style-AI-Travel-Assistant) · 个人维护

**基于 LangGraph 的多 Agent 旅行服务系统，含人工确认机制**

基于 LangChain 与 LangGraph 构建的有状态多 Agent 旅行服务系统，模拟旅行社业务：主助手识别意图并动态路由至机票、酒店、租车、行程四个子 Agent。机制上采用 Hub-and-Spoke 架构与 dialog_stack 管理子 Agent 生命周期，将工具分为只读安全工具与写操作敏感工具，敏感操作通过 interrupt_before 中断并由用户输入确认，用 MemorySaver 持久化会话状态，工具失败时由 fallback 机制交还 LLM 修复。以 Python 仓库形式提供，需配置 OpenAI 与 Tavily API key，通过 CLI 交互运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 主助手 + 4 个专门子 Agent 的动态路由与 dialog_stack 生命周期管理
- 安全/敏感工具分级，敏感操作经 human-in-the-loop 确认后执行
- MemorySaver 会话状态持久化，支持中断恢复
- 工具调用失败的 fallback 处理，交还 LLM 修正查询

## 适用场景

- 体验多 Agent 编排与人工确认的完整旅行预订流程
- 学习 LangGraph 状态机、任务委派与权限控制实现
- 作为客服/预订类对话系统的参考实现

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: An advanced, multi-agent intelligent service system based on **LangChain** and **LangGraph**, designed to simulate a
> L11: Traditional chatbot systems often struggle with state management in long-running conversations and the safe executi
> L25: 3. **Human-in-the-Loop:** Automated workflow interruption (`interrupt_before`) for sensitive operations, requiring 

## 星数曲线

```mermaid
xychart-beta
    title "Haohao-end/Ctrip-Style-AI-Travel-Assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-25 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f9c5098f223b` · [字段定义](../../DATASET.md)*
