# YUJIE2002/ClawBody

⭐ 16 · TypeScript · MIT · 推送 2026-03-01 · [GitHub](https://github.com/YUJIE2002/ClawBody) · 个人维护 · 中文 README

**给 AI 智能体配 3D 虚拟身体的桌面伴侣应用**

基于 Tauri v2 (Rust) + React + Three.js 的桌面应用，在桌面上以无边框透明覆盖层渲染 VRM 3D 角色，通过 WebSocket 连接 OpenClaw AI 智能体框架，将 AI 的情绪（8 种状态）、语音输出映射为表情与口型动画。支持语音输入、TTS、唤醒词、摄像头视觉、自定义 VRM 模型导入与 11 种待机动画。需 Node.js 20+ 与 Rust 1.75+，从源码构建运行（cargo tauri dev），插件系统为规划中功能。

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

- VRM 3D 角色透明桌面覆盖层（Three.js + @pixiv/three-vrm）
- WebSocket 连接 OpenClaw，AI 情绪→8 种表情动画、口型同步
- 语音输入/输出、唤醒词检测、摄像头视觉输入
- 支持导入任意 VRM 模型（VRoid Hub/VRoid Studio）

## 适用场景

- 让我的 OpenClaw 智能体以桌面角色形式可视化呈现
- 用带语音与表情的虚拟角色与 AI 对话
- 自定义 VRM 模型打造个性化桌面伙伴

## 场景标签

`AI 助手` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L22: The character is connected to OpenClaw, an AI agent framework. When the AI thinks, the character thinks. When it sp
> L39: |🧠 OpenClaw Integration|✅|WebSocket bridge to AI agent gateway (ws:// & wss://)|
> L60: |**AI Brain**|OpenClaw|Agent framework — emotions, speech, tools|

## 星数曲线

```mermaid
xychart-beta
    title "YUJIE2002/ClawBody 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `879503970401` · [字段定义](../../DATASET.md)*
