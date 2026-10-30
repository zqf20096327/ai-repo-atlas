# fabriziosalmi/iamnotacoder

⭐ 34 · Python · MIT · 推送 2026-09-06 · [GitHub](https://github.com/fabriziosalmi/iamnotacoder) · 个人维护

**LLM 驱动的 Python 代码自动优化与生成工具包**

面向开发者的 Python 代码工具套件，包含四个脚本：scraper 按条件发现 GitHub Python 仓库；iamnotacoder 主工具结合静态分析（black/isort/pylint/flake8/mypy）、LLM 重构、pytest 自动测试生成与 GitHub PR 流程（含安全 fork）优化既有代码；process 批量编排；create_app_from_scratch 用多个 LLM 角色从自然语言生成应用原型。默认模型 qwen2.5-coder-14b-instruct-mlx，支持 OpenAI API 与 LM Studio 本地模型。自声明为实验性工具，建议审查生成代码后再使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 静态分析 + LLM 重构 + 自动测试生成 + GitHub PR 的组合流程
- 支持 OpenAI API 与本地 LLM（LM Studio，OpenAI 兼容接口）
- 按 style/maintenance/security/performance/tests 五类自定义提示词
- Dry Run / 本地提交 / fork 仓库三种安全模式

## 适用场景

- 批量改进我 GitHub 仓库中 Python 代码的风格与安全问题
- 用本地 LLM 自动生成并运行单元测试以提高覆盖率
- 从自然语言描述快速生成应用原型

## 场景标签

`编码 Agent` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L14: * **`iamnotacoder.py` (The Optimizer 🛠️):** Your primary tool for enhancing existing Python code within GitHub repo
> L47:  * Leverages LLMs to suggest and apply code refactorings.
> L60:  * Generates unit tests using an LLM, increasing your code coverage.

## 星数曲线

```mermaid
xychart-beta
    title "fabriziosalmi/iamnotacoder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3ec2eea8e802` · [字段定义](../../DATASET.md)*
