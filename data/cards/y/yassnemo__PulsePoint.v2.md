# yassnemo/PulsePoint.v2

⭐ 16 · TypeScript · MIT · 推送 2026-04-10 · [GitHub](https://github.com/yassnemo/PulsePoint.v2) · [官网](https://pulsepoint.yerradouani.me) · 个人维护

**网页应用：粘贴文章链接，AI 生成摘要与要点**

基于 Web 的文章摘要应用：用户粘贴文章 URL，应用抓取网页正文，调用 Gemini API（默认 gemini-1.5-flash）生成 2-3 句摘要、关键要点列表、压缩率统计与文章配图。需配置 GEMINI_API_KEY；AI 调用失败时自动回退到基础摘要。支持本地 npm 运行（Node.js 18+）与 Vercel 部署，摘要提示词可在 api/summarize.ts 中自定义。面向忙碌职场人士、学生等希望减少信息过载的用户。

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

- 粘贴 URL 即生成摘要、要点、压缩率与文章配图
- 基于 Gemini API，模型可通过 GEMINI_MODEL 环境变量更换
- AI 失败时自动回退到基础摘要
- 提示词位于 api/summarize.ts，可自定义

## 适用场景

- 快速了解长文核心内容，减少阅读负担
- 汇总新闻与资讯文章要点
- 自定义摘要提示词适配不同用途

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: > *Turn lengthy articles into bite-sized insights with AI-powered summarization*
> L92:  - 📝 A concise summary (2-3 sentences)

## 星数曲线

```mermaid
xychart-beta
    title "yassnemo/PulsePoint.v2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0fc629364958` · [字段定义](../../DATASET.md)*
