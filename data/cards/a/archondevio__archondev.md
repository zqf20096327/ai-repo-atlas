# archondevio/archondev

⭐ 165 · MIT · 推送 2026-07-08 · [GitHub](https://github.com/archondevio/archondev) · [官网](https://archondev.io) · 个人维护

**治理 AI 助手代码的本地 CLI：架构约束与质量门禁**

面向使用 AI 编码助手的开发者的治理工具：读取项目架构文件约束每次变更，对每个 diff 运行质量门禁，跟踪文件依赖以防重构破坏调用方，并提供 0-100 风险评分、ship 发布流水线（review→test→version→PR）、视觉 QA、会话回顾等命令。免费、本地优先、BYOK（API 密钥本地 AES-256-GCM 加密存储）。以 npm 安装的 CLI 提供，也可作为 Lite 规则文件集成到 Cursor、Claude Code、Windsurf、VS Code + Copilot 等工具。远程登录/云执行路径已停用。

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

- 变更前读取架构文件并对每个 diff 运行质量门禁
- 文件级依赖跟踪与下游影响检查（deps check/graph）
- BYOK 多供应商密钥，本地加密存储（AES-256-GCM，0600 权限）
- Lite 包含 29 个按需加载的 AI 技能与 Claude Code 21 个斜杠命令

## 适用场景

- 约束 Cursor/Claude Code 等 AI 编码助手遵守项目架构规范
- 在 AI 写入代码前拦截低质量或不合规变更
- 跟踪文件依赖避免重构时破坏调用方
- 通过 ship 流水线完成审查、测试、版本与 PR

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: **Govern AI code with local-first quality gates.**
> L5: Development governance for code written by AI coding assistants. Reads your architecture file before any change, run
> L148: |**Download / Governance**|$0|Governance/workflow layer with no built-in AI calls|

## 星数曲线

```mermaid
xychart-beta
    title "archondevio/archondev 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 163 --> 166
    line [164, 165, 165]
```

2026-10-18 164 → 2026-10-30 165（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c0e3228427f7` · [字段定义](../../DATASET.md)*
