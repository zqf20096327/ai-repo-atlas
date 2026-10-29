# bnlbnf/relaywatch

⭐ 42 · Python · MIT · 推送 2026-08-10 · [GitHub](https://github.com/bnlbnf/relaywatch) · [官网](http://relaywatch.online) · 个人维护 · 中文 README

**AI API 中转站聚合监控与模型比价平台**

面向 NewAPI/Sub2API 中转站生态的自部署 Web 平台：采集并归一化公开中转站信息，提供全网站点聚合、模型维度比价（价格/成功率/延迟/TPS）、公告流、官方 API 状态汇总、AI 资讯聚合、用自己的 Key 做模型检测，以及 OpenAI 兼容接口的在线对话代理。后端为 Python/FastAPI，前端 React/Vite，支持本地 JSON 与 PostgreSQL 分代存储两种模式，通过 Uvicorn/systemd/Docker 或反向代理部署。仅做信息聚合与比价，不参与交易。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按模型维度对比多站点价格、成功率、延迟与 TPS
- 使用自己的 API Key 做协议检测、质量检测与实时调用验证
- 本地 JSON 与 PostgreSQL 分代导入、原子切换双存储模式
- 汇总 OpenAI/Claude/Gemini/DeepSeek 官方状态页与站点公告流

## 适用场景

- 对比各中转站的模型价格与稳定性以辅助选站
- 追踪中转站公告、价格调整与上游 API 状态波动
- 用自己的 Key 验证站点模型可用性与质量

## 场景标签

 · 领域:AI API 基础设施/监控

## 证据(README 行号)

> L25: RelayWatch 是一个面向 AI API 中转站生态的聚合监控平台，用来把分散的中转站信息整理成可搜索、可比较、可追踪的目录。它支持全网站点发现、NewAPI/Sub2API 站点采集、模型价格对比、公告流、官方 API 状
> L36: |NewAPI / Sub2API 生态适配|面向常见中转站接口结构做采集、归一化、去重、探活和比价展示。|

## 星数曲线

```mermaid
xychart-beta
    title "bnlbnf/relaywatch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-29 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `feb43084b5ff` · [字段定义](../../DATASET.md)*
