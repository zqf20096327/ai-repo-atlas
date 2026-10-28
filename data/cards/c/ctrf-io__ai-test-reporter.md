# ctrf-io/ai-test-reporter

⭐ 61 · TypeScript · MIT · 推送 2026-10-11 · [GitHub](https://github.com/ctrf-io/ai-test-reporter) · [官网](https://ctrf.io) · 组织维护

**给 CI/测试开发者的 AI 测试失败摘要报告工具**

基于 CTRF 开放标准的 CLI 工具：读取 CTRF 格式的测试报告 JSON，将失败测试逐条发送给所选 LLM（支持 OpenAI、Anthropic Claude、Azure OpenAI、Grok、DeepSeek、Mistral 等提供商，以及 Ollama/LocalAI 等自定义 OpenAI 兼容服务），把 AI 摘要写回报告，并可合并汇总、输出按 code/timeout/application 分类的结构化 JSON 分析。需自备 API key，费用自担；框架无关，任何测试框架可经 CTRF 或 JUnit 转换接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 300+ 模型，覆盖 OpenAI/Claude/Azure/Grok/DeepSeek/Mistral 等提供商
- AI 摘要嵌入 CTRF JSON 报告，可整合进 GitHub Actions、Slack/Teams 流程
- 可生成按问题类别（code/timeout/application）分类的结构化 JSON 分析
- 支持 Ollama/LocalAI 等自定义 OpenAI 兼容服务

## 适用场景

- CI 流水线中自动为失败测试生成原因分析与修复建议
- 在 PR 与 Slack/Teams 通知中附带 AI 测试摘要
- 汇总大量失败测试识别共性根因

## 场景标签

 · 领域:测试/开发者工具

## 证据(README 行号)

> L3: AI Test Reporter is a powerful tool that generates intelligent summaries of test results using a wide range of AI mo
> L22: - 🤖 **Smart Analysis**: Get AI-powered explanations of why tests failed and suggestions for fixes
> L57: Generate a CTRF report using your testing framework. CTRF reporters are available for most testing frameworks and e

## 星数曲线

```mermaid
xychart-beta
    title "ctrf-io/ai-test-reporter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-28 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `69b8b96802e7` · [字段定义](../../DATASET.md)*
