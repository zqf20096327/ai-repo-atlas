# earthwalker17/MiniDSH

⭐ 16 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/earthwalker17/MiniDSH) · [官网](https://www.npmjs.com/package/minidsh) · 个人维护

**本地优先的极简编码 agent 运行框架，面向终端与浏览器**

用 TypeScript 实现的小型编码 agent harness：在模型外围提供工具、会话与权限层，支持 DeepSeek、Anthropic、OpenAI 三家 provider 并可会话中途切换模型。核心机制包括：操作系统级 shell 沙箱（Linux bubblewrap / macOS Seatbelt，Windows 无）、仅追加的 JSONL 事件日志使进程被杀后可恢复或分叉、上下文自动压缩、带权限上限的子 agent 委派、后台任务、受围栏的浏览器检查前端、可选 Tavily 网页搜索与 SKILL.md 技能。约三万三千行代码、单一运行时依赖，同时作为可通读的参考架构与架构优先的系统工程实验，非 DeepSeek 官方项目，单人维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三家 provider（DeepSeek/Anthropic/OpenAI），会话中途可切换模型
- 仅追加 JSONL 日志：进程被杀后可恢复、分叉并审计权限历史
- OS 级 shell 沙箱与文件写入围栏，逐条审批记录可回读
- 子 agent 委派（权限只可收窄）、后台任务、受围栏浏览器

## 适用场景

- 在终端、浏览器或脚本中以受控权限让模型编辑代码与运行命令
- 进程中断后从日志恢复或分叉继续编码会话
- 把编码任务委派给权限受限的子 agent 或视觉模型做检查
- 作为可通读的 agent 架构参考实现来学习

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: MiniDSH is a small, local-first coding-agent harness: the runtime around a model that gives it tools, sessions and 
> L20: 1. **Useful software.** A coding agent that edits files and runs commands under an authority you set — which files 

## 星数曲线

```mermaid
xychart-beta
    title "earthwalker17/MiniDSH 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5dd3006db957` · [字段定义](../../DATASET.md)*
