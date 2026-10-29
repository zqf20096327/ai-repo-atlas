# ZsTs119/openclaw-launcher

⭐ 19 · TypeScript · GPL-3.0 · 推送 2026-04-10 · [GitHub](https://github.com/ZsTs119/openclaw-launcher) · [官网](https://github.com/ZsTs119/openclaw-launcher/releases) · 个人维护 · 中文 README

**零基础用户一键安装运行 OpenClaw AI 编程助手的桌面启动器**

基于 Tauri v2（React + Rust）的桌面应用，面向无编程经验的用户，将 OpenClaw 的安装流程封装为图形操作：自动下载便携版 Node.js 至 AppData 沙盒、从 GitHub 拉取源码（可自动切换国内镜像）、执行依赖安装并启停服务，启动后自动打开浏览器进入对话界面。内置 Groq、SiliconFlow、OpenRouter、DeepSeek、OpenAI 等提供商配置，支持任意 OpenAI 兼容 API。提供 Windows/macOS/Linux 安装包；开发者从源码构建需 Node.js ≥ 22、Rust ≥ 1.70。采用 GPL-3.0，另提供商业授权联系渠道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动下载便携版 Node.js 并隔离在 AppData 沙盒，不污染系统环境
- 多提供商支持（Groq/SiliconFlow/OpenRouter/DeepSeek/OpenAI）及任意 OpenAI 兼容 API
- 网络容灾：主备线路全自动切换，3 秒超时降级
- Windows/macOS/Linux 均提供安装包

## 适用场景

- 不会命令行操作，想在自己电脑上运行 OpenClaw AI 编程助手
- 国内网络环境下顺利完成 Node.js 与源码下载
- 在多个模型提供商之间配置和切换默认模型

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: *OpenClaw Launcher 让你无需任何编程经验，也能在自己的电脑上运行 OpenClaw AI 编程助手。*
> L36: OpenClaw 本身是一个强大的 AI 编程框架，但对非技术用户来说，安装 Node.js、配置环境变量、执行命令行操作是巨大的门槛。
> L48: - **🔧 零环境配置** — 自动下载便携版 Node.js，隔离在 AppData 沙盒中，不污染系统环境

## 星数曲线

```mermaid
xychart-beta
    title "ZsTs119/openclaw-launcher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `a993033eefc9` · [字段定义](../../DATASET.md)*
