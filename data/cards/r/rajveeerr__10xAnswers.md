# rajveeerr/10xAnswers

⭐ 15 · JavaScript · 推送 2026-10-02 · [GitHub](https://github.com/rajveeerr/10xAnswers) · [官网](https://10x-answers.vercel.app/) · 个人维护

**给网站访客提供 AI 问答的可嵌入 React 聊天组件**

基于 React 与 Recoil 构建的可定制、可拖拽聊天机器人组件：传入人设 prompt 与后端 URL 即可在项目中嵌入 AI 问答，响应支持 Markdown（含代码块与表格高亮），用户可编辑提问与复制回答，样式通过 props 与 Tailwind 类配置。后端可自建或使用作者托管的代理服务以在服务端保管模型 key；也可直接传入 Gemini API key 前端直连（README 标注不推荐，因 key 会暴露）。v1.1.14 及更早版本因依赖 Recoil 而与 React 19 不兼容，官方建议使用 React 18，状态管理正迁移至 Zustand。以 npm 包形式安装。

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

- 配置 prompt 与 backendUrl 即可嵌入 AI 聊天窗，支持自建或托管后端
- 响应渲染 Markdown（代码块、表格），提问可编辑、回答可复制
- 托管代理将模型 API key 保留在服务端；亦支持 Gemini key 前端直连（不推荐）
- 样式与位置可定制：内联样式、Tailwind 类名、可拖拽与初始坐标

## 适用场景

- 给自己的网站快速加一个 AI 问答窗口
- 通过自定义 prompt 控制聊天机器人的人设与回答行为
- 不想自建后端时使用托管的代理服务调用模型

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: 10xAnswers is an easy-to-integrate, fully customizable, and draggable chatbot component built with React and Recoil.
> L5: With 10xAnswers, you get both the frontend component and a backend solution, streamlining the process of adding a ch
> L191: If you don't have a working backend you can directly use Google's Gemini API and pass it in the props, and send re

## 星数曲线

```mermaid
xychart-beta
    title "rajveeerr/10xAnswers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ba14d077200d` · [字段定义](../../DATASET.md)*
