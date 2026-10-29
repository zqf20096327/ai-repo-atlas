# itsrouk/your-ai-focus-group

⭐ 24 · TypeScript · MIT · 推送 2026-05-26 · [GitHub](https://github.com/itsrouk/your-ai-focus-group) · [官网](https://your-ai-focus-group.vercel.app) · 个人维护

**用合成 AI 焦点小组为创意与文案做 Likert 打分**

基于 Next.js 14 的 Web 应用：用户输入要测试的产品创意、标语或概念，工具剥离品牌词后生成 10 个多样化合成人格，用户选 3-5 个组成小组，逐个提出最多 5 个开放问题，每个回答获得 1-5 的 Likert 评分，最终输出记分卡（有效点、待改进点、共识度、关键洞察），可复制完整访谈记录。方法自称基于 follow-up Likert rating（FLR）。运行需 Node.js 18+ 与免费 Google Gemini API key，pnpm 安装后本地启动。面向需要快速方向性反馈的营销与产品人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成 10 个合成人格，用户挑选 3-5 个组成焦点小组
- 剥离品牌词以避免偏差，逐个顺序回答最多 5 个开放问题
- 输出 Likert 1-5 评分记分卡：有效点/待改进/共识度/关键洞察
- 可复制完整访谈记录为纯文本

## 适用场景

- 在写文案前快速测试标语或 pitch 的反响
- 为产品概念获取方向性反馈而无需组织真实焦点小组
- 对比不同目标人群视角对同一创意的共识与分歧

## 场景标签

 · 领域:营销/市场调研工具

## 证据(README 行号)

> L3: You have a product idea, a tagline, a pitch, or maybe something you just want feedback on. This tool spins up a pane
> L24: Behind the scenes, the tool strips out brand-specific details to avoid biasing the results (it won't say "Nike shoe
> L30: At the end, each response gets a Likert score (1–5), and you get a **scorecard** that surfaces:

## 星数曲线

```mermaid
xychart-beta
    title "itsrouk/your-ai-focus-group 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-29 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2bbb3ed0fdc4` · [字段定义](../../DATASET.md)*
