# gouravraghuwanshi/saturn-agent

⭐ 8 · Kotlin · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/gouravraghuwanshi/saturn-agent) · [官网](https://gouravraghuwanshi.github.io/saturn-agent/) · 个人维护

**在 Android 手机上运行 agent 完成任务的独立应用**

Saturn 是一个 Android 应用，内嵌 Pi agent 运行循环与设备端 Linux 用户空间（Node.js、bash、git、ripgrep、ssh 等，以 jniLibs 打包 Termux 构建的二进制文件，免 root、无后端服务器）。用户选定模型提供商并给出任务后，agent 可编辑文件、运行命令、构建 web 应用或触发手机动作；支持并发任务会话、Artifacts 收集、Termux:API 兼容的手机硬件命令、定时任务与内置浏览器/GitHub/SSH。安装方式为从 Releases 下载 APK，要求 Android 10+ arm64。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端 Linux 用户空间：内置 Node.js、bash、git、ssh 等，无需 Termux 或 root
- 每个任务运行在独立 pi --mode rpc 进程，会话可回访/分支/导出
- Termux:API 兼容命令控制手电筒、相机、定位、传感器等手机硬件
- 无账号、无后端服务器，数据留在设备私有存储

## 适用场景

- 在手机上让 agent 编辑文件、跑命令、构建小型 web 应用
- 用自然语言触发手机硬件动作（拍照、定位、通知、TTS）
- 定时执行 cron 风格的后台任务，应用关闭也能运行
- 通过 SSH 或内置浏览器让 agent 操作远程机器和网页

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: Saturn is an agent that can do anything on your phone, not just code. Pi runs the agent loop, and Saturn gives it a
> L16: - **On-device Linux userland:** Ships Node.js, bash, git, ripgrep, ssh, and built-in utilities (`jq`, `pdftotext`, 
> L23: - **Flexible models:** Sign in with ChatGPT, Claude, Copilot, and others, or bring your own API key (OpenRouter, An


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `1bab469bb7d2` · [字段定义](../../DATASET.md)*
