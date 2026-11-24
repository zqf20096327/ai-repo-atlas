# TekihiXac52/unfiltered-ai-chat

⭐ 66 · C++ · MIT · 推送 2026-11-23 · [GitHub](https://github.com/TekihiXac52/unfiltered-ai-chat) · 个人维护

**本地 Windows 便携版 LLM 聊天客户端，带角色预设**

UnfilteredAiChat 是一个以本地方式运行的 LLM 聊天工具，提供 Windows x64 便携预编译包，配置全部集中在 config/settings.json，支持热重载而无需重启。README 描述的引擎组件包括环形缓冲管线、崩溃可回滚的原子 JSON 状态、配置监视器与默认静默的 stderr 遥测。压缩包带访问码，需运行 Setup 可执行文件；也提供 CMake 从源码构建路径。README 未说明其接入的模型或推理后端。

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

- 提供 Windows x64 预编译便携包，无需编译即可运行
- config/settings.json 热重载配置，修改不需重启
- 原子 JSON 状态引擎，带崩溃安全回滚
- 支持 CMake 从源码构建

## 适用场景

- 在本地机器上运行不依赖云端的聊天 CLI
- 通过角色预设定制对话行为
- 以便携方式在 Windows 上部署聊天工具

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L20: **UnfilteredAiChat — Local unfiltered AI chat — your machine, your rules** (`unfiltered-ai-chat`) ships as a native
> L3: # UnfilteredAiChat — Local Unfiltered LLM Chat with Character Presets (One-Command Setup, Prebuilt Release)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 low · 依据 README sha `77acc202fc56` · [字段定义](../../DATASET.md)*
