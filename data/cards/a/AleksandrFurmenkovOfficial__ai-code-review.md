# AleksandrFurmenkovOfficial/ai-code-review

⭐ 36 · JavaScript · MIT · 推送 2026-10-02 · [GitHub](https://github.com/AleksandrFurmenkovOfficial/ai-code-review) · 个人维护

**面向开发者的 GitHub Action：用多家 AI 模型自动审查 PR 代码**

一个 GitHub Action，在 pull request 上自动执行代码审查：调用 OpenAI、Anthropic、Google、X、Deepseek 或 Perplexity 的模型分析变更代码并给出反馈。支持按文件扩展名和目录路径做包含/排除过滤，可通过仓库内文件注入自定义审查规则到 AI 系统提示词，可配置审查失败时是否使 Action 失败。每个 provider 需对应 API key 与可选模型名，README 给出六种 provider 的 workflow 示例及超时、上下文超限的排查建议。以 workflow YAML 配置方式使用，无需本地编译。

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

- 支持 6 家 AI provider（OpenAI/Anthropic/Google/X/Deepseek/Perplexity）
- 按扩展名与路径过滤审查范围
- 自定义审查规则文件注入 AI 系统提示词
- 提供各 provider 的 workflow 配置示例

## 适用场景

- CI/CD 流水线中自动审查 pull request
- 团队按指定文件类型和路径范围做 AI 代码审查
- 通过自定义规则文件约束 AI 审查标准

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L6: Perform code review using various AI models from OpenAI, Anthropic, Google, X, Deepseek or Perplexity to analyze and
> L18: ***ai_provider*** - Required. The AI provider to use { openai, anthropic, google, x, deepseek}. Default is 'openai'

## 星数曲线

```mermaid
xychart-beta
    title "AleksandrFurmenkovOfficial/ai-code-review 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4e62ce7b8450` · [字段定义](../../DATASET.md)*
