# mindfiredigital/AUTOTEST

⭐ 42 · Python · MIT · 推送 2026-04-09 · [GitHub](https://github.com/mindfiredigital/AUTOTEST) · 组织维护

**给测试人员的 LLM 网页自动化测试用例与 Selenium 脚本生成工具**

开源 GenAI 测试自动化应用：以 BFS 从基础 URL 递归提取站内链接，逐页提取页面元数据，再由 LLM 生成页面专属测试用例和可执行的 Python Selenium 脚本，覆盖正向与负向场景。借助 LangChain 的 LLM 抽象层支持 openai、groq、anthropic 等多提供商，双模型分工（页面分析与脚本生成），可通过 auth_test_data.json 做登录/注册等数据驱动测试。以 CLI 和 Python 包两种方式运行，需在 .env 提供 API key，需 Python 3.10.12 与 Selenium 4.15.2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BFS 递归提取站内 URL 至指定深度后逐页生成测试用例
- LangChain 抽象层支持 openai/groq/anthropic 等多家 LLM 提供商
- 双模型分工：页面分析与测试生成、Selenium 脚本生成各用一个模型
- LLM 动态提取失败时回退到 Selenium 选择器的静态元数据提取

## 适用场景

- 为我批量生成整个网站的 Selenium 自动化测试脚本
- 对登录/注册页面做数据驱动的正负向用例测试
- 用不同 LLM 提供商生成并执行网页测试用例

## 场景标签

`浏览器自动化` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L11: An open-source Generative AI (GenAI) application designed to generate automated test cases and python Selenium scri
> L16:  - The application is built with comprehensive support for all major open-source and closed-source LLMs due to lang

## 星数曲线

```mermaid
xychart-beta
    title "mindfiredigital/AUTOTEST 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a5815bbf5019` · [字段定义](../../DATASET.md)*
