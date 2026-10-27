# tarmojussila/zai-code-review

⭐ 43 · JavaScript · MIT · 推送 2026-09-16 · [GitHub](https://github.com/tarmojussila/zai-code-review) · 个人维护

**用 Z.ai 模型在 GitHub Actions 中自动审查 PR 的 Action**

一个 GitHub Action：在 Pull Request 上调用 Z.ai 模型（默认 glm-4.7）生成代码审查评论，覆盖缺陷检测与改进建议。使用时需在仓库 Secrets 中配置 ZAI_API_KEY，可自定义模型、系统提示词、审查者名称，支持排除文件模式（默认各类 lock 文件）与限制发送到 API 的 diff 字符数；模型/提示词等参数也可改为 GitHub Actions 变量管理，无需改动 workflow 文件。面向使用 GitHub 仓库的开发者与团队，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 GitHub Action 形式在 PR 上生成 AI 审查评论
- 默认使用 glm-4.7，可切换其他 Z.ai 模型
- 可自定义系统提示词与审查者名称
- 支持排除文件模式与 diff 字符数上限

## 适用场景

- 在 CI 流水线中自动获得 PR 的 AI 代码审查评论
- 用安全导向的提示词聚焦漏洞与不安全模式检查
- 通过 Actions 变量在不改 workflow 的情况下切换模型与提示词

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: AI-powered GitHub Pull Request code review using Z.ai models. Automatic PR comments, bug detection, and improvement 
> L28: |`ZAI_MODEL`|No|`glm-4.7`|Z.ai model to use for review|

## 星数曲线

```mermaid
xychart-beta
    title "tarmojussila/zai-code-review 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `221418f4e5e1` · [字段定义](../../DATASET.md)*
