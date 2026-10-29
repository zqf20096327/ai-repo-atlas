# neeraj-gs/CoverMe-AI-Chrome-Extension

⭐ 21 · TypeScript · 推送 2026-08-18 · [GitHub](https://github.com/neeraj-gs/CoverMe-AI-Chrome-Extension) · [官网](https://live-coverme-ai.vercel.app/) · 个人维护

**Chrome 扩展：结合简历与 LinkedIn 职位描述生成求职信**

基于 ReactJS 的 Google Chrome 扩展（CRA 构建）：用户输入简历与 OpenAI API key（存储于浏览器 Local Storage），扩展抓取当前 LinkedIn 职位页面的职位描述，将两者结合后调用 OpenAI API 生成定制求职信。目前仅支持 LinkedIn 网站。仓库另含用 Vite + React + three.js 构建的公开落地页 site/，可部署至 Vercel/Netlify。扩展本身需本地 npm install 构建后以 Load Unpacked 方式装入 Chrome。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 抓取 LinkedIn 职位描述并与用户简历结合
- 调用 OpenAI API 生成定制求职信
- API key 与简历存储于浏览器 Local Storage

## 适用场景

- 在 LinkedIn 上浏览职位时一键生成匹配的求职信
- 避免手写针对每个职位定制求职信

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: A Google Chome Extension that uses the Power of AI and generates Cover Letters for Jobs.
> L95:   Enter Your OpenAI API key and Resume and then click on Generate to get the Cover Letter

## 星数曲线

```mermaid
xychart-beta
    title "neeraj-gs/CoverMe-AI-Chrome-Extension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c198bc01ba43` · [字段定义](../../DATASET.md)*
