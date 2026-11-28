# wzc520pyfm/open-intelligent-ui

⭐ 4 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/wzc520pyfm/open-intelligent-ui) · [官网](https://open-intelligent-ui.pages.dev) · 个人维护

**让模型基于 UI SDK 与 DESIGN.md 直接生成界面的 React/Vue 渲染框架**

提供一套 IUI 标记语言与多框架渲染器：模型流式输出 MDX 风格标记，渲染器将其转为实时界面，行为由 UI SDK 的 55 个入口组件提供，外观由 DESIGN.md 设计令牌驱动（parseDesign/designToCss 转为 CSS 变量，文案进入系统提示）。提供 buildSystemPrompt、checkMarkup 与 repairMessage 组成的校验与自动修复回路，支持 React/Vue/Svelte/Solid/Web Components 五种渲染目标，npm 包形式分发，并附带面向编码 agent 的 SKILL.md。

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

- 模型书写 IUI 标记，渲染器流式生成界面，无需组件目录
- DESIGN.md 令牌同时驱动 CSS 与系统提示，换文件即换主题
- checkMarkup + repairMessage 在服务端校验并自动修复回复
- 同一标记适配 React/Vue/Svelte/Solid/Web Components 五种渲染器

## 适用场景

- 让 LLM 应用在对话中动态生成带状态与工具调用的界面
- 为 agent 产品搭建模型输出 UI 的渲染与校验管线
- 在多个前端框架中复用同一套模型生成的界面标记

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L9: The model writes MDX-like markup; the renderer turns that stream into a live interface. UI SDK gives the behavior of
> L22: This project separates the two. UI SDK supplies behavior only, and the model decides the shape with layout, SVG and
> L100: There is a renderer for each framework UI SDK supports. Each takes the same props, and each is installed with the 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `738ba4b42b9b` · [字段定义](../../DATASET.md)*
