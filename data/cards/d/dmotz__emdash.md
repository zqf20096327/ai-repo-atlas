# dmotz/emdash

⭐ 180 · Elm · GPL-3.0 · 推送 2026-07-10 · [GitHub](https://github.com/dmotz/emdash) · [官网](https://emdash.oxism.com) · 个人维护

**用设备端 AI 整理读书摘录与笔记的工具**

面向电子书读者的摘录管理应用：导入 Kindle 划线或 json/csv/手工输入的高亮片段，在设备端运行 AI 分析，提供概念相似段落发现（跨作者找相近观点）、全文与语义搜索、随机回顾、以及用比喻重新解释概念等功能；支持打标签、评分、批注并导出回 epub 或开放格式。分析在本地完成，数据留在设备上。需 npm install && npm start 从源码运行，面向愿意自部署的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端 AI 分析：跨作者寻找概念相似段落
- 全文检索与模糊语义匹配
- 导入 Kindle 高亮/json/csv，导出回 epub 与开放格式，无锁定
- 随机发现被遗忘的摘录并用比喻重新解释

## 适用场景

- 整理 Kindle 划线并建立可检索的读书摘录库
- 跨书发现不同作者对同一概念的论述
- 回顾旧摘录并加深理解

## 场景标签

`知识库管理` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L12: On-device AI analysis finds passages with similar ideas from other authors,
> L37: On-device analysis means your collection stays on your device until you opt into

## 星数曲线

```mermaid
xychart-beta
    title "dmotz/emdash 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 179 --> 181
    line [180, 180]
```

2026-10-18 180 → 2026-10-22 180（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `ae604141c9ff` · [字段定义](../../DATASET.md)*
