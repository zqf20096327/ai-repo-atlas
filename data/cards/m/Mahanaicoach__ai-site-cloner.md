# Mahanaicoach/ai-site-cloner

⭐ 22 · JavaScript · MIT · 推送 2026-07-22 · [GitHub](https://github.com/Mahanaicoach/ai-site-cloner) · 个人维护

**让编程 Agent 把任意网站克隆为像素级还原的 Next.js 应用的技能与脚本管线**

面向 Claude Code、Cursor、Copilot 等 12 种编程 Agent 的网站克隆工具：以 /clone-website 命令驱动六阶段流水线——爬取站点、用 Playwright 脚本实测每项计算样式（字体、间距、颜色等，非截图猜测）、生成组件规格并经 lint 门禁、在 git worktree 中派发并行构建 Agent、以 pixelmatch 像素差异评分循环 QA 直至每个区块在三种视口下达到 95%。产物为可维护的 Next.js 组件化代码，另有 /restyle 换品牌。声明用途为自有站点迁移、源码找回与学习，禁止钓鱼与冒充。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Playwright 脚本实测计算样式与响应式断点，Agent 不自行猜测数值
- 并行构建 Agent + git worktree，pixelmatch 每区块每视口 95% 门槛
- 紧凑工件设计控制 Agent token 消耗（如整页提取 889KB 压至 445KB）
- 技能文件一次编写并同步到 12 种 Agent 工具的原生格式

## 适用场景

- 把我拥有但丢失源码的网站迁移为可维护的 Next.js 代码
- 研究生产级网站的构建方式并得到像素级可验证的复刻
- 克隆模板后用 /restyle 快速换成自己的品牌

## 场景标签

`编码 Agent` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: One command. `/clone-website` turns Claude Code (or Cursor, Copilot, Gemini CLI — 12 tools supported) into a full cl
> L117: The two skills are written once in `.claude/skills/` and synced to every other tool's native format (`node scripts
> L119: **Claude Code** (native) · **Cursor** · **Windsurf** · **GitHub Copilot** · **Gemini CLI** · **Amazon Q** · **Code

## 星数曲线

```mermaid
xychart-beta
    title "Mahanaicoach/ai-site-cloner 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26", "2026-10-29"]
    y-axis "stars" 18 --> 23
    line [19, 20, 22, 22]
```

2026-10-18 19 → 2026-10-29 22（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `38a1d3843327` · [字段定义](../../DATASET.md)*
