# SenpaiSpide664/ai-visual-prompt-cookbook

⭐ 5 · HTML · MIT · 推送 2026-11-27 · [GitHub](https://github.com/SenpaiSpide664/ai-visual-prompt-cookbook) · 个人维护

**给图像生成者的可复用 JSON 风格提示词数据集**

以自包含 JSON 模板组织的 AI 图像生成风格数据集：每个风格一个目录，含 style.json（prompt_template、变量声明、示例、保真锚点、排除项、负面提示）与 16:9/9:16 两张预览图。渲染提示词在生成时由模板加变量派生而非存储，条目按 schema_version 2.1/2.2 版本化，每周更新。面向研究提示词图像合成的研究者与从业者，兼容 Nano Banana Pro、GPT Image、Midjourney 等模型，采用 CC BY 4.0 许可。

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

- 每个风格为自包含 style.json，可独立迁移到任何兼容多模态工作流
- prompt_template 加 values 在生成时派生渲染提示词，不存储渲染结果
- style_fidelity_anchors 与 source_content_to_avoid 约束风格不变量并避免复现参考素材
- 每周更新条目，变量契约变更反映在 schema_version

## 适用场景

- 为不同主题和构图复用同一风格定义生成一致图像
- 按类别（海报、拼贴、编辑排版等）浏览挑选视觉风格
- 在提示词图像合成研究中使用结构化风格数据

## 场景标签

`提示工程` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L1: # AI Visual Prompt Cookbook: Structured Style Prompt Collection — Dataset
> L7: The AI Visual Prompt Cookbook is a structured dataset of reusable style definitions for AI image generation, distrib


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `55f162b73e23` · [字段定义](../../DATASET.md)*
