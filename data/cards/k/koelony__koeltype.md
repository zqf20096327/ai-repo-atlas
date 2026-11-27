# koelony/koeltype

⭐ 27 · Rust · MIT · 推送 2026-11-26 · [GitHub](https://github.com/koelony/koeltype) · [官网](https://oratype.sennettlau.me) · 个人维护 · 中文 README

**macOS 语音键盘：任意应用中说一下即得整洁文本**

面向 macOS 用户的语音键盘应用：按快捷键说话，将语音转为文本，去除填充词、套用自定义修正、添加标点并粘贴到当前输入位置；支持最多三种目标语言的实时翻译与对选中文本提问。基于 Tauri 构建，语音识别默认由内置 whisper.cpp 完成，文本润色由 llama.cpp server 完成，一键下载模型并做 SHA-256 校验；也可连接任何 OpenAI 兼容服务器或自带 key 的云服务。MIT 许可，无账号无遥测，仅支持 Apple Silicon (M1 及以后)。

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

- 任意应用中按快捷键说话即得整洁文本并自动粘贴
- 内置 whisper.cpp 语音识别与 llama.cpp server AI 润色，一键配置模型
- 语言预设与路由：按检测到的语言套用对应语言的书写规则
- 翻译目标语言可在录音过程中按键切换

## 适用场景

- 在 macOS 各应用中用语音代替打字
- 说话内容实时翻译成多种目标语言
- 高亮文本后让 AI 改写或回答问题
- 本地运行模型，语音不经第三方

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L17: OraType is a voice keyboard for macOS. Hold or tap a shortcut and speak. OraType turns your
> L84: On Apple Silicon, both halves can run on your computer with nothing else to install.
> L85: whisper.cpp handles speech recognition inside the app,
> L86: and llama.cpp's server handles AI polish. Press


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `e9fb7d5d836c` · [字段定义](../../DATASET.md)*
