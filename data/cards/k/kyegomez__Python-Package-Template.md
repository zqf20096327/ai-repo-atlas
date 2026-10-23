# kyegomez/Python-Package-Template

⭐ 202 · Shell · MIT · 推送 2026-10-19 · [GitHub](https://github.com/kyegomez/Python-Package-Template) · [官网](https://discord.gg/GYbXvDGevY) · 个人维护

**Python 包开发模板：预置文档、测试、CI 与代码质量工具链**

面向 Python 包开发者的项目模板，包含文档配置（MK docs 与 readthedocs 配置）、pytest 测试结构、GitHub Actions 工作流（PR 时检查代码质量与测试、发版时经 twine 发布到 PyPI）、代码质量工具（black、ruff、make 目标）以及发布流程说明（编辑 __version__、打 tag、poetry build/publish）。README 中未包含 AI 相关功能描述。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预置 pytest 测试结构与 make 测试命令
- GitHub Actions CI：PR 检查代码质量与测试，发版自动发布到 PyPI
- 内置 black/ruff 代码格式化与质量检查
- 附带 MK docs 与 readthedocs 文档配置

## 适用场景

- 快速初始化一个带完整工具链的 Python 包项目
- 让新包自动获得 CI 测试与 PyPI 发布流程
- 复用现成的文档与代码质量配置

## 场景标签

 · 领域:软件开发/工程模板

## 证据(README 行号)

> L7: A easy, reliable, fluid template for python packages complete with docs, testing suites, readme's, github workflows,
> L45: We use GitHub actions to automatically run tests and check code quality when a new PR is done on `main`.

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/Python-Package-Template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 201 --> 203
    line [202, 202]
```

2026-10-18 202 → 2026-10-23 202（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 low · 依据 README sha `23697a65e7db` · [字段定义](../../DATASET.md)*
