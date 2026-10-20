# debpalash/VoiceStudio

⭐ 74,627 · Python · AGPL-3.0 · 推送 2026-10-18 · [GitHub](https://github.com/debpalash/VoiceStudio) · [官网](https://voicestudio.sh) · 个人维护 · 中文 README

**本地运行的开源语音工作台：克隆、配音、转写与有声书制作**

基于 Electron 的桌面语音工作台，默认引擎为 k2-fsa/OmniVoice，支持语音克隆、语音设计、视频配音、听写、转写与有声书批量制作，覆盖 646 种语言。本地工作流在用户硬件上运行，按 GPU/CPU 提供不同加速方式（CUDA、Metal、CPU），并可安装管理本地语音模型；提供本地 API 与 MCP 接入供 agent 调用，支持配方与监视文件夹。Tauri 桌面壳已移除，Electron 为唯一桌面应用与 Web UI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 42,89 位贡献者
- 涨星:近 1 天 **+3,065**(自 20261016 起算)
- 安装:npm 包 `skills` 月下载 23,786,800
- 平台:WINDOWS / MACOS / LINUX · 协议:MCP

## 能力要点

- 语音克隆、语音设计、视频配音、听写、转写、有声书制作，支持 646 种语言
- CUDA / Metal (MPS) / CPU 三类硬件加速路径，无独显也可用（较慢）
- 本地 API 与 MCP 接口，支持 agent 集成与监视文件夹等自动化
- 一键安装脚本覆盖 macOS/Linux/Windows，也可从源码运行

## 适用场景

- 克隆自己的声音并生成语音或有声书
- 给视频做带时间轴的本地配音
- 在没有云端服务依赖的环境下做语音转写与听写
- 让编码 agent 按文档在本机安装并验证语音工具链

## 场景标签

`语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L30: Start with **VoiceStudio** (default, powered by k2-fsa/OmniVoice), or choose another engine. Features & engine cata
> L72: |NVIDIA GPU (Windows / Linux)|CUDA acceleration|
> L108: > **Electron is the only desktop app and web UI.** Version 0.5.3 was the final Tauri release. Existing Tauri users

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `435f07bd08ac` · [字段定义](../../DATASET.md)*
