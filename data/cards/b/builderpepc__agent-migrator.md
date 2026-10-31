# builderpepc/agent-migrator

⭐ 19 · Python · CC-BY-SA-4.0 · 推送 2026-06-26 · [GitHub](https://github.com/builderpepc/agent-migrator) · 个人维护

**在 AI 编程工具间迁移对话历史的 CLI 工具**

面向使用多种 AI 编程工具的开发者的命令行工具：在 Claude Code、Codex、Gemini CLI、Cursor 四种工具之间双向迁移对话历史，全部两两组合均支持。迁移时将对话读取为工具无关的规范化格式（TextMessage 与 ToolCallMessage 轮次）再写出为目标格式；文本消息、工具调用与 Plan 均可迁移（→Cursor 的 Plan 仅作为上下文文档）。提供交互式与 JSON 输出的非交互式两种用法，迁移过程中 Ctrl+C 可取消并回滚。新增工具只需实现 AgentAdapter 接口。安装依赖 uv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | CC-BY-SA-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种 AI 编程工具全两两组合双向迁移
- 工具无关的规范化中间格式与 AgentAdapter 适配器架构
- 交互式向导与输出 JSON 的 list/move 子命令
- 迁移中 Ctrl+C 取消并回滚

## 适用场景

- 换用新的 AI 编程工具时带走既有对话历史
- 同时使用多个编程工具时同步迁移项目上下文
- 脚本化批量迁移项目内全部对话

## 场景标签

 · 领域:开发者工具

## 证据(README 行号)

> L3: A CLI tool for migrating conversation history between AI coding tools.

## 星数曲线

```mermaid
xychart-beta
    title "builderpepc/agent-migrator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8b97e9d8f4b2` · [字段定义](../../DATASET.md)*
