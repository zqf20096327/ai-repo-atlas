# kusesad-1122/XINCODE-Public

⭐ 24 · C · GPL-3.0 · 推送 2026-09-22 · [GitHub](https://github.com/kusesad-1122/XINCODE-Public) · 个人维护 · 中文 README

**运行在 Android 手机上的纯 Kotlin 原生 AI 智能体应用**

无跨端框架的原生 Android 应用，用 Kotlin 与 Jetpack Compose 构建。智能体核心接入 OpenAI Chat Completions/Responses、DeepSeek、Anthropic 等多供应商，支持工具调用循环、结构化输出、子智能体并行协作与计划模式。记忆采用 FTS 全文检索加向量语义检索，普通对话互通、项目内按项目隔离。内置 root/Ubuntu（chroot）终端环境、在线插件市场（27 个实测插件、8 分类）、MCP 支持（stdio + HTTP）与权限确认、审计日志等安全机制。不内置托管密钥，API Key 仅存于设备 Keystore。从源码构建需 JDK 17 与 Android SDK，用户自行填入供应商端点与 Key。

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

- 多供应商接入（OpenAI/DeepSeek/Anthropic，自定义端点与模型清单）
- 主脑派发任务给多个专职子智能体并行协作并汇总
- 长期记忆：FTS 全文检索 + 向量语义检索，项目内按项目隔离
- 内置 root/Ubuntu（chroot）终端环境与在线插件市场（27 个插件、8 分类）
- MCP 支持（stdio 本地传输 + HTTP）

## 适用场景

- 在手机上运行自主 AI Agent 完成长任务与工具调用
- 通过子智能体协作模式并行处理拆解后的任务
- 在手机本地终端执行 Ubuntu 命令与开发环境部署
- 通过插件市场扩展气象/金融/知识等技能

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: **纯 Kotlin 原生 Android AI 智能体。** 一个运行在手机上的自主 AI Agent:多供应商接入、工具调用循环、子智能体并行协作、在线插件市场、技能场景自动引用、长期记忆、内置 root/Ubuntu 环境与终
> L9: - **智能体核心** — OpenAI Chat Completions / Responses API / DeepSeek / Anthropic 等多供应商,自定义端点与模型清单;工具调用循环 + 结构化输出 + Promp

## 星数曲线

```mermaid
xychart-beta
    title "kusesad-1122/XINCODE-Public 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1e84ab7aab88` · [字段定义](../../DATASET.md)*
