# yaniv-golan/pretext-skill

⭐ 15 · HTML · MIT · 推送 2026-07-14 · [GitHub](https://github.com/yaniv-golan/pretext-skill) · 个人维护

**教 AI agent 正确使用 pretext 文本测量库的 Agent Skill**

基于开放 Agent Skills 标准的技能包，内容为教 AI 助手正确使用 @chenglou/pretext——一个通过 CanvasRenderingContext2D.measureText 测量文本、无需 DOM reflow 的 TypeScript 库。技能覆盖 13 个核心函数与 5 个 rich-inline 函数的 API 用法、参数顺序陷阱、集成与创意布局模式，以及不适用场景。可通过 zip 上传、插件市场、npx 等方式安装到 Claude Desktop/Code、Cursor、ChatGPT、Codex CLI、Windsurf 等 40+ 兼容 agent，触发词包括提及 pretext 或相关能力短语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 13 个核心函数与 5 个 rich-inline 函数的正确用法与陷阱
- 文档化集成模式：自适应字号、障碍物绕排、rich inline chips/mentions
- 明确列出不适用场景（CSS-only 方案、HTML 内容等）
- 支持 40+ 兼容 agent 的多种安装途径（zip/插件市场/npx）

## 适用场景

- 让我的 AI 编程助手在布局代码中正确调用 pretext API
- 虚拟滚动、瀑布流等需要预知文本尺寸的前端开发
- 实现聊天气泡内 @mention、code span 等 rich inline 渲染

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L13: An AI agent skill that helps developers use **@chenglou/pretext** — a small, tree-shakable TypeScript library that 
> L30: This skill teaches AI agents how to use pretext correctly:

## 星数曲线

```mermaid
xychart-beta
    title "yaniv-golan/pretext-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `aa193b71454f` · [字段定义](../../DATASET.md)*
