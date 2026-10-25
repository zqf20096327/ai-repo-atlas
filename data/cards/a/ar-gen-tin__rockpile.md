# ar-gen-tin/rockpile

⭐ 41 · Swift · NOASSERTION · 推送 2026-07-01 · [GitHub](https://github.com/ar-gen-tin/rockpile) · 个人维护 · 中文 README

**栖身 MacBook 刘海区的像素宠物，实时可视化 AI agent 状态**

macOS 桌面应用：在 MacBook 刘海区显示像素小龙虾/寄居蟹，通过 Unix Socket、TCP 或 WebSocket 连接 Claude Code 等 AI agent，把思考、工具调用、等待、报错等状态映射为实时精灵动画与水下环境变化；并以街霸式血条呈现 token 消耗（O₂ 值）。提供双机配对模式（MacBook 监控远程 Mac Mini 的 agent）、会话足迹记录，情绪由 Claude Haiku 分析用户消息情感得出。要求 macOS 15+ 与带刘海的 MacBook，提供 DMG 安装包与源码构建两种途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 种 agent 状态 × 4 种情绪的实时精灵动画
- O₂ 血条映射 token 消耗，支持 Claude 订阅配额与 Anthropic/xAI/OpenAPI API 用量查询
- Local/Monitor/Server 三种模式，WebSocket 网关可反向向远程 agent 发送命令
- 首次启动向导自动生成 Hook 插件到 ~/.rockpile/plugins/

## 适用场景

- 在刘海区随时一眼看到 AI agent 在思考还是干活
- 用 MacBook 远程监控 Mac Mini 上跑的 agent 状态与 token 消耗
- 回顾每次会话的 token 用量与工具调用摘要

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L23: Rockpile is a pixel-art crawfish companion that lives in your MacBook's **Notch area**. It connects to your AI Agen
> L91: Emotions are analyzed in real time by Claude Haiku from user message sentiment, with natural 60-second decay.

## 星数曲线

```mermaid
xychart-beta
    title "ar-gen-tin/rockpile 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a6a15e90d37c` · [字段定义](../../DATASET.md)*
