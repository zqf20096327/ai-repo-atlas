# scos-lab/markview

⭐ 14 · TypeScript · MIT · 推送 2026-08-25 · [GitHub](https://github.com/scos-lab/markview) · [官网](https://stl-lang.org) · 组织维护

**面向 LLM 输出的只读 Markdown 阅读器（已停止开发）**

Windows/Linux 桌面端 Markdown 阅读器，定位只读不编辑：渲染 Mermaid 图表、Vega-Lite 图表、KaTeX 数学、GFM 表格与 100+ 语言语法高亮，用于查看 LLM 生成的回复与技术报告；另含目录生成、文档内搜索、文件监听、token 数估算等功能。基于 Tauri 2 (Rust)+React 构建，提供 .exe/.msi/.deb/.AppImage 安装包。注意：项目已宣告 feature-frozen，不再发布更新，1.0.5 版存在未消毒 HTML 安全漏洞（修复仅在 main 分支与社区 fork），后续开发转移至 Rho MD 与 Scorpse/markview fork。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Mermaid/Vega-Lite/KaTeX/GFM 一体化渲染
- 文档内搜索、文件监听自动重载、token 估算
- 提供 Windows 安装包与 Linux .deb/.AppImage

## 适用场景

- 把 Claude/ChatGPT 回复中的图表和公式直接渲染成可视化
- 阅读 LLM 生成的技术报告与仓库 README/发布说明
- 作为系统默认 .md 文件阅读器

## 场景标签

 · 领域:桌面文档工具

## 证据(README 行号)

> L15: An AI-native Markdown reader for Windows and Linux — renders Mermaid
> L35: - **See LLM output rendered immediately** — paste a Claude / ChatGPT / Gemini reply that contains Mermaid diagrams 
> L39: If you need editing, sync, plugins, or note-taking, Obsidian, Typora, and MarkText are great. MarkView is intention

## 星数曲线

```mermaid
xychart-beta
    title "scos-lab/markview 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `1e7914322af8` · [字段定义](../../DATASET.md)*
