# OpenGHz/embodied-ai-paper-writer

⭐ 15 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/OpenGHz/embodied-ai-paper-writer) · 个人维护 · 中文 README

**具身智能顶会论文写作技能包：从63篇论文提炼写作范式**

以 SKILL.md 格式分发的 agent 技能：从 CoRL/RSS/ICRA/IROS/Science Robotics 的 63 篇论文（2022–2026）中提炼量化写作规则（摘要结构与字数、图表标题模板、贡献短语复现次数等），把可加载 markdown 上下文的 LLM agent（Claude Code、Cursor 等）变为论文写作教练。含 8 个操作 playbook 与 9 个可溯源研究文件，定义 5 种执行场景（新写、修改、问答、图注、全文弧线检查）。明确边界：仅涉及写作规范，不判断可发表性或实验设计；默认按 CoRL 校准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 63 篇顶会论文语料提炼的量化写作规则（每条可溯源）
- SKILL.md + 8 个 playbook 的双层结构，按需路由加载
- 5 种执行场景覆盖新写/修改/图注/全文审阅
- 通过 npx skills add 一条命令安装到任意 agent

## 适用场景

- 撰写或润色 CoRL/ICRA 等具身智能论文的摘要、Intro、图注
- 按顶会惯例检查论文整体叙事弧线与措辞
- rebuttal 与 Limitations 段落写作参考

## 场景标签

`AI 写作` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: > A portable agent skill (SKILL.md + reference playbooks) that coaches the **writing craft** of embodied-AI papers —
> L30: - "Abstract = 120–250 words, 5 moves (Frame → Gap → Contribution → Method → Results)."
> L95: - **Sample**: 63 papers, 2022–2026, CoRL / RSS / ICRA / IROS / Science Robotics. NeurIPS / ICML robotics tracks are

## 星数曲线

```mermaid
xychart-beta
    title "OpenGHz/embodied-ai-paper-writer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `511526d261af` · [字段定义](../../DATASET.md)*
