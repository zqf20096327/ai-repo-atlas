# oguzhankayan/turkish-native

⭐ 89 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/oguzhankayan/turkish-native) · 个人维护

**写作原生土耳其语、消除翻译腔的 agent 技能包**

面向 agent 的土耳其语写作/编辑技能：以 SKILL.md 运行时指令和 references/ 详细规则包形式提供，用于改写 AI 生成与本地化文案中语法正确但句式外来的土耳其语。核心机制为 meaning-first 工作流（先定受众与语域、先修结构再改词汇、重建外语句式），含 57 个模式分类（六组）与 105 个回归用例及包结构/基准校验脚本。安装途径为 skills CLI（npx）、Claude Code 插件或手动复制文件。当前 v0.5.0，pre-1.0，模式命名与评估 schema 可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 57 个翻译腔模式分类（六组：句式架构、动词搭配、产品/本地化、营销文案、语域与忠实度、页面一致性）
- 105 个回归用例含正向对照，附包校验与基准校验脚本
- meaning-first 工作流：先结构后词汇，保留事实与术语
- 提供 npx / Claude Code 插件 / 手动复制三种安装方式

## 适用场景

- 审校 AI 生成或本地化的土耳其语文案，消除翻译腔
- 重写产品/UI/SaaS/营销文案为更自然的土耳其语
- 翻译到土耳其语时保留事实与术语但不保留英文句式

## 场景标签

`AI 写作` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: Turkish Native is an open-source agent skill for writing and editing natural Turkish. It targets a specific failure 

## 星数曲线

```mermaid
xychart-beta
    title "oguzhankayan/turkish-native 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-24 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `a8a83bd065b7` · [字段定义](../../DATASET.md)*
