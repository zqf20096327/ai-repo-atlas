# missingus3r/friday-showcase

⭐ 196 · HTML · 推送 2026-10-11 · [GitHub](https://github.com/missingus3r/friday-showcase) · [官网](https://missingus3r.github.io/friday-showcase/) · 组织维护

**基于 Claude Code 的 24/7 个人 AI 助手系统展示与搭建方案**

运行于个人 Windows/Linux/macOS 机器的常驻个人 AI 助手：以 Claude Code CLI（Anthropic Max Plan，$100/月）为运行时，通过 Telegram 交互，借助 MCP 插件与 cron 调度实现定时简报、自主监控、邮件、Git、语音（ElevenLabs）、网络研究等能力。附带 Flask+SQLite 记忆服务器（含 RAG、实体追踪、D3.js 图可视化）与自进化子系统（技能习得、夜间反思、偏好学习、自我改进提案）。本仓库提供 SETUP.md 让 Claude Code 自动生成各用户的代码实例，无需微调或编排框架。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仅依赖 Claude Code CLI + Telegram，无自定义 AI 后端与编排框架
- Flask+SQLite 单文件记忆层：对话日志、3072 维向量 RAG、混合检索（FTS5+语义 RRF）
- 自进化子系统：技能习得、夜间反思、偏好学习、世界建模、需批准的自我改进提案
- 可选本地视觉检测：YOLOv8n + OpenCV 在设备上识别人员并发 Telegram 告警

## 适用场景

- 搭建全天候 Telegram 个人助手处理简报、邮件、Git 与研究任务
- 长期跟踪个人偏好与记忆并主动发起提醒
- 把安全摄像头接成本地人员检测告警

## 场景标签

`AI 助手` `Agent 记忆` `目标检测` · 领域:Agent 开发

## 证据(README 行号)

> L5: An always-on personal AI system using only Claude Code CLI ($100/month) and Telegram — no custom AI, no cloud VMs, n
> L11: A self-evolving AI assistant that runs 24/7 on a standard Windows, Linux, or macOS machine. It talks over Telegram,
> L15: Claude Code sits at the center, reaching external services through MCP (Model Context Protocol) plugins and shell t

## 星数曲线

```mermaid
xychart-beta
    title "missingus3r/friday-showcase 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 195 --> 197
    line [196, 196]
```

2026-10-18 196 → 2026-10-27 196（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f2ac3df0bd79` · [字段定义](../../DATASET.md)*
