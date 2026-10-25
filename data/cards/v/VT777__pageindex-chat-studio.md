# VT777/pageindex-chat-studio

⭐ 41 · Python · MIT · 推送 2026-06-30 · [GitHub](https://github.com/VT777/pageindex-chat-studio) · 个人维护 · 中文 README

**AI 文档工作台：复杂文档结构化索引与带引用溯源的问答**

基于 PageIndex 构建的文档理解与问答应用（FastAPI 后端 + Vue 前端，Docker Compose 一键部署）。先为 PDF 等文档构建可视化 TOC 与来源锚点，再由 LLM 驱动的 flat_tool_loop Agent 通过 9 个有界工具（浏览文档、读页、取图、表格聚合、AnySearch 网络搜索等）逐步读取证据作答，引用可回溯到页、段、表格区间或图片。支持 OCR/VLM、多格式解析、多模型提供商配置与 UI 内设置。面向需要可核查文档问答的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层 TOC 构建按内容形态路由（文本文档/扫描件/混合 PDF），控制成本
- LLM Agent 工具循环，9 个有界工具，过程与引用经 SSE 流式可见
- OCR/VLM 解析扫描件与图片型 PDF，视觉模型可直读页面图像
- 引用绑定到文档、页、表格区间、图片或网页来源

## 适用场景

- 对 PDF、扫描件、表格、幻灯片等文档做可溯源的问答
- 在可视化 TOC 中检查文档结构并跳转原始页面证据
- 结合网络搜索回答需要外部实时信息的问题

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: PageChat is an AI document workspace for complex document understanding, structured indexing, and source-grounded qu
> L56: PageChat uses `flat_tool_loop` by default. It is not a fixed stage machine, nor a backend-hardcoded workflow of “pl
> L100: +-- backend/                 FastAPI backend service

## 星数曲线

```mermaid
xychart-beta
    title "VT777/pageindex-chat-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `384f60ec064d` · [字段定义](../../DATASET.md)*
