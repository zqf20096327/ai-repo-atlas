# yfge/zhiforge

⭐ 16 · MIT · 推送 2026-03-02 · [GitHub](https://github.com/yfge/zhiforge) · [官网](https://yfge.github.io) · 个人维护 · 中文 README

**把 Markdown 博客知识库自动转成知乎回答并发布的 Skill**

面向 Claude Code 与 OpenClaw 的自动化 Skill：读取配置与已回答列表后，搜索知乎热点问题与邀请，匹配用户 Jekyll 博客知识库中的相关文章，由 AI 按作者风格撰写回答，经浏览器自动化（Chrome MCP/OpenClaw 内置 browser）发布到知乎，再做多模型交叉质量审核，并以 Jekyll frontmatter 形式 git push 回存知识库，共 9 步闭环。知识库需为标准 Jekyll _posts 结构；Claude Code 路径要求 Node.js 18+、Chrome 浏览器并安装 Chrome MCP，OpenClaw 路径无需额外安装。

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

- 热点搜索→知识库匹配→撰写→发布→审核→回存的 9 步闭环流程
- 基于 Jekyll Markdown 博客知识库生成回答并保持作者风格
- OpenClaw 路径内置 browser 工具，Claude Code 路径经 Chrome MCP 操作页面
- 发布后自动以 Jekyll frontmatter 回存知识库（OpenClaw）

## 适用场景

- 我想让 AI 根据我的博客内容自动回答知乎问题
- 我想把知乎回答沉淀回自己的博客知识库形成闭环
- 我想批量查看知乎邀请并匹配已有文章草拟回答

## 场景标签

`浏览器自动化` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L10: **知炼**是一个自动化工具，能够将你的 Markdown 知识库（博客文章）智能转化为高质量的知乎回答，并自动发布。
> L14: - 🤖 **全自动流程**：搜索热点问题 → 去重 → 匹配知识库 → 撰写文章 → 发布回答
> L64: #### OpenClaw 完整流程（9 步闭环）

## 星数曲线

```mermaid
xychart-beta
    title "yfge/zhiforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `f92d52f48d0c` · [字段定义](../../DATASET.md)*
