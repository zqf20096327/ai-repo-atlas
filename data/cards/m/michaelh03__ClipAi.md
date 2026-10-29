# michaelh03/ClipAi

⭐ 23 · Swift · MIT · 推送 2026-06-24 · [GitHub](https://github.com/michaelh03/ClipAi) · 个人维护

**macOS 菜单栏剪贴板管理器，可一键将剪贴板内容发给 AI 处理**

macOS 菜单栏剪贴板历史管理工具：记录并搜索剪贴板内容，支持文本、图片与代码的语法高亮预览，提供全局快捷键。AI 为可选功能：配置 OpenAI 或 Google Gemini 的 API key 后，可用内置或自定义提示词（如代码审查、JIRA 工单生成、文本润色）一键处理剪贴板内容。通过 Homebrew Cask、发布页下载或 Xcode 源码构建安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 剪贴板历史存储与搜索，文本/图片/代码语法高亮预览
- 一键将剪贴板内容交给 AI 处理，支持 OpenAI 与 Google Gemini
- 自定义提示词模板（{input} 占位符）并可绑定全局快捷键
- 内置提示词：代码审查、JIRA 工单生成、文本改写

## 适用场景

- 在菜单栏快速查找和预览历史剪贴板内容
- 复制代码后不切换窗口，直接用 AI 做代码审查或生成工单
- 为自己的工作流定制提示词并通过快捷键调用

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11: ClipAI remembers everything you copy and lets you send it to AI with one click no more breaking your flow switching
> L21: - **Smart Clipboard History** - Store and search through your clipboard history with an intuitive interface
> L24: - **Multiple AI Providers** - Choose between OpenAI or Google Gemini

## 星数曲线

```mermaid
xychart-beta
    title "michaelh03/ClipAi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4fe033cb16bc` · [字段定义](../../DATASET.md)*
