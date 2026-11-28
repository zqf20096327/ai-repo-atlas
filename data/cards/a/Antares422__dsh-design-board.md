# Antares422/dsh-design-board

⭐ 3 · HTML · MIT · 推送 2026-11-27 · [GitHub](https://github.com/Antares422/dsh-design-board) · 个人维护 · 中文 README

**为 DeepSeek Harness 提供设计画布插件，按内置设计体系生成可交互页面**

一个 DSH（DeepSeek Harness）插件，在右侧提供无限画布，将 Agent 生成的交互式 HTML 设计稿渲染为可视化页面。内置 165 套设计体系（含设计规范、CSS 变量表与参考组件），选定风格后 AI 按规范出稿；支持多方案并排对比、点选/框选 DOM 元素添加批注并回传给 Agent 原地修改、Play 模式真实交互、深浅主题切换、质量校验与会话隔离，可导出 PNG/PDF/单文件 HTML。通过 DSH 应用内插件安装或 CLI 安装，预构建产物无需本地编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 165 套设计体系，含规范、CSS 变量表与参考组件
- 画布内点选/框选元素并批注，选择器自动回传给 Agent 修改
- 支持多方案同屏对比、Play 交互模式与深浅主题
- 导出 PNG、多页 PDF 或单文件 HTML 画廊

## 适用场景

- 在对话中说需求，直接在画布上得到可交互的设计稿
- 用 Linear/Apple 等指定风格生成管理后台页面
- 多方案并排对比并点选元素原地改稿
- 导出设计稿为 PNG/PDF/HTML 分享

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L10: **给 DeepSeek Harness 装上一块设计画布。**
> L18: - **165 套内置设计体系**：涵盖 Apple、Linear、Airbnb、Stripe、Notion、Vercel 等风格，每套均包含设计规范、CSS 变量表与参考组件。在右上角预览并选用后，AI 即按该规范直接出稿；未指


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `4f81a7382357` · [字段定义](../../DATASET.md)*
