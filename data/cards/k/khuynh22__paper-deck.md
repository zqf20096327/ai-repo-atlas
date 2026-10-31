# khuynh22/paper-deck

⭐ 15 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/khuynh22/paper-deck) · [官网](https://www.ppdeck.com/) · 个人维护

**聚合 arXiv/HF/Semantic Scholar 论文的多用户阅读应用**

多用户响应式 Web 应用，从 arXiv、Hugging Face Daily Papers、Semantic Scholar 等来源聚合 AI/ML 论文，按 arXiv ID 去重合并为统一语料，提供 Latest/Trending/Famous 三种视图。用户可收藏论文、在应用内阅读（arXiv HTML 与 pdf.js 回退），并支持跨设备的滚动位置续读与"读到此处"标记同步。本地开发需 Node 20+、pnpm 与 Docker（运行本地 Supabase）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- arXiv/HF/Semantic Scholar 多源聚合并按 arXiv ID 去重
- Latest/Trending/Famous 三种视图
- 应用内 HTML/PDF 阅读器，支持块级/页级续读与标记
- 收藏与阅读进度按用户账户跨设备同步

## 适用场景

- 在一个界面追踪最新和热门 AI 论文
- 收藏论文稍后阅读并跨设备同步进度
- 按引用量浏览经典论文

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: Your AI/ML research, on one deck. A responsive, multi-user web app that aggregates
> L18: - **One deduplicated corpus, three views** — Latest (arXiv), Trending (Hugging Face
> L20: - **Sources** — arXiv, Hugging Face Daily Papers, Semantic Scholar, Google Scholar

## 星数曲线

```mermaid
xychart-beta
    title "khuynh22/paper-deck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `63d2e7ddde57` · [字段定义](../../DATASET.md)*
