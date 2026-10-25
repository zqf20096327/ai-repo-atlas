# SoCloseSociety/MiloAgent

⭐ 44 · Python · MIT · 推送 2026-06-14 · [GitHub](https://github.com/SoCloseSociety/MiloAgent) · 组织维护

**自主 AI 增长代理：在 Reddit 自学习发帖推广产品**

基于 LLM 的 Reddit 自主运营代理：定时扫描、评分相关帖子，生成贴合社区语境的评论与原创帖子，并通过反馈（点赞/删除/情绪）调整子版块、关键词与语气策略。支持多账号 karma 分级配额轮换、A/B 测试与提示词自进化；LLM 栈按 Groq→Gemini→Ollama 自动故障转移以实现零成本运行。提供 FastAPI Web 面板、TUI、Telegram 控制与 Docker/VPS 部署脚本，需 Python 3.10+ 与 Reddit 账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Groq→Gemini→Ollama 自动故障转移的零成本 LLM 栈
- 多账号 karma 分级（New→Veteran）日发帖配额体系
- 自我学习引擎：表现加权、情绪分析、A/B 测试、提示词进化
- Web/TUI/Telegram 三种控制面板与 12 类定时任务

## 适用场景

- 让 AI 代理在 Reddit 上持续以评论/发帖方式推广我的产品
- 多账号多项目并行运营 Reddit 社区并跟踪效果
- 通过 Telegram 远程监控与控制运营代理

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5:  An AI agent that lives on Reddit, learns from every interaction, and grows your product organically.
> L39: He reads Reddit like a human. He understands what people are asking, what tone fits each community, and when your p
> L51: |**Cost**|API fees|**$0/month** -- runs on free-tier LLMs|

## 星数曲线

```mermaid
xychart-beta
    title "SoCloseSociety/MiloAgent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-25 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3cc0a2dda508` · [字段定义](../../DATASET.md)*
