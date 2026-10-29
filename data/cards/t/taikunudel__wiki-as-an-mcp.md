# taikunudel/wiki-as-an-mcp

⭐ 44 · Python · MIT · 推送 2026-08-10 · [GitHub](https://github.com/taikunudel/wiki-as-an-mcp) · 个人维护 · 中文 README

**首个通用 Wiki MCP：让 agent 读写、维护与体检个人知识库**

遵循 Google Open Knowledge Format 与 Andrew Karpahyt LLM wiki 设计理念的通用 MCP 服务器，供 LLM agent 使用、管理、维护并对个人 wiki（知识库）做健康检查。知识库是独立的 git 仓库，版本即提交、版次即分支；read 模式固定单一提交只读服务 5 个工具，manage 模式提供全部 14 个工具编辑工作树并快照提交。支持多主题注册表，在首次读取时选择主题。通过 git clone 源码安装，setup.sh 构建虚拟环境并自检。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- read/manage 双模式，5 个只读工具与 14 个管理工具，读取会话不注册写入工具
- 基于 git 的版本管理：版本为提交、版次为分支，已发布版本不可被编辑破坏
- 规则手册随数据内置为 MCP instructions 并由写入工具强制执行
- 多主题注册表：一个服务器按主题在首次读取时选择知识库

## 适用场景

- 让我的 agent 安全地查阅和维护个人知识库
- 团队在管理者编辑期间保持读者会话内容冻结不变
- 在一个 MCP 服务器后挂多个主题知识库供 agent 按任务选用

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L14: To our best knowledge, this is the first general purpose MCP for building and using your own personal wiki (knowled
> L67: - **read** — 5 tools (`kb_index`, `kb_list`, `kb_get`, `kb_grep`, `kb_rules`), pinned to one

## 星数曲线

```mermaid
xychart-beta
    title "taikunudel/wiki-as-an-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ceba51c2938e` · [字段定义](../../DATASET.md)*
