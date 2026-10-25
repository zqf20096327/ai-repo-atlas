# makermate/clarvis-ai

⭐ 205 · Shell · MIT · 推送 2026-03-12 · [GitHub](https://github.com/makermate/clarvis-ai) · [官网](https://www.clarv.is/) · 组织维护

**聊天驱动的 3D 打印助手：对话生成/搜索/切片/打印模型**

面向 3D 打印用户的开源助手，通过 Telegram、Discord、WhatsApp 等聊天渠道交互：发送草图、照片或文字描述，由 AI agent（Gemini 2.5 Flash 作为大脑）生成或编辑 3D 模型，或从 Thingiverse 等模型库搜索现成模型，经 CuraEngine（5.6.0 HTTP API）切片为 G-code，再通过 Moonraker（Klipper）或 PrusaLink 发送到打印机。它整合 OpenClaw、claw3d、claw3d-skill 与 curaengine-slicer-api 四个开源组件，以 Docker Compose 编排提供一键运行的发行版，另有托管服务 clarv.is。需要 Docker 与相应 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 草图/照片/文字 → 3D 模型的 AI 生成与编辑流水线
- CuraEngine 切片并经 Moonraker/PrusaLink 发送到打印机
- 基于 OpenClaw 的多聊天渠道接入（Telegram/Discord/WhatsApp）
- 整合 4 个开源组件的 Docker Compose 一键发行版

## 适用场景

- 在聊天里描述需求直接生成并打印 3D 模型
- 搜索现成 3D 模型、调整方向/强度后切片打印
- 通过对话向 agent 登记 3D 打印机并下发打印任务

## 场景标签

 · 领域:3D 打印/制造业工具

## 证据(README 行号)

> L7: Open-source 3D printing assistant powered by AI. Talk to it from Telegram, Discord, or WhatsApp — send a sketch, pho
> L30: - **Video/image/text → 3D model** — AI-powered 3D generation and 3D editing pipeline

## 星数曲线

```mermaid
xychart-beta
    title "makermate/clarvis-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 204 --> 206
    line [205, 205]
```

2026-10-18 205 → 2026-10-25 205（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `19640274d618` · [字段定义](../../DATASET.md)*
