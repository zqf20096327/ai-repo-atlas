# dat-hoangnguyentuandat/GlibClaw

⭐ 14 · Shell · MIT · 推送 2026-05-04 · [GitHub](https://github.com/dat-hoangnguyentuandat/GlibClaw) · 个人维护

**在已 root 的 Android (aarch64) 上安装运行 OpenClaw 的 Magisk/KernelSU 模块**

一个 Magisk/KernelSU 刷入模块，把 OpenClaw 及其 glibc Node.js 运行时部署到 Android 设备（仅支持 aarch64，root 为前提）。v1.0.2 起不再打包 Node.js，改为刷入时从 nodejs.org 下载；安装路径为 /data/adb/openclaw/，通过 root 终端（Termux）执行 configure/status/tail 等命令管理，Action 按钮可一键拉起网关并在浏览器打开仪表盘。卸载模块时保留用户数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Magisk/KernelSU 模块形式安装 OpenClaw 与 glibc Node.js 运行时
- v1.0.2 刷入时从 nodejs.org 下载 Node.js，不再内置重包
- Action 按钮一键启动网关并打开 dashboard
- 卸载模块时保留 /data/adb/openclaw/home 用户数据

## 适用场景

- 在已 root 的 Android 设备上长期运行 OpenClaw 网关
- 通过手机浏览器访问 OpenClaw dashboard
- 用 Termux root 终端配置与查看 OpenClaw 状态和日志

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: A Magisk/KernelSU module that installs OpenClaw on Android (aarch64) using a bundled glibc runtime.
> L20: - Android device with root access (Magisk or KernelSU)

## 星数曲线

```mermaid
xychart-beta
    title "dat-hoangnguyentuandat/GlibClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `0868f6e0a5fa` · [字段定义](../../DATASET.md)*
