# mintuz/skills

⭐ 29 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/mintuz/skills) · 个人维护

**面向 Web/iOS 开发者的可复用 agent 技能合集（Codex/Claude/OMP）**

一套以 Markdown 指令形式编写的开发技能合集，可安装到 Codex、Claude Code 与 OMP 三种 agent 宿主中使用。核心技能包括：按请求匹配 playbook 并委托执行与验证的 adam-mode、通过多轮构建者/评审者把单一产物打磨到标准的 gauntlet-loop、生成并评审多个候选方案的 arena、由标签种子推导配色排版的 creative-seed、做行为账本式最小化重构的 reducer，以及先写失败测试的 yagni 和只读的 how/why 代码解释。另含 54 个改编自 pstack 的原则技能，并提供 Go 脚本生成扁平目录以接入其他技能加载器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- adam-mode 将请求匹配到 13 类 playbook 并在可逆操作上自动继续、危险操作前停止
- gauntlet-loop 多轮构建-评审直到达到确认的标准
- arena 生成多个独立候选并按统一 rubric 合成
- Go 脚本 codex-sync.go 生成扁平技能目录，兼容其他技能加载器

## 适用场景

- 在 Claude Code/Codex/OMP 中按名称调用工作流技能处理评审、实现、排障
- 对 UI 方案做多候选生成与单轮评审择优
- 对既有系统做行为不变的最小化重构
- 解释代码现状与存在原因

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Development Skills
> L3: Reusable development skills for Codex, Claude and OMP. The new workflow and principle skills use portable Markdown i
> L25: Keep each complete skill directory, including references. For the 54 skills adapted from pstack (7 core workflows a

## 星数曲线

```mermaid
xychart-beta
    title "mintuz/skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d6ba43b5dda7` · [字段定义](../../DATASET.md)*
