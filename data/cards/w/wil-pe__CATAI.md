# wil-pe/CATAI

⭐ 62 · Swift · 推送 2026-05-27 · [GitHub](https://github.com/wil-pe/CATAI) · [官网](https://github.com/wil-pe/CATAI/releases/latest) · 个人维护

**带本地 AI 聊天与多猫辩论的 macOS 桌面宠物应用**

面向 macOS 用户的像素风桌面宠物：猫在 Dock 栏行走、栖息窗口、追踪鼠标，最多支持 7 只不同性格的猫。AI 功能通过本地 Ollama 实现点击聊天与辩论模式——各猫按自身性格就用户话题多轮辩论并合成最终答案，作为头脑风暴与想法打磨工具。整个应用为单个约 2000 行的 Swift 文件，无外部依赖，提供 Releases 预构建 .app、build.sh 与 swiftc 三种运行方式。要求 macOS 14+，Ollama 为聊天功能所需且标注为可选。多平台移植（Tauri v2）标注为进行中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 最多 7 只猫，各有独立性格与技能，368 帧 8 方向手绘精灵动画
- 辩论模式：多猫按性格多轮辩论并合成最终答案
- AI 聊天由本地 Ollama 驱动，会话记忆持久化于 UserDefaults
- 单 Swift 文件实现，无外部依赖，无 Xcode 工程

## 适用场景

- 在 macOS 桌面养像素猫作为日常陪伴
- 让多个 AI 性格就一个话题辩论以打磨想法
- 离线/本地环境下与桌面宠物对话

## 场景标签

`聊天机器人` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: Virtual desktop pet cats for macOS — pixel art cats that live on your dock, chat with you via Ollama LLM, and debate
> L19: - **AI chat** — Click a cat to open a pixel-art chat bubble, powered by Ollama
> L53: - macOS 14+ (Apple Silicon or Intel)

## 星数曲线

```mermaid
xychart-beta
    title "wil-pe/CATAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-30 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `473e6569ec0b` · [字段定义](../../DATASET.md)*
