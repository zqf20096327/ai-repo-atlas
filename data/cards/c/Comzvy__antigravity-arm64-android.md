# Comzvy/antigravity-arm64-android

⭐ 3 · JavaScript · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/Comzvy/antigravity-arm64-android) · [官网](https://github.com/Comzvy/antigravity-arm64-android/releases/latest) · 个人维护

**在 Android ARM64 上原生运行 Antigravity AI 编程代理的 APK 移植**

将 Antigravity v2.35.0（Linux ARM64 版 AI 编程代理）移植到 Android Bionic 用户空间，无需 PRoot/chroot，通过 liblse_compat.so 提供 ARMv8.0 LSE/SIMD 仿真。提供 BYOK 多供应商接入、技能与插件目录（10 插件/23 技能）、触屏适配的 Workbench 界面、语音模式（端侧识别与云端转录）、内置 PTY 终端（pkg 包管理）与后台任务调度。要求 Android 7.0+ ARM64，APK 从 Release 下载，也可源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Antigravity language_server 直接运行于 Android Bionic，无 PRoot/chroot
- BYOK 接入 Gemini、OpenAI、Anthropic Claude、OpenRouter、Groq、DeepSeek 及兼容端点
- 内置插件目录一键安装/卸载（10 插件、23 技能）
- 语音模式含端侧语音识别与 Whisper/Gemini 云端转录

## 适用场景

- 在 Android 手机或平板上使用 AI 编程代理
- 自带 API key 在移动端接入多家模型服务
- 通过内置终端在移动设备上运行命令行工具

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L4:  Run the Antigravity AI coding agent on Android (ARM64 APK).
> L26: - **Multi-provider AI (BYOK)** — Gemini, OpenAI, Anthropic Claude, OpenRouter, Groq, DeepSeek, or any OpenAI/Anthro

## 星数曲线

```mermaid
xychart-beta
    title "Comzvy/antigravity-arm64-android 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-26 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `19fb6b6302fc` · [字段定义](../../DATASET.md)*
