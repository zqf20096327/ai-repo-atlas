# vlad-ryzhkov/AI-QA-workshop-feb19

⭐ 26 · Kotlin · Unlicense · 推送 2026-03-07 · [GitHub](https://github.com/vlad-ryzhkov/AI-QA-workshop-feb19) · [官网](https://youtu.be/7VnjM44qkmc      ) · 个人维护

**QA 工程 AI 提示词/技能与反模式集合（附工作坊材料）**

面向 QA 工程师的 AI 工作坊配套资源库：提供一组经验证的 .md 格式提示词技能（/repo-scout、/spec-audit、/test-cases、/api-tests 等），覆盖从 API 规格审计、测试用例生成到生成 Kotlin/JUnit 5/Allure API 测试的流程；附配置生成技能（/init-project 等）、20+ 反模式检查文件与文档。以 Claude Code/OpenCode 原生文件结构为主，提供 Cursor、GitHub Copilot、Codex 等 IDE 的兼容映射表。安装方式为复制 .claude/ 目录到项目根并运行 /init-project。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 技能文件化（.md），指定 AI 任务、检查项与输出格式
- 兼容矩阵覆盖 Claude Code/OpenCode/Cursor/Copilot/Codex 七类工具
- 生成 Kotlin + JUnit 5 + Allure 的可运行 API 测试
- Progressive Disclosure 与 Token Management 等项目模式，附 20+ 反模式文件

## 适用场景

- 让 AI 审计 API 规格并产出缺陷清单与风险矩阵
- 从规格自动生成测试用例矩阵和 Kotlin API 测试
- 为新 QA 项目生成 CLAUDE.md 等分层 AI 配置文件

## 场景标签

`提示工程` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L8: Готовая коллекция AI-промптов, агентов и анти-паттернов для QA-процессов: от анализа спецификаций до генерации API-т
> L10: Структурированные промпты дают стабильный результат — каждый скилл в репозитории это проверенный `.md`-файл, которы

## 星数曲线

```mermaid
xychart-beta
    title "vlad-ryzhkov/AI-QA-workshop-feb19 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `cdcf767f396d` · [字段定义](../../DATASET.md)*
