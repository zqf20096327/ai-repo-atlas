# howardpen9/kimi-code-reviewer

⭐ 10 · TypeScript · MIT · 推送 2026-06-08 · [GitHub](https://github.com/howardpen9/kimi-code-reviewer) · 个人维护 · 中文 README

**用 Kimi 大模型为 GitHub PR 生成代码审查的 Action**

以 GitHub Action 与自托管 GitHub App 两种形式运行的 PR 代码审查工具：调用 Moonshot Kimi API，利用 256K 上下文窗口读取 PR 全量文件内容而非仅 diff，按 PR 大小采用 Full/Mixed/Chunked 三种上下文打包策略。审查结果以行内标注形式写入 PR diff，输出 0–100 质量分、critical/warning/suggestion/nitpick 四级严重度，可按阈值使 CI 失败；支持 .kimi-review.yml 按仓库配置规则、文件过滤与五种语言的审查意见。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 256K 上下文按 PR 大小自动选择 Full/Mixed/Chunked 打包策略
- 行内标注写入 PR diff，输出 0–100 质量分与四级严重度
- 自托管 GitHub App 支持 @kimi review 评论触发
- .kimi-review.yml 按仓库自定义规则，审查意见支持五种语言

## 适用场景

- 给 GitHub 仓库的每个 PR 自动跑 AI 代码审查
- 在 PR 评论里 @kimi 触发一次完整审查
- 按仓库自定义审查规则与严重度阈值控制合并

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3:  AI-powered code review for GitHub using Moonshot Kimi with 256K context window
> L17: - **256K Context Window** — Reviews entire PRs with full file context, not just diffs
> L154: PR Event → Extract Context → Pack (256K) → Kimi API → Parse → Annotations


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `f89e1ec5ce45` · [字段定义](../../DATASET.md)*
