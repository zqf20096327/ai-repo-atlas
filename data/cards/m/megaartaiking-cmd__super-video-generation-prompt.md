# megaartaiking-cmd/super-video-generation-prompt

⭐ 3 · MIT · 推送 2026-11-26 · [GitHub](https://github.com/megaartaiking-cmd/super-video-generation-prompt) · 个人维护

**面向视频生成 AI 用户的母提示词与工作流模板集**

一份以 Markdown 形式提供的可复制提示词文档：将 Meta Muse AI 视频生成模型用作长视频制作工具，包含一个需填写 [BRACKET] 占位符的主提示词、6 种风格包（Bollywood/Hollywood/anime/cartoon/印度/巴基斯坦剧集）、分批续接用的 per-clip 模板、三种故障修复提示词以及交付前质量检查清单。工作流核心是先生成并确认 Continuity Bible，再逐段从上一段末帧续接。文档明确声明不能保证零错误。

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

- 提供单一母提示词，含 Continuity Bible 与分批剪辑计划机制
- 6 种风格包可替换：Bollywood、Hollywood、anime、cartoon、印度剧、巴基斯坦剧
- per-clip 模板从上一段末帧续接，用于保持角色与场景一致
- 附带角色漂移、黑帧/静音、接缝跳变三类修复提示词与质量检查清单

## 适用场景

- 用 Meta Muse AI 分批生成有连贯角色的长视频
- 制作 anime/cartoon 风格的 YouTube Shorts 内容
- 视频出现黑帧或接缝跳变时按模板修复单个片段

## 场景标签

`提示工程` `视频生成` · 领域:Agent 开发

## 证据(README 行号)

> L3: A single copy-paste prompt that turns Meta Muse AI into a professional long-video director — with locked characters,
> L16: ## The Super Prompt — copy from here
> L88: This prompt removes the common causes of failure — vague character descriptions, clips started from scratch, unplan


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `ccecd351f207` · [字段定义](../../DATASET.md)*
