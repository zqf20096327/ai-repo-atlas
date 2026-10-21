# nanaism/yomiyasu

⭐ 2,262 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/nanaism/yomiyasu) · 个人维护

**供 AI 编码环境调用的日文推敲技能：改写 AI 日文为自然日文**

面向 Claude Code、Codex、Cursor 等 AI 编码环境的 Agent Skill：按 7 条转换原则修正 AI 生成日文中的不自然比喻、含糊主谓关系、过度装饰，覆盖技术文章、设计书、PR 说明、社内报告等实务文体。2.0.0 起加入文档类型（12 种）与读者知识判定、改写前后六点比对、附带 yomiyasu_check.py 做 lint 与 diff 检查；2.1.0 增加语序与许可/能力/保证表述的检查规则。提供 npx skills add、gh skill、openskills、Claude Code 插件、ZIP 注册、仓库内复制共六种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 条转换原则修正比喻、主谓关系、句长与装饰等结构问题
- 改写前按 12 种文档类型与 3 级读者知识判定处理策略
- yomiyasu_check.py 提供 lint 与 diff 检查（--fail-on=meaning-risk）
- 六种安装途径覆盖 Claude Code / Codex / Cursor / Claude.ai Web

## 适用场景

- 在 Claude Code 或 Codex 中推敲 PR 说明文、设计书等 AI 生成日文
- 在指令文件中加入一行让代理每次撰写日文时都经过该技能
- 按文档类型（议事录、障害报告等）保留其惯用写法仅修问题句

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L12: 『**yomiyasu（よみやす）**』はAIが生成した日本語の不自然な比喩、曖昧な主述関係、不要な装飾を直し、読みやすい文章に整えるスキルです。
> L16: Claude Code、Codex、CursorをはじめとするAIコーディング環境に読み込ませて使用してください。

## 星数曲线

```mermaid
xychart-beta
    title "nanaism/yomiyasu 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 2161 --> 2271
    line [2170, 2262, 2262]
```

2026-10-18 2,170 → 2026-10-21 2,262（+92）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4d7f96d34a34` · [字段定义](../../DATASET.md)*
