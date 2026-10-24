# pengpengyi92/dsh-quant

⭐ 54 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/pengpengyi92/dsh-quant) · 个人维护

**面向 AI agent 的量化研究插件：59 个量化工具覆盖数据到报告全链路**

dsh-quant 是运行于 dsh 插件框架 Node 运行时内的量化研究工具包，以插件形式向 agent 提供 59 个 quant_* 工具，覆盖数据、alpha、ML、风险、执行、生态 6 个域，可经 quant_research_pipeline 一次调用完成 PDAT→PET 研究链（行情获取→质量检查→因子评估→回测→指标→风险→纸面/基金模拟→报告）。实现为 21 个 TypeScript 文件、零运行时依赖；Python 类数据源通过知识库指引 agent 自行 spawn。内部 alpha 与研究模型不开源，开源的是范式与框架。附带 UI 工作台与零依赖 CLI。

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

- 59 个 quant_* 工具覆盖 6 个域，298 个测试，零运行时依赖
- 工具 schema 注入系统提示，等长 null 对齐，全部并发安全
- quant_research_pipeline 一次调用完成数据→回测→风险→报告全链
- 提供 K 线/净值曲线 UI 工作台与纯 Node 终端 CLI

## 适用场景

- 让编程 agent 通过工具调用完成端到端量化研究流水线
- 在 dsh 框架中按插件范式组装自己的数据源、因子与交易系统
- 计算期权希腊字母、债券久期、VaR 回测等量化指标并生成 Markdown 报告

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L17: > **AI-native & DSH-native quant toolkit for every quant aspect** — 59 tools · 6 domains
> L47: dsh-quant's primary consumer is the **agent (the model), not the human** — a
> L66: - dsh-quant is a **dsh plugin** running inside the harness's Node runtime: same

## 星数曲线

```mermaid
xychart-beta
    title "pengpengyi92/dsh-quant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-24 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `2bb3924de031` · [字段定义](../../DATASET.md)*
