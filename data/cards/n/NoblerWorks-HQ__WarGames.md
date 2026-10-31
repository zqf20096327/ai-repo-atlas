# NoblerWorks-HQ/WarGames

⭐ 17 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/NoblerWorks-HQ/WarGames) · [官网](https://wargames.noblerworks.com/) · 组织维护

**LLM 驱动的地缘政治战略棋盘模拟，三国由 AI 对弈**

基于 TypeScript/Vite/Leaflet/Express 的回合制地缘战略模拟：NATO、俄罗斯、中国三方在交互地图上争夺领土与资源，每个阵营由一个 LLM（Gemini/OpenAI/Anthropic 任选）每回合作出最多 3 条指令，另有一名叙述者 AI 生成新闻式战报。支持按阵营混用不同模型、种子可复现的骰子、存档/回放/分享、模型间锦标赛与 Elo 排行榜，并统计各家 token 花费。每局消耗所配 provider 的 API key；可设 OPENAI_BASE_URL 接入 Ollama/vLLM 等兼容端点。npm 启动，另提供 Docker 只读展示模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三方阵营各由独立 LLM 指挥，可按席位混用不同 provider/model
- npm run tournament 跑多模型锦标赛：轮换席位、共享种子、预算控制、输出 results.md/json
- Elo 排行榜汇总所有已完成对局的 provider/model 胜率与成本
- 存档/回放/单文件 HTML 战报分享，READ_ONLY=1 可零花费公开展示

## 适用场景

- 观看不同 LLM 在同一战略棋盘上的对弈差异
- 用锦标赛与排行榜对比各家模型的决策质量与成本
- 向他人分享完整对局回放或静态战报页

## 场景标签

`多智能体` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L16: AI-powered geopolitical strategy simulation. Three great powers - NATO, Russia, and China - compete for territory, 
> L73: ## AI Providers
> L163: ```bash

## 星数曲线

```mermaid
xychart-beta
    title "NoblerWorks-HQ/WarGames 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b7d921945dcb` · [字段定义](../../DATASET.md)*
