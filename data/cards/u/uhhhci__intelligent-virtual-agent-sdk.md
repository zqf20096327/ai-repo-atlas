# uhhhci/intelligent-virtual-agent-sdk

⭐ 36 · C# · NOASSERTION · 推送 2026-08-10 · [GitHub](https://github.com/uhhhci/intelligent-virtual-agent-sdk) · [官网](https://presence-xr.eu/) · 组织维护

**Unity 虚拟人对话 agent 开发工具包，支持多模型接入与文档接地**

面向 Unity 开发者的智能虚拟人（IVA）SDK：以人-AI 交互循环为核心，提供多模态提示、LLM/VLM 结构化输出驱动的注视/动作/表情行为，兼容 CC4、Microsoft Rocketbox 与 DIDIMO 三类 3D 虚拟人。v3.0 加入基于自有 Markdown 语料的文档接地（三种策略，含逐轮 RAG）、游戏内 HUD、Setup Wizard、结构化日志与类型化异常。对话后端接入 Google AI Studio 与 Vertex AI 的 Gemini Live 实时模型，依赖含 GPT4All 与 Whisper Unity 包。需 Unity 2022.3 LTS 及以上与 URP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模态提示与 LLM/VLM 结构化输出驱动的虚拟人行为（注视/动作/表情）
- 三种文档接地策略：整文档注入、逐轮 RAG（Gemini embedding）、连接时一次性检索
- 游戏内 HUD：转写面板与麦克风/摄像头/视觉流/打断控制设置
- Setup Wizard 统一处理依赖、凭证与自检

## 适用场景

- 在 Unity 项目中搭建可对话的 3D 虚拟人
- 让虚拟人基于自有文档语料回答问题
- XR/社交虚拟现实场景中的实时语音 agent 原型与用户研究

## 场景标签

`语音 Agent` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L63: * Conversational intelligent virtual agents with human-AI interaction loop.
> L100:  Add the package to the project the package by adding this by git URL to your Unity Package Manager:

## 星数曲线

```mermaid
xychart-beta
    title "uhhhci/intelligent-virtual-agent-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-29 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d84fe18c317f` · [字段定义](../../DATASET.md)*
