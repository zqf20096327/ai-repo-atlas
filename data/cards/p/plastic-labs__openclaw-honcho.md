# plastic-labs/openclaw-honcho

⭐ 87 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/plastic-labs/openclaw-honcho) · [官网](https://honcho.dev) · 组织维护

**为 OpenClaw agent 接入 Honcho 对话记忆的插件**

OpenClaw 平台的记忆插件：将对话消息持久化到 Honcho 服务，为用户与 agent 分别建立独立表示模型；提供 honcho_context、honcho_ask 等工具供 AI 会话中检索上下文，并在 before_prompt_build 阶段注入。与内置 memory-core 并行运行而非取代其记忆槽位。支持将既有 workspace 记忆文件非破坏性上传迁移，群聊中按 sender_id 为每个参与者建立独立 peer。需配置 Honcho API key（托管）或自建实例；支持自托管本地服务器。

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

- 为用户与 agent 分别建模的 peer 范式记忆
- 与 memory-core 并行运行，不占用记忆槽位
- 群聊/DM 中按 sender_id 为每个参与者建立独立记忆
- 非破坏性迁移既有 memory 文件，保留原始时间戳

## 适用场景

- 让 OpenClaw agent 跨会话记住用户上下文
- 群聊场景中为每个参与者维持独立记忆
- 从文件式记忆迁移到 Honcho 托管/自托管记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: AI-native memory with dialectic reasoning for OpenClaw. Uses Honcho's peer paradigm to build and maintain separate m
> L7: This plugin runs alongside OpenClaw's built-in memory (`memory-core`) rather than replacing it. memory-core keeps th

## 星数曲线

```mermaid
xychart-beta
    title "plastic-labs/openclaw-honcho 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-18 87 → 2026-10-26 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `98369d89d1d4` · [字段定义](../../DATASET.md)*
