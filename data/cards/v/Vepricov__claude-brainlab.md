# Vepricov/claude-brainlab

⭐ 34 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Vepricov/claude-brainlab) · [官网](https://vepricov.github.io/claude-brainlab/lab-showcase/) · 组织维护

**研究实验室的 Claude Code 配置包：67 个技能+钩子+git 知识库**

BRAIn 实验室在用的 Claude Code 工作台配置，打包供其他实验室安装：67 个技能、10 个斜杠命令、13 个 agent、9 个钩子、11 条规则，覆盖文献摄取（arXiv→Zotero→Obsidian）、实验记录、论文写作与审稿等八个研究环节。知识库是普通 git 仓库（GitLab 组），一棵目录树同时充当 Obsidian vault；改动须经人工合并的 merge request 进入，运行记录由 lab_run.py 写入。安装为 git clone 加 bootstrap/setup 脚本，需 Claude Code、Python 3.10+、Node.js 与 rsync；无实验室 GitLab 访问也可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 67 个技能/13 个 agent/9 个钩子组织研究闭环的八个阶段
- 知识库为纯 git：一棵树同时是 Obsidian vault 与 GitLab 知识库
- paper-ingest：arXiv→BibTeX（外部 API，非 LLM 生成）→Zotero→Obsidian 笔记
- push 到 main 对所有人禁用，改动经人工合并的 merge request

## 适用场景

- 科研团队为 Claude Code 部署整套研究工作流配置
- 用 git 版本化管理论文、声明与实验记录
- 自动摄取 arXiv 论文到 Zotero 与 Obsidian 阅读笔记

## 场景标签

`科研工具` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L26: The repository is the lab's own configuration, packaged so another lab can install it. Claude Code
> L34: Eight stages, one loop, with the lab GitLab at the centre. Each stage is a handful of skills you
> L95: |**Skills**|67|the working units: literature, experiments, Obsidian, code, writing, review|`skills/`|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `13bbf452d055` · [字段定义](../../DATASET.md)*
