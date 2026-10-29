# skovtun/coherent-design-method

⭐ 21 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/skovtun/coherent-design-method) · [官网](https://getcoherent.design) · 个人维护

**治理 AI 编码 agent 前端编辑的验证层：圈定范围、浏览器验证、回滚**

面向使用编码 agent 构建 Next.js 前端的开发者：agent 声明编辑范围后，Coherent 基于 TypeScript AST 构建代码图谱并给出影响分析，随后在真实浏览器中执行类型检查（对照基线）、生产构建、桌面/移动截图与像素 diff、水合与身份泄漏检测，输出 verified/failed 等判定；失败编辑不提交并默认回滚。以 npm CLI 与 MCP server 形式提供，需 Node.js 20+ 与 Claude Code 或 Codex。自 v0.27.0 起不再自行生成设计，旧的生成管线（coherent chat 等）已声明弃用，将于未来版本移除。

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

- TypeScript AST 构建应用代码图谱（页面/布局/共享组件/导入关系）
- 编辑前声明范围并返回必须改变/不得改变的路由影响
- 真实浏览器验证：截图、像素 diff、生产构建、水合错误与身份泄漏检测
- 失败编辑不提交，回滚仅触及该编辑自身文件

## 适用场景

- 让 Claude Code/Codex 修改 UI 时自动核验编辑未越界
- 防止共享组件改动波及其他页面（像素 diff 控制路由）
- agent 编辑失败时自动回滚且保留并发的人工修改

## 场景标签

 · 领域:前端开发工具/AI agent 治理

## 证据(README 行号)

> L4:  An open-source platform that governs AI-built frontends: your coding agent designs and builds the UI;
> L18: 1. **Inventory.** A graph of your app built from the code itself (TypeScript AST): pages, layouts, shared component
> L62:       ──► (agent writes files)    PreToolUse hook denies writes outside the write set

## 星数曲线

```mermaid
xychart-beta
    title "skovtun/coherent-design-method 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `96da62a75166` · [字段定义](../../DATASET.md)*
