# crussella0129/Animus_GECK

⭐ 18 · Rust · GPL-3.0 · 推送 2026-07-22 · [GitHub](https://github.com/crussella0129/Animus_GECK) · 个人维护

**为 Animus Sprint Loops 生成项目启动文档的 Sprint 0 向导**

Rust 编写的单二进制向导式工具，用于软件项目启动（Sprint 0）阶段：交互式向导收集项目名称、目标、成功标准、语言、平台等约 15 类字段，生成 mission-spec.md（含机器可读 YAML frontmatter 的任务规格文档）与 launch-prompt.md（粘贴到 Claude Code、Codex CLI 或开放 harness 的启动提示词），并按 Sprint Loops 自身的 schema 确定性、幂等地种子化 decisions.md、agent-tasks/ 与 confidence.txt。内建 21 种项目形态 profile；安装需 git clone 后 cargo build，要求 Rust 1.75+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成 mission-spec.md 与 launch-prompt.md 两个启动工件
- 以幂等方式种子化 Sprint Loops 状态文件（decisions.md/agent-tasks/confidence.txt）
- 交互式向导覆盖约 15 个配置节，21 种内建项目 profile
- geck prompt 可从既有 spec 重渲染提示词并可切换目标 harness

## 适用场景

- 启动软件项目时用向导一次成型地写下任务规格与启动提示词
- 让 AI 编码 agent 的 Sprint 0 按完整任务上下文运行
- 跨会话保持项目使命基线，供后续 sprint 对比漂移

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L11: - **`launch-prompt.md`** — the complete instructional prompt you paste into
> L12:  Claude Code, Codex CLI, or an open harness to start Sprint 0 correctly,
> L119: GECK is a **launcher**, not an adapter. Animus Sprint Loops

## 星数曲线

```mermaid
xychart-beta
    title "crussella0129/Animus_GECK 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [19, 18, 18]
```

2026-10-18 19 → 2026-10-29 18（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `bccc2da3020f` · [字段定义](../../DATASET.md)*
