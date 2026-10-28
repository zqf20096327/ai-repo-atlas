# uaoa/claude-commit-vscode

⭐ 19 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/uaoa/claude-commit-vscode) · 个人维护

**VS Code 扩展：用 Claude 读取 git diff 自动生成提交信息**

Commit Pen 是一个 VS Code 扩展，读取工作区 Git 仓库的 diff，通过本地 Claude Code CLI（优先）或 Anthropic API 生成提交信息并填入源代码管理输入框，用户审阅后提交。支持 Conventional Commits 等多种风格与自定义提示模板、四种输出语言、Haiku/Sonnet/Opus 模型选择、多仓库工作区、WSL/Remote-SSH/dev container 环境，API 密钥存于系统密钥库。要求 VS Code 1.75+ 与已登录的 Claude Code CLI 或 API key。前身为 Claude Git Commit 扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 diff 后经 Claude Code CLI 或 Anthropic API 生成提交信息
- CLI 自动发现（PATH/VS Code 扩展/shell 配置/常见安装目录）
- Conventional Commits、自定义提示模板与四种输出语言
- API 密钥存于 OS 密钥库而非 settings.json

## 适用场景

- 写提交信息时让 AI 根据 diff 自动生成草稿再修改
- 团队统一 Conventional Commits 风格的提交信息
- 多仓库工作区中针对当前仓库生成提交信息

## 场景标签

 · 领域:开发者工具/Git

## 证据(README 行号)

> L10: Commit Pen writes Git commit messages for you. It reads the diff of your repository, sends it to Claude through the
> L19: - **CLI first, API as a fallback.** Uses the local Claude Code CLI when it is available, so no separate API key is 

## 星数曲线

```mermaid
xychart-beta
    title "uaoa/claude-commit-vscode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `fffb060bdcdf` · [字段定义](../../DATASET.md)*
