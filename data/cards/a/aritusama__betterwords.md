# aritusama/betterwords

⭐ 18 · MIT · 推送 2026-10-14 · [GitHub](https://github.com/aritusama/betterwords) · 个人维护

**给 AI 写作用户的文风规则技能：改进草稿与编辑质量**

以单个规则文件 betterwords.md 为核心的写作质量系统，包含 72 条编号规则、操作说明与自检清单，覆盖起草、改写、编辑与审计。通过跨 agent 的 Skills CLI（npx）安装为技能，也可作为 Codex 插件、Claude 技能/插件、Gemini CLI 扩展、GitHub Copilot 仓库指令加载；无技能支持的宿主可直接使用规则文件。规则来源包括 Elements of Style、Orwell、ASD-STE100 及多项 AI 文风研究。项目声明其不能判定文本由人还是模型写作，不用于作者身份标注。MIT 许可。

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

- 核心产物为单个规则文件 betterwords.md，含 72 条编号规则与自检清单
- 支持多种宿主加载：Skills CLI、Codex 插件、Claude、Gemini CLI、Copilot 指令
- 明确声明不做作者身份判定，不用于规避披露要求

## 适用场景

- 让 AI 按规则集改进我的草稿或发布说明的写作质量
- 对已有文本做编辑质量审计并保留规则编号引用
- 在不支持技能的宿主中直接以 betterwords.md 作为写作规则

## 场景标签

`AI 写作` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: `betterwords.md` is the product. The skill, plugin manifests, and platform notes are convenience methods for loading
> L53: Before starting, read the complete rule file, including the operating notes, all 72 numbered rules, and final self-

## 星数曲线

```mermaid
xychart-beta
    title "aritusama/betterwords 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6afcac818980` · [字段定义](../../DATASET.md)*
