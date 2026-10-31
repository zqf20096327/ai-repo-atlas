# eason69113-source/AI_Trip_Planner

⭐ 24 · Python · MIT · 推送 2025-12-30 · [GitHub](https://github.com/eason69113-source/AI_Trip_Planner) · 个人维护 · 中文 README

**多智能体旅行规划助手：输入目的地生成行程计划**

基于 LangChain 1.1 + FastAPI + 高德地图 MCP Server 的行程规划应用：景点搜索、天气查询、酒店推荐、行程规划四个 Agent 并行工作，调用高德地图官方 API 获取 POI 与天气数据，输入目的地和日期后生成含每日景点、三餐、酒店与预算的旅行计划，通过 SSE 流式输出到前端页面。LLM 使用 DeepSeek API，兼容通义千问。自定位为入门级 agent 教学项目，需自行申请高德与 LLM 的 API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 景点/天气/酒店/行程四 Agent 并行的多智能体架构
- 通过高德地图 MCP Server 调用官方 POI 与天气 API
- SSE 流式输出，前端实时渲染 Markdown
- 支持自然语言自定义偏好（如「亲子友好」「避开人流」）

## 适用场景

- 输入目的地和日期生成含预算的旅行计划
- 学习 agent 与 MCP 的原理和实现
- 出行前查看目的地 7 日天气预报与穿衣建议

## 场景标签

`多智能体` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L12: |✅ 多智能体|景点搜索 / 天气查询 / 酒店推荐 / 行程规划 四 Agent 并行，互不串台|
> L29: - **LLM**：DeepSeek（通义千问/DeepSeek API 双兼容）

## 星数曲线

```mermaid
xychart-beta
    title "eason69113-source/AI_Trip_Planner 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28", "2026-10-31"]
    y-axis "stars" 21 --> 25
    line [22, 23, 24, 24]
```

2026-10-18 22 → 2026-10-31 24（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `c81d71be02c3` · [字段定义](../../DATASET.md)*
