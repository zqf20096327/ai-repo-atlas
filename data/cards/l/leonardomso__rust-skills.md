# leonardomso/rust-skills

⭐ 615 · Python · MIT · 推送 2026-06-14 · [GitHub](https://github.com/leonardomso/rust-skills) · 个人维护

**给 AI 编码 agent 用的 265 条 Rust 规范规则集（26 类）**

面向 Claude Code、Cursor、Windsurf、Copilot、Codex、Aider、Zed、Amp、Cline 等支持 skills 的编码 agent 的规则集合：265 条 Rust 编码规则分 26 类（所有权与借用、错误处理、Unsafe、Async、性能等），每条含说明、正反代码示例与相关链接。SKILL.md 作为轻量索引，agent 按前缀按需加载相关规则以控制上下文成本；CLAUDE.md 与 AGENTS.md 为符号链接以兼容不同 agent 约定。通过 npx add-skill 安装，或对各类 agent 提供手动 git clone/curl 安装方式。内容为对官方文档、书籍与开源 crate 惯例的独立综合，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 265 条规则分 26 类，每条含正反代码示例
- SKILL.md 索引 + 前缀分组，agent 按需渐进加载规则
- 通过 npx add-skill 一键安装，自动识别已装的 agent
- 为 9 种以上编码 agent 提供手动安装方式

## 适用场景

- 让我的 AI 编码 agent 写出更地道的 Rust 代码
- 用 /rust-skills 命令让 agent 审查函数的错误处理或内存问题
- 在 Claude Code、Cursor、Copilot 等不同 agent 间共用同一套 Rust 规范

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: 265 Rust rules your AI coding agent can use to write better code. Current for Rust 1.96 (2024 edition).
> L10: Works with Claude Code, Cursor, Windsurf, Copilot, Codex, Aider, Zed, Amp, Cline, and pretty much any other agent t
> L110: - **`SKILL.md`** is a lightweight index — every rule listed as a one-line summary, grouped by category, with a lin

## 星数曲线

```mermaid
xychart-beta
    title "leonardomso/rust-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 599 --> 607
    line [600, 606, 606]
```

2026-10-18 600 → 2026-10-21 606（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `88051848bff1` · [字段定义](../../DATASET.md)*
