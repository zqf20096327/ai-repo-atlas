# bryan-shea/Annotative

⭐ 13 · TypeScript · MIT · 推送 2026-04-05 · [GitHub](https://github.com/bryan-shea/Annotative) · [官网](https://marketplace.visualstudio.com/items?itemName=bryan-shea.annotative) · 个人维护

**VS Code 扩展：结构化标注 markdown 计划、AI 回复与本地 diff 并导出反馈**

面向开发者的 VS Code 扩展，围绕持久化 AI 审查工作流：对 markdown 计划、AI 回复文本和本地 git diff 生成可持久化的审查工件，在侧面板中按工件/节/块/diff hunk 添加结构化反馈（修改要求、风险、问题、缺失步骤、测试缺口），跟踪 open/resolved 状态并导出为 Markdown 或面向 AI 的提示词。支持代码内标注、自定义标签、过滤分组等侧边栏工作流，数据存于项目本地 .annotative/ 目录。可选集成 GitHub Copilot Chat 的 @annotative 参与者，提供 /issues /explain /fix /review 命令。要求 VS Code 1.105.0+，diff 审查需 Git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个持久化审查工作流：Review Markdown Plan / Review Last AI Response / Review Local Diff
- 结构化反馈（修改要求、风险、问题、缺失步骤、测试缺口）与 open/resolved 状态跟踪
- 导出为 Generic Markdown 或 Copilot Review Prompt，按意图（review/bugs/optimization/documentation）导出
- 可选注册 @annotative Copilot Chat 参与者

## 适用场景

- 在实现前审查 markdown 计划并记录结构化意见
- 审查 AI 生成的回复并转为后续提示词
- 对本地 git diff 添加持久化的针对性审查笔记

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: Annotative is a VS Code extension for persistent AI review workflows—review markdown plans, AI responses, and local 
> L24: - Export review artifacts as readable Markdown or Copilot-ready prompts
> L117: When GitHub Copilot Chat is installed and `annotative.copilot.enabled` is enabled, Annotative registers an `@annot

## 星数曲线

```mermaid
xychart-beta
    title "bryan-shea/Annotative 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6d50b8f66609` · [字段定义](../../DATASET.md)*
