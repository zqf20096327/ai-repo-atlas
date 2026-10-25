# loquix-dev/loquix

⭐ 42 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/loquix-dev/loquix) · [官网](https://loquix.dev) · 组织维护

**构建 AI/LLM 聊天界面的框架无关 Web Components 组件库**

基于 Lit 3.x 与 TypeScript 严格模式构建的 Web Components UI 库，提供 50+ 组件覆盖 AI 聊天界面：消息列表、流式指示器、模型选择器、文件上传、引用、推理展示、工具调用时间线、参数面板与智能搜索（RAG 场景）等。组件以标准自定义元素（loquix- 前缀）交付，可在 vanilla/React/Vue/Svelte/Angular 中使用，支持 100+ CSS 自定义属性主题化、WCAG 2.1 AA 目标与可插拔国际化。通过 npm 安装或 CDN 引入，附 Storybook 浏览组件。库本身不接入模型，交互经类型化自定义事件交由应用处理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 50+ 生产就绪组件，覆盖消息、流式、附件、引用、工具调用、智能搜索
- 标准 Web Components，任意框架或无框架环境可直接使用
- 100+ CSS 自定义属性主题化，内置明暗主题与 ::part() 深度样式
- WCAG 2.1 AA 为目标，axe-core 检查与键盘/ARIA/焦点管理内建

## 适用场景

- 为 AI 产品快速搭建聊天界面而不用从零实现消息气泡与流式指示器
- 在 React/Vue/Svelte 等任意技术栈中嵌入可组合的聊天 UI 组件
- 构建带引用、来源过滤与生成回答的 RAG 搜索界面

## 场景标签

 · 领域:前端/AI 界面组件

## 证据(README 行号)

> L10: A framework-agnostic UI kit of 50+ production-ready components for building AI and LLM chat interfaces. Built with 
> L22: The component library is the foundation. The long-term vision is a full ecosystem for building AI agents: additiona

## 星数曲线

```mermaid
xychart-beta
    title "loquix-dev/loquix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cefcea2c89fb` · [字段定义](../../DATASET.md)*
