# marc-ing/article-image-generator

⭐ 15 · TypeScript · 推送 2026-08-21 · [GitHub](https://github.com/marc-ing/article-image-generator) · 个人维护 · 中文 README

**本机 Markdown 文章配图工作台：规划并生成首图与章节图**

本地运行的 Web 工作台，四步流程（上传→规划→生成→导出）：上传 UTF-8 Markdown 后用确定性规则识别插图锚点，由文本模型完善摘要与 alt 文本；用户在规划阶段统一设置首图/章节图尺寸、风格与来源，确认后通过 OpenAI-compatible Images API 并行生成图片，最后导出含新 Markdown 与 images/ 的 ZIP。API Key 仅存本机 data/private-settings.json，或经环境变量提供。需 Node.js 22+，从源码运行；v0.4.0 已冻结为 Local-first Web MVP，不再维护 Codex 插件形态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规划与 AI 执行严格分离，确认方案前不调用图片生成服务
- 通用 OpenAI-compatible 连接，文本分析与图片生成分别配置模型 ID
- 每张图片可独立重新生成或用本地上传替换
- 导出不覆盖原文，生成带图片引用的 Markdown ZIP

## 适用场景

- 为技术文章批量规划并生成首图和章节配图
- 在配图计划中逐图选择 AI 生成、本地上传或跳过
- 使用自选的 OpenAI 兼容网关在本地完成配图工作流

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Article Image Gen 是一个本机运行的 Markdown 文章配图工作台。上传文章后，它会先分析结构并给出可编辑的配图计划；用户在规划步骤统一确认首图与章节图尺寸、位置、风格和来源，确认后直接开始生成，最后导出包含新 
> L19: - 使用兼容 Images API 的服务真实生成图片，多张图片并行执行

## 星数曲线

```mermaid
xychart-beta
    title "marc-ing/article-image-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `056bc863cfa9` · [字段定义](../../DATASET.md)*
