# emergencescience/histrategy

⭐ 34 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/emergencescience/histrategy) · [官网](https://emergence.science/play/histrategy) · 组织维护 · 中文 README

**LLM 驱动的历史叙事策略游戏（三国/罗马/南明）**

开源历史策略游戏，提供三个剧本：207 年三国、公元前 44 年罗马三头同盟、1645 年南明，玩家指挥势力进行回合制博弈。核心机制为 V3 混合引擎：确定性数值基线叠加 LLM 非线性叙事层与护栏，AI NPC 基于性格与局势自主决策；已下线的 V1 引擎因 LLM 幻觉数值被移除。提供 pip 安装的 SDK（Room 编程接口）、Docker Compose 单容器自建（默认 SQLite）、FastAPI 服务与 Web UI，并支持 OpenAI 兼容端点（默认 DeepSeek key）。可为 OpenClaw、Hermes 等 AI agent 安装技能以主持多人对局。原云端服务已停止，需自建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个历史剧本：三国、罗马三头同盟、南明（山河鼎革）
- V3 混合引擎：确定性基线 + LLM 非线性层，含护栏
- AI NPC 基于性格与局势自主决策
- 文件化游戏状态，agent 上下文重置后可恢复（Room.load）

## 适用场景

- 自建 LLM 策略游戏服务，与好友对局历史剧本
- 通过编程接口（SDK）在自有应用中运行对局
- 让 OpenClaw/Hermes 等 agent 在聊天中主持多人策略游戏

## 场景标签

 · 领域:游戏/LLM 应用

## 证据(README 行号)

> L3: **An open-source, AI-powered historical strategy game.**
> L54: - **引擎**：V3（生产引擎：确定性基线 + LLM 非线性层）—— **无需任何引擎环境变量**。
> L99: - **AI NPCs**: Opposing warlords make their own decisions based on personality and situation.

## 星数曲线

```mermaid
xychart-beta
    title "emergencescience/histrategy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-26 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `4074cf6905aa` · [字段定义](../../DATASET.md)*
