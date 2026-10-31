# mirzayasirabdullahbaig07/AgentPay-AI

⭐ 46 · Python · 推送 2026-02-09 · [GitHub](https://github.com/mirzayasirabdullahbaig07/AgentPay-AI) · [官网](https://agentpay07.streamlit.app/) · 个人维护

**按请求计费的 GenAI agent 演示平台：模拟 USDC 代币计费**

基于 Streamlit 与 Google Gemini/PaLM 的概念验证项目：用户提交 prompt 后系统估算 token 用量成本，从会话内模拟 USDC 钱包扣费，余额充足才执行 AI 任务。定位为 AIaaS 计费逻辑的演示，支持 API key 认证、可调温度与最大 token 数，自述可作为 GenAI/Web3/SaaS 求职的作品集项目。计费为模拟，不含真实链上支付。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- token 用量成本估算与会话内 USDC 钱包扣费
- 余额不足时拒绝执行 AI 任务
- Google Gemini / PaLM 文本生成，温度与最大 token 可调
- API key 认证与环境变量配置（python-dotenv）

## 适用场景

- 演示按请求/按 token 计费的 AIaaS 计费流程
- 搭建 AI agent 市场或 Crypto+AI 集成的原型基础
- 作为 GenAI/Web3/SaaS 方向的作品集项目展示

## 场景标签

 · 领域:AI 应用/计费演示

## 证据(README 行号)

> L15: AgentPay-AI is a **GenAI agent interface** built using Streamlit and Google Gemini models that:
> L69: - 🧠 Google Gemini / PaLM text generation

## 星数曲线

```mermaid
xychart-beta
    title "mirzayasirabdullahbaig07/AgentPay-AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-31 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `68248de474b8` · [字段定义](../../DATASET.md)*
