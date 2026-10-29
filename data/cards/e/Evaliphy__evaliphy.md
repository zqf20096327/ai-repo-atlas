# Evaliphy/evaliphy

⭐ 18 · TypeScript · MIT · 推送 2026-05-07 · [GitHub](https://github.com/Evaliphy/evaliphy) · [官网](https://evaliphy.com) · 组织维护

**面向开发者的 E2E AI 系统测试工具：LLM-as-Judge 断言+CI 回归检测**

基于 TypeScript 的 AI 系统端到端评测框架：将用户的 AI 应用视为黑盒，评测文件通过 HTTP 调用真实运行的服务，内置 LLM-as-Judge 断言（忠实性、相关性、有据性、连贯性、无害性），由评审模型打分 0.0-1.0 并与阈值比较判定通过与否；支持自定义 prompt 覆盖内置提示词，断言失败时以非零退出码接入任意 CI 流水线，输出 console/json/html 报告。通过 Vercel AI SDK 支持 OpenAI、Anthropic、Azure、Gemini、Mistral 及 OpenAI 兼容网关。当前处于 open beta，API 可能随版本变化；确定性断言与 csv/xlsx 报告标注为 v1 待推出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内置 5 种 LLM-as-Judge 断言（忠实性/相关性/有据性/连贯性/无害性），0.0-1.0 打分制
- 评测通过 HTTP 调用真实运行的服务，非 mock 或离线数据集
- 断言失败返回非零退出码，兼容任意 CI 流水线，附 GitHub Actions 示例
- 支持以 markdown 文件覆盖内置断言提示词

## 适用场景

- 为已部署的 LLM/RAG 服务编写回归测试并在 CI 中运行
- 检测 RAG 回答是否忠实于检索上下文与源文档
- 在多个 LLM 提供商之间切换评审模型并统一评估结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L16: Evaliphy is an AI system tool that treats your AI system as a black box. Write assertions against your real API, ge
> L224: 3. The assertion sends a rendered prompt to the judge model

## 星数曲线

```mermaid
xychart-beta
    title "Evaliphy/evaliphy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3215b0856713` · [字段定义](../../DATASET.md)*
