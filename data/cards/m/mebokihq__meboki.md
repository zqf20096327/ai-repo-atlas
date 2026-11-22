# mebokihq/meboki

⭐ 4 · Swift · GPL-3.0 · 推送 2026-11-20 · [GitHub](https://github.com/mebokihq/meboki) · [官网](https://meboki.com/) · 个人维护

**macOS 本地私有语法检查工具：开源 LLM 在本机运行**

面向 macOS 的菜单栏应用：通过 Accessibility API 读取各应用文本框内容，由本机运行的开源模型（经 llama.cpp 服务器的 Gemma 4）或 Apple Intelligence 在设备端检查拼写与语法，用户以波浪下划线和弹卡逐条应用修正。支持任意应用中的文本框、⌃⌥G 按需检查、英美式英语与 casual 模式、按应用开关。可选配置自己的 OpenRouter/OpenAI key 走云端，默认关闭。无账号、无遥测；源码 GPL-3.0，签名版应用为试用+许可模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 llama.cpp 在本机运行 Gemma 4，文本不出设备，下载模型后可离线使用
- 支持任意应用文本框（Safari/Chrome/Gmail/Notion/Slack 等）与 ⌃⌥G 按需检查
- macOS 26 上可选用 Apple Intelligence 设备端模型，无需下载
- 可选自有 OpenRouter/OpenAI key 的云端检查，默认关闭

## 适用场景

- 在写邮件、文档或聊天时获得本地语法修正而不上传文本
- 无网络环境下离线检查英文拼写与语法
- 按应用单独启用或关闭语法检查

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5:  A private grammar checker for macOS.
> L18: - **Runs on your Mac:** Gemma 4 through a bundled llama.cpp server. Works offline after the model download.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `02722861d9c1` · [字段定义](../../DATASET.md)*
