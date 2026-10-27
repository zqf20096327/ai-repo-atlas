# pajeronda/xai_conversation

⭐ 32 · Python · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/pajeronda/xai_conversation) · 个人维护

**Home Assistant 的 xAI Grok 对话代理集成**

面向 Home Assistant 用户自定义组件，将 xAI Grok 接入对话助手：支持三种交互模式（Intelligent Pipeline 意图管线、Tool Control 工具调用、Chat Only 纯对话），三种运行模式（服务端记忆、零数据保留 ZDR 本地加密、本地聊天记录）。提供 YAML 扩展工具、Live Search 与 X 搜索、无状态 ASK/照片分析服务、成本与 token 传感器等维护功能。通过 HACS 安装，需 xAI API key，使用官方 xAI Python SDK。GPL v3 许可，非 xAI 官方集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种交互模式：意图管线/工具调用/纯对话，可自动回退
- 零数据保留（ZDR）模式本地加密存储会话状态
- ASK 与 photo_analysis 无状态服务，可按次覆盖模型/温度/搜索设置
- 模型成本、token 计数、缓存效率实时传感器与内存清理服务

## 适用场景

- 在 Home Assistant 中用 Grok 语音或文字控制智能家居
- 处理传感器数据、照片分析等一次性 AI 任务
- 关注隐私时用 ZDR 模式本地保存会话上下文

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L13: A complete conversation agent integration for Home Assistant that offers multiple ways to manage your conversation 
> L52: Grok acts as an advanced **ASR/NLU orchestrator**, providing three distinct ways to interact with your Home Assista

## 星数曲线

```mermaid
xychart-beta
    title "pajeronda/xai_conversation 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-27 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0d1535df4e20` · [字段定义](../../DATASET.md)*
