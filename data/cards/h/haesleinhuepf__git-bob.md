# haesleinhuepf/git-bob

⭐ 70 · Python · BSD-3-Clause · 推送 2026-05-30 · [GitHub](https://github.com/haesleinhuepf/git-bob) · 个人维护

**在 GitHub CI 中用 LLM 解决 issue 的 AI 编程助手**

运行于 GitHub Actions 或 GitLab CI 的 AI agent：通过在 issue/PR 中评论触发词（comment/review/solve/split/deploy 等）调用 Claude、GPT、Gemini、Mistral、DeepSeek 等模型，理解请求、生成文本与代码并提交 PR。讨论过程被保留可复现，用户需自行配置 API key 并承担费用。支持读写多种文件格式（notebook、docx、pptx、图像等），主要面向 Python 项目测试，作者声明其为研究项目，存在幻觉与长文件处理限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 GitHub Actions/GitLab CI 运行，本地无需安装
- comment/review/solve/split/deploy 等触发词驱动工作流
- 支持 Anthropic/OpenAI/Google/Mistral/DeepSeek/GitHub Models 等多家 LLM 端点
- 可读写 Notebook、docx、pptx、图像等多种文件格式

## 适用场景

- 让 AI 直接在仓库里解决 issue 并提交 PR
- 让 AI 审查拉取请求的代码质量
- 把复杂 issue 拆分为多个子 issue

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: git-bob uses AI to solve GitHub issues. It runs inside the GitHub CI or Gitlab runners, no need to install anything 
> L12: Under the hood it uses Anthropic's Claude or OpenAI's chatGPT or Google's Gemini or your institutional LLM service 
> L16: `git-bob` is a research project aiming at streamlining GitHub interaction in software development projects. Under t

## 星数曲线

```mermaid
xychart-beta
    title "haesleinhuepf/git-bob 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-25 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9e5e561bdb14` · [字段定义](../../DATASET.md)*
