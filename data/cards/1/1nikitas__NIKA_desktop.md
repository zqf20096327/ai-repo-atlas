# 1nikitas/NIKA_desktop

⭐ 34 · Swift · 推送 2026-10-13 · [GitHub](https://github.com/1nikitas/NIKA_desktop) · 个人维护

**macOS 本地 LLM 桌面助手：离线聊天与文档对话**

用 SwiftUI 和 llama.cpp 构建的原生 macOS 聊天应用：下载或导入 GGUF 模型在本地离线运行，支持文本与可提取文本的 PDF 对话、本地历史与记忆、日历/提醒事项集成（动作执行前需确认）。提供 NIKA Mini/Balance/Smart/Quality 四档 Qwen3.5 模型及内存指引。云端功能（Telegram 登录、云 agent）为可选，云端后端不在本仓库。需 Apple Silicon、macOS 26+、Xcode 16.4+ 源码构建，无公证发布版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GGUF 模型本地离线运行，本地聊天无需账号
- PDF 与文本文档对话，视觉投影器可启用图像输入
- 本地模型出错不会静默转发请求到云端
- 可选接入 NIKA 云：云 agent、工具与自定义助手

## 适用场景

- 在 Mac 上离线与本地 LLM 对话
- 对本地 PDF 和文本文档做问答
- 创建带自定义指令与素材的助手

## 场景标签

`AI 助手` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L7: **Your AI assistant, running on your Mac.** Download a local model, chat offline, and work with your documents. Buil
> L37: - **Local LLMs:** download a model or import a compatible GGUF and run it through llama.cpp.

## 星数曲线

```mermaid
xychart-beta
    title "1nikitas/NIKA_desktop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-30 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `966c6e9fcbd4` · [字段定义](../../DATASET.md)*
