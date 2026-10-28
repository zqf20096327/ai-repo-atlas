# Mocas-12/ai-model-rankings

⭐ 24 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Mocas-12/ai-model-rankings) · [官网](https://ai-model-rankings.streamlit.app/) · 个人维护 · 中文 README

**水墨风大模型实时战力榜：用量/基准/性价比可视化**

基于 Streamlit 与 ECharts 的大模型排行榜单页应用：浏览器并发拉取 12 个 OpenRouter 公共端点（三路重试），规范化后渲染用量 Top12、维度冠军、价格-性能散点、速度散点、30 天趋势、厂商份额等图表，每 5 分钟自动刷新。每日 CI 将 costPerRequest 快照提交入 git 仓库，实现无后端的价格降幅对比。提供静态版与 Streamlit 版两种运行方式，无需 API key，全部数据端点公开并支持 CORS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合 OpenRouter 用量、基准（Artificial Analysis）、价格与速度数据的多维排行榜
- 无后端架构：浏览器直连公共端点 + git-as-database 每日价格快照
- 支持模型对比、免费模型榜、中外对决、成本计算器等工具
- 静态版零依赖，Streamlit 版两条命令运行

## 适用场景

- 查看当前各模型的用量、价格与速度排名以辅助选型
- 对比两个候选模型的各维度数据
- 跟踪模型价格下降与每周涨幅趋势

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5:  Real-time AI model power rankings on an ink-wash dashboard (水墨风大模型实时战力榜) — usage, benchmarks, price-performance, sp
> L24: - **🏆 Usage Top 12** — real token consumption & request counts of the last 24h across 400+ live models, free varian
> L25: - **👑 Capability Summary** — three leading models for intelligence / coding / agentic tasks (Artificial Analysis).

## 星数曲线

```mermaid
xychart-beta
    title "Mocas-12/ai-model-rankings 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9365f4d78032` · [字段定义](../../DATASET.md)*
