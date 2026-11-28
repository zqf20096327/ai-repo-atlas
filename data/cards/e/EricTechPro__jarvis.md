# EricTechPro/jarvis

⭐ 28 · JavaScript · AGPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/EricTechPro/jarvis) · 个人维护

**语音驱动的桌面 AI 助手：看屏、指点、画图、点击并调用工具**

以 Tauri 构建的桌面语音助手，用户按住快捷键对话，程序读取本地笔记目录（AGENTS.md 加 _context/_raw/_research 结构）作为记忆来源，语音回答并在屏幕上指点、画图或点击。支持 Gemini/Claude/ChatGPT 云端模型与 Ollama、LM Studio 本地模型；本地模型需具备视觉、工具调用与 32k+ 上下文。文件编辑、命令、应用控制等风险操作默认关闭，密钥存于系统 keychain。macOS/Linux/Windows 提供一键安装脚本，也可从源码构建（需 Rust、Node.js 22+、Tauri）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取本地笔记目录作为第二大脑记忆，每次对话以 AGENTS.md 开头
- 屏幕感知与指点、画图、点击等计算机操作
- 支持云端（Gemini/Claude/ChatGPT）与本地（Ollama/LM Studio）模型
- 风险操作默认关闭，密钥存入 keychain

## 适用场景

- 对着电脑语音提问并让它代为点击或标注屏幕
- 基于个人笔记库做语音问答
- 本地模型保证数据不出机的离线助手场景

## 场景标签

`语音 Agent` `AI 助手` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5:  Talk to your computer like Jarvis.
> L97: - Local     Ollama, LM Studio
> L37: cd jarvis/showcase/tauri


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `80f819a7929c` · [字段定义](../../DATASET.md)*
