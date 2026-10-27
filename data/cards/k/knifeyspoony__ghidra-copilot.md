# knifeyspoony/ghidra-copilot

⭐ 40 · Java · 推送 2026-03-21 · [GitHub](https://github.com/knifeyspoony/ghidra-copilot) · 个人维护

**Ghidra 内的 LLM 聊天助手：逆向分析中问答与工具调用**

Ghidra 逆向工程平台的扩展插件：嵌入聊天面板，针对当前打开的程序回答问题、建议下一步操作并直接执行符号搜索、数据提取、重构辅助等工具调用。通过 Spring AI 接入 OpenAI、Azure OpenAI、Anthropic 与 Ollama，在 Ghidra 内 Tool Options 中配置 provider 与 API key/base URL。要求 Ghidra 11.4.2 或兼容版本、Java 17+，需 gradlew 构建 zip 后经 Install Extensions 安装；截图尚未提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天面板与当前打开程序保持上下文关联
- 工具调用：符号搜索、数据提取、重构辅助
- 支持 OpenAI / Azure OpenAI / Anthropic / Ollama（经 Spring AI）
- 以 Ghidra 扩展形式构建安装

## 适用场景

- 在 Ghidra 中通过对话询问当前程序的分析问题
- 让 AI 建议逆向分析的下一步操作
- 用本地 Ollama 模型做离线辅助分析

## 场景标签

`网络安全` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: AI-assisted companion for Ghidra. It embeds a chat panel that can answer questions about your current program, sugge
> L8: - Works with OpenAI, Azure OpenAI, Anthropic, and Ollama through Spring AI.

## 星数曲线

```mermaid
xychart-beta
    title "knifeyspoony/ghidra-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-27 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `dd53c9ad9263` · [字段定义](../../DATASET.md)*
