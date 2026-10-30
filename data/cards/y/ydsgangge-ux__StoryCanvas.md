# ydsgangge-ux/StoryCanvas

⭐ 18 · TypeScript · 推送 2026-09-23 · [GitHub](https://github.com/ydsgangge-ux/StoryCanvas) · 个人维护 · 中文 README

**画布式叙事创作系统：作者在自由画布上组织故事结构，AI 生成正文**

面向小说/剧本/世界构建作者的自托管 Web 应用：作者在 React Flow 画布上摆放 35 种叙事块、用 8 种连线组织结构（因果/时序/铺垫/回收等），系统将结构转化为 AI 上下文，经五层 Agent 管线生成章节细纲与正文，并输出 12 维度审计清单。支持 DeepSeek/OpenAI/Claude/Gemini/Ollama/自定义 6 种提供商，提供快照回滚、多时间线、铺垫追踪与 Markdown/JSON 导出。前后端分置（React+FastAPI+SQLite），需自行部署运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 35 种块类型 + 8 种连线类型的画布式叙事结构编辑
- 五层 Agent 管线 SSE 流式生成章节细纲与正文
- 支持 6 种 LLM 提供商（含 Ollama 本地）并带一键连接测试
- 三层快照体系（实时保存/15 分钟自动快照/手动检查点）与铺垫追踪、信息边界检测

## 适用场景

- 在空间化画布上搭建长篇小说或剧本的世界观与角色关系
- 让 AI 依据画布结构生成章节细纲和正文并迭代修订
- 追踪多线叙事中的伏笔回收与角色信息边界

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: > **在画布上摆放、连接、组织叙事元素，AI 协助你将结构转化为高质量正文。**
> L460: |POST|`/api/projects/{id}/generate/chapter-content`|生成章节正文（五层 Agent 管线）|
> L494: 系统支持 6 种 LLM 提供商，通过 Web UI 或 `.env` 配置。

## 星数曲线

```mermaid
xychart-beta
    title "ydsgangge-ux/StoryCanvas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e0f17378768b` · [字段定义](../../DATASET.md)*
