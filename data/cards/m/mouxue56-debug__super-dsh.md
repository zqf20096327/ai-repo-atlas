# mouxue56-debug/super-dsh

⭐ 3 · JavaScript · NOASSERTION · 推送 2026-11-21 · [GitHub](https://github.com/mouxue56-debug/super-dsh) · 个人维护 · 中文 README

**手机优先的多助理个人助理中枢，用任务板接力干活**

SDS 是建在 DeepSeek Harness 内核之上的手机优先个人助理中枢，跑在用户自己的机器上：用户与首席助理对话，它带一小队带形象的助理在文件任务板上接力执行任务，带账本记录调用次数。关键机制包括三档权限（全开/改动前问/只读）且花钱、对外发送、删除、动线上服务四类操作强制先确认；首席助理可修改 SDS 自身源码并自动存还原点，可一键退回；语音转写与合成不自带模型，接用户自备的 OpenAI 兼容接口且限私网地址。当前为 v0.2.0-beta，仅在 macOS 开发验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多助理协作 + 文件任务板接力，支持外部 agent（Codex/Claude Code/Grok CLI）命令行领单
- 三档权限与四类强制确认卡（花钱/对外发送/删除/动线上服务）
- 首席助理可改 SDS 自身源码，自动还原点 + 改动记录退回 + 救援脚本
- 语音转写/合成接用户自备的 OpenAI 兼容私网接口

## 适用场景

- 在手机上通过对话让一群助理替我处理任务
- 让外部 agent（Codex/Claude Code/Grok）从任务板领单干活
- 让助理帮我改这个助理应用本身，改坏了能退回

## 场景标签

`多智能体` `AI 助手` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L8: the DeepSeek Harness kernel and runs on your own machine. You talk to one lead assistant; it works with a small team
> L20: SDS 是一个**手机优先的个人助理中枢**，建在 DeepSeek Harness（DSH）内核之上、跑在你自己的机器上：你只和首席助理说话，它带着一小队带形象的助理替你干活，进度全在一块任务板上；花钱、对外发送、删除、动线上服
> L33: - **任务板与接力**：一件事一张卡；可以派给某位助理、让空闲的助理自己领、交给首席安排、定时、排成一条接力路线（一棒交一棒，可要求「要我看一眼」才放行）；Codex、Claude Code、Grok 等外部 agent 用命令


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `61fa61c771d2` · [字段定义](../../DATASET.md)*
