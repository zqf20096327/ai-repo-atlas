# Evalogical-Inc/devReady

⭐ 4 · Python · MIT · 推送 2026-11-16 · [GitHub](https://github.com/Evalogical-Inc/devReady) · [官网](https://devready-ten.vercel.app/) · 组织维护

**给开发者与 AI agent 做项目环境要求预检的只读 CLI**

DevReady 是零依赖、只读的命令行工具：读取项目声明的要求（.nvmrc、.python-version、package.json engines、pyproject.toml requires-python 等），与本机实际安装的 Python、Node、Git 等比对，逐项输出 PASS/WARN/FAIL 及修复提示，退出码 1 表示未满足，可直接用于 CI。支持 JSON/SARIF/JUnit 输出、monorepo 递归检查、GitHub Actions 与 pre-commit 集成；不安装、不修改、不联网。为 AI agent 提供版本化 JSON schema、Claude Code 插件与 MCP server（依赖 uv）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取项目声明的版本钉并比对本机实际安装，逐项报告 PASS/WARN/FAIL
- 只读设计：不安装不删除、无网络调用与遥测，输出仅含解析后的版本与固定文本
- 同一引擎提供三种 agent 接入：Claude Code 插件、MCP server（check_environment 工具）、AGENTS.md
- 支持 monorepo 递归检查、GitHub Actions 与 SARIF/JUnit/pre-commit 集成

## 适用场景

- 新员工或学生克隆项目后，一条命令定位环境缺失项
- 在 CI 中做预检步骤，未满足声明要求即失败
- 让 Claude Code / Codex 在安装构建前先获取环境真实状态
- 维护者把 devready check 放进 README 设置步骤减少环境类 issue

## 场景标签

 · 领域:开发者工具/环境检查

## 证据(README 行号)

> L6: Built for humans, CI, and AI coding agents (Claude Code, Codex, any MCP client).
> L54: |🤖 **Agent-ready**|Stable, versioned JSON schema, a Claude Code plugin, an MCP server and `AGENTS.md`. Agents check
> L259: - Checks today: Python, Git (+ identity set), Node.js, npm, project pins (`.nvmrc`, `.node-version`, `.python-vers

## 星数曲线

```mermaid
xychart-beta
    title "Evalogical-Inc/devReady 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-11-10", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-28 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `5bfbb4775cb9` · [字段定义](../../DATASET.md)*
