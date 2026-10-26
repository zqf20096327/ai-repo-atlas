# LOGIN-TB/claude-skills

⭐ 80 · Python · MIT · 推送 2026-09-17 · [GitHub](https://github.com/LOGIN-TB/claude-skills) · 组织维护

**德语 Claude Agent Skills 集合：写作、邮件送达与 DACH 营销技能**

面向 Claude 生态的 SKILL.md 格式技能仓库，共 15 个德语技能：vermenschlichen（改写文本以减少 AI 式语言痕迹）、zustellbarkeit（带确定性检查脚本分析邮件为何进垃圾箱、纯本地运行）、以及 13 个基于 MIT 许可 coreyhaines31/marketingskills 策展改编的 DACH 营销技能（含来源、上游 Commit 与改动文档）。技能可在 Claude Code（插件市场或手动复制）、Claude-App（ZIP 上传）与 API 中加载；其他 Agent 可将正文用作系统提示。仓库声明技能安装不授权其中描述的外部动作，法律引用非法律建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个德语 SKILL.md 技能，可在 Claude Code / Claude-App / API 使用
- zustellbarkeit 附确定性检查脚本，纯本地运行、不抓取链接或图片
- 13 个营销技能为 MIT 上游项目的策展德语改编，改动记录于文档
- 其他 Agent 可将 SKILL.md 正文用作系统提示（开放格式）

## 适用场景

- 让 Claude 按德语写作规则改写文章与邮件草稿
- 在发送前分析邮件被判为垃圾邮件的结构与内容原因
- 面向德奥瑞市场执行 SEO 审计、冷邮件等营销任务

## 场景标签

`提示工程` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L3: Agent Skills zur freien Nutzung. Ein Skill ist eine Markdown-Datei mit Anweisungen, die Claude lädt, sobald sie zum 
> L68: Die dreizehn Skills sind kuratierte Bearbeitungen der MIT-lizenzierten `coreyhaines31/marketingskills`. Herkunft, g
> L161: `vermenschlichen` und `zustellbarkeit` sind Eigenentwicklungen. Die dreizehn Marketing-Skills sind kuratierte deut

## 星数曲线

```mermaid
xychart-beta
    title "LOGIN-TB/claude-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-26 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4857c495b93a` · [字段定义](../../DATASET.md)*
