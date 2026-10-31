# sholajegede/openloops

⭐ 20 · TypeScript · MIT · 推送 2026-06-14 · [GitHub](https://github.com/sholajegede/openloops) · 个人维护

**本地浏览器扩展：把浏览历史聚成意图线程并给出下一步**

仅本地运行的 Manifest V3 Chrome 扩展，用 TypeScript/React/Vite 构建，数据存于 IndexedDB。核心流水线为：回填 14 天历史、噪声过滤、30 分钟空闲切分会话、贪心凝聚聚类成线程、按多信号置信度与 active/stalled/dormant 状态评分。每条线程提供摘要、下一步与 Resume 按钮。三项可选功能需自带 API key 且显式触发：context.dev 品牌富化、Claude 线程标注、基于线程数据的 AI 助手聊天；核心流水线无网络调用即可产出意图图。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览历史→会话→意图线程的本地聚类流水线（Jaccard 相似度 + 环境域排除）
- 每线程给出类型徽章、置信度、下一步与 Resume 按钮
- 三栏仪表盘：流水线操作、线程卡片列表、AI 助手聊天
- 三项 AI 功能均为 opt-in，需用户自有 Anthropic/context.dev key

## 适用场景

- 找回未完成的调研/比价/决策线索并一键恢复页面
- 问 AI 助手本周该关闭哪些线程
- 在不上传数据的前提下梳理自己的浏览意图

## 场景标签

 · 领域:浏览器/个人生产力工具

## 证据(README 行号)

> L21: openloops is a local-only Chrome extension that turns raw browsing history into **intent threads** — the open loops
> L64: None of the three steps is required. The core pipeline — capture, noise filter, sessions, clustering, scoring — run
> L68: The core pipeline — capture, noise filtering, session segmentation, ambient detection, clustering, and scoring — ru

## 星数曲线

```mermaid
xychart-beta
    title "sholajegede/openloops 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-31 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `c6c23ea28c56` · [字段定义](../../DATASET.md)*
