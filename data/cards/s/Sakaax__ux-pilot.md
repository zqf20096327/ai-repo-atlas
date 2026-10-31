# Sakaax/ux-pilot

⭐ 21 · TypeScript · MIT · 推送 2026-04-02 · [GitHub](https://github.com/Sakaax/ux-pilot) · [官网](https://ux-pilot.sakaax.com/) · 个人维护

**Claude Code 的 UX 设计插件：376 条规则驱动从需求到验证流**

面向 Claude Code 的 UX 设计技能插件：以对话式 Discovery 流程先梳理产品、用户与目标，生成持久化 UX Brief；再按需加载 376 条源自 WCAG 2.1、Nielsen Norman Group 与 Laws of UX 的规则，对现有前端代码做扫描审计（检测框架含 Next.js/React/Vue/Svelte，输出带评分的 HTML 报告与自然语言修复提示）；随后启动本地预览服务器生成多个命名版本页面并支持热重载，最终导出 UX 规格与 React/Svelte/Vue 组件。可选接入 Playwright MCP 做截图视觉审计，未安装时回退为静态 CSS 分析。规则内置 Anti "AI slop" 约束（禁用 Inter/Roboto 等字体、紫色渐变等）。以 TypeScript 编写，运行时为 Bun（可回退 Node.js）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 376 条 UX 规则按屏幕类型按需加载（6 类：UX Patterns、Conversion、SEO/AEO、Psychology、Aesthetics、Product Type）
- 四阶段流程：Discovery→Audit→Preview→Export，输出持久化 ux-brief.md
- 本地预览服务器 + SSE 热重载，每屏生成 2-3 个命名版本
- 可选 Playwright MCP 截图视觉审计（375/768/1280px），回退静态 CSS 分析

## 适用场景

- 在 Claude Code 中以结构化流程设计前端界面而非直接生成代码
- 对现有前端项目做 UX/可访问性/SEO 审计并按提示修复
- 生成多个风格化界面方案并在本地预览中迭代验证
- 将确认后的界面导出为 React/Svelte/Vue 组件

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L16: A Claude Code plugin that acts as a **senior UX designer**. It doesn't generate code blindly — it understands your 
> L56: Instead of jumping straight to code, it runs a **structured discovery flow** — asks about your product, users, and 

## 星数曲线

```mermaid
xychart-beta
    title "Sakaax/ux-pilot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `18d794801c1f` · [字段定义](../../DATASET.md)*
