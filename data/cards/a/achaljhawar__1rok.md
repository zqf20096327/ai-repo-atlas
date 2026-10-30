# achaljhawar/1rok

⭐ 50 · TypeScript · MIT · 推送 2026-05-13 · [GitHub](https://github.com/achaljhawar/1rok) · [官网](https://investingbench.vercel.app) · 个人维护

**多 LLM 投资组合构建代理运行框架，对接 Alpaca 模拟交易**

独立的多 LLM 交易测试框架：将 OpenAI、Anthropic、Gemini、xAI、DeepSeek、GLM、OpenRouter 的模型接入同一工具调用循环，运行四阶段、十个专业代理（宏观、筛选、六类分析、编排、构建）的周度流水线，生成组合构建 JSON 工件；execute 命令经 Alpaca 下单（默认 paper，--live 才触达实盘）。工具面覆盖行情、个股、研究、技术指标、期权、财报、组合与 Tavily 搜索八组，Zod schema 统一转换为各 provider 格式。面向具备 Bun ≥1.1.0 与各 API key 的开发者，附在线 leaderboard 对比各模型表现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七个 LLM provider 统一在单一工具调用循环后
- run/execute 分离：run 不触经纪商，execute 默认 paper 下单
- 四阶段十代理流水线，组合评分含基本面/估值/风险等加权
- 八组 Zod 类型化工具内联注册（Alpaca/FRED/Tavily/Yahoo）

## 适用场景

- 我想在同一金融工具面上横向对比多个 LLM 的组合构建能力
- 我想跑自动化投研流水线并在 Alpaca 模拟盘验证
- 我想以编程方式复用其工具注册表与 provider 适配器

## 场景标签

`多智能体` `金融量化` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L5: `1rok` is a standalone harness for running portfolio-construction agents across OpenAI, Anthropic, Gemini, xAI, Deep
> L16: - **Seven LLM providers** — OpenAI (GPT-5.2/5.4/5.5), Anthropic (Claude Opus 4.7 / Sonnet 4.6 / Haiku 4.5), Gemini,
> L18: - **Two-stage pipeline** — `run` emits a portfolio-construction JSON artifact; `execute` reads it and places orders

## 星数曲线

```mermaid
xychart-beta
    title "achaljhawar/1rok 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-30 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7712eab03f38` · [字段定义](../../DATASET.md)*
