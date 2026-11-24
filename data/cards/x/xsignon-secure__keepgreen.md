# xsignon-secure/keepgreen

⭐ 4 · TypeScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/xsignon-secure/keepgreen) · 组织维护

**自托管 GaaS：AI 代理在你的 CI 中生成并修复 Playwright E2E 测试**

KeepGreen 是一个 MIT 许可的 npm CLI 与 GitHub Action，定位为'GaaS'——不设自有服务器，完全运行在用户自己的 GitHub Actions runner 或本地，使用用户自己的 AI key 并由 max-usd 上限控制开销。核心流程为 explore（检查页面、规划未覆盖的用户流、每个流生成一个测试）、heal（UI 变更后生成修复 PR）与防作弊守卫（无真实断言、跳过、伪造网络应答的测试被丢弃，新测试须连续多次通过）。支持 Playwright Test 与 pytest-playwright，heal 另覆盖 Cypress 与 WebdriverIO。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- explore 自动发现未被测试的用户流并生成测试，仅保留连续通过（默认 5 次）且有真实断言的测试
- AutoHeal 在 UI 变更导致测试失败时生成修复 PR，真实应用 bug 会被报告而非掩盖
- max-usd 单次花费上限，OpenRouter 价格自动查询
- 通过 playwright-e2e-mcp 与 AutoHeal 两个项目组合实现

## 适用场景

- 给缺少 E2E 覆盖的 Web 应用自动补齐测试
- UI 变更后自动修复失效的选择器并出 PR
- 在自有 CI 中用本地模型或自有 API key 运行 AI 测试

## 场景标签

`浏览器自动化` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L6:  The AI test agent that writes, fixes and keeps your end-to-end tests green.
> L47: - 🔍 **It explores.** It opens your app, finds the important flows nobody tested, and writes the tests.
> L25: KeepGreen runs **on your own CI runner or laptop, with your own AI key**: Anthropic, OpenAI,

## 星数曲线

```mermaid
xychart-beta
    title "xsignon-secure/keepgreen 星数(近 3 点)"
    x-axis ["2026-11-14", "2026-11-19", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-14 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `525fe3fc412e` · [字段定义](../../DATASET.md)*
