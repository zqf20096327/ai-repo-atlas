# DSH-APP/DSHA

⭐ 3,744 · Java · MIT · 推送 2026-11-27 · [GitHub](https://github.com/DSH-APP/DSHA) · 组织维护 · 中文 README

**免 ROOT 免 Termux 在手机运行 DeepSeek Harness 的启动器**

DSHA 将 DeepSeek 官方 agent harness（@deepseek-ai/dsh）打包进一个 Android APK：内含 Ubuntu 24.04 arm64 离线 rootfs、Node.js 24 与 pnpm，首次启动解包校验后在后台启动 web 服务，用户通过 Web UI 配置 provider、模型与 API key。提供 proot/proroot 两种运行时、组件自检修复、定时备份与导出迁移，并通过无障碍服务与 ADB 让 agent 操作手机。要求 Android 11+ / arm64-v8a，APK 约 302 MiB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 打包完整 Ubuntu 24.04 离线 rootfs，支持 apt/PTY/原生模块编译
- 六步安装管线逐步探测、校验，仅重试失败步骤
- 无障碍服务 + ADB + 独立虚拟屏，agent 可读屏、点击、装应用
- 组件级自检、定向修复与独立恢复 DSH

## 适用场景

- 在 Android 手机上运行 DeepSeek 编码 agent 而不依赖 Termux
- 通过 Web UI 配置多 provider 与 API key 使用 agent
- 利用无障碍与 ADB 能力让 agent 自动化操作手机

## 场景标签

`编码 Agent` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3:  DeepSeek Harness launcher for Android
> L75: DeepSeek Harness (`@deepseek-ai/dsh`) is DeepSeek's official agent harness, written for glibc Linux. Running it dir
> L77: **DSHA packs all of that into one APK.** On first launch it unpacks and verifies a bundled offline environment, the

## 星数曲线

```mermaid
xychart-beta
    title "DSH-APP/DSHA 星数(近 27 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 2031 --> 3899
    line [2313, 2413, 2473, 2550, 2606, 2711, 2784, 2849, 2186, 3197, 3267, 3290, 3326, 3375, 3406, 3442, 3469, 3517, 3542, 3575, 3602, 3633, 3651, 3674, 3717, 3731, 3744]
```

2026-10-26 2,313 → 2026-11-28 3,744（+1,431）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `5eaec2b8979f` · [字段定义](../../DATASET.md)*
