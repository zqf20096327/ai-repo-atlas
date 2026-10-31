# inspecto-dev/inspecto

⭐ 22 · TypeScript · MIT · 推送 2026-09-04 · [GitHub](https://github.com/inspecto-dev/inspecto) · [官网](https://inspecto-dev.github.io/inspecto/) · 组织维护 · 中文 README

**前端调试工具：点击页面组件直达源码并把上下文交给 AI 处理**

浏览器与编辑器/AI 助手之间的桥接工具：点击浏览器中的组件用 Alt+Click 跳转到对应源码位置，Inspect 模式把组件上下文交给 AI 助手，Annotate 模式收集 UI 标注、创建 MCP agent 任务并在侧边栏跟踪进度；支持通过 .inspecto/prompts.json 定义自定义工作流按钮。以 npm 包（plugin/core/cli）提供，一条 npx 命令可安装 Copilot、Cursor、Trae、CodeBuddy 等编辑器集成，也支持无 IDE 的独立 MCP 模式。

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

- 点击组件即跳转源码位置（Alt+Click）
- Inspect/Annotate 模式把 UI 上下文交给 AI 助手处理
- Annotate 模式可创建 MCP agent 任务并跟踪进度与回复时间线
- 一条 npx 命令安装多种编辑器/AI 助手集成

## 适用场景

- 调试前端页面时快速定位组件源码
- 把页面上的 UI 问题连同上下文交给 AI 助手修复
- 以 MCP 模式让 agent 批量处理标注任务并跟踪进度

## 场景标签

 · 领域:开发者工具/前端调试

## 证据(README 行号)

> L10: > Click UI, jump to source, and let AI fix it or run your custom workflow with the exact frontend context.
> L53: - Only want source jump without AI: see the Installation Guide

## 星数曲线

```mermaid
xychart-beta
    title "inspecto-dev/inspecto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `90471ca5a486` · [字段定义](../../DATASET.md)*
