# can1357/llm-git

⭐ 60 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/can1357/llm-git) · 个人维护

**给开发者的 git 提交信息生成 CLI：用 LLM 从 diff 生成规范提交**

lgit 是 Python 编写的命令行工具，读取 git diff 并调用 Claude 或任意 OpenAI 兼容 API 生成 conventional commits 格式的提交信息（类型/范围/摘要≤72 字符）。支持 compose 模式将大批暂存改动拆分为多个原子提交、rewrite 模式重写整个仓库历史（自动备份）、按 Keep a Changelog 格式自动维护 CHANGELOG.md（含 monorepo 路由与语义去重），以及对大提交的 map-reduce 并行逐文件分析。配置经 TOML 文件与环境变量，默认接入 LiteLLM 代理。需 Python 3.14+、Git 与 LLM API 访问。

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

- 从 diff 生成 conventional commits（类型/范围/摘要≤72 字符）
- compose 模式拆分大改动为多个原子提交；rewrite 模式重写全历史（自动备份）
- 自动维护 CHANGELOG.md，支持 monorepo 路由与语义去重
- 兼容 Anthropic、OpenAI、OpenRouter 及任意 OpenAI 兼容端点

## 适用场景

- 我不想手写提交信息，让 AI 根据暂存改动生成规范提交
- 把一大批改动拆成多个逻辑清晰的原子提交
- 把旧仓库历史统一改写为 conventional commits 并维护变更日志

## 场景标签

`代码生成` `AI 写作` · 领域:编码与开发

## 证据(README 行号)

> L10:  Generates conventional commits from git diffs using Claude AI or any OpenAI-compatible API.
> L20: - **Any LLM provider** — Works with Anthropic, OpenAI, OpenRouter, or any OpenAI-compatible API

## 星数曲线

```mermaid
xychart-beta
    title "can1357/llm-git 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 58 --> 61
    line [59, 60, 60]
```

2026-10-18 59 → 2026-10-27 60（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `db4d04e7ac9e` · [字段定义](../../DATASET.md)*
