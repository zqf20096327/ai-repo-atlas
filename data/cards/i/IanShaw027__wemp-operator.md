# IanShaw027/wemp-operator

⭐ 113 · JavaScript · MIT · 推送 2026-02-02 · [GitHub](https://github.com/IanShaw027/wemp-operator) · 个人维护 · 中文 README

**微信公众号自动化运营 OpenClaw 技能：采集、分析、互动**

面向 OpenClaw agent 框架的微信公众号运营技能：封装 70 个微信公众号 API（统计、草稿、发布、评论、用户、标签、模板消息、素材、客服消息、菜单、二维码、群发），并从 Hacker News、微博、知乎、B站等 20+ 数据源采集热点，自动生成含 AI 洞察的日报/周报，支持评论检查与精选。用户通过自然语言对话触发（如『采集今天的 AI 热点』），也可直接调用 Node.js 脚本。需在 openclaw.json 配置公众号 AppID/AppSecret，要求 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 70 个微信公众号 API，无需额外依赖
- 20+ 数据源热点采集，支持关键词过滤与深度抓取
- 自然语言触发工作流，附命令行脚本用于调试与自动化
- 自动生成含用户增长、阅读数据与 AI 洞察的日报/周报

## 适用场景

- 运营者让 AI agent 代为采集热点、生成日报
- 通过对话批量检查与精选公众号评论
- 自动化草稿创建与文章发布流程

## 场景标签

`工作流自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L13:  微信公众号自动化运营 OpenClaw Skill - 内容采集、数据分析、互动管理
> L62: 安装 skill 后，直接用自然语言与 OpenClaw 对话即可。Skill 会根据触发词自动激活。
> L286: ├── SKILL.md              # AI 指令文件

## 星数曲线

```mermaid
xychart-beta
    title "IanShaw027/wemp-operator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-24 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `609c1ba010ce` · [字段定义](../../DATASET.md)*
