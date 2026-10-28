# buzinas/react-trace

⭐ 114 · TypeScript · MIT · 推送 2026-09-25 · [GitHub](https://github.com/buzinas/react-trace) · [官网](http://react-trace.js.org/) · 个人维护

**React 开发期组件检查器：定位组件源码并联动编辑器与 AI 代理**

面向 React 开发者的开发时组件检查器：在页面上识别已渲染组件，定位其源码位置，支持在编辑器中打开对应文件的具体行、基于 Monaco 的浏览器内源码预览与行内编辑、添加注释并复制粘贴给 AI 代理，或发送到 OpenCode 会话。以 pnpm 安装的 npm 包形式提供（推荐 @react-trace/kit 全家桶，或 @react-trace/core 自选插件），提供插件脚手架 CLI（pnpm create react-trace-plugin），要求 react/react-dom >= 18 作为 peer 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 识别渲染组件并定位源码行，可在本地编辑器中打开
- Monaco 源码预览与可选行内编辑
- 注释收集后复制给 AI 代理或发送到 OpenCode 会话
- 插件化架构与官方脚手架 CLI（pnpm create react-trace-plugin）

## 适用场景

- 开发时在浏览器中快速定位 React 组件的源码定义
- 把组件源码片段与注释交给 AI 代理或 OpenCode 处理
- 在浏览器内直接预览并小改组件代码
- 为检查器编写自定义插件扩展功能

## 场景标签

 · 领域:前端开发工具

## 证据(README 行号)

> L3: A development-time React inspector for your components.
> L11: - Add comments and then copy & paste to your AI agents
> L12: - Or even send them to your session on OpenCode for a seamless review experience

## 星数曲线

```mermaid
xychart-beta
    title "buzinas/react-trace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-28 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `67266ff3e157` · [字段定义](../../DATASET.md)*
