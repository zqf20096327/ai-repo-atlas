# halo-dev/upage

⭐ 555 · TypeScript · NOASSERTION · 推送 2026-09-23 · [GitHub](https://github.com/halo-dev/upage) · [官网](https://upage.cn) · 组织维护 · 中文 README

**自然语言生成网页的可视化构建平台，代码可导出**

UPage 是基于大语言模型的可视化网页构建平台：用户以自然语言描述需求，生成个性化网页，并提供所见即所得的可视化编辑器与实时预览。支持多页面一键生成、响应式全端适配，自动生成规范 HTML/CSS/JS 代码并支持自由导出。LLM 接入采用 OpenAI 兼容规范，可配置默认模型、次要模型与可选视觉 sidecar 模型。部署方式为 Linux 服务器上 Docker 一键运行，也可通过 1Panel 应用商店安装；另有网页版 upage.cn。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言描述需求生成网页，可视化编辑器实时预览
- 多页面一键生成与响应式全端适配
- 生成标准 HTML/CSS/JS 代码，支持自由导出
- 兼容 OpenAI 规范 API，支持配置默认/次要/视觉模型

## 适用场景

- 用自然语言快速搭建个人或项目网站
- 生成规范代码后导出到现有项目二次开发
- 配合本地模型（如 Ollama）自托管生成服务

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L9: UPage 是一款基于大语言模型的可视化网页构建平台，支持接入主流大模型，只需通过自然语言描述需求，即可快速生成个性化、高颜值的网页，让创作更高效、更智能。
> L32: - `-e LLM_PROVIDER=OpenAI`：设置默认的 LLM 提供商为 OpenAI，同时兼容支持 OpenAI 规范的 API 接口。
> L33: - `-e PROVIDER_BASE_URL=your-provider-base-url`：设置 LLM 提供商的 API 基础 URL，部分提供商需要设置此项，例如 Ollama、LMStudio、OpenAI 提供商可选此

## 星数曲线

```mermaid
xychart-beta
    title "halo-dev/upage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 554 --> 556
    line [555, 555]
```

2026-10-18 555 → 2026-10-22 555（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `62543dbc8781` · [字段定义](../../DATASET.md)*
