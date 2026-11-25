# op7418/guizang-pages-skill

⭐ 4 · CSS · AGPL-3.0 · 推送 2026-10-31 · [GitHub](https://github.com/op7418/guizang-pages-skill) · 个人维护 · 中文 README

**供 AI Agent 将 Markdown 排成单页 HTML 阅读页的 Skill**

适配 Claude Code、Codex 等 Agent 环境的排版 Skill：读取 Markdown 文档、文章或笔记，生成精排单文件 HTML，支持导出 PDF 与长图。提供杂志风与瑞士风两种风格、忠实/解释两种模式，针对中文排版有专门规则（窄栏、不用斜体等）。机制上是模型输出标注 JSON（说明哪些行升格为组件），由确定性脚本 render.mjs 渲染，原文全量保留不删改。安装支持 npx 一行命令或 git clone，渲染需 Node.js 18+，导出需 Chrome/Chromium。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型输出标注 JSON、脚本确定性渲染，原文每一行进入最终页面
- 杂志风与瑞士风两种风格，支持品牌色受约束生成主题
- 中文排版专门规则：窄栏居中、不用斜体、裸 URL 短链显示
- 导出 PDF 与 1440 宽长图

## 适用场景

- 把文章或笔记排成杂志风阅读网页
- 将 Markdown 文档生成瑞士风页面并导出 PDF
- 为中文长文生成移动端不溢出的单页 HTML

## 场景标签

 · 领域:内容生成/排版工具

## 证据(README 行号)

> L10: 一个适配 Claude Code、Codex 等 Agent 环境的排版 Skill，能把 Markdown 文档、文章或笔记排成**精排单页 HTML**，也可以导出 PDF 和长图。
> L42: **模型负责判断，脚本负责渲染。**

## 星数曲线

```mermaid
xychart-beta
    title "op7418/guizang-pages-skill 星数(近 3 点)"
    x-axis ["2026-11-01", "2026-11-02", "2026-11-25"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-01 3 → 2026-11-25 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `7b397a722064` · [字段定义](../../DATASET.md)*
