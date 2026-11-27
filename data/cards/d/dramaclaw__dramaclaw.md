# dramaclaw/dramaclaw

⭐ 7,213 · TypeScript · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/dramaclaw/dramaclaw) · [官网](https://dramaclaw.ai) · 组织维护 · 中文 README

**自托管 AIGC 视频引擎：剧本到成片一条流水线**

自托管的 AI 短剧/视频生产流水线：内置 Xia Director 智能体规划并执行画布工作流、XiaHua 无限画布（图像/视频/音频/3D/交互故事节点）与 Series 系列流水线（结构化解析剧本、分集规划、分镜、配音、剪辑导出）。通过 OpenAI 兼容网关接入任意模型，模型推理在网关侧运行，本地无 GPU/数据库/队列要求，状态存本地磁盘。以 Docker Compose 发布镜像部署，另支持源码 Docker 与本地开发模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Xia Director 智能体：自然语言简报→画布节点图→确认后执行，支持失败恢复
- 无限画布统一图像、视频、音频、3D、交互故事、网页等节点类型
- 系列流水线：剧本结构化、分镜生成、情感配音、成片导出，支持断点续跑
- 通过 MCP（Agent Kit）向 Codex、Claude Code 等外部智能体开放工作流

## 适用场景

- 从小说或剧本批量生成分集短剧并导出成片
- 制作电商与 IP 角色广告等社媒视频内容
- 生成分支叙事的互动故事并导出独立播放器
- 在画布上用 3D 预演舞台先定机位与走位再生成视频

## 场景标签

`视频生成` `图像生成` `多模态` · 领域:内容生成

## 证据(README 行号)

> L61: DramaClaw is a **self-hostable production line for AI drama**: from manuscript to finished episodes, and from a one
> L65: - **Series (XiaJi)** — the pipeline. Drop in a novel or screenplay; DramaClaw structures the story, writes scripts,
> L67: Bring any model through an OpenAI-compatible gateway, run it on your own machine, and keep your material.

## 星数曲线

```mermaid
xychart-beta
    title "dramaclaw/dramaclaw 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 6297 --> 7902
    line [6430, 6449, 6470, 6497, 6545, 6573, 6659, 6728, 6841, 6430, 7386, 7662, 7679, 7686, 7699, 7705, 7716, 7732, 7742, 7758, 7769, 7590, 7152, 7156, 7169, 7199, 7213]
```

2026-10-25 6,430 → 2026-11-27 7,213（+783）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `669668a2f7ed` · [字段定义](../../DATASET.md)*
