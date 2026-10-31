# LC-di-yan/Lincan-Travel-Assistant-Agent

⭐ 15 · Python · 推送 2026-10-21 · [GitHub](https://github.com/LC-di-yan/Lincan-Travel-Assistant-Agent) · [官网](https://lc-di-yan.github.io/Lincan-Travel-Assistant-Agent/) · 个人维护 · 中文 README

**中文差旅助手：一句话生成可执行行程的多智能体 Web 应用**

基于 AgentScope 1.0.16 + FastAPI + React 19 的差旅规划系统，面向终端用户：意图识别（规则快路由 + LLM 兜底）→ 按优先级并行调度 10 个技能智能体（行程/酒店 POI/12306 车票/天气/记账/汇率/翻译/知识库问答），配两层记忆（10 轮短期 + JSON/PG 长期）、Milvus Lite RAG、OpenAI 兼容多通道故障转移与整链超时预算。运行需 Python 3.12 + Node 18+，必填 OpenAI 兼容 key；PostgreSQL/Redis 可选。已知限制：TTS 需额外 MiMo key、同会话串行、前端需自行构建。

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

- 10 个技能智能体按优先级并行调度，SSE 流式回显
- 模型多通道路由与故障转移（401/403/429/5xx 自动切换 + 总超时预算 + 熔断）
- 两层记忆：10 轮短期会话 + 长期 JSON/PG 偏好与历史
- 8 份差旅制度文档的 RAG 问答，回答标注依据

## 适用场景

- 一句话生成多日可执行行程，含车次与每日安排
- 查 12306 车票、高德酒店、天气并完成记账与汇率换算
- 记住偏好（酒店品牌/座位/住址），下次规划自动应用
- 按差旅制度文档做合规问答

## 场景标签

`多智能体` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L5: 基于 **AgentScope 多智能体框架 + FastAPI + React 19** 的差旅规划系统：意图识别 → 优先级并行调度 → 10 个技能智能体 → 两层记忆 → SSE 流式回显。
> L3: > 一句中文需求 → 一份能直接照着走的行程，顺带把酒店、车票、天气、记账、汇率、翻译一起办了。

## 星数曲线

```mermaid
xychart-beta
    title "LC-di-yan/Lincan-Travel-Assistant-Agent 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-22 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6225070f39ed` · [字段定义](../../DATASET.md)*
