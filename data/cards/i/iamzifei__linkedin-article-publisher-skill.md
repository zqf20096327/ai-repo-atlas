# iamzifei/linkedin-article-publisher-skill

⭐ 22 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/iamzifei/linkedin-article-publisher-skill) · 个人维护 · 中文 README

**Claude Skill：将 Markdown 文章一键发布为 LinkedIn 草稿**

面向 Claude Code 用户的技能插件：解析 Markdown 文件，转换为 HTML 富文本，经由剪贴板粘贴与 Playwright MCP 浏览器自动化，把文章（含封面图与内容图）发布到 LinkedIn Articles，并只保存为草稿、不自动发布。图像采用 block_index 定位与倒序插入保证位置准确。要求 Claude Code、Playwright MCP、Python 3.9+ 与 LinkedIn 账号，目前仅支持 macOS，通过 git clone 或插件市场安装。

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

- Markdown 转 HTML 富文本剪贴板粘贴，保留标题/加粗/链接等格式
- block_index 图像定位与倒序插入机制
- 仅保存草稿，不自动发布
- 自然语言或技能命令两种调用方式

## 适用场景

- 我写好 Markdown 想直接发到 LinkedIn 文章而不手动排版
- 批量带图发布时保证图片插入位置准确
- 发布前以草稿形式人工审核内容

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L64: |Claude Code|claude.ai/code|
> L65: |Playwright MCP|Browser automation|
> L105: /linkedin-article-publisher /path/to/article.md

## 星数曲线

```mermaid
xychart-beta
    title "iamzifei/linkedin-article-publisher-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9c7040f6761e` · [字段定义](../../DATASET.md)*
