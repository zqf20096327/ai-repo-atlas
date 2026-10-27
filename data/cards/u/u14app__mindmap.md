# u14app/mindmap

⭐ 22 · TypeScript · NOASSERTION · 推送 2026-09-15 · [GitHub](https://github.com/u14app/mindmap) · [官网](https://mindmap.u14.app) · 个人维护 · 中文 README

**支持 AI 流式输出的 React 思维导图组件库**

模块化的 React + TypeScript 思维导图运行时，提供 headless 核心（解析、布局、补丁、流式处理）、静态 SVG、只读查看与编辑四个入口，以及可选的 Features（历史、搜索、导入导出、AI 等）与语法扩展（LaTeX 等）。解析器支持类 Markdown 树形语法，含任务状态、备注、折叠、跨链接等。AI Feature 接受宿主提供的同步或流式 Markdown 生成器，凭据需留在服务端代理。v0.9.0 为破坏性接口升级，未发布基准数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- core 入口独立于 React 与浏览器渲染，提供 headless 解析/布局/流式 API
- AI Feature 接受异步迭代 Markdown 块的宿主生成器，支持流式预览与事务提交/回滚
- 类 Markdown 语法：任务、备注、折叠、标签、跨链接、可选 LaTeX
- 输入边界硬限制（1,000,000 UTF-16 单元、20,000 节点、256 层嵌套）与远程图片默认拒绝

## 适用场景

- 在 React 应用中嵌入可编辑的思维导图编辑器
- 接入 AI 模型流式生成 Markdown 并实时渲染为思维导图
- 以 headless 核心在无浏览器环境做解析、布局与序列化
- 以只读查看器或静态 SVG 呈现导图内容

## 场景标签

 · 领域:前端可视化组件

## 证据(README 行号)

> L6: Open MindMap is a modular React and TypeScript runtime for interactive SVG mind maps. Version 0.9.0 separates the he
> L97: The AI Feature accepts a host generator that returns complete Markdown or an async iterable of Markdown chunks. The

## 星数曲线

```mermaid
xychart-beta
    title "u14app/mindmap 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-27 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e5a250e7a5b1` · [字段定义](../../DATASET.md)*
