# Arunachalamkalimuthu/merlin-ai-code-review

⭐ 19 · Rust · MIT · 推送 2026-08-07 · [GitHub](https://github.com/Arunachalamkalimuthu/merlin-ai-code-review) · [官网](https://merlin-review.com/) · 个人维护

**自托管的 AI 代码审查工具：在 CI 中审查 PR 并内联评论**

用 Rust 编写的自托管 CLI/服务，嵌入 CI 流水线运行：读取 pull request diff，调用用户自选的 12 家 AI 提供商（BYOK，含本地 Ollama）生成审查意见，以平台内置 bot 身份在 PR 上发布内联评论，代码不离开自有基础设施。支持 GitHub/GitLab/Bitbucket/Azure DevOps/Gitea 五个平台（CI 环境自动检测），并提供 22 个斜杠命令、自定义规则引擎、RAG 代码库索引、安全扫描、二遍复核过滤误报等能力。限制：需要一个 AI 提供商凭据；GitHub 需配置 permissions 块否则 403。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 家 AI 提供商 BYOK 接入（含本地 Ollama，无 API key）
- 5 个 git 平台支持，bot 身份用 CI 内置 token 自动化
- 自定义规则引擎 .merlin-rules.yaml 与 👍/👎 反馈降噪学习
- RAG 代码库索引与 Reflect & Review 二遍复核过滤误报

## 适用场景

- 在 CI 中自动审查 PR 并发内联评论
- 私有化部署 AI 代码审查，代码不离开自有基础设施
- 按团队规则（正则/自然语言/路径范围）定制审查行为
- 用本地 Ollama 做完全私密的代码审查

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L12: **Self-hosted AI code review for GitHub, GitLab, Bitbucket, Azure DevOps, and Gitea.**
> L14: Merlin runs inside your CI pipeline, reviews pull request diffs with the AI provider of your choice, and posts inli
> L29: |**AI providers**|Anthropic Claude, OpenAI, Google Gemini, AWS Bedrock, Azure OpenAI, Groq, Together AI, DeepSeek, 

## 星数曲线

```mermaid
xychart-beta
    title "Arunachalamkalimuthu/merlin-ai-code-review 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5f0e2e8162a1` · [字段定义](../../DATASET.md)*
