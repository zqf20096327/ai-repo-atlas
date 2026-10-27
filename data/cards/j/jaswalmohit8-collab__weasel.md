# jaswalmohit8-collab/weasel

⭐ 29 · HTML · MIT · 推送 2026-06-18 · [GitHub](https://github.com/jaswalmohit8-collab/weasel) · 个人维护

**约束长会话 AI 编码 agent 行为的单文件操作契约（CLAUDE.md）**

MIT 许可的公共 CLAUDE.md 模式文件，针对长时间 agent 会话中的运行漂移问题：上下文被当作持久记忆、计划反复重写、循环形成、重启后丢失下一步动作。文件给编码 agent 六条规则：检查通过即行动、以当前证据优先、保持状态紧凑、尽早打断循环、只学习改变行为的内容、保持安全护栏可用。另附 AGENTS.md 兼容垫片与 DEMO.md 测试提示词。使用方式为复制到项目并让编码 agent 读取。无框架、无服务器、无可执行组件。

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

- 六条紧凑运行规则写入 CLAUDE.md，复制即用
- 附带 YAML 状态文件结构作为会话交接面
- 提供 AGENTS.md 兼容垫片与两分钟测试提示词 DEMO.md

## 适用场景

- 长会话编码 agent 出现空转、反复重写计划时用来约束行为
- 在 Claude Code / Kimi 等编码工具中维持紧凑可交接的任务状态
- 重启会话时保留下一步动作与阻塞项

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L31: - CLAUDE.md - the copyable operating contract
> L120: Copy `CLAUDE.md` into a project where you use a coding agent.

## 星数曲线

```mermaid
xychart-beta
    title "jaswalmohit8-collab/weasel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d2c64c8795bd` · [字段定义](../../DATASET.md)*
