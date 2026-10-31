# Ice-Hazymoon/jevwright

⭐ 14 · TypeScript · MIT · 推送 2026-10-09 · [GitHub](https://github.com/Ice-Hazymoon/jevwright) · [官网](https://www.npmjs.com/package/@hazymoon/jevwright) · 个人维护

**面向业务流程的浏览器端到端测试框架：AI 定位控件一次，录制回放零成本**

基于 Playwright 的 E2E 测试框架：测试以用户操作步骤的文字编写，无需选择器或页面对象；首次运行时由 TypeSafe Jev 模型在真实页面上定位每步对应控件并录制为语义目标，之后通过 --mode replay 确定性回放，不再调用模型。判定通过与否由开发者代码决定：声明的请求、verify 回调读取数据库或 API、不变量与页面监控。失败按 product/agent/environment/model/timeout 五类归因并附证据。需要 Node.js 22+、Playwright 1.63+，AI 运行需 OpenRouter 或 Vercel AI Gateway 密钥，回放模式无需密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 步骤以用户意图文字编写，无需选择器；模型定位一次后录制回放，replay 模式不调用模型
- 测试通过与否由代码决定：声明请求、verify 回调（数据库/API）、不变量
- 失败归因为 product/agent/environment/model/timeout 五类，附截图、请求与 Playwright trace
- 每步隐式检查：未捕获异常、5xx/意外 4xx、控制台错误、hydration 不匹配、undefined/NaN 等文本

## 适用场景

- 用业务语言编写端到端测试，UI 重构不破坏测试
- CI 中以零模型成本的 replay 模式运行回归
- 通过数据库/API 校验业务事实而非只看页面
- 按证据归因测试失败，区分产品缺陷与 agent 失误

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: jevwright opens your app in Chromium and hands one step at a time to TypeSafe's Jev, which picks the control the ste
> L22: - **Recorded once, replayed for free.** The first run records each step as a semantic target (role, name, nearby te
> L70:    npx jevwright run --mode replay   # recordings only: no key, no model calls (CI)

## 星数曲线

```mermaid
xychart-beta
    title "Ice-Hazymoon/jevwright 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e28d3e3f1069` · [字段定义](../../DATASET.md)*
