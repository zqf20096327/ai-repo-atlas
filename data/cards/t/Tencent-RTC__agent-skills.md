# Tencent-RTC/agent-skills

⭐ 15 · JavaScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Tencent-RTC/agent-skills) · [官网](https://trtc.io) · 组织维护 · 中文 README

**面向开发者的 TRTC SDK 集成引导 agent 技能包**

腾讯 RTC 团队发布的 agent 技能包：以自然语言描述需求后，技能识别目标（跑 demo、集成能力、排障、查文档），检测项目框架与平台，询问澄清问题并逐步引导实现 TRTC 各产品的集成，覆盖 Web/iOS/Android/Flutter 的会议、音视频通话、IM、离线推送与对话式 AI 场景。提供 SDK 日志离线分析（支持 .log/.xlog 等格式）、错误码与定价查询，进度保存于 .trtc-session.yaml 可跨会话续接。通过 npx 安装到 Claude Code、Cursor、CodeBuddy、Codex 等 IDE agent。Conference/Chat/Push/Call 等提供引导集成，Live 与 RTC Engine 标注 Coming soon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言路由到对应 TRTC 产品与平台的集成路径，逐步引导至可用代码
- 离线分析 TRTC/IM/TUI/应用/崩溃日志，支持 .log/.txt/.clog/.xlog 与压缩包
- 对话式 AI 场景引导：语音 AI、客服、口语教练、实时翻译（含 LLM/STT/TTS 供应商切换）
- 集成进度保存于 .trtc-session.yaml，跨会话续接

## 适用场景

- 在我的 React 应用里加视频会议或音视频通话
- 用自然语言让 IDE agent 引导接入 TRTC 即时通讯或离线推送
- 排查 TRTC/IM 集成报错并分析 SDK 日志
- 从零搭建带语音 AI 客服或实时翻译的应用

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: Describe what you want to build in plain language. The skill routes your request to the right integration path, asks
> L61: ## How It Works

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-RTC/agent-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `12790699cf03` · [字段定义](../../DATASET.md)*
