# XiaoTongYuCode/CornAgent

⭐ 22 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/XiaoTongYuCode/CornAgent) · [官网](https://cornagent.xiaotongyu.com) · 个人维护 · 中文 README

**可自托管、可嵌入的全栈 AI agent 应用与运行时**

开源全栈 AI agent 项目：React 聊天页与侧边栏组件共享同一 Provider，FastAPI 运行时负责工具调用、并行多 agent 子任务与持久执行状态。模型经 LiteLLM 接入，默认 DeepSeek，兼容 OpenAI 风格 API；PostgreSQL 持久化会话与运行状态，Redis Streams 交付实时事件，支持 SSE 流式、暂停恢复、检查点接管与租约防旧写。面向想自建或向现有产品嵌入 agent 侧边栏的开发者；组件以源码提供，暂无独立 npm 包，恢复依赖 PostgreSQL 与附件存储完好。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SSE 流式输出、暂停恢复与服务重启后从检查点安全接管
- 主 agent 派发并行子任务，子任务有独立持久状态与取消机制
- 可嵌入 React 侧边栏/聊天页，与独立部署共享同一运行时
- PostgreSQL 持久状态 + Redis Streams 事件交付，租约与 fencing token 防旧执行器写入

## 适用场景

- 自托管一个带会话、附件与分支管理的 AI agent 应用
- 把 agent 侧边栏嵌入现有产品页面
- 在人工确认（等待用户回答）场景下运行可中断恢复的 agent 流程

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L31: CornAgent is an open-source, full-stack AI agent. Use it as a self-hosted AI agent application, or embed its React 
> L76: - **Models:** Connected through LiteLLM. The default configuration uses DeepSeek; OpenAI-compatible chat and tool-c

## 星数曲线

```mermaid
xychart-beta
    title "XiaoTongYuCode/CornAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dda52e852d0e` · [字段定义](../../DATASET.md)*
