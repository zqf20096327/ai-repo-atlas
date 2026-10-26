# Ryson-32/AI-Magnet-Assistant

⭐ 207 · Vue · MIT · 推送 2026-06-14 · [GitHub](https://github.com/Ryson-32/AI-Magnet-Assistant) · 个人维护 · 中文 README

**聚合多引擎磁力链接并用 AI 筛选整理的桌面工具**

基于 Tauri + Rust 后端与 Vue 3 + TypeScript 前端的磁力链接搜索应用：内置引擎先行返回，其余引擎并行聚合；两阶段 AI 管线先用 Gemini 从自定义引擎的原始 HTML 抽取标题、链接、大小等字段，再做内容分析（标题清理、生成标签、计算 0–100 纯净度分）。支持收藏、优先关键词、按分数/大小排序与快速下载（快速下载仅 Windows）。后端当前仅支持 Google Gemini，OpenAI 选项尚未接线；从源码构建需要 Node.js 18+ 与 Rust。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多引擎并行聚合搜索，实时显示所用模型与进度
- 两阶段 AI 管线：HTML 抽取 + 标题清理/标签/纯净度评分
- 收藏、优先关键词、按分数或大小排序
- 支持自定义引擎（模板或从示例自动生成）

## 适用场景

- 一次关键词搜索多个磁力引擎并合并结果
- 用 AI 清理杂乱标题、打标签、评纯净度以减少人工筛选
- 收藏与集中管理磁力链接并快速下载

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L13: **AI Magnet Assistant** is an intelligent magnet link search and optimization tool. It aggregates results from mult
> L21:  - Two-stage AI: Stage 1 HTML extraction (for custom engines) → Stage 2 content analysis (title cleaning, tags, pur

## 星数曲线

```mermaid
xychart-beta
    title "Ryson-32/AI-Magnet-Assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 206 --> 208
    line [207, 207]
```

2026-10-18 207 → 2026-10-26 207（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b2137724f2f7` · [字段定义](../../DATASET.md)*
