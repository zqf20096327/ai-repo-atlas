# microsoft/gpt-review

⭐ 301 · Python · MIT · 推送 2026-04-29 · [GitHub](https://github.com/microsoft/gpt-review) · 组织维护

**用 OpenAI/Azure OpenAI 审查 PR、问答与生成提交信息的 CLI**

Microsoft 维护的 Python CLI 与 GitHub Action，调用 OpenAI 或 Azure OpenAI 模型完成三类任务：审查 Pull Request 内容、向 GPT 提问（含基于文件的问答，可调 temperature/max-tokens 等参数）、生成 git commit message。API 凭证按优先级依次从 azure.yaml 上下文文件、Azure OpenAI 环境变量、OPENAI_API_KEY 或 Azure Key Vault 读取。通过 pip 安装，MIT 许可。

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

- 审查 Pull Request 内容
- gpt ask 支持带文件提问与采样参数配置
- gpt git commit 生成提交信息
- 四种 API 凭证配置途径（含 Azure Key Vault）

## 适用场景

- 在 CI 中自动审查 Pull Request 变更
- 命令行快速向 GPT 提问或总结文档
- 自动生成 git 提交信息

## 场景标签

`代码审查` `AI 写作` · 领域:编码与开发

## 证据(README 行号)

> L10: A Python based CLI and GitHub Action to use Open AI or Azure Open AI models to review contents of pull requests.
> L64: To submit a question to GPT and receive an answer, use the following format:
> L91: ### 3. Generate a git commit message with GPT

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/gpt-review 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 300 --> 302
    line [301, 301]
```

2026-10-18 301 → 2026-10-29 301（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `bbcebfed71c8` · [字段定义](../../DATASET.md)*
