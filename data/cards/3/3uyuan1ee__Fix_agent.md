# 3uyuan1ee/Fix_agent

⭐ 27 · Python · NOASSERTION · 推送 2025-12-28 · [GitHub](https://github.com/3uyuan1ee/Fix_agent) · 个人维护 · 中文 README

**基于 LangChain/DeepAgents 的代码缺陷检测与自动修复 Agent**

基于 LangChain 1.0 与 DeepAgents 构建的代码优化 Agent，实现项目问题检测→自动修复→效果验证的闭环。采用三子代理架构：缺陷分析（语法/逻辑/性能/安全）、代码修复（human-in-loop 下执行）、修复验证（测试运行与安全扫描）。支持主流编程语言分析，集成 pylint、flake8、mypy、bandit、eslint 等工具链，具备长期记忆能力。提供 CLI 与 Web 双模式，支持 pip 安装，需配置 LLM API 与 TAVILY_API，运行环境为 Python 3.11+、macOS/Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三子代理架构：缺陷分析→代码修复→修复验证闭环
- 集成 pylint/flake8/mypy/bandit/eslint 等统一工具链
- CLI 与 Web 双模式，human-in-loop 修复执行
- 长期记忆系统，支持 /memory edit 编辑记忆

## 适用场景

- 自动检测项目中的语法、逻辑、性能与安全缺陷
- 让 Agent 生成修复方案并经人工确认后执行修复
- 修复后自动运行测试与安全扫描验证效果

## 场景标签

`代码审查` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: 基于Langchian1.0和Deepagents，实现项目问题检测->自动修复->效果验证的闭环
> L14: ### 基于Deepagents的Three-subagents架构
> L23: - **智能修复** - 基于分析报告自动生成修复代码

## 星数曲线

```mermaid
xychart-beta
    title "3uyuan1ee/Fix_agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `994b705e7045` · [字段定义](../../DATASET.md)*
