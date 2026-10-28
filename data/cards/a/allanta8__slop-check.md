# allanta8/slop-check

⭐ 20 · MIT · 推送 2026-06-18 · [GitHub](https://github.com/allanta8/slop-check) · 个人维护

**面向 agent 的 AI 味写作审计技能：发布前检出模板化内容**

一个独立写作审计技能（skill），供 Codex 或 Claude Code 类 agent 调用，在发布前检查文本是否存在 AI slop 特征——包括禁用词汇与填充语、弱开头、伪平衡、模板化段落、无支撑的精确声明、机械节奏等。输出分违规层级、三项质量门检查、8 维评分卡与重写建议，最终裁决为 PASS / NEEDS REWRITE / REWRITE（阈值 9-10 PASS、6-7.9 需重写、低于 6 重写）。通过复制文件夹到技能目录安装，支持 X、LinkedIn、博客、落地页等多类内容。

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

- 检查 9 类 AI slop 模式（禁用词、伪平衡、机械节奏等）
- 输出 8 维评分卡与 PASS/NEEDS REWRITE/REWRITE 裁决
- 以技能文件夹形式安装到 Codex 或 Claude Code 类 agent
- 适用于 X、LinkedIn、博客、落地页、创始人更新等发布前审查

## 适用场景

- 发布 X 或 LinkedIn 帖子前让 agent 跑一遍 AI 味检查
- AI 辅助草稿发布前做人工质量把关
- 落地页文案与产品公告发布前获得重写建议

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: `slop-check` is a standalone writing-audit skill for catching AI-slop patterns before publishing.
> L47: For Claude Code-style skill folders:
> L58: Ask your agent to run `slop-check` on a draft:

## 星数曲线

```mermaid
xychart-beta
    title "allanta8/slop-check 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `cd2c86c80577` · [字段定义](../../DATASET.md)*
