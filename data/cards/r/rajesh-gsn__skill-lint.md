# rajesh-gsn/skill-lint

⭐ 15 · JavaScript · MIT · 推送 2026-04-30 · [GitHub](https://github.com/rajesh-gsn/skill-lint) · [官网](https://skill-lint.com/) · 个人维护

**浏览器端 SKILL.md 校验器：实时 lint、评分与 token 估算**

面向编写 Claude SKILL.md 技能文件的用户，提供纯浏览器端的校验工具：20 条验证规则覆盖 frontmatter 缺失、触发描述模糊、正文过长等错误/警告/提示级别，并给出 A–F 质量评分与 AI token 消耗估算。支持语法高亮、点击问题跳转行、拖放 .md 文件与暗色模式。实现为零依赖的纯 HTML/CSS/ES2020，无构建步骤，本地运行只需 git clone 后用浏览器打开或静态服务器承载，CI 自动部署到 Netlify。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 条验证规则，分 error/warning/info 三级
- A–F 质量评分与 AI token 消耗估算
- SKILL.md 感知的语法高亮与点击跳转到问题行
- 零依赖纯前端实现，无服务器、数据不上传

## 适用场景

- 发布前检查 SKILL.md 的 frontmatter 完整性与触发描述质量
- 估算技能文件的 token 占用是否超出上下文限制
- 追踪技能文件质量评分的改进情况

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: skill-lint.com — a free, browser-based validator for Claude SKILL.md files. No sign-up, no server, no data sent anyw
> L9: A `SKILL.md` is a structured Markdown file that tells Claude how to behave for a specific task — when to trigger, wh

## 星数曲线

```mermaid
xychart-beta
    title "rajesh-gsn/skill-lint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `b3ea6c260a3a` · [字段定义](../../DATASET.md)*
