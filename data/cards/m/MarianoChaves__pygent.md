# MarianoChaves/pygent

⭐ 16 · Python · MIT · 推送 2026-09-16 · [GitHub](https://github.com/MarianoChaves/pygent) · [官网](https://pygent-ai.com/) · 个人维护

**Python 工具调用 Agent 循环框架：自带模型与函数即可运行**

用于构建工具调用型 AI agent 的 Python harness：用户提供聊天模型与普通 Python 函数，Pygent 运行 agent 循环，提供显式工具绑定、JSON Schema 输入校验、人工审批、执行预算（步数/调用数/输出长度/超时）与可序列化结果。默认零工具、不自动创建工作区，文件与 shell 访问需显式开启，CLI 可选 Docker 隔离。同步进程内设计，无 MCP 客户端、持久化工作流引擎或原生异步流。适合在已有应用逻辑外包裹有界 agent 循环的场景。

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

- Model 协议仅一个 chat 方法，内置 OpenAI 兼容 Chat Completions 适配器
- RunLimits 执行预算与 requires_approval 审批机制
- ScriptedModel 确定性测试替身，可离线断言工具调用
- 零工具起步，文件/shell 权限需显式绑定，CLI 支持 Docker 隔离

## 适用场景

- 为已有内部工具或仓库维护逻辑加一个有边界的 agent 循环
- 在更大工作流中嵌入可控的 agent 步骤
- 离线用 pytest 断言 agent 的工具调用行为

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A small Python harness for tool-using AI agents.** Bring a chat model and ordinary
> L7: Pygent is useful when you already have application logic and need a bounded agent

## 星数曲线

```mermaid
xychart-beta
    title "MarianoChaves/pygent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bbc89503857d` · [字段定义](../../DATASET.md)*
