# myunwang/ppt-report-skills

⭐ 80 · HTML · MIT · 推送 2026-06-03 · [GitHub](https://github.com/myunwang/ppt-report-skills) · 个人维护 · 中文 README

**把数据汇报生成 16:9 网页 PPT 的 Claude Code skill/工程模板**

一套将“数据报告 → 网页幻灯片”流程工程化的模板，提供两种用法：作为 Claude Code Skill 放入 ~/.claude/skills/ 让 Claude 按规范自动生成汇报；或作为独立工程模板运行 python3 build.py 打包单 HTML。核心机制：每页 = HTML+CSS+JS 三个 ≤200 行小文件（改一页省 token）、数据用 Excel/CSV/JSON 物理分离后自动注入、9 个页面模板（含人体剪影、价值链、产业图谱）、5 套主题一键切换、ECharts 图表选型决策表、playwright+img2pdf 一键导出 PDF。声明不适合文字密集型与复杂动画场景。

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

- 每页 3 个小文件的物理分离结构，改一页不触及其余页面
- 9 个页面模板（KPI 总览、2×2 矩阵、人体剪影、价值链等）与 5 套预设主题
- Excel/CSV/JSON 数据源，build 自动转 JSON 注入，更新只改数据文件
- 支持 16:9 与竖屏多平台规格导出 PDF/图片

## 适用场景

- 让 Claude Code 按固定规范把月度/季度数据做成网页 PPT
- 数据团队做含多图表的对比实验、多主体趋势、KPI 总览汇报
- 生成小红书 3:4、公众号长图等竖屏规格内容

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L37: 1. **As a Claude Code Skill** — drop this repo into `~/.claude/skills/ppt-report-generator/` and let Claude build r
> L92: Then in Claude Code just say **"make a monthly report"** / **"turn this data into a slide deck"**, and Claude will 
> L38: 2. **As a standalone project template** — copy `assets/` to `src/` and run `python3 build.py` to bundle a single HT

## 星数曲线

```mermaid
xychart-beta
    title "myunwang/ppt-report-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 79 --> 82
    line [81, 80, 80]
```

2026-10-18 81 → 2026-10-25 80（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `1e0a02e903c0` · [字段定义](../../DATASET.md)*
