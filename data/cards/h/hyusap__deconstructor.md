# hyusap/deconstructor

⭐ 263 · TypeScript · 推送 2026-04-01 · [GitHub](https://github.com/hyusap/deconstructor) · [官网](https://deconstructor.app) · 个人维护

**用 AI 拆解单词词根词源并可视化的 Web 应用**

基于 Next.js 与 React Flow 的交互式网页应用：用户输入任意单词，由 Claude Sonnet 4.5 分析词源与构成成分，以图形展示各词素（拉丁、希腊等来源）及含义组合。默认走 Anthropic API，需自备 API key；代码内注释示例支持切换 OpenAI 模型，其他供应商可经 Vercel AI SDK 接入。使用 Bun 安装依赖并运行开发服务器，属自部署项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 分析单词词源并拆解为词素
- React Flow 图形化展示词构成与来源
- 支持通过 Vercel AI SDK 更换模型供应商
- 提供深色模式与实时动画

## 适用场景

- 查询单词的词根构成与词源解释
- 语言学习时直观理解单词组合方式
- 自部署一个词源可视化小工具

## 场景标签

 · 领域:语言学习/工具

## 证据(README 行号)

> L12: - 🧠 AI-powered word deconstruction using Claude Sonnet 4.5
> L58: The project currently uses **Anthropic's Claude Sonnet 4.5** as the default model, but supports any provider throug

## 星数曲线

```mermaid
xychart-beta
    title "hyusap/deconstructor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 262 --> 264
    line [263, 263]
```

2026-10-18 263 → 2026-10-25 263（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `cbaf5c96265c` · [字段定义](../../DATASET.md)*
