# RajeshTechForge/pinac_workspace

⭐ 36 · TypeScript · MIT · 推送 2026-10-02 · [GitHub](https://github.com/RajeshTechForge/pinac_workspace) · [官网](https://pinac.rajeshmondal.com) · 组织维护

**本地优先的跨平台桌面 AI 聊天助手，自带 API Key 使用**

基于 Tauri 与 React 构建、由 Python FastAPI 后端驱动的桌面 AI 聊天应用，面向希望控制自身数据的使用者。用户自带 API Key 接入所支持的模型（含扩展思考模式），对话历史通过 SQLite 本地持久化，不依赖云同步。后端可替换组件、添加端点。开发需 Node.js，完整运行另需 Python+uv 与 Rust；提供仅前端的 Mock UI 路径供界面测试。底层为自研 Kitkat Python 库，仍在积极开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自带 API Key 接入任意所支持的模型，含扩展思考模式
- 对话历史经 SQLite 本地持久化，无云同步依赖
- Tauri+React 桌面端与 FastAPI 后端分进程运行
- 低内存占用设计，可与其他开发环境并行运行

## 适用场景

- 在桌面本地与各家 LLM 对话且自行保管 API Key
- 希望聊天记录只存在本机、不依赖云同步
- 在前端 Mock UI 中单独调试界面改动

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L8: ### Privacy-first, cross-platform desktop AI assistant for everyone
> L12: Pinac-Workspace is a minimalist-designed & lightweight secure desktop AI-chat experience built with Tauri & React a

## 星数曲线

```mermaid
xychart-beta
    title "RajeshTechForge/pinac_workspace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-31 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f6e4e72918f7` · [字段定义](../../DATASET.md)*
