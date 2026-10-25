# Garrus800-stack/genesis-agent

⭐ 42 · JavaScript · MIT · 推送 2026-07-30 · [GitHub](https://github.com/Garrus800-stack/genesis-agent) · [官网](https://github.com/Garrus800-stack/genesis-agent/discussions/16) · 个人维护

**桌面端自我修改认知型 AI 代理：读写并验证自身代码，跨会话记忆**

自包含的 Electron 桌面应用，本体即一个 AI 代理而非开发框架：通过 SelfModel 读取自身源码，在沙箱（VM+进程）中测试修改、git 快照后才应用；每步由 66 项确定性检查（AST、退出码、导入）验证而非 LLM 自评。具备 5 层记忆（情景/语义/向量/对话/知识图谱）、空闲时 DreamCycle 记忆固化、FormalPlanner 多步规划与跨重启的目标持久化、5 维情绪状态作为行为转向信号，以及 Obsidian vault 只读桥接。支持 MCP 双向（客户端+服务器，对外暴露 7 个工具），可运行于 Claude、GPT 或本地 Ollama，断网时自动切换 Ollama。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取并修改自身源码：沙箱测试+git 快照，测试通过才应用
- 66 项确定性检查替代 LLM 自评做逐步验证
- 5 层记忆 + 空闲时 DreamCycle 固化，目标跨重启持久
- MCP 双向：作为服务器向外部 IDE 暴露 7 个工具
- NetworkSentinel 断网检测，自动切换本地 Ollama

## 适用场景

- 让一个常驻桌面的 AI 代理自主完成多步开发任务
- 跨会话保留任务记忆与经验教训
- 通过 MCP 让外部 IDE 调用该代理的验证与分析能力

## 场景标签

`编码 Agent` `Agent 记忆` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L26: Genesis is not a framework for building agents. **Genesis *is* the agent.**
> L28: It's a self-contained Electron application that reads its own source code, modifies itself, verifies its own output

## 星数曲线

```mermaid
xychart-beta
    title "Garrus800-stack/genesis-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `feb053059872` · [字段定义](../../DATASET.md)*
