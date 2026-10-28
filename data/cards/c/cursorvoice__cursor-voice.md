# cursorvoice/cursor-voice

⭐ 26 · Swift · MIT · 推送 2026-06-10 · [GitHub](https://github.com/cursorvoice/cursor-voice) · [官网](https://cursorvoice.app) · 组织维护

**macOS 原生语音助手：看到屏幕、操控电脑并语音回答**

Swift 编写的 macOS 菜单栏语音助手：按热键唤醒后通过 gpt-realtime 实现语音对话，可经 ScreenCaptureKit 读取屏幕内容，通过 CGEvent 合成鼠标键盘输入、按名称点击 Accessibility 树中的 UI 元素，并支持执行 AppleScript 与 shell 命令、免 key 网页搜索、跨会话本地记忆与设备端唤醒词。需自备 OpenAI API key（存于 Keychain），音频在会话期间流式传输至 OpenAI Realtime API。提供 curl 一键安装、Homebrew cask 与 DMG 手动安装，仅支持 Apple Silicon 与 macOS 14+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音进出 + 屏幕理解 + 操控 Mac（鼠标键盘合成、AX 树点击、AppleScript/shell）
- 5 种 Realtime 模型可选，含实时语音翻译模型
- 设备端唤醒词（SFSpeechRecognizer）与本地记忆存储
- curl 一键安装 / Homebrew cask / DMG 三种安装方式

## 适用场景

- 用语音指挥 Mac 打开应用、点按钮、执行命令
- 让助手根据当前屏幕内容回答问题
- 免手操作场景下的语音控制与信息查询

## 场景标签

`语音 Agent` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: A native macOS voice assistant that lives next to your cursor. Press a hotkey, talk to it, and it sees your screen, 
> L18: - **Voice-in / voice-out** via `gpt-realtime` (configurable per-session)
> L20: - **Drives the Mac** — synthesizes mouse and keyboard input via CGEvent; clicks UI elements by name via the Accessi

## 星数曲线

```mermaid
xychart-beta
    title "cursorvoice/cursor-voice 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-28 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `57aa7fd3214e` · [字段定义](../../DATASET.md)*
