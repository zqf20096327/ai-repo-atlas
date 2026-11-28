# pingfanfan/deepseek-search-bench

⭐ 5 · HTML · MIT · 推送 2026-10-18 · [GitHub](https://github.com/pingfanfan/deepseek-search-bench) · [官网](https://pingfanfan.github.io/deepseek-search-bench/) · 个人维护 · 中文 README

**测试 DeepSeek Search/Fetch API 信源质量的基准工具**

围绕 DeepSeek Search/Fetch API 构建的信源质量测试台：提供 63 道易污染问题、86 道分级题与封闭平台探测等测试集，调用 API 后人工标注域名类别并与返回的 authority 字段对照，输出 SEO/GEO 污染、IP 本地化、封闭平台边界等维度的分析结果。使用方式有三：GitHub Pages 在线页面（浏览器填 key 直连）、本地 server.py、命令行 bench.py/analyze.py（仅依赖 Python 3.9+ 标准库）。测试日期为 2026-10-18，单一标注者、每条件单次运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个 JSON 测试集：易污染题、分级题、封闭平台边界、国内外抓取对比
- 支持 --engine tavily / --engine brave 用同一批题跑对照引擎
- 在线测试台无需安装，key 仅存浏览器，记录可导出 JSON 分享
- 域名→信源类别标注表 domains.json 接受 PR 补充

## 适用场景

- 评估 DeepSeek 搜索 API 对 SEO 垃圾站与 GEO 软文的过滤表现
- 做 RAG 前了解搜索结果排序与权威度字段的实际行为
- 探测搜索 API 对公众号、小红书等封闭平台的覆盖边界
- 用相同问题集横向跑 tavily/brave 做对照

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: 测一测 DeepSeek Search / Fetch API 的信源质量：它挡得住 SEO 垃圾站吗？挡得住 GEO 软文吗？
> L15: 我用 63 个容易被污染的问题测试，中英文各半，每题取前 10 条，共 630 条结果。结果里出现的每个域名都人工归了类，再和 API 返回的 `authority`（权威度，0–4）对照。
> L94: 63 题约 63 次请求，按 $0.75 / 千次计算不到 5 美分。有对照组的 key 时，可以用同一批题跑别家：`--engine tavily` 或 `--engine brave`。

## 星数曲线

```mermaid
xychart-beta
    title "pingfanfan/deepseek-search-bench 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-22", "2026-11-28"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-26 4 → 2026-11-28 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `ba3f0f0894f6` · [字段定义](../../DATASET.md)*
