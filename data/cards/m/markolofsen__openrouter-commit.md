# markolofsen/openrouter-commit

⭐ 23 · TypeScript · MIT · 推送 2026-06-24 · [GitHub](https://github.com/markolofsen/openrouter-commit) · [官网](https://www.npmjs.com/package/orcommit) · 组织维护

**用 LLM 生成 git 提交信息的命令行工具**

面向使用 git 的开发者的 CLI 工具：读取暂存区 diff，经 Gitleaks 扫描密钥后发送给 LLM 提供商（OpenRouter、OpenAI、Ollama 本地模型或任意 OpenAI 兼容端点），返回符合 Conventional Commit 规范的提交信息，用户可确认、重生成或编辑后提交。大 diff 自动分块，提交信息按仓库缓存以避免重复计费。内置默认模型（gemini-2.5-flash-lite / gpt-4o-mini），自定义提供商须指定 --model。由 Reforms.ai 维护，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取暂存 diff 生成 Conventional Commit 格式提交信息
- 提交前用 Gitleaks 扫描密钥，命中即阻止提交
- 支持 OpenRouter、OpenAI、Ollama 及任意 OpenAI 兼容自定义端点
- 大 diff 自动分块，提交信息按仓库缓存避免重复计费

## 适用场景

- 我不想手写提交信息，让 AI 按 diff 生成
- 防止 API key 等密钥误提交进 git 历史
- 切换不同 LLM 提供商（含本地 Ollama）生成提交信息

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L12: ORCommit reads your staged diff and writes a clean, Conventional Commit message for you — using OpenRouter, OpenAI,
> L71: 3. **Sends** the diff to your AI provider, which returns a structured commit

## 星数曲线

```mermaid
xychart-beta
    title "markolofsen/openrouter-commit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2440d84b770a` · [字段定义](../../DATASET.md)*
