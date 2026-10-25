# Vinist123/zhuling

⭐ 51 · Java · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/Vinist123/zhuling) · [官网](https://blog.csdn.net/vinist/article/details/163280950) · 个人维护 · 中文 README

**面向 Java 开发者的零配置 AI Agent 开发脚手架**

基于 SpringBoot 4.1 + Spring AI 2.0 + DDD 六边形架构的 AI Agent 开发脚手架：通过一份 YAML 配置文件定义 Agent，支持多 Agent 独立注册与运行时隔离、同步与 SSE 流式对话接口、多轮会话记忆持久化（MySQL/PostgreSQL）、MCP 工具调用（Local/SSE/Stdio 三种模式）、Skills 脚本包加载，以及单 Agent ReAct 执行内核。提供 Token 统计、工具遥测、Trace ID 等可观测能力，并内置纯静态对话工作台 UI。需 JDK 21+、Maven 3.8+ 与数据库，从源码克隆编译运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一份 YAML 定义 Agent，支持多 Agent 注册与运行时隔离
- MCP 工具调用（Local / SSE / Stdio 三种模式）与 Skills 脚本包
- 单 Agent ReAct 执行内核（thought→act→observe 多步循环）
- 内置可观测对话工作台 UI 与版本化 SSE 事件信封

## 适用场景

- Java 开发者快速搭建带工具调用的 LLM Agent 服务
- 通过 YAML 配置声明式管理多个 Agent 并隔离运行
- 需要观测 Token 消耗、工具调用与推理步骤的 Agent 应用

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: > 铸造 AI 灵魂 —— 基于 SpringBoot 4.1 + Spring AI 2.0 + DDD 六边形架构的 AI Agent 开发脚手架
> L14: 铸灵（ZhuLing）帮助 Java 开发者**零代码启动 Agent 应用**。只需编写一份 YAML 配置文件，即可获得：
> L16: - ✅ 多 Agent 独立注册与运行时隔离

## 星数曲线

```mermaid
xychart-beta
    title "Vinist123/zhuling 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-25 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4ed9abc1e5bf` · [字段定义](../../DATASET.md)*
