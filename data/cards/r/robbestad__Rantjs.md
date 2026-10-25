# robbestad/Rantjs

⭐ 219 · TypeScript · ISC · 推送 2026-09-04 · [GitHub](https://github.com/robbestad/Rantjs) · [官网](https://rantjs.vercel.app) · 个人维护

**JavaScript 种子化程序化文本生成引擎，写模式即得句子**

面向 JavaScript 开发者的过程式文本生成库：用小型模式语言（查询、块、标签、载体）描述句子形状，由基于 Rantionary 编译的英文词典填充词条，同一模式加同一种子产出同一句子。提供 rant()/compile() 等 API、CLI、ESM/CommonJS/浏览器 IIFE 构建，并附可直接粘贴给编码助手的提示块以生成 rantjs 模式。明确声明不依赖模型调用；rantjs 3.0 已冻结，后继语言为 Skald（npm 包 skald-lang），种子不可跨语言移植。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一模式+同一种子输出确定性可复现句子
- 查询/加权块/重复/载体同步的小型模式语言
- 基于 Rantionary 编译并按类别索引的英文词典
- ESM、CommonJS、CLI 与浏览器 IIFE 多端运行

## 适用场景

- 为游戏生成 NPC 对话、物品风味文本和世界设定
- 生成确定性测试夹具与提示词变体
- 保存种子以在测试、存档中复现相同文本

## 场景标签

 · 领域:程序化文本生成/游戏开发

## 证据(README 行号)

> L3: **Write a pattern. Get a sentence.** A seeded procedural-text engine for JavaScript — names, verbs, places, and the 
> L26: - **Repeatable.** The same pattern plus the same seed is the same sentence. That makes tests, save games, and LLM p
> L37: Paste the block below into ChatGPT, Codex, Claude, or another coding assistant, then replace the bracketed brief. I

## 星数曲线

```mermaid
xychart-beta
    title "robbestad/Rantjs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 218 --> 220
    line [219, 219]
```

2026-10-18 219 → 2026-10-25 219（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `64720359b5d3` · [字段定义](../../DATASET.md)*
