# findscripter/everything-skills

⭐ 12 · Python · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/findscripter/everything-skills) · [官网](https://findscripter.github.io/everything-skills/) · 个人维护 · 中文 README

**按任务查找/组合/安装 Agent Skills 的技能目录与索引工具**

以目录形式聚合 1,115 个技能文件夹（1,094 个现行、21 个归档、1 个模板），按 11 个卷组织，含 6,797 条关系边；另收录 4,700 条外部技能仓库索引条目（不捆绑技能本体）。提供 CLI 本地搜索（search/why/compose/show 命令）、Claude Code 插件市场安装与 skills CLI 单技能安装两种途径；compose 仅返回组合计划不执行。README 要求阅读各技能自身的许可与运行时依赖，部分条目审查状态标记为 unknown/unreviewed。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,115 个捆绑技能按 11 卷分类，6,797 条关系边（requires/related/combines_with）
- Node.js CLI 提供本地搜索与技能关联查询，无第三方依赖
- 支持 Claude Code 插件安装与 skills CLI 按单技能安装（Codex/Cursor/Gemini CLI 可用导航文件）
- 4,700 条外部技能仓库目录按 6 类组织，含许可与审查状态元数据

## 适用场景

- 按交付物（审查补丁、诊断报告）查找并组合可用的 agent 技能
- 在 Claude Code 或 Codex 项目中按卷/按技能安装技能包
- 浏览 4,700 条外部技能仓库索引了解生态覆盖

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L13:  1115 skills · 11 volumes · 6797 relation edges · 4700 indexed entries
> L9:  Skill catalog · Knowledge graph · Skill repositories · Contributing
> L139: **4700 external repository entries** provide discovery metadata for upstream projects. Their skill bodies are not 

## 星数曲线

```mermaid
xychart-beta
    title "findscripter/everything-skills 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-27"]
    y-axis "stars" 10 --> 13
    line [11, 12]
```

2026-11-10 11 → 2026-11-27 12（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `263bf2ad5b34` · [字段定义](../../DATASET.md)*
