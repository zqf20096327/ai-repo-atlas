# RuedigerVoigt/exoskeleton

⭐ 22 · Python · Apache-2.0 · 推送 2026-09-27 · [GitHub](https://github.com/RuedigerVoigt/exoskeleton) · 个人维护

**面向科研批量下载的 Python 爬虫框架，MariaDB 管队列**

Python 编写的爬虫/采集框架，用于构建长期运行、容错的礼貌爬虫，避免对目标服务器造成过高负载。核心机制：用 MariaDB 管理下载队列与文档数据，URL 去重，支持下载文件到磁盘、存储页面源码或正文、生成网页 PDF 副本，多版本文件管理与标签分组，并向管理员发送进度报告。README 声明版本 2 不再更新，版本 3 计划于 2025 年 11 月发布。以 Python 库形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MariaDB 管理下载队列与文档数据
- URL 去重，避免重复处理同一地址
- 支持文件下载、页面源码/正文入库、网页 PDF 副本
- 文件多版本存储、标签分组与进度报告

## 适用场景

- 为机器学习等应用批量下载成千上万个文件
- 长期运行、容错地构建网页/文件存档
- 对下载内容做多版本管理与标签检索

## 场景标签

`网页抓取` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L14: Machine Learning and other applications make it necessary to download thousands or sometimes hundreds of thousands 
> L18: Exoskeleton is a Python framework that helps you build a crawler / scraper that avoids too high loads on the connec

## 星数曲线

```mermaid
xychart-beta
    title "RuedigerVoigt/exoskeleton 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `fc3091484bd2` · [字段定义](../../DATASET.md)*
