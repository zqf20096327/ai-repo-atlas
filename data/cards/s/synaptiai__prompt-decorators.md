# synaptiai/prompt-decorators

⭐ 44 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/synaptiai/prompt-decorators) · [官网](https://synaptiai.github.io/prompt-decorators/) · 组织维护

**提示词装饰器规范与 Python 参考实现：可组合注解控制 LLM 行为**

由 Synaptiai 维护的框架与标准：通过 `+++Reasoning` 等可组合装饰器注解，标准化修改 LLM 处理与响应提示词的方式。仓库包含正式规范（v1.0）与生产就绪的 Python 参考实现：注册表式装饰器管理、参数校验、版本管理、兼容性检查、文档生成与运行时动态加载；内置 140+ 预置装饰器。另提供 MCP 服务器（接入 Claude Desktop 等）与 Claude Code 插件（`::Name(params)` 展开、/decorate 命令、可选 Haiku 自动选择器）。项目处于活跃开发中，以 pip 包分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 正式 Prompt Decorators 规范（v1.0）+ Python 参考实现
- 140+ 预置装饰器覆盖推理、格式化等场景
- 注册表式管理：参数校验、语义版本、兼容性检查、文档自动生成
- MCP 服务器与 Claude Code 插件（/decorate 命令、可选 Haiku 自动选择器）

## 适用场景

- 用可组合注解控制不同 LLM 的推理与输出格式
- 在 Claude Desktop 中通过 MCP 使用装饰器功能
- 定义领域专属装饰器并在团队间复用

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L27: Prompt Decorators introduces a standardized annotation system inspired by software design patterns that allows user
> L33: 3. **MCP Integration**: A Model Context Protocol server that enables prompt decorator functionality in tools like C

## 星数曲线

```mermaid
xychart-beta
    title "synaptiai/prompt-decorators 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ac0bc1d4c6ac` · [字段定义](../../DATASET.md)*
