# xiaoxiao44443/DSH-Sugar

⭐ 3 · Kotlin · MIT · 推送 2026-11-22 · [GitHub](https://github.com/xiaoxiao44443/DSH-Sugar) · 个人维护 · 中文 README

**在 Android 手机上运行 DeepSeek Harness 的 AI Agent 客户端**

将 DeepSeek Harness（DSH）与 Linux 环境打包到 Android 手机上运行的开源应用：每个工作区有独立 /workspace、终端与项目进程，支持 Bash、Git、Python、Node.js 本机执行。Agent 可被指派操作主屏或虚拟屏，通过 Python 接口读取控件、截图、点击与拖动；桌宠便签与语音插件可在其他应用中接续对话。以 APK 分发，要求 Android 10+ ARM64，无需 root，Root 为可选能力；源码需在 Windows 上用 PowerShell 脚本构建。

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

- 工作区文件隔离，多对话共享项目文件与 DSH 配置
- 主屏/虚拟屏两种模式供 Agent 操作手机（共用 Python 接口）
- 桌宠便签与语音插件支持在其他应用中回复任务
- 提供 GitHub Actions 云端打包生成签名 APK

## 适用场景

- 在手机上与 DSH 对话写代码、开终端、交付文件
- 让 Agent 操作手机屏幕完成计算器等应用操作
- 把手机目录设为工作区，从已有项目开始

## 场景标签

`AI 助手` `编码 Agent` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: **在 Android 手机上运行 DeepSeek Harness。** 在熟悉的 DSH 对话里写代码、开终端、交付文件，也可以把当前屏幕或一块独立的虚拟屏交给 Agent 操作。DSH 和项目的 Linux 环境都运行在手机上
> L27: 比如让 Agent 打开计算器核对一笔账。选主屏时，你能看见它打开应用、按键和读数的全过程。选虚拟屏时，计算器在另一块屏幕里运行，主屏可以继续用。两种模式共用一套 Python 接口，能读取控件、截图、点击、长按和拖动，也能按页面


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `edf4c0381a93` · [字段定义](../../DATASET.md)*
