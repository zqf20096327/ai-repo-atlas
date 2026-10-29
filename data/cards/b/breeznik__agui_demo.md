# breeznik/agui_demo

⭐ 18 · JavaScript · 推送 2026-08-19 · [GitHub](https://github.com/breeznik/agui_demo) · 个人维护

**无框架前端的 AG-UI + LangGraph agent 接线参考实现**

一个航班预订演示（Breeze），用 AG-UI 协议把 LangGraph ReAct agent 接到浏览器：流式输出、工具调用、共享状态与 human-in-the-loop 中断。提供 React (Vite) 与无构建的 vanilla JS 两个行为一致的前端，共用同一套协议代码。后端 FastAPI + Poetry，自带密钥（BYOK），密钥经请求头传入、服务器不存储。作者声明代码由 AI agent 编写、非人工维护，定位是参考而非依赖。含 106 个无需网络与密钥的测试。

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

- React 与无框架 vanilla JS 双前端，共用同一协议代码
- human-in-the-loop 中断（confirm_booking 暂停等待用户确认）
- 自带密钥（BYOK）：服务器不保存任何 API key
- 63 个后端测试与 43 个前端测试，无需网络与密钥

## 适用场景

- 在无 Next.js/CopilotKit 的既有前端中接入 AG-UI 协议
- 学习 AG-UI + LangGraph 的中断恢复与共享状态接线方式
- 参考带外密钥传递与服务端部署的安全做法

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: A LangGraph ReAct agent talking to a browser: streaming, shared state, tool
> L60: |how the browser talks to the agent|`frontend/src/hooks/useAgentChat.js` ← **copy this one**|

## 星数曲线

```mermaid
xychart-beta
    title "breeznik/agui_demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `b8b285e91b2a` · [字段定义](../../DATASET.md)*
