# koelony/munia

⭐ 27 · Rust · MIT · 推送 2026-11-27 · [GitHub](https://github.com/koelony/munia) · [官网](https://oratype.sennettlau.me) · 个人维护 · 中文 README

**macOS 语音键盘：任意应用内说话即得整洁文本**

面向 macOS（Apple Silicon）的语音输入工具：按快捷键在任何应用中说话，经语音识别、填充词去除、自订修正与标点处理后，将文本粘贴到光标处，另支持翻译与针对选中文本提问。默认在本地运行 whisper.cpp（识别）与 llama.cpp server（润色），一键设置按硬件自动下载模型并校验 SHA-256；也可接入任何 OpenAI 兼容服务器或自有 API key 的云服务。MIT 许可，无账号、无遥测，提供 DMG 安装包与源码构建路径（需 Rust、Node.js 22.12+、Xcode CLT、CMake）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 快捷键即说即粘贴，支持填充词清理、自订修正与标点
- 语言预设与路由：按识别语言套用对应书写规则（如粤语、英语、普通话）
- 本地运行 whisper.cpp 与 llama.cpp server，模型自动下载并校验 SHA-256
- 最多三个翻译目标语言，录音中按键切换

## 适用场景

- 在任意应用中用语音替代键盘输入文字
- 说话同时口译为其他语言
- 选中一段文本让 AI 改写或回答问题
- 粤语使用者在 Apple Silicon Mac 上本地语音打字

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L17: Munia is a voice keyboard for macOS. Hold or tap a shortcut and speak. Munia turns your
> L86: whisper.cpp handles speech recognition inside the app,
> L87: and llama.cpp's server handles AI polish. Press


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `4cf827af56ba` · [字段定义](../../DATASET.md)*
