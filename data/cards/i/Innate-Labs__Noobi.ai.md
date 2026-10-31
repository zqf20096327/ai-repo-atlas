# Innate-Labs/Noobi.ai

⭐ 251 · TypeScript · 推送 2026-09-26 · [GitHub](https://github.com/Innate-Labs/Noobi.ai) · 组织维护 · 中文 README

**macOS 桌面 agent：用 Codex 从一句话生成可玩的网页/Godot 游戏**

基于 Electron 的 local-first 桌面应用，通过 Codex App Server 驱动有边界的游戏生产循环：只读 Planner 划定范围，Implementer 在隔离目录内构建，独立 Reviewer 审查，宿主执行构建与自动化试玩，失败检查触发最多三轮修复。Agent 在 Web 与 Godot 4 之间选择输出，产物为用户工作区内的独立工程。媒体（图像/音频/3D）走可配置 provider 或 Codex ImageGen 及程序化回退。当前为 macOS 开发者预览，需 ChatGPT/Codex 账户，无签名发布包，需从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Planner→Implementer→Reviewer→构建→试玩 的审查门控生产循环，含最多三轮修复
- 输出为本地独立 Web 或 Godot 4 工程，可继续用 Codex 或提交 Git
- 媒体管线支持图像/音乐/语音/3D 的可配置 REST provider 与程序化回退
- 沙箱化 Electron Renderer、safeStorage 密封密钥、仅 127.0.0.1 预览服务器

## 适用场景

- 用自然语言描述想法并得到可玩的独立游戏工程
- 在本地检查、继续编辑生成的游戏项目文件
- 通过扩展媒体 provider、MCP 服务器或 Codex Skills 定制生产流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5:  Turn one game idea into a reviewed, playable Web or Godot game.
> L6:  A local-first desktop production agent powered by Codex App Server and Godot 4.
> L29: |**From prompt to playable**|Start with a natural-language brief, let the Agent choose Web or Godot 4, and preview 

## 星数曲线

```mermaid
xychart-beta
    title "Innate-Labs/Noobi.ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 250 --> 252
    line [251, 251]
```

2026-10-18 251 → 2026-10-31 251（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1fa4d99ae5e7` · [字段定义](../../DATASET.md)*
