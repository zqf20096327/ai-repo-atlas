# MarcosNahuel/antigravity-plugin-cc

⭐ 32 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/MarcosNahuel/antigravity-plugin-cc) · [官网](https://traidagency.com/labs/antigravity) · 个人维护

**Claude Code 插件：经 agy 调用 Gemini 做文档综合、转录与深度研究**

一个 Claude Code 插件，通过 Google Antigravity CLI（agy，Gemini 3.x）把文档阅读、网络检索等重负载工作从 Claude 的上下文转移出去。核心命令 /agy:notebook 将整个文件夹的文档（PDF/扫描件/图片/docx，多模态 OCR）生成为逐文档摘要、相关性索引、带引用的综合报告、时间线与实体表，并编译为可 SQL 查询的 SQLite 知识库（FTS5）；另有音频视频转录、多智能体深度研究（证据矩阵+红队环节）等 22 个斜杠命令。需本机安装 agy CLI 并登录 Google 账号，无需 Node.js 运行时；状态标注为 alpha。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 文件夹级文档综合：逐文档摘要+相关性索引+带引用的 RESUMEN_MAESTRO
- 知识库命令将 facts.json 编译为可 SQL 查询的 SQLite（FTS5，仅 Python 标准库）
- 音频/视频转录与多模态问答（含 YouTube URL），Gemini 执行
- 多智能体深度研究：证据矩阵+计划门控+自适应轮次+红队环节

## 适用场景

- 在 Claude Code 内对一批 PDF/合同/会议记录做带引用的综合与追问
- 让 Claude Code 处理音频/视频内容（转录、按时间点提问）
- 执行带引用的多角度网络深度研究并输出报告

## 场景标签

`多智能体` `语音识别` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **A local NotebookLM, multi-agent deep research, and 21 more commands — for Claude Code, powered by Google Antigra
> L23: **TL;DR** — `/agy:notebook <folder> | <objective>` turns a folder of documents into a **local NotebookLM**: one obj
> L140: |`/agy:notebook <folder> \|<objective>`|**Local NotebookLM.** Sweeps every document in a folder (PDF/scan/image/do

## 星数曲线

```mermaid
xychart-beta
    title "MarcosNahuel/antigravity-plugin-cc 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26", "2026-10-30"]
    y-axis "stars" 29 --> 33
    line [30, 31, 32, 32]
```

2026-10-18 30 → 2026-10-30 32（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `a2dd584275be` · [字段定义](../../DATASET.md)*
