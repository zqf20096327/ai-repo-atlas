# gameswu/NyaDeskPet

⭐ 18 · TypeScript · MIT · 推送 2026-02-27 · [GitHub](https://github.com/gameswu/NyaDeskPet) · 个人维护 · 中文 README

**基于 Live2D 与内置 AI Agent 的跨平台桌面宠物应用**

开源模块化桌宠框架，基于 Electron：透明无边框窗口展示 Live2D 模型，支持 AI 驱动的表情动作、按部位配置的触碰反应、TTS 口型同步与流式音频播放。内置 AI Agent 支持多个模型供应商、函数工具与 MCP 管理、自定义指令，Agent 消息处理采用 Pipeline 架构并可在各阶段注册 Handler 插件。前端与后端 Agent 通过 WebSocket 解耦，提供完整文档与插件开发指南。移动端移植项目 NyaDeskPetAPP 开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Live2D 模型展示，AI 驱动表情动作与触碰反应
- 内置 AI Agent：多模型供应商、函数工具、MCP 管理、自定义指令
- 前后端通过 WebSocket 解耦，任何 WebSocket 客户端可接入
- 插件化架构：前端插件与 Agent Handler 插件均可扩展

## 适用场景

- 在桌面养一只可对话交互的 Live2D 宠物
- 通过插件扩展桌宠的功能与 Agent 行为
- 接入自定义指令与工具让 Agent 执行任务

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L4:  基于 Live2D + AI Agent 的跨平台桌面宠物应用
> L19: - AI 驱动的表情和动作，丰富生动的交互体验
> L29:  支持多个主流模型供应商

## 星数曲线

```mermaid
xychart-beta
    title "gameswu/NyaDeskPet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `f880e2a1fae7` · [字段定义](../../DATASET.md)*
