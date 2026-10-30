# wenzhenl/wikitimeline

⭐ 57 · TypeScript · MIT · 推送 2026-03-23 · [GitHub](https://github.com/wenzhenl/wikitimeline) · [官网](https://wiki-timeline.com) · 个人维护

**将维基百科文章转换为可交互 AI 时间线并支持并排对比的 Web 应用**

基于 Next.js 14 构建的 Web 应用：用户搜索任意维基百科条目，应用调用 Google Gemini API 抽取并组织时间性事件，生成交互式时间线，支持多主题并排对比、缩放滚动浏览、深浅色主题与响应式界面。数据经 Vercel KV (Redis) 存储，可一键部署到 Vercel。运行需自备 Gemini API key 并配置 Vercel CLI 与 KV 存储。提供 Live Demo 在线试用。

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

- 调用 Gemini 从维基百科文章抽取时间性事件生成时间线
- 多时间线并排对比（如华盛顿与乾隆）
- 自动补全的条目搜索与缩放滚动交互
- 支持部署到 Vercel，使用 Vercel KV 存储

## 适用场景

- 搜索维基百科人物或事件并生成可视化时间线
- 对比不同历史人物或事件的并排时间线
- 教育或历史学习场景下的时间线可视化展示

## 场景标签

 · 领域:教育/历史可视化

## 证据(README 行号)

> L15: - 🤖 **AI-Powered**: Utilizes Google Gemini to extract and organize chronological events
> L75: 4. Click "Generate Timeline" to view your interactive timeline

## 星数曲线

```mermaid
xychart-beta
    title "wenzhenl/wikitimeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-30 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `31defb7511ca` · [字段定义](../../DATASET.md)*
