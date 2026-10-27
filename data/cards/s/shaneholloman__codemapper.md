# shaneholloman/codemapper

⭐ 31 · Python · MIT · 推送 2025-11-04 · [GitHub](https://github.com/shaneholloman/codemapper) · 个人维护

**把代码库/文档转成单文件 Markdown 供 LLM 使用的 Python 工具**

Python 编写的命令行工具：扫描本地目录或 GitHub 仓库，生成包含完整目录树、文件内容（带语法高亮）与 Git 元数据（分支、提交、远程地址）的单一 Markdown 文件，作为语言模型的上下文或代码分析输入。智能过滤二进制文件、锁文件、缓存目录及超过 30 万字符的文件，默认遵循 .gitignore。支持 --docs 仅生成文档地图、--exclude 排除目录及 TOML 配置文件自定义输出位置。需 Python 3.12+。

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

- 生成含目录树、文件内容与 Git 元数据的单一 Markdown
- 自动过滤二进制/锁文件/缓存/超 30 万字符文件
- 遵循 .gitignore（可用 --include-ignored 覆盖）
- 支持 --docs 文档地图模式与 TOML 集中式输出配置

## 适用场景

- 把整个项目打包成单文件喂给 AI 做代码分析
- 为 LLM 提示词准备完整的代码库上下文
- 生成仅含文档的项目地图用于知识整理

## 场景标签

`提示工程` `文档解析` · 领域:Agent 开发

## 证据(README 行号)

> L3: > Converts codebases/docs into single-file Markdown documents for language model context and code analysis.
> L78: - Files over 300k characters (too large for AI context)

## 星数曲线

```mermaid
xychart-beta
    title "shaneholloman/codemapper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3931bee3c587` · [字段定义](../../DATASET.md)*
