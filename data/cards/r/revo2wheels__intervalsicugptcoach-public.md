# revo2wheels/intervalsicugptcoach-public

⭐ 51 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/revo2wheels/intervalsicugptcoach-public) · [官网](https://www.montis.icu) · 个人维护

**基于 Intervals.icu 数据的确定性耐力训练教练引擎**

面向耐力运动爱好者的训练教练引擎：从 Intervals.icu 读取运动员数据，经 Tier-0 至 Tier-3 的确定性流水线（数据规范化、完整性审计、性能智能、纵向适应进展、自适应决策引擎）产出受治理的机器可读教练状态，LLM 位于引擎下游，仅负责将结果转为对话。提供本地 CLI（--direct 直连 Intervals.icu API）、Railway 后端入口及 Montis App、ChatGPT Actions、MCP 客户端等接口。MIT 许可仅覆盖引擎与文档，托管服务的私有基础设施不在此仓库内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性引擎流水线：Tier-0 数据规范化到 Tier-3 自适应决策与治理
- LLM 位于引擎下游，接收受治理的语义输出而非独立生成决策
- 本地 CLI --direct 模式使用自有 API key 直连 Intervals.icu，不依赖 Montis 服务器
- 同一引擎输出通过 Montis App、ChatGPT Actions、MCP、REST 等多接口暴露

## 适用场景

- 基于 Intervals.icu 训练数据获得有据可查的教练决策与状态
- 在本地运行完整教练引擎，数据不经第三方服务器
- 通过 ChatGPT 或 Claude 等 MCP 客户端以对话方式查看训练分析结果

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L13: Montis controls the coaching intelligence. AI explains and discusses the result — it does not independently invent 
> L15: The language model is downstream of the engine. It receives governed semantic output and turns that result into use

## 星数曲线

```mermaid
xychart-beta
    title "revo2wheels/intervalsicugptcoach-public 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-28 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `94c258116767` · [字段定义](../../DATASET.md)*
