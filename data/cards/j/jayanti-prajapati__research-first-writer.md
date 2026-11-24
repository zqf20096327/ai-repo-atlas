# jayanti-prajapati/research-first-writer

⭐ 5 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/jayanti-prajapati/research-first-writer) · 个人维护

**面向内容作者的研究优先文章写作 Claude Code 技能**

以 Claude Code 插件、Claude 技能或纯 Markdown 剧本形式分发的写作技能：先检索并阅读真实搜索结果页面，从 3-5 个基线页面学习，用事实台账为每个数字标注出处与 URL，无法一手验证的经验性表述以 [[NEEDS_HUMAN]] 标记留空；写作经规则检查脚本与独立评审双重把关，在发现、基线选择、大纲三个检查点暂停等待批准。附带的 check_article.py 与 check_originality.py 仅依赖 Python 标准库，可在 CI 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 事实台账机制：每个 %/价格/小数追踪到引文与 URL
- [[NEEDS_HUMAN]] 标记替代虚构的"我们测试过"表述
- check_article.py 规则检查与独立 judge 评审，三级检查点暂停
- check_originality.py 检测 14 词以上连续重合与 20% 以上短语重合

## 适用场景

- 按关键词生成带出处的 SEO/GEO 文章
- 审计已有草稿中的虚构测试声明与无出处数字
- 把 SKILL.md 剧本手动交给人类写手或任意 agent 使用

## 场景标签

`AI 写作` `科研工具` · 领域:内容生成

## 证据(README 行号)

> L3: **An agent skill that writes articles the way a careful editor would: read what really ranks, find what it misses, c
> L5: Works as a Claude Code plugin, a Claude skill, or a plain-Markdown playbook for any agent or human writer.
> L30: It is built for Google *and* for AI answer engines (ChatGPT, Perplexity, AI Overviews). Answer engines favour pages

## 星数曲线

```mermaid
xychart-beta
    title "jayanti-prajapati/research-first-writer 星数(近 2 点)"
    x-axis ["2026-11-02", "2026-11-24"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-11-02 5 → 2026-11-24 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `0e991a13273c` · [字段定义](../../DATASET.md)*
