# Iamsohungrynow/compagnon-eveil

⭐ 18 · HTML · 推送 2026-07-07 · [GitHub](https://github.com/Iamsohungrynow/compagnon-eveil) · [官网](https://compagnon-eveil.vercel.app/) · 个人维护

**学习陪伴与情绪打卡的 AI 伴侣演示应用（Next.js）**

面向个人用户的 AI 陪伴对话演示：覆盖学习、日常例行、情绪打卡、实体化伴侣与创作者风格角色交互。核心机制包括轻量记忆、状态反馈、微行动引导、SSE 流式聊天与 TTS/STT 语音（渐进增强，无密钥时回退浏览器语音或 mock 行为）。主交付物为 web/ 下的 Next.js 15 应用，运行时源码在 server/ 打包进单次部署；通过 npm 本地运行，也可一键部署到 Vercel。曾入围 UCWS Singapore Hackathon 2026 Top 20。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然对话 + 轻量记忆 + 状态反馈的伴侣运行时
- SSE 流式聊天与 TTS/STT 语音路由，无密钥时回退 mock/浏览器语音
- 运行时打包进 Next.js 单部署，无需独立后端
- 支持 3D 桌面形象演示路径

## 适用场景

- 学习与日常例行中与 AI 伴侣对话打卡
- 进行情绪检查与微行动引导
- 体验带语音与记忆的伴侣交互 demo

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: Compagnon Eveil is an AI companion demo for study, daily routines, emotional check-ins, object-based companions, and
> L36: - `/api/*` - the companion runtime, including chat, SSE streaming, TTS, and STT routes

## 星数曲线

```mermaid
xychart-beta
    title "Iamsohungrynow/compagnon-eveil 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-26 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3dfddc382038` · [字段定义](../../DATASET.md)*
