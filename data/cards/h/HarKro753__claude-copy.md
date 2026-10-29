# HarKro753/claude-copy

⭐ 18 · Python · MIT · 推送 2026-08-02 · [GitHub](https://github.com/HarKro753/claude-copy) · [官网](https://www.officeos.co) · 组织维护

**Claude Code 插件：像素级复刻网页界面并用渲染差异验证**

由 Chrome MV3 扩展与 Claude Code 插件组成的界面重建管线：扩展采集线上页面的整页截图、DOM 与计算样式；插件据此重建页面，输出静态 HTML 或 shadcn/ui React 组件，再在 headless Chromium 中渲染并与原图逐像素对比评分，未达标区域循环返工。评分器为纯 Python（PIL + Playwright），不含模型。限制：无响应式输出、无业务逻辑、检查循环较慢。面向使用 Claude Code 的前端开发者。

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

- 采集截图+DOM+计算样式，重建后逐像素 diff 评分
- 双目标输出：静态 page.html 与 shadcn/ui React 组件
- 纯 Python 评分器（PIL+Playwright），循环至所有区域达标
- 跨多屏采集共享设计系统（tokens、字体、图标）

## 适用场景

- 从线上页面提取真实的设计系统（色阶、字阶、间距）
- 复刻界面并用客观测量结果验证还原度
- 将页面悬停/聚焦/对话框状态转为带行为的 React 组件

## 场景标签

`编码 Agent` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: A Chrome extension captures a live site's screenshot, DOM, and computed styles. A Claude Code plugin rebuilds the pa
> L95: `clone` is a Claude Code plugin. Install it from this repo's marketplace:
> L63: - **A real oracle, not eyeballing.** The clone renders in headless Chromium at the capture's exact DPR, is cropped 

## 星数曲线

```mermaid
xychart-beta
    title "HarKro753/claude-copy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8d21d67c527b` · [字段定义](../../DATASET.md)*
