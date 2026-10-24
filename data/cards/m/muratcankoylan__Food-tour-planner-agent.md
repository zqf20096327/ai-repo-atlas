# muratcankoylan/Food-tour-planner-agent

⭐ 97 · Python · 推送 2025-11-06 · [GitHub](https://github.com/muratcankoylan/Food-tour-planner-agent) · [官网](https://x.com/koylanai/status/1985741020743467472) · 个人维护

**AI 美食之旅规划应用：多智能体生成个性化巡游方案**

基于 LangChain DeepAgents 的美食之旅规划应用：用户在地图上添加搜索点并用自然语言描述需求（如周日早午餐、浪漫晚餐），系统由 DeepAgent API 协调 Restaurant Finder、Neighborhood Researcher、Dashboard Creator 三个子智能体，结合 Google Maps API 与 Tavily 检索生成 HTML 之旅报告。架构含 Node.js 扫描管理器与仪表盘服务器、Python DeepAgent API 三个服务；也支持无 AI 的基础扫描模式。需自备 Google Maps、Tavily 及 Anthropic/OpenAI API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个协作子智能体：餐厅搜索、街区研究、仪表盘生成
- 地图点选+自然语言 prompt 的交互式规划流程
- 支持无 AI 的基础扫描模式，按需导出以节省 API 调用
- 自动生成含照片与评论的 HTML 之旅报告

## 适用场景

- 在陌生街区规划个性化美食巡游路线
- 调研某区域的餐饮与文化特点并生成报告
- 参考多智能体任务委派与规划的实现模式

## 场景标签

 · 领域:旅游/餐饮规划

## 证据(README 行号)

> L3: AI-powered food tour planner using LangChain DeepAgents, Google Maps API, and Tavily research.
> L25: - **AI Planning**: Use natural language prompts to let AI plan personalized food tours
> L36: - **DeepAgent API** (Python): Coordinates AI agents for intelligent tour planning

## 星数曲线

```mermaid
xychart-beta
    title "muratcankoylan/Food-tour-planner-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-24 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `32191a8c6666` · [字段定义](../../DATASET.md)*
