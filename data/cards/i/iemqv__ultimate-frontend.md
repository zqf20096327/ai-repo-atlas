# iemqv/ultimate-frontend

⭐ 4 · Rust · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/iemqv/ultimate-frontend) · [官网](https://www.npmjs.com/package/ultimate-frontend) · 个人维护

**给编码 agent 装的前端技能：设计、修 UI、验证可用性**

以 npm 包形式分发的单一 agent skill，面向使用 Codex、Claude Code、Cursor、GitHub Copilot、Gemini CLI、OpenCode、Pi 等编码 agent 的用户。安装后 agent 可按用户描述的任务调用该技能，区分新建站点、局部修复、对照 mockup 审查三类工作方式；技能声明遵循项目已有设计系统与 mockup，并区分浏览器中实际验证的内容与仅代码检查的内容。浏览器本地验证引擎为可选组件，不随 npm install 一起安装。安装需 Node.js 20 及以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 skill 供多个编码 agent 调用（支持 7 种 agent）
- 按任务类型选择做法：新建设计、局部修复、只审查不改代码
- 区分浏览器实际验证与仅代码检查
- 本地验证引擎为可选，不包含在 npm install 内

## 适用场景

- 让 agent 从 brief 构建作品集类网站
- 让 agent 修复现有页面的键盘可操作性并保留布局
- 让 agent 对照已批准的 mockup 审查结账流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: One skill for coding agents that design, build, and review web interfaces. Give your agent a brief, a mockup, or a b
> L11: Choose your agent and reload it. Requires Node.js 20 or later. Supports Codex, Claude Code, Cursor, GitHub Copilot,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `f08e0e8552cc` · [字段定义](../../DATASET.md)*
