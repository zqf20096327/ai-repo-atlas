# S0L0GUY/NOVA-AI

⭐ 19 · Python · MIT · 推送 2026-06-11 · [GitHub](https://github.com/S0L0GUY/NOVA-AI) · [官网](https://s0l0guy.github.io/NOVA-AI-Website/) · 个人维护

**本地优先的个人 AI 助手框架，用于对话 agent 实验**

本地优先的个人助手框架，集成记忆、视觉、音频与简单工具，用于快速实验对话型 agent。包含音频输入输出、基于 SQLite 的持久化记忆存储（默认 memories.db）、截图与基础视觉日志、UI 与命令行入口。安装方式为 git clone 源码后以 pip 安装依赖，通过 config.yaml 配置 API key 与本地路径，运行 main.py 或 nova.py 启动，另有 memory_ui.py 查看（如可用）。README 未指定默认 LLM 后端，描述与仓库主题（VRChat OSC 聊天机器人）存在差异。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SQLite 持久化本地记忆系统（memories.db）
- 音频输入输出与截图/视觉日志组件
- config.yaml/prompt.yaml 可配置 API key 与提示词
- 提供 main.py/nova.py/memory_ui.py 多个入口

## 适用场景

- 快速实验带记忆与多模态输入的对话 agent
- 构建本地运行的个人助手原型
- 通过 OSC 接入 VRChat 做语音对话（据仓库主题标签）

## 场景标签

`AI 助手` `聊天机器人` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: NOVA-AI is a local-first personal assistant framework that integrates memory, vision, audio, and simple tools to ena
> L7: - Local memory system persisted in SQLite (`memories.db`)
> L9: - Screenshot and basic vision logging

## 星数曲线

```mermaid
xychart-beta
    title "S0L0GUY/NOVA-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `8782ce55ac9e` · [字段定义](../../DATASET.md)*
