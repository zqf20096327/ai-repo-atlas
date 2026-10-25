# anowell/are-we-learning-yet

⭐ 537 · Rust · CC-BY-4.0 · 推送 2026-10-19 · [GitHub](https://github.com/anowell/are-we-learning-yet) · [官网](http://arewelearningyet.com) · 个人维护

**Rust 机器学习生态的策展目录站点（arewelearningyet.com）**

受 Are We Web Yet? 启发的静态网站项目，编目 Rust 机器学习生态中的 crate。仓库含两部分：抓取工具读取 crates.yaml，从 crates.io 与 GitHub API 获取下载量、星标等元数据并生成排序分数，输出数据文件供站点构建；站点内容经 cobalt.rs 生成静态页面，由 GitHub Pages 发布，合并到 master 自动发布并有每周定时任务更新 crate 统计。本地运行需 cobalt >=0.20.0、Rust 工具链 1.85+，推荐 just 任务运行器，抓取时建议配置 GITHUB_TOKEN 避免 API 限流。面向关注 Rust ML 生态选型的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 crates.io 与 GitHub API 抓取 crate 元数据并生成排序分数
- cobalt.rs 静态站点生成，GitHub Pages 自动发布
- 每周 cron 定时更新下载量与星标统计
- 抓取数据缓存于 _tmp 目录以避免重复请求 API

## 适用场景

- 了解 Rust 在机器学习方向的生态覆盖情况
- 查找与比较 Rust ML 相关 crate 的活跃度指标
- 为 Rust 技术栈选型提供生态参考

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L7: Inspired by Are We Web Yet?, this project aims to catalog the the Rust ML ecosystem.
> L3: **Rust is a systems programming language, but is it a machine learning language?**

## 星数曲线

```mermaid
xychart-beta
    title "anowell/are-we-learning-yet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 536 --> 538
    line [537, 537]
```

2026-10-18 537 → 2026-10-25 537（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b43d8af782ce` · [字段定义](../../DATASET.md)*
