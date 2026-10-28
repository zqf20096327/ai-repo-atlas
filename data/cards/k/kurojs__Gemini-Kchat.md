# kurojs/Gemini-Kchat

⭐ 20 · QML · LGPL-2.1 · 推送 2026-10-11 · [GitHub](https://github.com/kurojs/Gemini-Kchat) · [官网](https://www.pling.com/p/2327619/) · 个人维护

**KDE Plasma 桌面聊天挂件：在面板中直接使用 Google Gemini**

面向 KDE Plasma 6 用户的桌面 plasmoid，通过 Google AI Studio API 接入 Gemini，支持在面板中快速聊天、多模型下拉选择（Flash/Pro/Gemma 等十余种）、会话保存与多会话管理。提供文件与命令功能：Gemini 可列目录、读写文件、执行 shell 命令（以用户权限运行，非沙箱，可在设置中开关）。内置多种 TTS 提供商（云端与本地）、Markdown 渲染与完整的颜色/字体/图标自定义。以 .plasmoid 文件或源码 ZIP 通过 kpackagetool6 安装，需自备 Google AI Studio API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面板内直接与 Gemini 对话，支持十余种 Gemini 模型下拉选择
- 文件操作与 shell 命令执行（以用户权限运行，可在设置中启用/禁用）
- 多 TTS 提供商：ElevenLabs、OpenAI、espeak-ng、Piper、Speech Note
- 会话持久化、多会话管理与完整的界面自定义

## 适用场景

- 在 KDE Plasma 桌面上不离开工作区地与 Gemini 对话
- 让 Gemini 读取目录、写文件并执行 shell 命令
- 为聊天回复配本地或云端语音朗读

## 场景标签

`AI 助手` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L3: Gemini-Kchat is a KDE Plasma plasmoid that integrates Google Gemini AI directly into your desktop. Chat with Gemini 
> L8: - Direct integration with Google Gemini AI
> L119: 3. **Important**: Enter your Google AI Studio API key in the "General" tab

## 星数曲线

```mermaid
xychart-beta
    title "kurojs/Gemini-Kchat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `dcedb1c383d0` · [字段定义](../../DATASET.md)*
