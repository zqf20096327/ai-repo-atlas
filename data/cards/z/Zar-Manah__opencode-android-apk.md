# Zar-Manah/opencode-android-apk

⭐ 17 · Java · NOASSERTION · 推送 2026-10-08 · [GitHub](https://github.com/Zar-Manah/opencode-android-apk) · 个人维护

**Android 原生 AI 编程代理：手机上自主编码并编译安装 APK**

在 Android 设备上原生运行（arm64、musl 链接器、无 PRoot）的 AI 编程代理与 App 工厂：内置 OpenJDK 21、Android SDK 与 Gradle，可在设备上完成脚手架、编译、签名、安装 APK，并通过 pc 系列 CLI 截屏、点击、输入、启动应用形成自主验证闭环；提供跨会话的长期记忆与 24/7 前台守护通知。免 root，需 Android 8.0+/arm64-v8a，从 GitHub Releases 下载 APK 安装，支持免费 OpenCode 模型或自定义 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯原生 arm64 执行（musl 动态链接器，无 PRoot/容器）
- 设备端自主完成 APK 编译、签名、安装与 UI 截屏验证闭环
- pc CLI 提供截屏/点击/滑动/输入/装包/发通知等设备控制
- 内置 OpenJDK 21、Android SDK、Gradle 工具链，无需 PC

## 适用场景

- 只用手机完成 Android 应用的编码、编译与安装
- 让 AI 代理通过截屏和点击在设备上验证自己的产出
- 在无桌面 PC 的环境下运行长时 AI 编程任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: > **The first fully autonomous, native AI software engineering workstation and Android app factory directly on your
> L48: ### 4. 🏭 Autonomous On-Device Android App Factory 🔥
> L109: OpenCode includes the `pc` device control CLI, accessible directly from the agent's environment:

## 星数曲线

```mermaid
xychart-beta
    title "Zar-Manah/opencode-android-apk 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23", "2026-10-30"]
    y-axis "stars" 11 --> 18
    line [12, 14, 15, 17, 17]
```

2026-10-18 12 → 2026-10-30 17（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `191c16aee845` · [字段定义](../../DATASET.md)*
