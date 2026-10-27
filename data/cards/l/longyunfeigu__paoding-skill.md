# longyunfeigu/paoding-skill

⭐ 25 · Python · Apache-2.0 · 推送 2026-06-26 · [GitHub](https://github.com/longyunfeigu/paoding-skill) · 个人维护 · 中文 README

**把 AI skill 拆解成解剖手册的 Claude Code skill**

运行在 Claude Code 中的 skill：对目标 skill 做反事实拆解，按「去掉它会坏什么」扫描难点（七维度归档），配合读文本、挖标本、活体切片、定点消融四级取证，产出三种交付物——轻量评审、难点卡片、六章 Web 解剖手册（含证据分级与可带走工具箱）。面向想学习 skill 设计模式、评审或改写 skill 的开发者。附带脚本化流水线：content 层手写、data.js 与构建由脚本生成，check-content.py 作为硬性构建门槛。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 反事实拆解：对每条规则问「去掉它第一个坏什么」，难点按七维度归档
- 四级取证：读文本→挖标本→活体切片→定点消融，论断标四级证据等级
- 三种产出：Keep/Cut 评审、难点卡片、六章 Web 解剖手册
- 源包脚本有合法输入即必须真跑的硬规则
- 生产流水线含 check-content.py 硬 gate，规格未过 gate 拒绝构建

## 适用场景

- 收藏了很多 skill 但说不清为什么好用，想拆开学设计模式
- 评审自己的 skill，决定哪些该删该留
- 从成熟 skill 中提取可迁移的模式用到自己的领域

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: 你收藏了 100 个 skill，说不出其中任何一个为什么好用。
> L10: 以前钻源码学设计模式，现在该拆 skill 学 **skill 设计模式**了。
> L12: **庖丁把一个 skill 拆开，产出一本手册，讲清三件事：效果好在哪、怎么做到的、哪些招你能直接用。**

## 星数曲线

```mermaid
xychart-beta
    title "longyunfeigu/paoding-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-27 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `765d4554652d` · [字段定义](../../DATASET.md)*
