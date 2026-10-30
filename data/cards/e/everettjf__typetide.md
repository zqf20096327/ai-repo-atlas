# everettjf/typetide

⭐ 33 · C++ · MIT · 推送 2026-10-29 · [GitHub](https://github.com/everettjf/typetide) · [官网](http://xnu.app/typetide/) · 个人维护 · 中文 README

**macOS/Windows 系统级 AI 划词翻译与原位改写工具**

驻留菜单栏/系统托盘的桌面翻译应用：划选外文文本弹出翻译，或用自己的母语输入后按快捷键将输入框内容原位改写为目标语言，可在任意应用中工作。通过 Accessibility API（macOS）/UI Automation（Windows）读取选区，剪贴板作回退。后端可插拔：Apple Silicon 内置离线 MLX 模型（TranslateGemma 4B，约 2.22 GB 下载）、Ollama 或任意 OpenAI 兼容 API。支持 10 种语言，macOS 需授予辅助功能权限；非沙盒应用。SwiftUI 与 Win32 C++ 原生实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 划选翻译与原位改写两种模式，全局快捷键触发，适用于任意应用
- 三种可插拔后端：内置离线 MLX 模型 / Ollama / OpenAI 兼容 API
- 替换保留应用原生撤销栈，剪贴板用后即恢复
- API key 存 Keychain / Windows Credential Manager，无托管中转或遥测服务

## 适用场景

- 在聊天、邮件、IDE 中划词查看外文翻译
- 用母语输入后原位改写成外语直接发送
- 离线/本地模型环境下进行私有翻译

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L10: - **Read** — select foreign text, hit a shortcut, and a translation pops up next to it.
> L11: - **Write** — **type in your own language**, hit a shortcut, and it’s rewritten in place into the target language, 
> L33: - **Local or cloud** — pluggable backends: **Built-in MLX** (Apple Silicon Mac), **Ollama** (offline, private), or 

## 星数曲线

```mermaid
xychart-beta
    title "everettjf/typetide 星数(近 7 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-25", "2026-10-26", "2026-10-29", "2026-10-30"]
    y-axis "stars" 26 --> 34
    line [27, 28, 29, 30, 31, 33, 33]
```

2026-10-18 27 → 2026-10-30 33（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0b5c616fcd99` · [字段定义](../../DATASET.md)*
