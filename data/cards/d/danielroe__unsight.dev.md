# danielroe/unsight.dev

⭐ 135 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/danielroe/unsight.dev) · [官网](https://unsight.dev) · 个人维护

**跨仓库检测重复 GitHub issue 与问题聚集区的 Web 应用**

基于 Nuxt 4 与 Nitro 的 GitHub App 型 Web 应用：读取关联仓库的 issues，通过 AI 嵌入与 k-means 聚类发现重复 issue 与需要关注的聚集区域，经 @octokit/rest 集成 GitHub，部署在 Cloudflare（NuxtHub、Workers AI、D1、KV、Vectorize），并提供 Chrome/Firefox 浏览器扩展。本地可 UI-only 模式连接远程 API 体验；完整开发环境需创建 GitHub App、配置密钥并关联 Cloudflare 账号。

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

- AI 嵌入 + k-means 聚类检测重复 issue 与聚集区域
- GitHub App 集成（@octokit/rest），读取仓库 issues
- 部署于 Cloudflare：Workers AI、D1 (SQLite)、KV、Vectorize
- 提供 Chrome 与 Firefox 浏览器扩展

## 适用场景

- 维护多个相关仓库时发现重复提交的 issue
- 查看某仓库 issue 的聚类，识别需要关注的区域
- 通过浏览器扩展直接在 GitHub 页面查看聚类结果

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: > Detect duplicate GitHub issues, areas of concern and more across related repositories
> L14: - AI-powered issue embeddings and k-means clustering

## 星数曲线

```mermaid
xychart-beta
    title "danielroe/unsight.dev 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 134 --> 136
    line [135, 135]
```

2026-10-18 135 → 2026-10-26 135（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5258e992687c` · [字段定义](../../DATASET.md)*
