# Joho6666/voyage

⭐ 14 · TypeScript · MIT · 推送 2026-10-05 · [GitHub](https://github.com/Joho6666/voyage) · 个人维护 · 中文 README

**开源 AI 原生旅行操作系统：对话规划真实行程并伴随旅途执行**

基于 Next.js 15 / React 19 / Supabase 的本地优先旅行规划应用：用户用自然语言描述需求，Agent 追问补全后生成带高德坐标、路网路线与天气感知的结构化行程；每个修改指令编译为 Zod 校验的 TravelAction 提案，在 Diff 审阅确认后应用（proposalToken 防重放）。支持导入小红书/抖音攻略并逐名核验地点、Today 模式现场执行、Cmd+K 动态调整与撤销。Provider 按 0-3 级配置，无任何 Key 可用 Demo 模式，缺失时降级并标注 REAL/ESTIMATED 状态。面向旅行者，也提供 CLI 与 MCP server 驱动方式。

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

- 自然语言指令编译为 TravelAction 提案，Diff 确认后应用（一次性 token，10 分钟有效）
- 四级 Provider 体系：Demo 模式零配置，高德/LLM/社交/报价逐级解锁，降级如实标注
- 小红书/抖音/微信攻略导入，地点由高德逐名核验后进入行程
- 同一 Runtime 以 CLI、MCP server（Claude Desktop/Cursor）和 Web Agent 三种方式驱动

## 适用场景

- 用一句话让 AI 规划带真实路线与天气的完整行程
- 旅途中用自然语言临时改行程（下雨/太累/省钱）并确认 Diff
- 把小红书/抖音攻略链接转成带地图标注的可执行行程

## 场景标签

 · 领域:旅行/消费应用

## 证据(README 行号)

> L3: # Voyage · Open-source AI-native Travel OS
> L38: Voyage 在几秒钟内生成一个**真实的、结构化的、带高德坐标与路网、受天气感知、可持久化、随时可修改的完整旅行项目**。
> L46: 每一个自然语言指令，都会被编译成经过 Zod 校验的结构化 `TravelAction`，生成量化对比报告（`TripChangeSet`）呈现在 Diff 审阅弹窗中，**待用户确认后才应用**（一次性 proposalToke

## 星数曲线

```mermaid
xychart-beta
    title "Joho6666/voyage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8ec8335dcdd3` · [字段定义](../../DATASET.md)*
