# spideydotjs/ollama-android

⭐ 29 · Kotlin · 推送 2026-05-27 · [GitHub](https://github.com/spideydotjs/ollama-android) · 个人维护

**Android 端个人助手 LAMI：本地 LLM 可选接入的聊天客户端**

基于 Jetpack Compose 的 Android 个人助手应用，核心功能（聊天界面、精灵动画反馈）完全离线运行，本地 LLM 连接为可选功能。通过状态机驱动 8 种精灵表情（Idle/Thinking/TalkShort/TalkLong/TalkCalm/ErrorLight/ErrorHeavy/Offline）给出可视化反馈。安装方式为从 GitHub Releases 下载 APK；要求 Android 13+、最低 4GB RAM（推荐 6GB+），本地 LLM 支持需自行部署可运行模型。开发侧提供 pre-commit、Android SDK 与 Gradle 测试流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Jetpack Compose 构建的动画 UI，单状态机管理 8 种精灵表情
- 本地 LLM 集成可选，核心功能完全离线运行
- GitHub Releases 提供 APK 直接下载安装
- 计划功能：TTS 语音同步、情感驱动的表情切换、插件支持

## 适用场景

- 在 Android 设备上与本地大模型对话且数据不出设备
- 通过精灵动画获得聊天状态的可视化反馈
- 开发者在其状态机与精灵集基础上扩展自有交互体验

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: A personal assistant called LAMI, built to run entirely on-device. The Android client uses Jetpack Compose for an ex
> L10: - **Flexible backend**: Local LLM integration is optional — core features work offline.
> L61: 2. (Optional) Enable local LLM connection and load your model.

## 星数曲线

```mermaid
xychart-beta
    title "spideydotjs/ollama-android 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-30 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `3068189597ed` · [字段定义](../../DATASET.md)*
