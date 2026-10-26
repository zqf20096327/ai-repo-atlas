# LiteSuggarDEV/nonebot_plugin_suggarchat

⭐ 43 · Python · GPL-3.0 · 推送 2026-08-21 · [GitHub](https://github.com/LiteSuggarDEV/nonebot_plugin_suggarchat) · 组织维护 · 中文 README

**NoneBot2 平台的 QQ 聊天智能体插件**

基于 AmritaCore 的 NoneBot2 插件，为 OneBot V11 协议端（NapCat/Lagrange/go-cqhttp 等）提供可直接运行的 LLM 聊天机器人：支持群聊/私聊、AT 触发与上下文管理、多模型与多预设热切换、Function Calling、可选 MCP、会话生命周期管理与用量频率限制；内置不良内容检测熔断与提示词防泄露。模型通过 JSON 预设配置，兼容 OpenAI/DeepSeek/Gemini 等协议。README 注明完整 Agent 编排能力需迁移至 AmritaBot。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 开箱即用的多模型协议支持（OpenAI/DeepSeek/Gemini 等）
- 群聊/私聊双模式、AT 触发、多模型与预设热切换
- Function Calling 与可选 MCP 支持
- 每日用量统计与群/用户/全局频率限制

## 适用场景

- 给 QQ 群或私聊部署一个 LLM 聊天机器人
- 在多个模型预设和提示词模板间在线切换
- 对群聊机器人做使用频率与内容安全管控

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L25: > 本插件定位为**轻量完整的聊天智能体**，面向日常聊天场景；
> L30: - ✅ 开箱即用的多种模型协议支持（OpenAI / DeepSeek / Gemini 等）

## 星数曲线

```mermaid
xychart-beta
    title "LiteSuggarDEV/nonebot_plugin_suggarchat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 42 --> 45
    line [44, 43]
```

2026-10-18 44 → 2026-10-26 43（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ca799dd29e79` · [字段定义](../../DATASET.md)*
