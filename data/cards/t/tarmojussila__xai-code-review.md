# tarmojussila/xai-code-review

⭐ 18 · JavaScript · MIT · 推送 2026-09-16 · [GitHub](https://github.com/tarmojussila/xai-code-review) · 个人维护

**用 xAI Grok 模型自动审查 GitHub PR 的 Action**

GitHub Action 形式的 PR 代码审查工具：在 CI 流程中调用 xAI Grok 模型，对 Pull Request 的代码改动生成 PR 评论，包括 bug 检测与改进建议。配置项涵盖模型选择（默认 grok-3）、可覆盖的系统提示词、审查者名称、排除文件模式（默认各类 lock 文件）与 diff 字符上限；API key 通过 GitHub Secrets 注入，模型等参数也可改为仓库变量管理，无需改工作流文件即可更新。面向使用 GitHub Actions 的开发者，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 GitHub Actions 中自动调用 xAI Grok 生成 PR 审查评论
- 默认排除 lock 文件，支持自定义排除模式与 diff 长度上限
- 系统提示词可覆盖（如聚焦安全审查）
- 模型/提示词/审查者名可经 Actions 变量管理，免改工作流

## 适用场景

- 让 AI 在 PR 中自动指出 bug 与改进点
- 以安全为导向定制提示词做 PR 安全审查
- 团队 CI 流程中统一接入 AI 代码审查

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: AI-powered GitHub Pull Request code review using xAI Grok models. Automatic PR comments, bug detection, and improvem
> L7: - 🚀 Detect bugs
> L9: - 🧠 AI-driven PR feedback

## 星数曲线

```mermaid
xychart-beta
    title "tarmojussila/xai-code-review 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e87423c4eb65` · [字段定义](../../DATASET.md)*
