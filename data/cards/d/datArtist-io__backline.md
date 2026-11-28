# datArtist-io/backline

⭐ 3 · TypeScript · MIT · 推送 2026-11-18 · [GitHub](https://github.com/datArtist-io/backline) · [官网](https://backline.travel) · 组织维护

**AI 旅行代理：一句话研究、规划并电话预订行程**

面向旅行者的 AI 代理 Web 应用：用户输入一句话需求，代理按 ReAct 循环（每轮推理+最多 3 个并行工具调用，预算 10 轮/24 次调用/90 秒）依次完成需求解析、Qloo 品味图谱匹配、地点/机票/活动检索与引用、逐小时行程规划、统一结账支付，并通过 Vapi 电话向酒店餐厅完成预订。3D 地球上以 MapLibre GL + Three.js 展示行程。需配置 Qloo、LLM、Supabase 等多项 API key，钱包为演示余额、无真实资金流动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct 代理循环：推理、并行工具调用、预算控制与未完成结果回检
- Qloo 品味图谱驱动地点与活动排序，检索结果带引用来源
- Vapi+Telnyx AI 电话：呼入规划、呼出向商家预订并播报确认
- 多模型供应商容灾：主 LLM 失效时依次切换备用 LLM2/LLM3

## 适用场景

- 输入一句话生成可批准、可支付的完整旅行计划
- 通过电话或浏览器语音让 AI 代理代为规划行程
- 在 3D 地球上预览按小时展开的每日行程路线

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: Backline is an AI travel agent. Tell it where you want to go and it researches, plans, phones and books the trip, th
> L15: |3|Research|A ReAct agent decides each step: Qloo places, OpenStreetMap, live hotel rates, real Google Flights fare
> L70: - Agent engine: framework-free TypeScript with Zod validation at every boundary; any OpenAI-compatible model provid


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `10e0d88137c7` · [字段定义](../../DATASET.md)*
