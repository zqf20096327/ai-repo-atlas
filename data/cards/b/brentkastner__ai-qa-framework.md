# brentkastner/ai-qa-framework

⭐ 62 · Python · Apache-2.0 · 推送 2026-02-23 · [GitHub](https://github.com/brentkastner/ai-qa-framework) · [官网](https://github.com/brentkastner/ai-qa-framework#readme) · 个人维护

**给开发/QA 团队：AI 自动爬取网站并生成执行测试的 QA 框架**

自动化 QA 框架：给定目标 URL 后，通过真实浏览器爬取页面、表单与 API，由 Claude AI 分析站点结构生成上下文相关的测试，再用 Playwright 执行，支持选择器失效时基于截图的 AI 修复，并输出含截图与 AI 总结的 HTML/JSON 报告。覆盖功能、视觉回归与安全（XSS/HTTPS/cookie）检查，带覆盖率记忆与自然语言提示机制。可配置 Anthropic API 或本地 Ollama 作为 AI 提供方；未配置任何 AI 时降级为模板式测试生成。需 Python 3.12+ 与 Chromium，面向开发团队、QA 工程师与独立开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四阶段流水线：爬取→AI 生成测试→Playwright 执行→HTML/JSON 报告
- 自愈测试：选择器失效时 AI 分析截图并修复
- 覆盖率记忆跟踪已测内容并聚焦缺口，含回归检测
- 支持 Anthropic API 或本地 Ollama，无 AI 时降级为模板式生成

## 适用场景

- 无人手写测试脚本地为网站生成并执行功能/视觉/安全测试
- 用自然语言提示引导 AI 测试优先级（如指定关键流程）
- 持续测试网站变更并自动检测回归与选择器失效

## 场景标签

`浏览器自动化` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: An autonomous AI-driven QA framework that automatically discovers, tests, and reports on any website—no manual test 
> L78: 2. **Plan** - Claude AI analyzes structure and generates contextual tests
> L93: - **Test generation** - Claude analyzes your site to create relevant tests

## 星数曲线

```mermaid
xychart-beta
    title "brentkastner/ai-qa-framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-25 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9fbe9490005e` · [字段定义](../../DATASET.md)*
