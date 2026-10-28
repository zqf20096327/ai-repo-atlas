# JesseRWeigel/minecraft-agent-swarm

⭐ 34 · Python · MIT · 推送 2026-09-29 · [GitHub](https://github.com/JesseRWeigel/minecraft-agent-swarm) · 个人维护

**本地 LLM 驱动的 5 机器人 Minecraft 协同生存系统**

基于 mineflayer 与 Ollama 的多智能体项目：5 个各有分工（探索/农耕/挖掘/建造/战斗）的机器人通过共享上下文的 Team Bulletin 协调，在 Minecraft 1.21.4 服务器上自主决策生存，所有成就均由机器人在游戏内自行获得。技能系统含手写 TypeScript 技能、Voyager 式 JS 技能与 LLM 动态生成技能。默认 Ollama + gpt-oss:20b，可切换任意 OpenAI 兼容 API（OpenRouter/Groq/vLLM 等）。另含直播支持（Mission Control 面板、3D 观察器、OBS 覆层、TTS、Twitch 集成）与独立实验评估轨道。需 Node.js 20+、Python 3.10+，机器人账号须为服务器 OP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个分工机器人经共享 Team Bulletin 协调，无中央调度机器人
- 混合技能系统：手写 TS 技能 + Voyager 式 JS 技能 + LLM 动态生成
- 默认 Ollama 本地运行 gpt-oss:20b，可切换任意 OpenAI 兼容网关
- 直播配套：Mission Control 面板、每机器人 3D 观察器、OBS 覆层与 TTS

## 适用场景

- 在 Minecraft 服务器上运行自主协作的 AI 机器人队伍并观察其生存进度
- 直播展示本地 LLM 多智能体的游戏行为
- 以轨迹记录与技能生成机制实验 agent 自我改进

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: A swarm of local-LLM agents that play Minecraft together, with persistent memory, shared coordination, and a hybrid 
> L5: Each of the 5 bots specializes in a different area — exploring, farming, mining, building, or combat — and they coor
> L98: |LLM client|`src/llm/index.ts`|Ollama API with retry + JSON repair|

## 星数曲线

```mermaid
xychart-beta
    title "JesseRWeigel/minecraft-agent-swarm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-28 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d7388458858b` · [字段定义](../../DATASET.md)*
