# HumanMeatSack/claw-assistant-android

⭐ 3 · JavaScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/HumanMeatSack/claw-assistant-android) · 个人维护

**Android 端自托管语音助手：手机本地运行模型对话**

基于 OpenClaw 构建的 Android 开发者预览应用，提供按侧键或 "Hey Aiden" 唤起的语音助手面板。导入经校验的 Qwen3-4B 模型后，普通对话、唤醒检测（Parakeet 离线英文识别）与 TTS 回复均在手机本地完成；可选自托管 Gateway 作为独立会话路由，并支持显式 "Ask Codex" 请求经 Gateway 转发。需自行下载模型权重并按 Android 指南构建安装，无响应时间承诺。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 手机本地运行导入的 Qwen3-4B 模型对话，含校验和验证
- Parakeet 离线英文识别与 Android 离线 TTS 回复
- 侧键长按与 "Hey Aiden" 免提唤起，浮层于其他应用之上
- 可选自托管 Gateway 路由与显式 Codex 转发

## 适用场景

- 在 Android 手机上获得不依赖云端的本地语音助手
- 通过侧键或唤醒词在其他应用之上快速提问
- 对数据流向敏感、希望普通对话留在本机的用户

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L12:  Android handles offline recognition, imported Qwen3-4B conversation, phone utilities, and voice playback. A privat
> L39: 2. For phone-local conversation, download the pinned Qwen3-4B model separately. Open **Settings → Voice → Local pho
> L57: The development handset is a Galaxy S24 Ultra running Android 17. The local runtime is an ARM64/GPU-oriented previe


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `7058d7d54aa6` · [字段定义](../../DATASET.md)*
