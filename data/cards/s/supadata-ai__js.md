# supadata-ai/js

⭐ 22 · TypeScript · 推送 2026-10-16 · [GitHub](https://github.com/supadata-ai/js) · [官网](https://supadata.ai) · 组织维护

**Supadata 网页/视频抓取 API 的官方 TypeScript SDK**

面向 JavaScript/TypeScript 开发者的官方 SDK，封装 Supadata 云 API：获取 YouTube、TikTok、Instagram、Twitter 等平台的媒体元数据与字幕转录、翻译转录，用 AI 从视频内容抽取结构化数据（可用 prompt 自动确定 schema），并支持网页抓取。需在 supadata.ai 注册获取 API key；数据获取与 AI 处理均由远端 API 完成，SDK 提供类型定义与 SupadataError 错误处理。以 npm 包形式安装，附示例目录与 MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多平台媒体元数据与字幕转录获取（YouTube/TikTok/Instagram/Twitter）
- 基于 AI 的视频内容结构化抽取（prompt 或自定义 schema）
- 网页内容抓取与转录翻译接口
- SupadataError 错误类型与示例目录

## 适用场景

- 在 Node/前端项目中集成 YouTube 字幕获取
- 批量抓取网页内容供 LLM 处理
- 用自然语言 prompt 从视频抽取结构化数据

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L6: The official TypeScript/JavaScript SDK for Supadata.
> L8: Get your free API key at supadata.ai and start scraping data in minutes.

## 星数曲线

```mermaid
xychart-beta
    title "supadata-ai/js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `844baca30fa0` · [字段定义](../../DATASET.md)*
