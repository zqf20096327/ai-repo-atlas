# Yhoanes/deepseek-android

⭐ 4 · Python · NOASSERTION · 推送 2026-11-24 · [GitHub](https://github.com/Yhoanes/deepseek-android) · [官网](https://yhoanes.github.io/deepseek-android/) · 个人维护

**在 Android 手机本地运行 DeepSeek 自主编程 IDE 的原生 ARM64 APK**

将 DeepSeek Harness Desktop 自主软件工程工作区打包为 91 MB 自包含 Android 应用（com.ds.ide）：通过内核 execve() 直接执行，内嵌 Rust+Zstandard 引导引擎、ARM64 Node.js 运行时与 Bionic 用户空间，不依赖 PRoot、Termux 或 Gradle。提供多会话 agent 线程、子代理、PTY 终端、文件 diff、15 个原生 MCP 插件（GitHub、Ghidra、Chromium 等）、PKCE OAuth 登录与 GitHub Releases OTA 更新。仅支持 arm64-v8a 设备，Android 9+，许可证为 BY-NC 非商业条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 免 PRoot/Termux，经 Linux kernel execve() 在移动端原生执行
- 15 个原生 ARM64 MCP 插件，热挂载零重启
- DeepSeek 账号 PKCE 一键登录及自定义 OpenAI/Anthropic 兼容模型接入
- 无 Gradle/Android Studio 的确定性源码构建管线

## 适用场景

- 在手机或平板上运行 DeepSeek 自主编程代理进行软件开发
- 通过 MCP 插件在移动端做逆向分析、视频渲染或 GitHub 管理
- 离线语音输入与本地会话管理代码工作区

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L19: **DeepSeek for Android (`v0.2.2-r4`)** brings the official **DeepSeek Harness Desktop (`@deepseek-ai/dsh`)** autono
> L37: |**Desktop-Identical DeepSeek Experience**|Runs the authentic `@deepseek-ai/dsh-web-app` & Cordis plugin architectu


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `f79a95607e57` · [字段定义](../../DATASET.md)*
