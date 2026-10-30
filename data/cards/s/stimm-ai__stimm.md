# stimm-ai/stimm

⭐ 52 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/stimm-ai/stimm) · [官网](https://stimm.ai/) · 组织维护

**基于 LiveKit 的低延迟语音 agent 运行时（双 agent 协作）**

构建在 livekit-agents 之上的 Optimistic VUI 运行时：VoiceAgent 负责低延迟的实时语音回合（VAD→STT→快速 LLM→TTS），Supervisor 在后台异步推理、规划与工具编排，通过 LiveKit 数据通道交换类型化协议消息。支持 autonomous/relay/hybrid 三种运行模式、对话桥接（bridge）风格、pre-TTS 分级缓冲，以及从 LiveKit 文档生成的 provider 目录与 extras 安装命令生成。以 pip 包提供，插件依赖不打入 wheel，由集成方环境安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双 agent 架构：VoiceAgent 处理实时语音，Supervisor 异步转向不阻塞首响应
- autonomous/relay/hybrid 三种运行模式
- bridge 对话风格：等待深推理时由快速 LLM 生成一句过渡语
- get_provider_catalog() 与 extras_install_command() 生成按需安装命令

## 适用场景

- 客服语音 agent 在后台检索继续时快速应答
- 电话/SIP 助手在业务逻辑完成前保持响应感
- 需要早期开口但保留监督与纠偏的实时语音副驾

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L27: Stimm is an Optimistic VUI runtime built on livekit-agents.
> L37: - Low-latency conversational loop (`VAD -> STT -> fast LLM -> TTS`).
> L137: Stimm is fundamentally built around two cooperating agents:

## 星数曲线

```mermaid
xychart-beta
    title "stimm-ai/stimm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-30 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `11cc08d95aef` · [字段定义](../../DATASET.md)*
