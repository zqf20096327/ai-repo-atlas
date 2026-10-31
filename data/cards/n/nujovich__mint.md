# nujovich/mint

⭐ 27 · JavaScript · MIT · 推送 2026-10-14 · [GitHub](https://github.com/nujovich/mint) · 个人维护

**审计遗留 CSS 并生成可导出设计系统的 CLI/网页工具**

面向前端开发者与设计工程团队：以 Claude 分析 CSS/SCSS/HTML，将近似重复颜色聚类、检测字体、检查间距是否契合 4px 网格，并对布局可访问性、@property 类型契约、遗留 CSS 模式与颜色对比度做 lint，输出 chaos score 与审计报告；经人工筛选后生成设计 tokens，可导出为 Tailwind 配置、Astro 组件等格式，并用确定性（无 LLM）的 apply 命令将源码中的字面值重写为 var(--token) 引用。提供 CLI（npx mint-ds）与网页 playground 两种形态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 颜色/字体/间距/阴影/动效的聚类审计与命名 tokens 生成
- 布局可访问性、@property 类型安全、遗留 CSS 模式、WCAG 对比度 lint 规则集
- mint-ds apply 以确定性方式（无 LLM 调用）将源 CSS 值重写为 token 引用
- 导出目标含 Tailwind 配置与 Astro 组件

## 适用场景

- 把多年累积的遗留 CSS 整理成统一的设计 tokens
- 在引入设计系统前排查颜色重复与间距混乱
- 以 git diff 形式审阅地将现有样式迁移到 token 引用
- 检测 CSS 中的可访问性与过时浏览器 hack 问题

## 场景标签

 · 领域:前端/设计工具

## 证据(README 行号)

> L15: CSS / SCSS / HTML  →  Claude Audit  →  Review & curate  →  Clean tokens  →  Export  →  Apply
> L18: 1. **Audit** — Claude analyzes your CSS, groups near-duplicate colors into clusters, detects fonts, flags spacing v

## 星数曲线

```mermaid
xychart-beta
    title "nujovich/mint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9a3d2326e3b9` · [字段定义](../../DATASET.md)*
