# designready-ai/designready-ai

⭐ 16 · TypeScript · MIT · 推送 2026-04-29 · [GitHub](https://github.com/designready-ai/designready-ai) · 组织维护

**为设计师生成 Claude 可用代码提示词的 Figma 插件**

在 Figma 内运行的插件：对组件按 6 维度（命名/结构/Tokens/Meta/完整度/变体）打 AI 就绪度分，分数达 75+ 后生成结构化代码提示词，粘贴给 Claude 生成组件代码；提示词附带 Skill Sync 指令，让 Claude 维护随扫描迭代的设计系统技能文件。另提供 Auto Layout 修复、快捷修复、原子组件分类（atom/molecule/organism）、批量扫描与提示注入防护。通过 git clone + npm 构建、Figma 开发模式加载，无打包安装版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 维度加权评分（结构 22%、命名/Tokens 各 18% 等）
- 75+ 分后生成含完整组件规格与自检块的代码提示词
- Skill Sync 让 Claude 自动创建并迭代设计系统技能文件
- 原子设计分类与批量扫描按 atoms→molecules→organisms 排序

## 适用场景

- 在交给 AI 写代码前检查 Figma 组件的规范化程度
- 把设计系统组件批量转成结构化提示词让 Claude 生成代码
- 维护随每次扫描自动更新的设计系统技能文件

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L26: - **6-Dimension Scoring** — Naming, Structure, Tokens, Meta, Completeness, Variants
> L43: 3. **Copy the prompt** — Once score is 75+, copy the prompt and paste it into Claude. The prompt contains everythin
> L31: - **Auto Layout Fix** — Confidence-based analysis + one-click apply (bottom-up, skips icons/overlaps). Frames below

## 星数曲线

```mermaid
xychart-beta
    title "designready-ai/designready-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6a34574711e4` · [字段定义](../../DATASET.md)*
