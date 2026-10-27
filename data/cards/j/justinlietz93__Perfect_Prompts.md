# justinlietz93/Perfect_Prompts

⭐ 23 · Python · MIT · 推送 2026-08-24 · [GitHub](https://github.com/justinlietz93/Perfect_Prompts) · 组织维护

**文件系统优先的提示词/Agent 资产库，附桌面搜索应用**

存放提示词、规则、标准、角色设定与技能包等资产的可检索库，资产以普通文件形式存在于仓库目录中，可在文件管理器、编辑器或 Git 中直接浏览复制，无需专用数据库。另提供同名桌面应用，基于 SQLite FTS5 本地索引（Prompt Beacon）实现前缀/短语搜索、BM25 排序、批量查询与 GUI 增删管理，索引库可随时删除重建。通过仓库根目录的 python install.py 安装并创建原生启动器，另有 CLI 用于同步、查询与增删。当前版本 v2.0.2，开发已迁移至 Neuroca, Inc 组织。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 资产以文件系统形式存储，GUI 与文件双向同步，无私有应用存储
- 桌面应用提供 SQLite FTS5 索引、BM25 排序、过滤与批量查询
- 支持 Python/TypeScript/Rust/Go/JSON 等多种运行时表示
- 安装后附 CLI（sync/query/batch/add/remove）

## 适用场景

- 浏览和复用提示词、Agent 指令与技能包
- 用桌面应用对大型提示词库做全文检索与批量查询
- 在应用代码中直接引用运行时绑定的提示词实现

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: Perfect Prompts is a searchable library of prompts, rules, standards, and agent assets that lives in the filesystem 
> L9: Your personal filesystem-first library for **prompt engineering, context engineering, agent control, reusable AI wor
> L116: The corpus includes multiple generations of material developed through active use, including:

## 星数曲线

```mermaid
xychart-beta
    title "justinlietz93/Perfect_Prompts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e3fba78a99ab` · [字段定义](../../DATASET.md)*
