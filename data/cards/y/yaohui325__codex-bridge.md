# yaohui325/codex-bridge

⭐ 49 · Shell · MIT · 推送 2026-08-11 · [GitHub](https://github.com/yaohui325/codex-bridge) · 个人维护 · 中文 README

**把 Claude Code 桥接到 Codex CLI 的 skill：外化上下文并机械校验响应**

一个 Claude Code skill，用于在 Claude Code 中显式调用 Codex CLI：调用前把对话上下文、plan、相关文件、项目约定（CLAUDE.md/AGENTS.md）打包成磁盘 bundle，运行 codex exec 取回结构化 JSON 响应，由 Claude Code 用 jq 后处理校验。提供 plan-review、codify、review-iteration、verification-round 四个场景及对应的 sandbox 设置。通过 git clone + install.sh 安装，依赖 jq、bash 4+ 和 codex CLI；脚本含 macOS 专属 stat -f 用法，Linux 兼容性列为 v1.3 候选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 把对话上下文/plan/文件/约定外化为磁盘 bundle 后再调用 codex exec
- 响应 JSON 由 jq 后处理机械校验，不使用 --output-schema
- 4 个场景（plan-review/codify/review-iteration/verification-round）各带 sandbox 与模板
- 12+2 步强制工作流与 bundle 可复盘的目录约定

## 适用场景

- 让 Codex 审计我的 plan 或设计并结构化返回 finding
- 把会话中 ruled-out 的方案与隐性信息带入 Codex 调用
- 用 Codex 执行写码任务并机械校验其响应 schema

## 场景标签

`代码审查` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: > 显式触发的 **Claude Code → Codex CLI 桥接 skill**。把对话上下文 / plan / 相关文件 / 项目约定外化为 bundle 目录，调 `codex exec` 拿回结构化 JSON 响应 +
> L16: 本 skill 把"显性外化上下文"变成**强制工作流**——Claude Code 调 Codex 前必须先把所有相关信息打包成一个磁盘 bundle，调 `codex exec` 拿回结构化 JSON 响应。
> L43: git clone <this-repo-url> /tmp/codex-bridge

## 星数曲线

```mermaid
xychart-beta
    title "yaohui325/codex-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-27 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f1e9859b5d16` · [字段定义](../../DATASET.md)*
