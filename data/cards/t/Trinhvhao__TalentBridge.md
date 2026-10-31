# Trinhvhao/TalentBridge

⭐ 13 · JavaScript · MIT · 推送 2025-11-12 · [GitHub](https://github.com/Trinhvhao/TalentBridge) · 个人维护

**面向越南学生的 AI 求职平台：CV 解析与职位语义匹配**

面向越南学生的求职 Web 平台，基于 FastAPI 后端与 Vanilla JS 前端。核心机制：上传 PDF 简历后由 Google Gemini 2.5 Flash 解析为结构化 JSON 并评分（质量/市场匹配/完整度），用 Gemini text-embedding-004 生成 768 维向量，经 ChromaDB 做语义职位匹配，内置 TopCV 的 3,237 条职位数据；Dashboard 提供 6 类统计图表与 AI 分析。运行需配置 Google API key（建议 3 个以提升配额），本地通过 python main.py 启动。认证、聊天机器人等功能在 Roadmap 中未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini 2.5 Flash 将 PDF 简历解析为结构化 JSON 并三维度评分
- text-embedding-004 生成 768 维向量 + ChromaDB 语义职位匹配与 AI 排序
- 内置 TopCV 来源的 3,237 条职位数据与 6 类市场统计图表
- 全越南语界面，FastAPI 后端提供 Swagger API 文档

## 适用场景

- 上传简历后获得匹配度评分与改进建议
- 按地点、薪资、经验筛选并获取语义匹配的职位推荐
- 查看越南就业市场统计图表并获取 AI 分析

## 场景标签

`语义搜索` `推荐系统` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L13: **✨ Sử dụng AI để phân tích CV, gợi ý việc làm phù hợp và đánh giá chất lượng hồ sơ ✨**
> L96: - **🤖 AI Parse** - Gemini AI tự động đọc và trích xuất thông tin
> L131: - **🎯 AI Ranking** - Gemini AI xếp hạng độ phù hợp (0-100%)

## 星数曲线

```mermaid
xychart-beta
    title "Trinhvhao/TalentBridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c7d242bf7101` · [字段定义](../../DATASET.md)*
