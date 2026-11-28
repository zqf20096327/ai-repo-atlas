# musicalbee/design-ontology

⭐ 3 · HTML · MIT · 推送 2026-11-25 · [GitHub](https://github.com/musicalbee/design-ontology) · [官网](https://musicalbee.github.io/design-ontology/demo/) · 个人维护

**面向 coding agent 的设计风格数据集：551 种风格编译为可加载的技能文件**

以数据形式收录 16 个领域共 551 种设计风格（Bauhaus、visionOS 等），每条风格是含哲学、指令、反向模式、五维向量、色板、字型体系与 16 个必需 CSS token 的结构化记录，由编译器生成 SKILL.md 与 tokens.css。无运行时、无 API key。Claude Code 与 Cursor 各有单文件拉取命令，其他 agent（Windsurf/Cline/Codex/LangGraph）可直接粘贴内容进上下文；SKILL_INDEX.md 按触发词、用例、向量分路由选择风格。附带风格谱系图与 npm run icons 图标打包流程。

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

- 551 种风格、16 领域，JSON 编译为 SKILL.md + tokens.css
- 每风格固定 16 个 CSS token，可互相替换换肤
- 谱系图记录派生/拒绝关系，支持'更软/更大胆'路由到邻近风格
- 编译器自动派生对比度达 4.5:1 的文字色并生成 hero/pattern/icons 资源

## 适用场景

- 让 agent 按指定风格（如 neo-brutalism）生成落地页
- 给 cursor rules 加入可执行的设计规范
- 同一页面切换 data-style 快速换肤对比风格

## 场景标签

 · 领域:设计/agent 技能数据

## 证据(README 行号)

> L5: ** 551 styles in 16 domains, as data. Each one compiles into a skill that any coding agent can load.**
> L6: Bauhaus to visionOS. JSON in, `SKILL.md` + `tokens.css` out. No runtime, no API key, no lock-in.
> L21: This repository holds the rules. A style here is not a mood board and not a paragraph of adjectives. It is a record


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `cfdbc4515dfb` · [字段定义](../../DATASET.md)*
