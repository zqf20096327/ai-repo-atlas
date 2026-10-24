# sahajamit/promptwright

⭐ 120 · TypeScript · MIT · 推送 2026-07-10 · [GitHub](https://github.com/sahajamit/promptwright) · [官网](https://www.youtube.com/watch?v=2c7P4du6hDQ) · 个人维护

**免登录 BYOK 的桌面 AI 测试代理：自然语言驱动浏览器并生成测试脚本**

Electron 桌面应用加 CLI 形式的 AI QA 代理：用户用自然语言描述任务，编排器分类意图并路由到专门 agent（Playwright CLI、Playwright MCP、API 测试、录制转 Gherkin），通过 CDP 驱动真实 Chrome 执行并实时流式回传步骤，可录制点击流回放生成 Gherkin 特性文件。免登录，自带密钥（BYOK），支持任意 OpenAI 兼容提供方（OpenAI/Azure/Anthropic/Moonshot）及 Ollama 本地模型。限制：应用未签名，Intel Mac 暂无构建，小型本地模型的工具调用能力不足。

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

- 自然语言描述或录制点击流，生成可运行的 Playwright/Cypress/Selenium 脚本与 Gherkin
- 编排器将任务路由到专门 agent，步骤实时流式回传
- 免登录 BYOK：任意 OpenAI 兼容提供方或 Ollama 本地模型
- Playwright CLI 与 Playwright MCP 两种浏览器驱动模式

## 适用场景

- 用自然语言让 AI 驱动真实浏览器执行并验证测试
- 录制手动点击流并转成可回放的 Gherkin 特性文件
- 用自己的模型密钥（含本地 Ollama）运行 QA 代理，不绑定厂商

## 场景标签

`浏览器自动化` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L6:  An AI QA agent that drives a real browser from natural language, or watches you click and turns it into Gherkin you
> L14: Promptwright started life under Testron AI as a tool that turned a natural-language prompt into an automated browse
> L44: - **Any OpenAI-compatible provider.** OpenAI, Azure AI Foundry, Anthropic, Moonshot (Kimi), or a fully local model 

## 星数曲线

```mermaid
xychart-beta
    title "sahajamit/promptwright 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 119 --> 121
    line [120, 120]
```

2026-10-18 120 → 2026-10-24 120（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `87d1a0d408de` · [字段定义](../../DATASET.md)*
