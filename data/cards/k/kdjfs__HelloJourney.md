# kdjfs/HelloJourney

⭐ 26 · Java · GPL-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/kdjfs/HelloJourney) · 个人维护 · 中文 README

**面向旅行者的 AI 行程规划工作台：生成可验证可编辑的行程**

HelloJourney 是一个全栈 AI 旅行规划平台，将目的地、预算和偏好转化为可执行行程。后端为 Spring Boot 服务，前端提供 React Web 端与 UniApp 微信小程序端；通过原生 Tool Calling 调用地图与天气能力，用结构化输出和 Review Agent 约束行程质量，行程可编辑、可撤销、可局部重新规划。支持 DeepSeek 及 OpenAI 兼容的多 LLM 提供商，集成腾讯地图/高德/Google 地图，异步生成经 WebSocket 推送进度。运行需 JDK 17、Maven、Node.js 20 并配置地图凭据等 API 密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agentic 生成管线：原生 tool calling、结构化 JSON 输出、Review Agent 拦截无效行程
- 集成腾讯地图/高德/Google 地图、天气、POI 与路径规划，带自动提供商回退
- 可编辑行程工作台：撤销/重做、跨天移动、AI 局部重规划变更集可应用或拒绝
- ECharts 知识图谱视图与 3D 地图行程可视化，zh/en/ja 三语 i18n

## 适用场景

- 按目的地和预算生成带地图与天气数据的旅行行程
- 对 AI 生成的行程手动编辑或要求局部重规划
- 在 Web 端和微信小程序端查看带实时进度更新的行程生成

## 场景标签

 · 领域:旅行/生活服务

## 证据(README 行号)

> L7: **HelloJourney** 是一个可验证、可编辑、可局部重新规划、可撤销的 AI Travel Workspace。系统通过原生 Tool Calling 调用地图与天气能力，用结构化输出和 Review Agent 约束行程
> L13: - **AI itinerary planning** with multi-provider LLM support and context-aware follow-up chat.
> L14: - **Agentic pipeline**: native tool calling, structured JSON output, and a Review Agent that blocks invalid plans.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `1ee288136c18` · [字段定义](../../DATASET.md)*
