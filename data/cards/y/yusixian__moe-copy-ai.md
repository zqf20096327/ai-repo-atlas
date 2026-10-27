# yusixian/moe-copy-ai

⭐ 144 · TypeScript · AGPL-3.0 · 推送 2026-04-03 · [GitHub](https://github.com/yusixian/moe-copy-ai) · [官网](https://moe.cosine.ren/docs) · 个人维护 · 中文 README

**AI 网页数据提取浏览器扩展：结构化抓取并生成 AI 摘要**

基于 Plasmo 框架、使用 xsAI SDK 的浏览器扩展，面向需要在浏览网页时提取干净结构化内容的用户。提供弹窗与侧边栏两种模式：智能识别文章主体、标题、作者，支持 CSS 选择器、Readability 与混合三种抓取模式，输出 Markdown 原始版与紧凑版，带字数与 token 估算；侧边栏支持批量链接抓取、正则过滤与 ZIP 导出。AI 部分为基于 xsAI 的可配置提供商摘要功能，支持自定义提示词与历史记录。作者自述处于早期开发阶段、以纯工具 side project 为主。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三种抓取模式（CSS 选择器 / Readability / 混合）与双版本输出
- 侧边栏批量抓取：可视化选区、正则过滤、分页翻页、ZIP 导出
- 基于 xsAI 的 AI 摘要：自定义提示词、模型选择、历史记录
- 页面元数据与图片提取、字数与 token 统计

## 适用场景

- 浏览网页时一键复制干净的正文、标题与元信息
- 批量抓取多个链接的文档内容并打包导出
- 抓取网页内容后直接调用 AI 生成摘要

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L9: Moe Copy AI 是一个基于 Plasmo 框架，使用 xsAI SDK 开发的浏览器扩展，能够智能识别并提取网页中的结构化数据，为 AI 模型提供高质量输入。
> L49: - **AI 内容摘要**:
> L84:  - 基于 xsAI 提供 AI 提供商配置功能

## 星数曲线

```mermaid
xychart-beta
    title "yusixian/moe-copy-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 143 --> 145
    line [144, 144]
```

2026-10-18 144 → 2026-10-27 144（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `4a6e3b0df0ab` · [字段定义](../../DATASET.md)*
