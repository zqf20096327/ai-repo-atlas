# Ayanami0730/paper-read-skill

⭐ 17 · 推送 2026-07-02 · [GitHub](https://github.com/Ayanami0730/paper-read-skill) · 个人维护 · 中文 README

**供 AI Agent 深度阅读论文与博客的 prompt 技能集**

面向 Cursor、Claude Code、Codex、OpenCode 等 agent 的 prompt/skills 集合，按内容类型自动路由分析框架：论文分为 benchmark、方法/算法、综述/观点三类，博客分为技术研究、产品发布、行业观点、案例故事四类；对 Nature/Science/Cell 系顶刊论文额外叠加期刊阅读维度（发表策略、Abstract 拆解、逐图分析等）。通过 npx skills add 命令安装，或手动复制 skills 目录到 ~/.cursor/skills/。仅需 agent 自带 web fetch 工具，无需付费抓取服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按论文类型（benchmark/方法/综述）自动路由分析框架
- Nature/Science/Cell 顶刊论文叠加期刊阅读维度
- 四类博客分析框架，中文自然语言段落输出
- 兼容 Cursor / Claude Code / Codex / OpenCode

## 适用场景

- 让编程 agent 在 Cursor/Claude Code 中代为深度阅读论文
- 对博客文章做去营销化的技术解读
- 分析投稿顶刊论文的发表策略与可复现性

## 场景标签

`提示工程` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L3: 让 AI Agent 深度阅读论文和博客的 prompt 集合。根据内容类型自动路由到对应的分析框架。
> L17: 根据论文类型自动路由分析框架：

## 星数曲线

```mermaid
xychart-beta
    title "Ayanami0730/paper-read-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `18a2c0399e09` · [字段定义](../../DATASET.md)*
