# Cyanosite/OllamaLab

⭐ 32 · Swift · 推送 2026-07-18 · [GitHub](https://github.com/Cyanosite/OllamaLab) · 个人维护

**macOS 本地 AI 聊天助手，基于 Ollama 运行模型**

使用 SwiftUI/SwiftData 构建的 macOS 原生 AI 助手应用，聊天数据本地保存，可浏览历史会话；通过 App Sandbox 限制对话数据仅本应用可读。功能包括：聊天、通过 ⌥+Space 唤起的 Companion Mode 常驻模式、直接在应用内从 Ollama 拉取与删除模型、设置界面。模型运行依赖本机 Ollama 服务，README 未给出安装与配置细节，信息以截图标题为主。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SwiftData 本地保存聊天记录，App Sandbox 隔离数据
- ⌥+Space 快捷键唤起 Companion Mode
- 应用内直接从 Ollama 拉取与删除模型

## 适用场景

- 在 macOS 上通过本地 Ollama 模型进行 AI 对话
- 通过常驻 Companion Mode 快速调用助手
- 在应用内管理本地模型（拉取/删除）

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L18: ### Pull Model directly from OllamaLab
> L20: Pull Model Feature

## 星数曲线

```mermaid
xychart-beta
    title "Cyanosite/OllamaLab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `cbb4a15b034e` · [字段定义](../../DATASET.md)*
