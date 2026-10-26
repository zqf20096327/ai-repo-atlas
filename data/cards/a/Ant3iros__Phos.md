# Ant3iros/Phos

⭐ 34 · Python · MIT · 推送 2026-07-05 · [GitHub](https://github.com/Ant3iros/Phos) · 个人维护

**AI 驱动的地缘政治叙事模拟游戏：扮演国家进行外交与决策**

受 Pax Historia 启发的开源文字模拟游戏：玩家扮演一个国家，在交互式世界地图上查看外交关系与稳定度，通过自然语言与 AI agent 扮演的他国实时谈判，向 AI 政治顾问咨询，提交自由行动由 AI 模拟后果，每回合（1 个月）由 AI 生成世界事件。内置 2016 年剧本（147 国，含 GDP/军事/意识形态等数据），支持自建剧本。后端 Python + FastAPI，提供 Docker 一键启动与 REST API。默认兼容 socle.ai，也可配 Ollama/text-generation-webui/DeepSeek 等任意 OpenAI 兼容端点，运行时在应用内配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言实时 AI 外交（SSE 流式）与 AI 政治顾问
- 内置 2016 剧本：147 国真实数据（GDP/军事/意识形态/关系）
- 自由行动提交，AI 模拟后果并每回合生成世界事件
- 兼容任意 OpenAI 兼容端点（socle.ai/Ollama/TextGen/DeepSeek），应用内配置

## 适用场景

- 扮演国家进行 AI 驱动的地缘政治模拟与外交谈判
- 自建架空世界观剧本（魔戒/星战/战锤 40k 等）游玩
- 本地部署 Ollama 后离线运行整个游戏

## 场景标签

 · 领域:游戏/AI 模拟

## 证据(README 行号)

> L3: OpenSource game inspired by the game Pax Historia
> L5: AI-powered geopolitical narrative simulation. Play as a nation, make political decisions, engage in real-time diplom

## 星数曲线

```mermaid
xychart-beta
    title "Ant3iros/Phos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c7a482930a42` · [字段定义](../../DATASET.md)*
