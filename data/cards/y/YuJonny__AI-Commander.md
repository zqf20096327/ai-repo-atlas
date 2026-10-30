# YuJonny/AI-Commander

⭐ 15 · Swift · MIT · 推送 2026-07-27 · [GitHub](https://github.com/YuJonny/AI-Commander) · 个人维护 · 中文 README

**把耳机播放键变成语音输入键的桌面工具（macOS/Windows）**

面向 macOS（Apple 芯片）与 Windows x64 的桌面应用：接管耳机播放/暂停媒体键，按一下开始、再按一下结束，将语音转写文字直接写入光标位置。提供两种方式：内置本地语音输入（Qwen3-ASR 高精度档或 SenseVoice 轻量档，基于 sherpa-onnx，可选 Qwen3-8B 经 llama.cpp 做润色），或仅做按键映射调用已安装的语音工具（内置豆包、微信、Typeless、Claude Code 等预设）。录音与文字全程本地处理，需授予辅助功能与麦克风权限；Intel Mac 不支持本地语音。以 Releases 安装包分发，也可从源码构建。

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

- 耳机媒体键一按即说的 push-to-talk 语音输入
- 两档本地语音识别：Qwen3-ASR（30 种语言+22 种中文方言）与 SenseVoice 轻量档
- 规则清理 + 可选 Qwen3-8B 本地大模型润色（去重、数字格式、断句）
- 内置豆包/微信/Typeless/Claude Code 等语音工具快捷键预设

## 适用场景

- 用耳机键一键唤起语音输入，文字直接落到当前输入框
- 口述后自动清理口语词并整理成稿，用于笔记或写作
- 通过耳机键快捷触发已安装的语音工具（如 Typeless、微信输入法）

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L40: AI 接线员 v2.1 有两种独立的使用方式：在 Apple 芯片 Mac 或 Windows x64 电脑上直接使用内置的本地语音输入；或只做耳机键映射，调用已经安装的语音工具。使用本地语音不需要安装 Typeless、微信输入
> L43: - **全程本地，永久免费**：识别、清理、润色全在本机，录音与文字不上传；开源可审计。

## 星数曲线

```mermaid
xychart-beta
    title "YuJonny/AI-Commander 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e52c6898dca8` · [字段定义](../../DATASET.md)*
