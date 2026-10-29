# app-vox/vox

⭐ 33 · TypeScript · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/app-vox/vox) · [官网](https://usevox.app/) · 组织维护

**本地 Whisper 语音转文字桌面应用，可选 LLM 纠正文本**

面向 macOS 与 Windows 用户的听写工具：按住快捷键说话，whisper.cpp 在本地完成语音转写，音频不出设备；转写文本可选发送至 OpenAI 兼容端点或 AWS Bedrock 做 LLM 纠正（去填充词、修语法、自定义提示词），再自动粘贴到当前应用。提供菜单栏常驻、多种 Whisper 模型（tiny~large）选择、按住/切换两种录音模式。Linux 支持未提供。以安装包形式分发，开发构建需 cmake。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- whisper.cpp 本地转写，音频不离开设备
- 可选 LLM 纠正：OpenAI 兼容端点或 AWS Bedrock，支持自定义提示词
- 五种 Whisper 模型（tiny~large）可选，权衡速度与准确率
- 菜单栏常驻、全局快捷键、自动粘贴到焦点应用

## 适用场景

- 在任意应用中用语音快速输入文字，替代打字
- 医疗/技术等场景用自定义提示词保留专业术语做口述记录
- 完全离线环境下做本地语音转写

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: Open-source voice-to-text app with local Whisper transcription and AI-powered correction.
> L52: - **🔒 100% Local transcription** — Powered by whisper.cpp, audio stays on your device
> L195: - **Local transcription**: Whisper.cpp converts your speech to text on your device. Fast, accurate, 100% private.

## 星数曲线

```mermaid
xychart-beta
    title "app-vox/vox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `da3f9e205b79` · [字段定义](../../DATASET.md)*
