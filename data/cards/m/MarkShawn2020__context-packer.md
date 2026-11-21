# MarkShawn2020/context-packer

⭐ 10 · Python · MIT · 推送 2025-11-26 · [GitHub](https://github.com/MarkShawn2020/context-packer) · [官网](https://pypi.org/project/context-packer/) · 个人维护

**把整个项目打包成单个 markdown 文件供 LLM 使用**

Python 编写的命令行工具（pip 安装，命令 ctxpack），将项目目录打包为一个面向 LLM 与文档场景优化的 markdown 文件。机制包括：项目树可视化与状态指示、自动排除构建产物/依赖/二进制文件、遵循 .gitignore、默认忽略 .env/.git/node_modules、符号链接跟随、大小与文件数与深度限制、大文件截断。文档给出 AI 分析、离线文档、代码审查、教学四种用法场景及 CLI 参数表。

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

- 支持符号链接工作流，用打包目录精确选择要纳入的文件
- 自动排除 .env/.git/node_modules 并遵循 .gitignore
- 输出含项目树、状态指示符与语法高亮的单文件 markdown
- 提供 --max-size/--max-files/--max-depth 等 CLI 参数控制输出

## 适用场景

- 为 AI 代码审查准备完整项目上下文
- 生成可离线浏览的单文件文档包
- 打包 PR 变更供审查
- 为教学整理示例代码材料

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L8: > 🎯 **One file, full context** - Package your entire project into a single markdown file optimized for LLMs and docu
> L23: Context Packer intelligently bundles your entire project into a **single, AI-optimized markdown file** - complete w

## 星数曲线

```mermaid
xychart-beta
    title "MarkShawn2020/context-packer 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-19 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `4b37ea4da681` · [字段定义](../../DATASET.md)*
