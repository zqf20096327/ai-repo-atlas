# Nikhil-creat/minecraft-ai-ecosystem

⭐ 3 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/Nikhil-creat/minecraft-ai-ecosystem) · [官网](https://nikhil-creat.github.io/minecraft-ai-ecosystem/) · 个人维护

**给 Minecraft 玩家的多 Agent 游戏内 AI 助手**

由 Fabric mod 与 Docker 化 FastAPI 后端组成的 Minecraft AI 生态系统：mod 将玩家遥测与屏幕帧流式传给后端，LangGraph 流水线按 Planner→Inventory→Executor→Critic 顺序运行在 Groq 模型上，把自然语言转为经过校验的世界操作；知识由 ChromaDB RAG 与 PyTorch CNN（MobileNetV3 方块分类）支撑，自主无人机负责建造/挖掘并支持 /ai undo 回滚。需要 Docker、JDK 17+ 与 Groq API key；仅支持单人或局域网主机场景。

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

- Planner/Inventory/Executor/Critic 四阶段 LangGraph 流水线，带自纠错循环与模型回退
- ChromaDB RAG 知识库，可摄入 .txt/.md/.json wiki 文件
- MobileNetV3 方块分类视觉、HUD 边界框与威胁雷达
- 支持 /ai undo 回滚的自主建造无人机

## 适用场景

- 在 Minecraft 单人世界中用自然语言指挥 AI 建造或挖掘
- 用 /rag 命令查询自定义知识库（如矿物分布）
- 通过 HUD 与威胁雷达查看 AI 识别的视野信息

## 场景标签

`多智能体` `AI 助手` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L15: NEXUS puts an autonomous AI crew inside Minecraft. A Fabric mod streams player telemetry and screen frames to a doc
> L16: There a LangGraph pipeline — **Planner → Inventory → Executor → Critic** — running on Groq turns natural language i
> L17: validated world actions, grounded by a ChromaDB knowledge base and a PyTorch CNN. The Autonomous Drone then builds 

## 星数曲线

```mermaid
xychart-beta
    title "Nikhil-creat/minecraft-ai-ecosystem 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-25 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `99fbf135ce7a` · [字段定义](../../DATASET.md)*
