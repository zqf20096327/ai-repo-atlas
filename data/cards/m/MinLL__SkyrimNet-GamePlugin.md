# MinLL/SkyrimNet-GamePlugin

⭐ 364 · Papyrus · NOASSERTION · 推送 2026-10-31 · [GitHub](https://github.com/MinLL/SkyrimNet-GamePlugin) · [官网](https://fateless.ai) · 组织维护

**为 Skyrim 全体 NPC 提供 AI 对话、记忆与实时语音的游戏模组**

以单个 Skyrim 模组形式运行（基于 SKSE 插件）：玩家通过麦克风或打字与任意 NPC 对话，NPC 以自有音色实时语音回应。每个 NPC 维护按语义召回且随时间衰减的私有记忆，能感知周围事件并执行跟随、递物、战斗等动作；支持本地与云端 TTS、本地语音识别、玩家自定义 LLM 后端。LLM 可选 Fateless 订阅（$10/月起）、OpenAI 兼容云服务，或经 LM Studio/Ollama/KoboldCpp/llama.cpp 本地运行。需安装多项前置模组与 VC++ 运行库，闭源许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全部 NPC 具备上下文对话、实时流式语音与手写人物小传
- 按语义召回的 NPC 私有记忆，随时间衰减，支持 NPC 日记
- 本地/云端 TTS 含语音克隆；语音识别在用户本机运行
- 提供 Papyrus/C++ API、YAML 触发器与 MCP server 供模组开发者扩展

## 适用场景

- 在 Skyrim 中与任意 NPC 进行带记忆的实时语音对话
- 让 NPC 感知环境、互相交谈并自主执行动作
- 模组作者通过 API 扩展 NPC 行为与触发器
- 用本地 LLM 私有化运行 AI NPC 对话

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L18: SkyrimNet turns every character in Skyrim into someone you can actually talk to. Speak into your microphone or type
> L20: NPCs **remember**. Each one keeps their own memories of what you did and said, and of what they saw happen around t
> L37: - **Voices.** Local and cloud text-to-speech engines, with voice cloning, plus voice effects for werewolves, draugr


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1c2c897d9ef4` · [字段定义](../../DATASET.md)*
