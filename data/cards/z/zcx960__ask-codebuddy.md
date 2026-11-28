# zcx960/ask-codebuddy

⭐ 6 · MIT · 推送 2026-10-21 · [GitHub](https://github.com/zcx960/ask-codebuddy) · 个人维护 · 中文 README

**把本机 CodeBuddy CLI 作为子代理的 Agent Skill**

一个适用于读取 SKILL.md 的客户端（Codex、Claude Code 等）的 Agent Skill，将本机已登录的 CodeBuddy CLI 作为辅助子代理，处理代码分析、代码审查、方案比较、问题定位和局部实现等可独立完成的任务。主代理负责拆分任务、提供上下文、核验差异与测试结果；子代理不继承对话上下文。README 详细说明数据边界（提示词与文件内容会发往服务端）、三种工具集模式、临时目录隔离流程，以及限制额度、登录失效时的处理约定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 主代理负责拆分核验、子代理只做被指派部分的协作机制
- 三种工具集模式：纯分析、只读审查、局部实现
- 私有临时目录 + stdin 传参，用后清理不留明文
- 逐项说明参数不能消除的数据外发边界

## 适用场景

- 让主代理把代码审查子任务委派给本机 CodeBuddy CLI
- 利用已有的 CodeBuddy 订阅或积分处理独立编码任务
- 在需要控制文件访问范围与数据外发边界的 agent 编排中使用

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L14: `ask-codebuddy` 是一个 Agent Skill（适用于 Codex、Claude Code 等读取 `SKILL.md` 的客户端）。它把本机已登录的 CodeBuddy CLI 当作辅助子代理，用来处理可以独立完
> L16: 设计原则是**主代理负责，子代理执行**：

## 星数曲线

```mermaid
xychart-beta
    title "zcx960/ask-codebuddy 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-08", "2026-11-28"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-10-26 5 → 2026-11-28 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `22a20a7dacea` · [字段定义](../../DATASET.md)*
