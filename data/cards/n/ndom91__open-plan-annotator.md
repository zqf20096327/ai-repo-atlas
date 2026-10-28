# ndom91/open-plan-annotator

⭐ 98 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/ndom91/open-plan-annotator) · 个人维护

**本地优先的编码 agent 计划标注插件：拦截计划模式并在浏览器中批注**

面向使用编码 agent（Claude Code、OpenCode、pi）的开发者的插件：当 agent 产出计划时，插件在本地启动临时 HTTP 服务并在浏览器打开 React 标注界面，用户可对计划做删除线、替换、插入或评论，批准放行或将结构化反馈发回 agent 修订，循环直至满意。通过各宿主插件机制或全局 npm/bun 安装，提供 CLI 直接审阅磁盘上的 Markdown 计划；全部本地运行，支持通过 skip 文件回退到原生批准流程。

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

- 拦截 Claude Code ExitPlanMode 钩子自动打开浏览器标注 UI
- 删除线/替换/插入/评论四类标注并结构化回传 agent
- 支持 Claude Code、OpenCode、pi 三种宿主及独立 CLI（review / doctor / agent-setup）
- 完全本地运行，可通过 OPEN_PLAN_ANNOTATOR_SKIP_FILE 切回原生批准

## 适用场景

- 在编码 agent 执行前逐段审阅并修改其计划
- 把对计划的意见以结构化反馈发回 agent 迭代修订
- 无原生插件支持的 agent 用 CLI 直接审阅 Markdown 计划文件

## 场景标签

 · 领域:开发者工具/编码 agent 插件

## 证据(README 行号)

> L7: A fully local agentic coding plugin that intercepts plan mode and opens an annotation UI in your browser. Mark up th
> L13: 1. Your coding agent (Claude Code, OpenCode, and pi) finishes writing a plan

## 星数曲线

```mermaid
xychart-beta
    title "ndom91/open-plan-annotator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 96 --> 99
    line [97, 98, 98]
```

2026-10-18 97 → 2026-10-28 98（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7e018e64719b` · [字段定义](../../DATASET.md)*
