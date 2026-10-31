# sa-san10/nyamuru-manga-name-studio

⭐ 34 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/sa-san10/nyamuru-manga-name-studio) · [官网](https://sa-san10.github.io/nyamuru-manga-name-studio/) · 个人维护

**与 LLM 和图像生成 AI 配合创作漫画分镜稿的开源 PWA 工作室**

基于 Astro/Preact 的 PWA，用纸面预览和结构化表单编辑漫画分镜稿（ネーム），数据以 Nyamuru Data Model（NDM）的 YAML 表示形式 OMNY 编写。图像生成的作画规则由独立 OMAY 文件管理，改写 meta.style_notes 即可换画风而保留页面结构。内置将故事原稿结构化为 OMNY 的 LLM 完整提示词、面向 AI agent 的漫画生成工作流文档；应用本身不直接运行模型。可在浏览器（GitHub Pages）使用，或下载单文件 HTML 离线运行。界面与文档仅日语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OMNY（NDM 的 YAML 形式）分镜稿的结构化编辑与纸面预览
- 作画规则独立为 OMAY 文件，meta.style_notes 换画风且保留页面结构
- 内置 LLM 分镜生成提示词与 AI agent 漫画生成工作流文档
- 单文件 HTML 离线运行，编辑内容自动保存至浏览器本地存储

## 适用场景

- 用结构化表单编写和管理漫画分镜稿
- 把分镜数据连同提示词交给 LLM 与图像生成 AI 产出成稿
- 通过更换画风格指定从同一份分镜数据生成不同风格版本

## 场景标签

`AI 写作` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L47: > - Storyboards are written in **Open Manga Name YAML (OMNY)**, a YAML representation of the **Nyamuru Data Model (
> L65: このPWAでは、NDMをYAMLで表現する **Open Manga Name YAML（OMNY）** 形式の漫画ネームを、紙面プレビューと構造化フォームで閲覧・編集できます。内蔵サンプルを初期データとして読み込み、NDM v1

## 星数曲线

```mermaid
xychart-beta
    title "sa-san10/nyamuru-manga-name-studio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-31 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7342e4bef064` · [字段定义](../../DATASET.md)*
