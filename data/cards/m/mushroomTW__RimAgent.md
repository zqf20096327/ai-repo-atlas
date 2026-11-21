# mushroomTW/RimAgent

⭐ 4 · C# · NOASSERTION · 推送 2026-11-20 · [GitHub](https://github.com/mushroomTW/RimAgent) · 个人维护 · 中文 README

**用自然语言管理 RimWorld 殖民地的游戏内 AI agent 模组**

面向 RimWorld 1.7 的游戏内 AI agent 模组，通过 82 个工具让玩家以自然语言查看殖民地状态并下达指令。提供四种执行模式（Confirm/Execute/Auto/Full access）控制操作是否需要玩家批准；支持子代理、持久目标 /goal、MCP 扩展与技能包。所有 LLM 供给（provider、API key、fallback 链、token 预算）由前置模组 RimLLM Framework 统一配置，RimAgent 本体只提供殖民地工具与分类别工具权限。 combat 指令受 LLM 推理延迟限制，定位为宏观战术而非瞬时微操。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 82 个工具覆盖殖民地检查、实时指令、网络搜索与全局/存档双域记忆
- 四种执行模式：逐步确认、例行放行+重大操作把关、AI 风险分级 Auto、完全自主
- 子代理机制：隔离工具与上下文，可分配独立模型与推理等级
- MCP 协议扩展本地外部工具，14 个内置技能与 6 条结局任务线

## 适用场景

- 用对话查询殖民地状况并下达如调整工作优先级的指令
- 通过 /goal 排队多步持久任务（巡逻、基地维护）
- 在 Auto 模式下让分类模型自动放行低风险操作
- 通过 MCP 接入自建的外部工具扩展 agent 能力

## 场景标签

 · 领域:游戏/游戏 AI 工具

## 证据(README 行号)

> L7: An in-game AI agent for RimWorld 1.7. Inspect your colony and issue orders in natural language through 82 tools, wit
> L26: > All LLM plumbing (provider selection, API key, model selection, fallback chains, and token budget) is configured 

## 星数曲线

```mermaid
xychart-beta
    title "mushroomTW/RimAgent 星数(近 3 点)"
    x-axis ["2026-11-19", "2026-11-20", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-19 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `d3dacdff31c0` · [字段定义](../../DATASET.md)*
