# tony-stark-eth/news-aggregator

⭐ 18 · PHP · MIT · 推送 2026-07-18 · [GitHub](https://github.com/tony-stark-eth/news-aggregator) · 个人维护

**自托管的 AI 增强 RSS/Atom 新闻聚合器**

基于 Symfony 8 + FrankenPHP + PostgreSQL + DaisyUI 构建的自托管新闻聚合应用：聚合可配置的 RSS/Atom 源，通过 OpenRouter 免费模型（symfony/ai-bundle，ModelFailoverPlatform 失败转移链）对文章做 AI 分类、摘要、关键词与情感抽取、多语言翻译，无 API key 时回退到基于规则的处理。另提供智能告警（关键词/AI/混合三型）、周期性 AI 编辑摘要、全文检索（SEAL+Loupe）、OPML 导入导出、Mercure SSE 实时更新。部署方式为 Docker 拉取 GHCR 镜像或从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 富集管线：分类、摘要、关键词抽取、情感评分、翻译，失败回退规则处理
- OpenRouter 免费模型路由 + 失败转移链（minimax/glm/gpt-oss/qwen/nemotron）
- 智能告警（keyword/ai/both 三种类型）与周期性 AI 编辑摘要
- 全文检索、OPML 导入导出、Mercure SSE 实时更新

## 适用场景

- 自建家庭服务器上的新闻聚合与阅读平台
- 按关键词或 AI 规则订阅特定主题新闻并接收通知
- 多语言阅读 RSS 内容并按情感滑杆筛选文章

## 场景标签

 · 领域:新闻聚合/自托管应用

## 证据(README 行号)

> L7: Self-hosted, AI-enhanced RSS/Atom news aggregator built with Symfony 8 + FrankenPHP.
> L26: - **AI-powered categorization & summarization** via OpenRouter free models (with rule-based fallback)
> L203: - **No API key required** — the system falls back to rule-based categorization/summarization.

## 星数曲线

```mermaid
xychart-beta
    title "tony-stark-eth/news-aggregator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `53f0f25c1df0` · [字段定义](../../DATASET.md)*
