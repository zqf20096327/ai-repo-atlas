# AskKumptenchen/agent-chat-selfie

⭐ 39 · Python · MIT · 推送 2026-03-26 · [GitHub](https://github.com/AskKumptenchen/agent-chat-selfie) · 个人维护 · 中文 README

**给 AI Agent 发情感自拍的技能：按心情生成图片并主动推送**

面向 OpenClaw 等 agent 框架的 SKILL.md 技能包：根据对话上下文判定 agent 当前情绪，生成或复用情绪贴图形式的‘自拍’，随回复一并发送；支持心跳推送机制让 agent 主动发送近况图片。不绑定单一图像后端，可适配内置图像工具、Nano Banana/GPT Images/Grok Imagine 等在线 API 或本地 Stable Diffusion+LoRA；生成成本高时可切换为固定情绪贴图复用模式。安装方式为让 agent 按 SKILL.md URL 自行安装，需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按对话情绪生成或复用心情贴图式自拍
- 心跳推送：agent 可主动发送近况图片
- 图像后端无关：内置工具/在线API/本地模型均可适配
- 固定情绪资产模式降低逐轮生成成本

## 适用场景

- 让陪伴型 AI Agent 在回复中带上符合当下情绪的自拍
- 让 agent 在无人对话时主动推送表达思念的图片
- 为 AI Agent 维持稳定的视觉形象与自我演化的 persona

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L27: No more cold lines like “task completed.” It will send you a selfie that belongs to that exact moment, shaped by th
> L66: - **Visualized emotion:** Based on the context of the conversation, the agent can either generate a fresh selfie or
> L81: It also does not depend on one fixed image stack. Whether the agent uses built-in image generation such as OpenClaw

## 星数曲线

```mermaid
xychart-beta
    title "AskKumptenchen/agent-chat-selfie 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-29 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c3e620508f3c` · [字段定义](../../DATASET.md)*
