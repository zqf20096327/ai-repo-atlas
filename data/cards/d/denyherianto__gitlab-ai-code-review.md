# denyherianto/gitlab-ai-code-review

⭐ 20 · TypeScript · MIT · 推送 2026-02-16 · [GitHub](https://github.com/denyherianto/gitlab-ai-code-review) · 个人维护

**面向 GitLab CI 的 Gemini AI 代码评审工具，在 MR 上发布分级评论**

名为 Niteni 的 AI 代码评审工具，接入 GitLab CI 流水线：读取合并请求 diff，通过 Gemini REST API（结构化输出 responseSchema）生成含严重级别、文件、行号、描述、建议及理由的 JSON 评审结果，并以行内评论形式发布到 MR，支持一键 Apply suggestion。提供 4 级严重度分类、文件过滤、diff 大小限制，以及 CRITICAL 发现时可选使流水线失败。通过环境变量配置，以 GitLab CI 作业形式集成，需 GEMINI_API_KEY 与 GITLAB_TOKEN。附 Vibecoding Prompt 供 AI 编码工具辅助集成。

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

- 通过 Gemini REST API 结构化输出直接获得类型化 JSON 评审结果
- 评审发现以行内 diff 评论形式发布，附 GitLab 一键应用建议块
- 4 级严重度分类（CRITICAL/HIGH/MEDIUM/LOW），可选 CRITICAL 时使流水线失败
- 支持 include/exclude 文件过滤与 diff 大小限制以控制 token 用量

## 适用场景

- 在 GitLab MR 流水线中自动生成 AI 代码评审评论
- 按严重级别过滤代码问题并在 CRITICAL 时阻断流水线
- 通过一键建议块快速应用修复

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: AI-powered code review for GitLab CI pipelines, powered by the Gemini REST API.
> L7: Analyzes code changes via the Gemini API with structured output, then posts severity-classified findings as GitLab M
> L11: Niteni calls the **Gemini REST API** with structured output (`responseSchema` + `responseMimeType: "application/jso

## 星数曲线

```mermaid
xychart-beta
    title "denyherianto/gitlab-ai-code-review 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `516f48dcdeb7` · [字段定义](../../DATASET.md)*
