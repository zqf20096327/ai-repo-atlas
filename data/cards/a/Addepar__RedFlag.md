# Addepar/RedFlag

⭐ 163 · Jinja · MIT · 推送 2026-05-22 · [GitHub](https://github.com/Addepar/RedFlag) · 组织维护

**用 AI 识别高风险代码变更的安全审计工具，支持批量与 CI 模式**

Addepar 开发的代码安全审查工具：调用 LLM（默认经 AWS Bedrock 上的 Claude 模型）对 commit 范围内的代码变更做风险评估。提供三种运行模式——批处理模式分析大量 commit 以圈定发布候选的手工安全测试范围、CI 模式经 GitHub Actions 在 PR 上标记并添加审查者、评测模式用自定义数据集评估模型表现。支持 GitHub/Jira/Slack 集成，输出 HTML/JSON 报告，配置可经 CLI、环境变量与配置文件设置。

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

- 批量模式支持按 commit 哈希/分支/tag 指定分析范围
- CI 模式经 GitHub Actions 对 PR 标记风险并添加审查者、Slack 告警
- 评测模式可用自有数据集评估模型在代码库上的表现
- 输出 HTML/JSON 报告，配置有四级优先级（CLI>环境变量>配置文件>默认值）

## 适用场景

- 发布候选前圈定需要人工安全测试的代码范围
- 在 CI 流水线中自动标记高风险 PR 并分派审查者
- 用自有数据集评估审查模型与提示词在自家代码库上的效果

## 场景标签

`代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L13: RedFlag leverages AI to determine high-risk code changes.
> L152: RedFlag can be run in evaluation mode to evaluate the performance of the AI model using your own custom
> L202: |Bedrock Model ID|--bedrock-model-id|RF_BEDROCK_MODEL_ID|bedrock.model_id|`anthropic.claude-3-sonnet-20240229-v1:0

## 星数曲线

```mermaid
xychart-beta
    title "Addepar/RedFlag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 162 --> 164
    line [163, 163]
```

2026-10-18 163 → 2026-10-24 163（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1b20f8a4e170` · [字段定义](../../DATASET.md)*
