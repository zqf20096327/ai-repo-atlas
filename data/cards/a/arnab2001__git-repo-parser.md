# arnab2001/git-repo-parser

⭐ 30 · TypeScript · MIT · 推送 2025-11-09 · [GitHub](https://github.com/arnab2001/git-repo-parser) · [官网](https://www.npmjs.com/package/git-repo-parser) · 个人维护

**把 GitHub 仓库全部文件抓取为 JSON/TOON/文本的工具，供 LLM 项目使用**

npm 包 git-repo-parser，提供三个 CLI 命令（git-repo-to-json / to-toon / to-text）与 Node.js API，将 GitHub 仓库临时克隆后抓取源码文件，输出 JSON、TOON 或 RepoScript v1 转录格式（确定性的目录/文件标记语法，面向 LLM 输入）。附带 CL100K 词表的 token 计数（基于 gpt-tokenizer）、可配置元数据行、以及评测抓取耗时与 token 用量的基准套件。忽略二进制、媒体、锁文件与配置文件，抓取后清理临时克隆。面向需要把代码仓库转为 LLM 输入的开发者。

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

- 三种输出格式：JSON、TOON、RepoScript v1 确定性转录
- 基于 CL100K 词表的 token 计数（CLI 与 API 均支持）
- 忽略二进制/媒体/锁文件等非源码文件
- 内置基准套件评测多仓库的抓取耗时与 token 用量

## 适用场景

- 把整个代码仓库导出为单个文件喂给 LLM
- 估算仓库内容的 token 占用
- 以确定性格式保留目录结构供模型处理

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: A powerful tool to scrape all files from a GitHub repository and convert them into JSON, Token-Oriented Object Notat
> L94: RepoScript is a deterministic, LLM-friendly transcript of a repository (formerly the “plain text” output).

## 星数曲线

```mermaid
xychart-beta
    title "arnab2001/git-repo-parser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `11c9b395cb7c` · [字段定义](../../DATASET.md)*
