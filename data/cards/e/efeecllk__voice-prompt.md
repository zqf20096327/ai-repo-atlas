# efeecllk/voice-prompt

⭐ 14 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/efeecllk/voice-prompt) · 个人维护

**语音输入生成 AI 提示词的桌面应用：说母语得英文提示词**

基于 Tauri 2.0 的跨平台菜单栏/托盘应用：录音后经 OpenAI gpt-transcribe 转文字，再用 GPT-4.1-nano 按所选格式处理，输出标准英文翻译、正式/随意英文、面向 Claude Code 的详细提示词或自定义模板；支持 20+ 源语言、全局快捷键跨应用听写并复制到剪贴板、历史/收藏/提示词库，以及直接发送到 Ghostty/Warp/iTerm2/Terminal.app。需用户自备 OpenAI API key（按用量计费）。macOS 提供 Homebrew 与签名 DMG，Windows 提供 MSI/NSIS，Linux 提供 deb/AppImage。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI gpt-transcribe 语音转文字 + GPT-4.1-nano 处理输出
- 全局快捷键任意应用内听写，结果自动复制到剪贴板
- Ralph Wiggum 模式将语音请求扩展为 Claude Code 提示词
- 可直接粘贴到 Ghostty/Warp/iTerm2/Terminal.app（可自动提交）

## 适用场景

- 用母语口述并生成可用的英文 AI 提示词
- 不切换窗口即可全局听写并粘贴结果
- 把生成的提示词直接送进终端工作流

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A lightweight cross-platform app that converts speech to text and processes it with AI. Perfect for crafting prompts
> L72: |**Speech-to-Text**|Powered by OpenAI gpt-transcribe - industry-leading accuracy|
> L263: |Speech-to-Text|OpenAI gpt-transcribe|

## 星数曲线

```mermaid
xychart-beta
    title "efeecllk/voice-prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2075f4218773` · [字段定义](../../DATASET.md)*
