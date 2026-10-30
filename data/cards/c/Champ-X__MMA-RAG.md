# Champ-X/MMA-RAG

⭐ 18 · Python · 推送 2026-10-28 · [GitHub](https://github.com/Champ-X/MMA-RAG) · 组织维护 · 中文 README

**自托管多模态 RAG 工作台：统一检索文档/图片/音视频并给出带引用回答**

Tessmora（仓库沿用 MMA-RAG 名称）是可自托管的多模态 RAG 与 Agent 研究工作台：将文档、表格、图片、音频、视频汇入知识库，经解析、分块与多模态索引（MinIO 存原文件、Qdrant 存索引）后，提供混合检索（Dense、BGE-M3 Sparse、CLIP、CLAP）与重排、常规问答、以及基于 Pi Agent SDK 的自主研究 Agent Mode，回答带可追溯引用。提供 Web UI、REST API、CLI 与飞书接入。限制：默认模型调用依赖外部服务商 API（自托管不等于离线推理）；尚无用户鉴权与租户隔离，面向本机单用户；仓库未附 LICENSE 文件。安装走终端向导 + Docker Compose，或源码开发模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档/图片/音频/视频统一入库与多模态检索（BGE-M3、CLIP、CLAP 等通道融合重排）
- Pi Agent Mode 自主规划检索、深读与媒体观察，回答带引用与过程账本
- 终端向导 + Docker 完整安装，无需手动编辑 .env
- 提供 Web UI、检索/对话 API、CLI、Codex Skill 与飞书 IM 接入

## 适用场景

- 把研究资料、图片、音视频汇入一个可自托管的知识库做问答
- 让 Agent 围绕复杂问题多轮检索并整理带引用的证据
- 通过 API/CLI/飞书在已有工作流中调用多模态检索

## 场景标签

`RAG` `文档问答` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L20: **Tessmora 是可自托管的多模态 RAG 与 Agent 研究工作台。** 将文档、表格、图片、音频和视频放入知识库，用自然语言搜索、比较和提问，再通过原文、图片预览或媒体时间片段核对回答。仓库沿用 `MMA-RAG` 名
> L31: |**找到关键词之外的内容**|常规检索结合 Dense、BGE-M3 Sparse、CLIP、CLAP 等通道，按问题意图融合召回并重排；未指定知识库时可按主题画像路由|
> L32: |**围绕复杂问题持续研究**|独立的 Pi Agent Mode 自主选择搜索、深读原文、扩展上下文、查看媒体或计算表格，再提交带引用的回答|

## 星数曲线

```mermaid
xychart-beta
    title "Champ-X/MMA-RAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `9646b0f59b03` · [字段定义](../../DATASET.md)*
