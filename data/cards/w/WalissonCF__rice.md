# WalissonCF/rice

⭐ 8 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/WalissonCF/rice) · [官网](https://ricenotes.app) · 个人维护

**Mac/Windows 本地会议记录应用：本机转录、AI 生成笔记**

记录麦克风与系统音频，用 whisper.cpp 在本机完成会议转录，音频不离开设备；录音结束后按模板（Summary、Decisions、Next actions 等）由用户选择的 AI 填写笔记，支持会中问答、跨会议检索回答、Markdown 导出与 PDF 分享。要求 Apple Silicon Mac 与 macOS 14+，或 Windows 10 22H2/11（x64）；转录需通过 Homebrew 安装 whisper.cpp，首次运行下载约 0.6 GB 模型；笔记与聊天功能需要一个 AI 服务账号或 API key，纯转录可不配置。

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

- 本地 whisper.cpp 转录麦克风与系统音频，音频不上传
- 可选 Claude、ChatGPT、Gemini 或 OpenCode 作为笔记生成后端
- 跨会议提问并附来源链接，会议存档为纯 Markdown 文件
- 提供终端一键安装脚本、.dmg 与 Windows .exe 安装包

## 适用场景

- 开会时录音并自动生成纪要与行动项
- 会后向聊天面板询问会议中说过什么
- 在多次会议笔记中检索并汇总答案

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L7: Rice is a Mac app that records your meetings, transcribes them on your machine and writes the notes for you.
> L11: - **Local transcription.** Records your microphone and the system audio (the other participants) and transcribes wi
> L12: - **Notes written by an AI, from templates.** When the recording ends, Rice fills in the sections of a template (Su

## 星数曲线

```mermaid
xychart-beta
    title "WalissonCF/rice 星数(近 3 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-11-23"]
    y-axis "stars" 6 --> 9
    line [7, 8, 8]
```

2026-10-21 7 → 2026-11-23 8（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `435a2f4919bc` · [字段定义](../../DATASET.md)*
