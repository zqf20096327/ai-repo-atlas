# SadmanMahi67/OpenFlow

⭐ 16 · TypeScript · MIT · 推送 2026-05-28 · [GitHub](https://github.com/SadmanMahi67/OpenFlow) · 个人维护

**Windows 桌面听写应用：按住热键说话，离线 Whisper 转写后自动粘贴**

面向 Windows 10/11 x64 用户的 Electron 听写应用：按住 Ctrl+Win 录音，经 whisper.cpp 在本地离线转写（支持 99 种语言、可选 Vulkan 加速），可选用 Groq 托管模型或本地 llama.cpp 模型做文本润色（支持 Llama 3.2 3B、Gemma 3 4B、Qwen 2.5 3B），结果经剪贴板自动粘贴到当前窗口。内置模型下载管理、转写历史、词汇表、自定义润色风格与提示词过滤器。多数用户从 GitHub Releases 下载安装包，也可 npm 从源码构建。多语言转写处于 beta，英文效果最好。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- whisper.cpp 离线转写，支持 99 种语言与可选 Vulkan 加速
- AI 润色可选 Groq 托管模型或本地 llama.cpp 完全离线
- 键盘布局自动检测语言、keybd_event 布局无关粘贴
- 应用内 Whisper 模型下载管理（Small 至 Large Turbo Q5）

## 适用场景

- 在任何 Windows 应用中按住热键语音输入文字
- 对语音转写文本做语气/格式润色后再粘贴
- 完全离线环境下的本地语音转写与整理

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: Openflow is a Windows desktop dictation app that records while the user holds `Ctrl + Win`, transcribes speech offli
> L36: - `whisper.cpp` Windows runtimes for offline transcription, bundling CPU fallbacks and an optional Vulkan build
> L54: - Offline local AI refinement with llama.cpp (supports Llama 3.2 3B, Gemma 3 4B, Qwen 2.5 3B)

## 星数曲线

```mermaid
xychart-beta
    title "SadmanMahi67/OpenFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `beb6c9fd175f` · [字段定义](../../DATASET.md)*
