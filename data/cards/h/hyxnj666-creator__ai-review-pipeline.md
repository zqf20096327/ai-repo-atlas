# hyxnj666-creator/ai-review-pipeline

⭐ 46 · JavaScript · MIT · 推送 2026-04-29 · [GitHub](https://github.com/hyxnj666-creator/ai-review-pipeline) · [官网](https://www.npmjs.com/package/ai-review-pipeline) · 个人维护 · 中文 README

**给开发者的 AI 代码审查流水线 CLI：审查+测试生成+报告**

npm CLI 工具，一条命令执行代码审查、AI 测试用例生成（功能/对抗/边界三类）与 HTML 报告；`--fix` 开启审查-修复-重测循环（默认最多 5 轮）。内置免费模型零配置运行，支持 OpenAI/DeepSeek/Claude/Qwen/Gemini/SiliconFlow/Ollama 及任意 OpenAI 兼容 API，按环境变量自动识别。提供分数门禁（Blocker/Major 阈值与退出码）接入 GitHub Actions/GitLab CI/git hook，JSONC 配置可团队共享，支持 11 种编程语言与中英双语 prompt。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零依赖零配置，内置免费模型 npx 即用
- 7 个 AI 提供商自动识别，含本地 Ollama 与 OpenAI 兼容自定义端点
- 分数门禁（阈值/Blocker/Major）+ 退出码，接入 CI 流水线
- AI 生成三类测试用例（功能/对抗/边界）与 HTML 报告

## 适用场景

- 在 CI 中对 PR 做 AI 代码审查并按分数门禁阻断合并
- 本地对 git 变更或指定文件跑审查并自动修复
- 为已有代码生成功能、对抗与边界测试用例

## 场景标签

`代码审查` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: AI-powered code quality pipeline CLI — Review + Test + Report in one command. Add `--fix` for auto-fix loop.
> L13: - **Multi-provider** — OpenAI / DeepSeek / Claude / Qwen / Gemini / SiliconFlow / Ollama, auto-detected

## 星数曲线

```mermaid
xychart-beta
    title "hyxnj666-creator/ai-review-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e0f8abcc5110` · [字段定义](../../DATASET.md)*
