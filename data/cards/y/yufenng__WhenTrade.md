# yufenng/WhenTrade

⭐ 25 · Python · MIT · 推送 2026-02-14 · [GitHub](https://github.com/yufenng/WhenTrade) · 组织维护 · 中文 README

**多 AI agent 协作的加密货币投资分析平台**

基于 FastAPI + Vue.js 3 的开源投资分析平台，受 TradingAgents 启发。多个专职 AI agent 协作完成市场数据分析、Bull vs Bear 投资策略辩论、多视角风险评估并生成投资建议；通过 LangChain + LangGraph 编排，WebSocket 实时推送结果。支持 OpenAI、Google Gemini、DeepSeek、Kimi 等多家 LLM 接入，需配置 PostgreSQL 与 Redis，API key 按需可选。声明仅供教育与研究用途，不构成实际交易建议。

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

- 多 agent 协作：分析、Bull/Bear 辩论、风险评估、生成投资建议
- 支持 OpenAI / Google Gemini / DeepSeek / Kimi 等多家 LLM
- LangGraph 状态图编排分析工作流，WebSocket 实时数据流
- FastAPI 后端 + Vue.js 3 前端，测试覆盖率声明 80%+

## 适用场景

- 跑多 agent 辩论获取加密货币投资分析观点
- 在本地部署可自定义 LLM 提供商的市场研究平台
- 学习多 agent 金融分析工作流的实现

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L24: When.Trade is an **open-source AI-powered investment analysis platform** that revolutionizes market analysis throug
> L29: - 💭 **Debate** investment strategies through Bull vs Bear perspectives
> L31: - 📊 **Generate** actionable investment recommendations

## 星数曲线

```mermaid
xychart-beta
    title "yufenng/WhenTrade 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2a20a65a9a4f` · [字段定义](../../DATASET.md)*
