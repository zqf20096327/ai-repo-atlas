# supermandiao/zhanshen-dsh

⭐ 3 · 推送 2026-11-16 · [GitHub](https://github.com/supermandiao/zhanshen-dsh) · 个人维护 · 中文 README

**Android 端本地代理对话应用，内置破甲系统提示词**

基于开源 DSH Go v1.0.14 的非官方 Android 修改版：通过 proot 容器在手机本地（免 Root）运行 Ubuntu 环境启动 DeepSeek Harness 代理服务，Flutter 原生界面与之对话，应用自身不提供模型，需用户自配 DeepSeek API Key。核心修改是把系统提示词替换为「战神条款」破甲框架，抑制拒答与审查倾向，并移除自动更新；仅分发 arm64 APK 二进制，仓库不含源码，仅限成年人使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- proot 容器内本地运行 Ubuntu + 代理服务，免 Root
- 系统提示词替换为「战神条款」，遇拒答自检改写重发
- 支持对话、工具调用、多轮任务、文件读写、识图、语音、桌宠
- 提供 APK 的 SHA-256 校验信息与签名说明

## 适用场景

- 在 Android 手机上通过 DeepSeek API 进行多轮对话与工具调用
- 本地终端环境里安装 node/python/git 并执行命令
- 需要识别图片、语音输入的移动端助手使用场景

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L10: 一个 Android 应用：在手机本地（免 Root，proot 容器里跑 Ubuntu）启动 DeepSeek Harness 代理服务，再用 Flutter 原生界面与之对话。它自己不提供模型，模型能力来自你自己配置的 Dee
> L44: - 对话、工具调用、多轮任务执行


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `a13e8187d401` · [字段定义](../../DATASET.md)*
