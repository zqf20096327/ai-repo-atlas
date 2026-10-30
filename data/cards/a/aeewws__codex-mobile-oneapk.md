# aeewws/codex-mobile-oneapk

⭐ 24 · Kotlin · MIT · 推送 2026-10-09 · [GitHub](https://github.com/aeewws/codex-mobile-oneapk) · 个人维护 · 中文 README

**把本地 Codex 运行时打包进单 APK 的 Android 手机客户端**

基于 Jetpack Compose 的 Android App：将社区版 Codex arm64 运行时打包进单个 APK，不再依赖外部 Termux App；由 App 自行解压 runtime 到私有目录、探测并拉起本地 codex app-server，管理其生命周期与认证状态。提供聊天优先的移动端交互、历史会话管理、模型/智力档位/权限切换、浏览器 OAuth 与设备码登录、附件输入。构建时需注入 runtime 产物，首版仅支持 arm64-v8a，Android 9+，root 为可选增强项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单 APK 内置 arm64 运行时，不依赖外部 Termux App
- 自动探测并拉起本地 codex app-server，支持恢复与重启
- App 内浏览器 OAuth、设备码登录与本地登出
- 历史会话归档/恢复、模型切换、权限模式与 Fast 模式

## 适用场景

- 在 Android 手机上继续本地 Codex 的 AI coding 会话
- 以移动 App 形态管理本地 Codex 运行时与登录状态
- 长对话中断后重连并续接线程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: 这一版不再依赖 Termux App 本身，而是把 arm64 运行时打包进 APK，由 App 自己管理本地 runtime、认证状态和 `codex app-server` 生命周期。
> L48: - App 自己拉起 backend：围绕本地 `codex app-server` 做探测、重启和恢复
> L116: 更准确地说，这个项目更适合被理解为“围绕本地 coding runtime 的 Android 产品外壳”，而不是一个无需环境假设就能直接跑起来的通用 App。

## 星数曲线

```mermaid
xychart-beta
    title "aeewws/codex-mobile-oneapk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `55b70e896fa1` · [字段定义](../../DATASET.md)*
