# InternLM/HuixiangDou

⭐ 2,502 · Python · BSD-3-Clause · 推送 2025-11-24 · [GitHub](https://github.com/InternLM/HuixiangDou) · [官网](https://openxlab.org.cn/apps/detail/tpoisonooo/huixiangdou-web) · 组织维护 · 中文 README

**面向群聊场景的 LLM 专业知识问答助手（RAG 管线）**

基于 LLM 的专业知识助手：构建知识库后通过预处理、拒答、响应三阶段管线回答问题，支持群聊场景（不刷屏、指代消解）与实时流式对话两种管线。无需训练，提供 CPU-only/2G/10G 多模态三档配置；检索支持稠密检索、知识图谱、图文与网络搜索，可接入微信、飞书、OpenXLab Web 与 Android。提供 Web 前后端源码（多租户、k8s），由 pip 安装依赖并运行 Python 模块，Word 等格式解析需 apt 安装系列系统库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预处理-拒答-响应三阶段管线，群聊场景不刷屏
- 无需训练，CPU-only/2GB/10GB 多模态三档配置
- 支持微信、飞书、Web、Android、Gradio、HTTP API 多种接入
- 提供 Web 前后端源码，多租户管理，k8s 友好

## 适用场景

- 在微信群/飞书群里部署领域知识问答机器人
- 基于自有文档（md/pdf/word/ppt 等）搭建客服问答
- 本地部署带拒答机制的技术支持助手

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L29: HuixiangDou1 is a **professional knowledge assistant** based on LLM.
> L33: 1. Design three-stage pipelines of preprocess, rejection and response
> L34:  * `chat_in_group` copes with **group chat** scenario, answer user questions without message flooding, see 2401.087

## 星数曲线

```mermaid
xychart-beta
    title "InternLM/HuixiangDou 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 2501 --> 2503
    line [2502, 2502]
```

2026-10-18 2,502 → 2026-10-24 2,502（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1dd481ff92b4` · [字段定义](../../DATASET.md)*
