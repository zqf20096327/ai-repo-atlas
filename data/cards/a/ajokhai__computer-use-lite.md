# ajokhai/computer-use-lite

⭐ 4 · Python · 推送 2026-10-26 · [GitHub](https://github.com/ajokhai/computer-use-lite) · [官网](https://github.com/ajokhai/computer-use-lite/releases/latest) · 个人维护

**让任意 AI 模型操控整台 Mac 的菜单栏 computer-use 代理**

macOS 原生菜单栏应用，通过内置 Rust 编写的 MCP 服务器（cu-mcp）和带语音输入的浮动条，让外部 AI 应用（Claude、VS Code、Cursor 等 MCP 客户端）或应用自带代理执行截图、点击、输入等整机操作。代理支持视觉模型与小型动作模型（Jev）两种分工模式，具备失败重试、经验教训记录与可导出分享的技能学习机制。API key 全部可选：走 MCP 时无需 key；本地模型经 Ollama/LM Studio 等接入。以 DMG 安装包分发，需授予辅助功能与屏幕录制权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置原生 Rust MCP 服务器 cu-mcp，20+ 桌面操作工具（截图/点击/输入/滚动等）
- 多种代理模式：Vision+Jev、Jev Only、Vision Only，视觉模型可用 Claude/OpenAI/Gemini/OpenRouter 或本地模型
- 全本地语音输入：Apple 内置、Moonshine、Parakeet（MLX），自定义 Hugging Face 模型
- 失败恢复、按应用记录 lessons、可从任务或录屏习得并导入导出的 skills

## 适用场景

- 用已登录的 Claude/Cursor 等 MCP 客户端代替我操作 Mac 应用
- 菜单栏语音/文字下达任务，让代理自动完成跨应用操作
- 在本地 Ollama 模型上跑 computer-use 而不用任何云 API
- 为自建模型运行 computer-use 基准测试

## 场景标签

`GUI 自动化` `模型评测` · 领域:效率与自动化

## 证据(README 行号)

> L3: AI computer use for the whole Mac, not just a browser. It works with any AI: Claude, OpenAI (ChatGPT), Gemini, any m
> L21: The app bundles `cu-mcp`, a native MCP server written in Rust. It needs no API key: the AI you already use does the

## 星数曲线

```mermaid
xychart-beta
    title "ajokhai/computer-use-lite 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-10-31", "2026-11-22"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-26 3 → 2026-11-22 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `b6fb3241db5e` · [字段定义](../../DATASET.md)*
