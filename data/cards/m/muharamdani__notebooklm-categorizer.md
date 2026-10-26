# muharamdani/notebooklm-categorizer

⭐ 29 · JavaScript · MIT · 推送 2026-08-01 · [GitHub](https://github.com/muharamdani/notebooklm-categorizer) · 个人维护

**给 NotebookLM 列表加分类筛选按钮的浏览器扩展**

浏览器扩展（含 userscript 版本），在 NotebookLM 笔记本列表中添加分类筛选按钮：基于标题关键词自动分组到 Tutorial、Finance 等类别，通过 arrive.js 监听 SPA 动态页面变化，用浏览器存储记住上次筛选，提供分类管理弹窗可自定义类别与关键词。面向 NotebookLM 用户，提供 Firefox 商店安装、XPI 手动安装、Chrome 加载未打包扩展和 Tampermonkey 脚本四种安装方式。分类完全基于标题关键词匹配，不调用任何模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于标题关键词的自动分类与筛选按钮 UI
- arrive.js 监听 SPA 动态导航，无需手动刷新
- 浏览器存储记住上次选中的筛选
- 分类管理弹窗支持自定义类别与关键词

## 适用场景

- NotebookLM 笔记本较多时按类别快速筛选
- 自定义关键词分组管理自己的笔记本列表

## 场景标签

 · 领域:浏览器扩展/生产力工具

## 证据(README 行号)

> L3: **NotebookLM Categorizer** is a browser extension that adds smart **category filter buttons** to the NotebookLM list
> L20: - 🗂️ Auto-categorizes based on title keywords

## 星数曲线

```mermaid
xychart-beta
    title "muharamdani/notebooklm-categorizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `edd5efb66da9` · [字段定义](../../DATASET.md)*
